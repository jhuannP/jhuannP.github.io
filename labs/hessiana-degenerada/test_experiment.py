from fractions import Fraction as Q
from itertools import product
import unittest
from .experiment import value,inspect

class HessianDegenerate(unittest.TestCase):
    def test_hessian_by_richardson_stencils(self):
        for mode in range(6):
            for h in [Q(1,2),Q(1,4),Q(1,8)]:
                def second(step,axis):
                    return (value(mode,step if axis==0 else 0,step if axis==1 else 0)+value(mode,-step if axis==0 else 0,-step if axis==1 else 0)-2*value(mode,0,0))/step**2
                diag=[(4*second(h/2,j)-second(h,j))/3 for j in (0,1)]
                z=inspect(mode)
                self.assertEqual(diag,[z['hessian'][0][0],z['hessian'][1][1]])
                mixed=(value(mode,h,h)-value(mode,h,-h)-value(mode,-h,h)+value(mode,-h,-h))/(4*h*h)
                self.assertEqual(mixed,0)
                for x,y in [(h,0),(0,h)]:self.assertEqual(value(mode,x,y),value(mode,-x,-y))

    def test_remainder_uniform_bound(self):
        for mode in range(6):
            z=inspect(mode);hx=z['hessian'][0][0];hy=z['hessian'][1][1]
            for i,j in product(range(-8,9),repeat=2):
                x,y=Q(i,16),Q(j,16);norm2=x*x+y*y
                remainder=value(mode,x,y)-(hx*x*x+hy*y*y)/2
                self.assertLessEqual(abs(remainder),norm2**2)
                if norm2:self.assertLessEqual(abs(remainder)/norm2,norm2)

    def test_degenerate_cases_and_directional_scaling(self):
        for x,y in product([Q(i,4) for i in range(-4,5)],repeat=2):
            self.assertGreaterEqual(value(3,x,y),0)
            if x or y:self.assertGreater(value(3,x,y),0)
            self.assertGreaterEqual(value(5,x,y),0)
            if not x:self.assertEqual(value(5,x,y),0)
        for t in [Q(1,2**k) for k in range(8)]:
            self.assertGreater(value(4,t,0),0);self.assertLess(value(4,0,t),0)
            self.assertEqual(value(3,0,t/2),value(3,0,t)/16)
        for mode,d,scale in product(range(6),range(3),range(1,11)):
            z=inspect(mode,d,scale)
            self.assertEqual(z['values'][0],z['values'][-1])
            self.assertEqual(z['values'][2],0)

    def test_contracts_and_original_example(self):
        self.assertEqual(inspect(0)['determinant'],-4)
        for args in [(-1,0,1),(6,0,1),(3,3,1),(3,0,0),(3,0,11),(True,0,1),(3,0,1.5)]:
            with self.assertRaises(ValueError):inspect(*args)
