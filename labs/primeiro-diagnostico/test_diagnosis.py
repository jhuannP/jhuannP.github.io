import unittest,subprocess,sys,tempfile,json
from pathlib import Path
from .run_cases import ROOT,observe

class DiagnosisTests(unittest.TestCase):
    def setUp(self):
        self.cases=json.loads((ROOT/'cases.json').read_text(encoding='utf-8'))

    def test_syntax_prevents_execution(self):
        result=observe(self.cases['sintaxe'])
        self.assertNotEqual(result['returncode'],0);self.assertEqual(result['stdout'],'')
        self.assertIn('SyntaxError',result['stderr'])

    def test_exception_keeps_prior_output(self):
        result=observe(self.cases['execucao'])
        self.assertNotEqual(result['returncode'],0);self.assertEqual(result['stdout'],'Início\n')
        self.assertIn('NameError',result['stderr']);self.assertNotIn('Fim',result['stdout'])

    def test_units_and_correct_program(self):
        wrong=observe(self.cases['unidades']);correct=observe((ROOT/'viagem.py').read_text(encoding='utf-8'))
        self.assertEqual(wrong['returncode'],0);self.assertEqual(wrong['stderr'],'')
        self.assertAlmostEqual(float(wrong['stdout'].split(':')[1]),300/54)
        self.assertEqual(correct['returncode'],0);self.assertEqual(correct['stderr'],'')
        # Oráculo dimensional independente em metros/segundo, não usa /3.6.
        expected_time=300/(54*1000/3600)
        self.assertEqual(expected_time,20)
        self.assertEqual(correct['stdout'],'Velocidade (m/s): 15.0\nTempo (s): 20.0\n')

    def test_paths_with_spaces_and_missing_file(self):
        with tempfile.TemporaryDirectory(prefix='primeiro teste ') as name:
            script=Path(name)/'minha viagem.py';script.write_text((ROOT/'viagem.py').read_text(encoding='utf-8'),encoding='utf-8')
            ok=subprocess.run([sys.executable,str(script)],capture_output=True,text=True,timeout=3)
            missing=subprocess.run([sys.executable,str(Path(name)/'inexistente.py')],capture_output=True,text=True,timeout=3)
            self.assertEqual(ok.returncode,0);self.assertIn('20.0',ok.stdout)
            self.assertNotEqual(missing.returncode,0);self.assertEqual(missing.stdout,'');self.assertTrue(missing.stderr)
