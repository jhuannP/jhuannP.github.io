import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
try:
    from .analyze import Measurement,parse_csv,fit_line,make_report,main
except ImportError:
    from analyze import Measurement,parse_csv,fit_line,make_report,main

SAMPLE='time_s,position_m\n0,1\n1,3.1\n2,4.9\n3,7.1\n4,8.9\n'
class MeasurementLabTests(unittest.TestCase):
    def test_exact_line_and_negative_velocity(self):
        for velocity in (-2,0,3):
            rows=tuple(Measurement(t,4+velocity*t) for t in (0,1,3,5))
            result=fit_line(rows)
            self.assertAlmostEqual(result['velocity_m_s'],velocity)
            self.assertAlmostEqual(result['intercept_m'],4)
            self.assertAlmostEqual(result['SSE_m2'],0)

    def test_residual_orthogonality_and_reference(self):
        rows=parse_csv(SAMPLE);r=fit_line(rows)
        self.assertAlmostEqual(r['velocity_m_s'],1.98)
        self.assertAlmostEqual(r['intercept_m'],1.04)
        self.assertAlmostEqual(r['SSE_m2'],.036)
        self.assertAlmostEqual(sum(r['residuals_m']),0)
        self.assertAlmostEqual(sum(row.time_s*res for row,res in zip(rows,r['residuals_m'])),0)
        self.assertEqual(rows,parse_csv(SAMPLE))

    def test_bad_csv_and_domains(self):
        for text in ('x,t\n1,2\n','time_s,position_m\n0,1\n',
                     'time_s,position_m\n0,1\n0,2\n','time_s,position_m\n1,1\n0,2\n',
                     'time_s,position_m\n-1,1\n0,2\n','time_s,position_m\n0,nan\n1,2\n',
                     'time_s,position_m\n0,1,extra\n1,2\n','time_s,position_m\n0,\n1,2\n'):
            with self.subTest(text=text),self.assertRaises(ValueError):parse_csv(text)
        with self.assertRaises(ValueError):Measurement(True,2)
        self.assertEqual(len(parse_csv('\ufeff'+SAMPLE)),5)

    def test_provenance_and_cli_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);source=p/'sample.csv';output=p/'result.json';source.write_text(SAMPLE)
            self.assertEqual(main(['--input',str(source),'--output',str(output),'--source-kind','synthetic']),0)
            report=json.loads(output.read_text());self.assertEqual(report['input']['source_kind'],'synthetic')
            self.assertEqual(report['input']['name'],'sample.csv');self.assertEqual(len(report['input']['sha256']),64)
            self.assertEqual(len(report['software']['code_sha256']),64)
            before=output.read_bytes()
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(['--input',str(source),'--output',str(output)]),2)
            self.assertEqual(before,output.read_bytes())

class InputBoundaryTests(unittest.TestCase):
    def test_invalid_header_is_reported_without_traceback(self):
        malformed='"time_s,position_m\n0,1\n'
        with self.assertRaisesRegex(ValueError,'CSV inválido'):parse_csv(malformed)
        with tempfile.TemporaryDirectory() as folder:
            source=Path(folder)/'bad.csv';source.write_text(malformed,encoding='utf-8')
            out,err=io.StringIO(),io.StringIO()
            with contextlib.redirect_stdout(out),contextlib.redirect_stderr(err):
                status=main(['--input',str(source)])
            self.assertEqual(status,2);self.assertEqual(out.getvalue(),'')
            self.assertIn('CSV inválido',err.getvalue());self.assertNotIn('Traceback',err.getvalue())
        for wrong in (True,1,None,b'time_s,position_m'):
            with self.assertRaisesRegex(ValueError,'texto'):parse_csv(wrong)

    def test_writer_roundtrip_and_line_endings(self):
        import csv
        for ending in ('\n','\r\n'):
            for quoting in (csv.QUOTE_MINIMAL,csv.QUOTE_ALL):
                output=io.StringIO(newline='')
                writer=csv.writer(output,lineterminator=ending,quoting=quoting)
                writer.writerow(['time_s','position_m'])
                writer.writerows([(0,0),(1,-2.5),(2,3)])
                rows=parse_csv(output.getvalue())
                self.assertEqual([(r.time_s,r.position_m) for r in rows],[(0,0),(1,-2.5),(2,3)])

    def test_missing_zero_nonfinite_and_temporal_precision(self):
        self.assertEqual(parse_csv('time_s,position_m\n0,0\n\n1,-1\n')[0].position_m,0)
        invalid=[
            'time_s,position_m\n0,\n1,1\n',
            'time_s,position_m\n0,1e309\n1,1\n',
            'time_s,position_m\n0,nan\n1,1\n',
            'time_s,position_m\n0,0\n1e-4000,1\n',
            'time_s;position_m\n0;1\n1;2\n',
            'time_s,time_s\n0,1\n1,2\n',
            'time_s,position_m\n0,"1,5"\n1,2\n',
        ]
        for text in invalid:
            with self.subTest(text=text),self.assertRaises(ValueError):parse_csv(text)

if __name__=='__main__':unittest.main()
