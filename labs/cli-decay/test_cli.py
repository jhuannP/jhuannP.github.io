import json
import subprocess
import sys
import unittest
from decimal import Decimal,localcontext
from pathlib import Path
from .cli import solve
SCRIPT=Path(__file__).with_name('cli.py')

def command(*args):return subprocess.run([sys.executable,'-B',str(SCRIPT),*args],capture_output=True,text=True,timeout=10)

class CLITests(unittest.TestCase):
    def test_numeric_oracle(self):
        with localcontext() as ctx:
            ctx.prec=60
            for n in (4,10,20):
                for rate in (0,0.5,1):
                    data=solve(n,1,rate,2)
                    exact=Decimal(2)*(-Decimal(str(rate))).exp()
                    discrete=Decimal(2)*(1-Decimal(str(rate))/n)**n
                    self.assertAlmostEqual(data['endpoint'],float(discrete),places=13)
                    self.assertAlmostEqual(data['reference'],float(exact),places=13)
    def test_real_command_success(self):
        first=command('--steps','4');second=command('--steps','4')
        self.assertEqual(first.returncode,0);self.assertEqual(first.stderr,'')
        self.assertEqual(first.stdout,second.stdout)
        data=json.loads(first.stdout)
        self.assertEqual(data['endpoint'],81/256)
        self.assertEqual(data['steps'],4)
        self.assertEqual(data['model'],'linear-decay-v1')
    def test_help(self):
        result=command('--help')
        self.assertEqual(result.returncode,0);self.assertEqual(result.stderr,'')
        self.assertIn('--steps',result.stdout)
        self.assertNotIn('endpoint',result.stdout.splitlines()[-1])
    def test_invalid_cli(self):
        cases=[('--steps','0'),('--steps','100001'),('--steps','2.5'),('--steps','4','--rate','8'),('--duration','0'),('--duration','nan'),('--initial','inf'),('--rate','-1'),('--method','other'),('--ste','4'),('--duration','0,5')]
        for args in cases:
            with self.subTest(args=args):
                result=command(*args)
                self.assertEqual(result.returncode,2);self.assertEqual(result.stdout,'');self.assertTrue(result.stderr.strip())
    def test_import_safe_and_exact(self):
        imported=subprocess.run([sys.executable,'-B','-c','import runpy,sys; runpy.run_path(sys.argv[1])',str(SCRIPT),'--unknown'],capture_output=True,text=True,timeout=10)
        self.assertEqual(imported.returncode,0);self.assertEqual(imported.stdout,'');self.assertEqual(imported.stderr,'')
        result=command('--method','exact','--rate','8','--steps','4')
        self.assertEqual(result.returncode,0)
        data=json.loads(result.stdout);self.assertEqual(data['absolute_error'],0)
    def test_direct_contracts(self):
        for options in [dict(steps=True),dict(initial=True),dict(rate=float('nan')),dict(method='bad')]:
            with self.assertRaises(ValueError):solve(**options)
        self.assertEqual(solve(4,1,0,2)['endpoint'],2)

if __name__=='__main__':unittest.main()
