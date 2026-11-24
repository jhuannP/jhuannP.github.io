import itertools
import unittest
from fractions import Fraction as F
from .green import green,solution,uniform_patch

class GreenTests(unittest.TestCase):
    def test_kernel(self):
        for L in (F(1),F(2),F(3,2)):
            for i,j in itertools.product(range(9),repeat=2):
                x,s=L*i/8,L*j/8
                self.assertEqual(green(x,s,L),green(s,x,L))
                self.assertGreaterEqual(green(x,s,L),0)
                self.assertEqual(green(0,s,L),0);self.assertEqual(green(L,s,L),0)
            for i in range(1,8):
                s=L*i/8;h=L/32
                left=(green(s,s,L)-green(s-h,s,L))/h
                right=(green(s+h,s,L)-green(s,s,L))/h
                self.assertEqual(right-left,-1)

    def test_polynomial_ode_oracle(self):
        # Integra diretamente -u''=f duas vezes e determina a reta pelas bordas.
        for cs in itertools.product((-1,0,2),repeat=3):
            for L in (F(1),F(2),F(3,2)):
                particular=lambda x:-sum((F(c)*x**(k+2)/((k+1)*(k+2)) for k,c in enumerate(cs)),F(0))
                slope=-particular(L)/L
                for j in range(9):
                    x=L*j/8
                    self.assertEqual(solution(cs,x,L),particular(x)+slope*x)

    def test_patch_via_integrated_step(self):
        for a in (F(1,3),F(1,2),F(2,3)):
            for e in (F(1,12),F(1,24)):
                lo,hi=a-e,a+e
                # Solução direta por potências truncadas, sem integrar G.
                def v(x):return -(max(x-lo,0)**2-max(x-hi,0)**2)/(4*e)
                for j in range(25):
                    x=F(j,24);actual=uniform_patch(x,a,e)
                    self.assertEqual(actual,v(x)-x*v(F(1)))
                    self.assertLessEqual(abs(actual-green(x,a)),e/2)
        self.assertEqual(green(F(1,2),F(1,2))-uniform_patch(F(1,2),F(1,2),F(1,8)),F(1,32))

    def test_linearity_and_boundary_lift(self):
        for j in range(9):
            x=F(j,8)
            self.assertEqual(solution((3,6),x),solution((3,),x)+solution((0,6),x))
            u=solution((0,6),x)+2*(1-x)-x
            self.assertEqual(u,2-2*x-x**3)

    def test_contracts(self):
        for args in ((-1,0,1),(0,0,0),(F(1,2),2,1)):
            with self.assertRaises(ValueError):green(*args)
        for v in (True,0.5,"1"):
            with self.assertRaises(ValueError):green(v,F(1,2))
        with self.assertRaises(ValueError):solution((),0)
        with self.assertRaises(ValueError):uniform_patch(F(1,2),F(1,2),0)
        with self.assertRaises(ValueError):uniform_patch(F(1,2),F(1,4),F(1,3))
