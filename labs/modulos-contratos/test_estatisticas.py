from decimal import Decimal,localcontext
from itertools import product,permutations
from pathlib import Path
import math
import subprocess
import sys
import unittest
if __package__:
    from .estatisticas import media
else:
    from estatisticas import media

class ModuleContractsTests(unittest.TestCase):
    def test_against_decimal_and_no_mutation(self):
        with localcontext() as ctx:
            ctx.prec=1100
            values=(-2.,-.5,0.,.5,3.)
            for n in range(1,5):
                for xs in product(values,repeat=n):
                    data=list(xs);before=data.copy()
                    expected=float(sum((Decimal.from_float(x) for x in data),Decimal(0))/n)
                    self.assertEqual(media(data),expected)
                    self.assertEqual(data,before)
            for data in [[sys.float_info.max]*2,[sys.float_info.max,-sys.float_info.max],
                         [1e16,1,-1e16],[1e-320]*3,[2**53+1,-2**53]]:
                expected=float(sum((Decimal(x) if type(x) is int else Decimal.from_float(x) for x in data),Decimal(0))/len(data))
                self.assertEqual(media(data),expected)
                self.assertTrue(math.isfinite(media(data)))
        for data in permutations([1e16,1.,-1e16]):self.assertEqual(media(list(data)),1/3)

    def test_rejected_inputs(self):
        for data in [[],(),(x for x in [1,2]),'12',[True],[False],['2'],[None],
                     [complex(1,0)],[math.inf],[-math.inf],[math.nan],[10**1000]]:
            with self.assertRaises(ValueError):media(data)

    def test_client_import_and_optimized_validation(self):
        folder=Path(__file__).parent
        silent=subprocess.run([sys.executable,'-c','import estatisticas'],cwd=folder,capture_output=True,text=True,check=True)
        self.assertEqual(silent.stdout,'');self.assertEqual(silent.stderr,'')
        result=subprocess.run([sys.executable,'cliente.py'],cwd=folder,capture_output=True,text=True,check=True)
        self.assertEqual(result.stdout,'4.0\n')
        script="from estatisticas import media\ntry: media([])\nexcept ValueError: print('rejeitado')\nelse: raise RuntimeError('validação ausente')"
        
        optimized=subprocess.run([sys.executable,'-O','-c',script],cwd=folder,capture_output=True,text=True,check=True)
        self.assertEqual(optimized.stdout,'rejeitado\n')

    def test_tolerances_near_zero(self):
        self.assertFalse(math.isclose(0,1e-12,rel_tol=1e-9,abs_tol=0))
        self.assertTrue(math.isclose(0,1e-12,rel_tol=1e-9,abs_tol=1e-12))
        self.assertFalse(math.isclose(math.nan,math.nan))
