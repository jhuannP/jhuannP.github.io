from fractions import Fraction as Q
from pathlib import Path
import json
import unittest
from .power import history

class PowerTests(unittest.TestCase):
    def test_reference(self):
        h=history(((3,0),(0,1)),(1,1),2)
        self.assertEqual(h[1]['vector'],(1,Q(1,3)))
        self.assertEqual(h[1]['rayleigh'],Q(14,5))
        self.assertEqual(h[1]['residual'],Q(3,5))
        self.assertEqual(h[1]['scaled'],Q(3,29))
        self.assertEqual(h[2]['rayleigh'],Q(122,41))
    def test_closed_form(self):
        for a,b in ((3,1),(4,3),(-3,1),(5,-2)):
            h=history(((a,0),(0,b)),(1,1),8)
            for k,row in enumerate(h):
                u,v=Q(a)**k,Q(b)**k
                scale=max(abs(u),abs(v))
                self.assertEqual(row['vector'],(u/scale,v/scale))
                rho=(a*u*u+b*v*v)/(u*u+v*v)
                self.assertEqual(row['rayleigh'],rho)
                self.assertEqual(row['residual'],max(abs((a-rho)*u),abs((b-rho)*v))/scale)
    def test_failures_are_observable(self):
        h=history(((3,0),(0,1)),(0,1),4)
        self.assertTrue(all(r['rayleigh']==1 and r['residual']==0 for r in h))
        h=history(((1,0),(0,-1)),(1,1),4)
        self.assertEqual(h[0]['vector'],h[2]['vector'])
        self.assertNotEqual(h[0]['vector'],h[1]['vector'])
        self.assertTrue(all(r['rayleigh']==0 and r['residual']==1 for r in h))
    def test_scaling_and_preserved_algorithm(self):
        A=((3,0),(0,1)); h=history(A,(1,1),3)
        for c in (Q(1,10),10,-2):
            scaled=history(tuple(tuple(c*v for v in row) for row in A),(1,1),3)
            for left,right in zip(h,scaled):
                self.assertEqual(right['rayleigh'],c*left['rayleigh'])
                self.assertEqual(right['residual'],abs(c)*left['residual'])
                self.assertEqual(right['scaled'],left['scaled'])
        p=Path(__file__).resolve().parents[2]/'content/lessons.json'
        l=next(x for x in json.loads(p.read_text()) if x['id']=='metodo-potencia')
        exec(l['python'],{});exec(l['codingPractice']['solution'],{})
    def test_contracts(self):
        with self.assertRaises(ArithmeticError): history(((3,0),(0,1)),(0,0),1)
        with self.assertRaises(ArithmeticError): history(((0,0),(0,1)),(1,0),1)
        with self.assertRaises(ValueError): history(((3,0),(0,1)),(1,1),101)
        with self.assertRaises(TypeError): history(((3,0),(0,1)),(1,1),True)
        with self.assertRaises(TypeError): history(((3.,0),(0,1)),(1,1),1)
        with self.assertRaises(ValueError): history(((3,),),(1,1),1)
if __name__=='__main__': unittest.main()
