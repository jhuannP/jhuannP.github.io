import unittest
from fractions import Fraction as F
from itertools import product
from .hermite import evaluate,bound

class HermiteTests(unittest.TestCase):
    def test_cubics_and_endpoint_derivatives(self):
        for coeff in product((-1,0,1),repeat=4):
            f=lambda x:sum(c*x**i for i,c in enumerate(coeff))
            df=lambda x:sum(i*coeff[i]*x**(i-1) for i in range(1,4))
            for a,b in ((F(-2),F(1)),(F(0),F(2)),(F(1,3),F(5,4))):
                data=(a,b,f(a),f(b),df(a),df(b))
                for j in range(5):
                    x=a+(b-a)*F(j,4)
                    self.assertEqual(evaluate(*data,x),(f(x),df(x)))

    def test_quartic_error_and_bound(self):
        self.assertEqual(bound(-1,1,24),1)
        for i in range(81):
            x=F(i,40)-1
            value,derivative=evaluate(-1,1,1,1,-4,4,x)
            self.assertEqual(value,2*x*x-1)
            self.assertEqual(derivative,4*x)
            self.assertEqual(x**4-value,(x*x-1)**2)
            self.assertLessEqual(abs(x**4-value),bound(-1,1,24))
        self.assertEqual(evaluate(-1,1,1,1,-4,4,0)[0],-1)
        # Shrinking a fixed quartic interval halves h and reduces exact midpoint error by 16.
        error=[]
        for b in (F(2),F(1),F(1,2)):
            x=b/2;v=evaluate(0,b,0,b**4,0,4*b**3,x)[0]
            error.append(x**4-v)
        self.assertEqual(error[0],16*error[1]);self.assertEqual(error[1],16*error[2])

    def test_data_perturbations(self):
        for e0,e1 in product((F(-1,4),F(0),F(1,4)),repeat=2):
            for i in range(25):
                t=F(i,24);x=2*t
                clean=evaluate(0,2,0,8,0,12,x)[0]
                changed=evaluate(0,2,0,8,e0,12+e1,x)[0]
                expected=2*((t**3-2*t*t+t)*e0+(t**3-t*t)*e1)
                self.assertEqual(changed-clean,expected)
                self.assertLessEqual(abs(changed-clean),F(8,27)*(abs(e0)+abs(e1)))
            self.assertEqual(evaluate(0,2,0,8,e0,12+e1,1)[0]-1,(e0-e1)/4)
        self.assertEqual(evaluate(0,2,0,8,F(1,4),12,1)[0],F(17,16))

    def test_contract(self):
        for bad in (True,1.0,'1',None):
            with self.assertRaises(TypeError): evaluate(0,2,0,8,bad,12,1)
        for a,b,x in ((0,0,0),(2,0,1),(0,2,3)):
            with self.assertRaises(ValueError): evaluate(a,b,0,8,0,12,x)
        with self.assertRaises(ValueError): bound(0,2,-1)
        with self.assertRaises(ValueError): evaluate(0,2,0,8,10**6+1,12,1)
