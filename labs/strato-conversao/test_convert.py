from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
import unittest
from .convert import conversion,linear_exponent,compare,base

class ConversionTests(unittest.TestCase):
    def test_two_prescribed_grids(self):
        a=compare((Q(1,2),Q(-1,2),Q(1,2),Q(1,2)))
        b=compare((Q(1,4),)*4)
        self.assertEqual(a,{'final':1,'left':0,'symmetric':Q(1,2),'qv':1})
        self.assertEqual(b,{'final':1,'left':Q(3,8),'symmetric':Q(1,2),'qv':Q(1,4)})
    def test_finite_identity_by_endpoint_formula(self):
        for dx in product((Q(-1,2),Q(0),Q(1,2)),repeat=4):
            r=compare(dx); endpoint=sum(dx); qv=sum(x*x for x in dx)
            self.assertEqual(r['left'],(endpoint**2-qv)/2)
            self.assertEqual(r['symmetric'],endpoint**2/2)
            self.assertEqual(r['symmetric']-r['left'],qv/2)
    def test_linear_conversion_and_ito_formula(self):
        for alpha,sigma,t,w in product((-1,0,2),(-2,0,3),(0,1,2),(-1,0,1)):
            ai=conversion(alpha,sigma,sigma)
            self.assertEqual(linear_exponent(ai,sigma,t,w,'ito'),linear_exponent(alpha,sigma,t,w,'stratonovich'))
        # Derivação independente por fórmula de Itô já implementada para X².
        for x in (-2,0,3):
            drift,diffusion=base.ito_polynomial((0,0,1),x,0,1)
            self.assertEqual((drift,diffusion),(1,2*x))
        self.assertEqual(conversion(4,3,0),4)
        self.assertEqual(linear_exponent(0,1,2,0,'ito'),-1)
    def test_smooth_refinement_is_not_brownian(self):
        dx=(Q(1,2),Q(-1,2),Q(1,2),Q(1,2));before=compare(dx)
        after=compare(tuple(value/2 for value in dx for _ in range(2)))
        self.assertEqual(after['qv'],before['qv']/2)
        self.assertEqual(after['symmetric'],before['symmetric'])
        # Modelo gaussiano teórico separado, não deduzido dessas grades.
        self.assertEqual(base.brownian_errors(4,1)['var_qv'],Q(1,2))
        self.assertEqual(base.brownian_errors(16,1)['var_qv'],Q(1,8))
    def test_preserved_material(self):
        ls=json.loads((Path(__file__).resolve().parents[2]/'content/lessons.json').read_text())
        l=next(x for x in ls if x['id']=='ito-stratonovich')
        exec(l['python'],{});exec(l['codingPractice']['solution'],{})
    def test_contracts(self):
        for bad in (True,1.0,'1'):
            with self.assertRaises(ValueError):conversion(bad,1,1)
        with self.assertRaises(ValueError):linear_exponent(0,1,-1,0,'ito')
        with self.assertRaises(ValueError):linear_exponent(0,1,1,0,'outro')
if __name__=='__main__':unittest.main()
