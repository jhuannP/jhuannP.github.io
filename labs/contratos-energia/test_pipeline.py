import copy
from contextlib import redirect_stdout,redirect_stderr
from io import StringIO
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from .pipeline import energy_batch,run_text,main,parse_request

REQUEST='{"unit_system":"SI","measurements":[[3,-4],[2,20],[0,10]]}'

class PurePipelineTests(unittest.TestCase):
    def test_core_preserves_inputs_and_prints_nothing(self):
        rows=[[3,-4],[2,20],[0,10]];before=copy.deepcopy(rows);out=StringIO()
        with redirect_stdout(out):
            result=energy_batch(rows)
        self.assertEqual(result,(24,400,0))
        self.assertIs(type(result),tuple)
        self.assertEqual(rows,before)
        self.assertEqual(out.getvalue(),"")
        self.assertEqual(energy_batch(rows),result)

    def test_text_round_trip_without_io(self):
        report=json.loads(run_text(REQUEST))
        self.assertEqual(report,{"energy_unit":"J","energies":[24,400,0]})
        self.assertEqual(parse_request(REQUEST),((3,-4),(2,20),(0,10)))
        self.assertEqual(run_text(REQUEST),run_text(REQUEST))

    def test_rejects_schema_duplicates_and_nonfinite(self):
        for text in ('{}','[]','{"unit_system":"CGS","measurements":[[1,2]]}',
                     '{"unit_system":"SI","unit_system":"SI","measurements":[[1,2]]}',
                     '{"unit_system":"SI","measurements":[]}',
                     '{"unit_system":"SI","measurements":[[1,2,3]]}',
                     '{"unit_system":"SI","measurements":[[true,2]]}',
                     '{"unit_system":"SI","measurements":[[1,NaN]]}',
                     '{"unit_system":"SI","measurements":[[1,1e999]]}',
                     '{"unit_system":"SI","measurements":[[-1,2]]}'):
            with self.assertRaises(ValueError):run_text(text)
        for rows in ([],[(1,2,3)],[True],"1,2"):
            with self.assertRaises(ValueError):energy_batch(rows)

    def test_file_boundary_and_no_overwrite(self):
        with TemporaryDirectory() as folder:
            src=Path(folder)/'input.json';dst=Path(folder)/'result.json'
            src.write_text(REQUEST)
            with redirect_stdout(StringIO()),redirect_stderr(StringIO()):
                self.assertEqual(main([str(src),'--output',str(dst)]),0)
                original=dst.read_text()
                self.assertEqual(main([str(src),'--output',str(dst)]),2)
            self.assertEqual(dst.read_text(),original)
            self.assertEqual(src.read_text(),REQUEST)
            self.assertEqual(json.loads(original)['energies'],[24,400,0])

    def test_invalid_late_record_does_not_create_output(self):
        with TemporaryDirectory() as folder:
            src=Path(folder)/'input.json';dst=Path(folder)/'result.json'
            src.write_text('{"unit_system":"SI","measurements":[[3,4],[-1,2]]}')
            out,err=StringIO(),StringIO()
            with redirect_stdout(out),redirect_stderr(err):
                self.assertEqual(main([str(src),'--output',str(dst)]),2)
            self.assertFalse(dst.exists())
            self.assertEqual(out.getvalue(),"")
            self.assertIn('massa',err.getvalue())

    def test_real_module_cli(self):
        root=Path(__file__).resolve().parents[2]
        fixture=Path(__file__).with_name('measurements.json')
        result=subprocess.run([sys.executable,'-m','labs.contratos-energia.pipeline',str(fixture)],cwd=root,text=True,capture_output=True)
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(json.loads(result.stdout)['energies'],[24,400,0])
        self.assertEqual(result.stderr,"")
