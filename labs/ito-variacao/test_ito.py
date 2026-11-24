import unittest
from fractions import Fraction as Q
from itertools import product
from .ito import square_sums,brownian_errors,ito_polynomial

class ItoTests(unittest.TestCase):
    def test_finite_telescoping(self):
        for increments in product((Q(-1,2),Q(0),Q(1,2)),repeat=4):
            for x0 in (0,2):
                s=square_sums(increments,x0)
                self.assertEqual(s['final']**2-x0*x0,2*s['left']+s['qv'])
                self.assertEqual(s['right']-s['left'],s['qv'])
                self.assertEqual(2*s['midpoint'],s['final']**2-x0*x0)
    def test_gaussian_moments_independent(self):
        for n in (1,2,4,8,16):
            for horizon in (Q(1,2),Q(1),Q(2)):
                h=horizon/n
                # Sum diagonal Gaussian fourth moments and ordered cross pairs.
                eq=sum((h for _ in range(n)),Q(0))
                eq2=sum((3*h*h for _ in range(n)),Q(0))+sum((h*h for i in range(n) for j in range(n) if i!=j),Q(0))
                variance=eq2-eq*eq
                stats=brownian_errors(n,horizon)
                self.assertEqual(stats['mean_qv'],eq)
                self.assertEqual(stats['var_qv'],variance)
                self.assertEqual(stats['mse_left'],variance/4)
                self.assertEqual(stats['mse_left'],sum((h*h/2 for _ in range(n)),Q(0)))
    def test_derivatives_by_independent_stencils(self):
        polynomials=[(1,),(0,1),(0,0,1),(2,-1,3),(1,2,-1,2),(1,0,2,0,-1)]
        h=Q(1,3)
        for coeffs in polynomials:
            def f(x):return sum(a*x**i for i,a in enumerate(coeffs))
            for x in (Q(-2),Q(0),Q(1,2)):
                first=(f(x-2*h)-8*f(x-h)+8*f(x+h)-f(x+2*h))/(12*h)
                second=(-f(x+2*h)+16*f(x+h)-30*f(x)+16*f(x-h)-f(x-2*h))/(12*h*h)
                for b in (-1,0,2):
                    for sigma in (0,1,3):
                        drift,diffusion=ito_polynomial(coeffs,x,b,sigma)
                        self.assertEqual(drift,b*first+sigma*sigma*second/2)
                        self.assertEqual(diffusion,sigma*first)
    def test_landmarks(self):
        self.assertEqual(brownian_errors(4)['var_qv'],Q(1,2))
        self.assertEqual(brownian_errors(4)['mse_left'],Q(1,8))
        self.assertEqual(brownian_errors(16)['mse_left'],Q(1,32))
        self.assertEqual(ito_polynomial((0,0,1),2,-4,3),(-7,12))
        self.assertEqual(ito_polynomial((0,0,0,1),2,0,1),(6,12))
        self.assertEqual(square_sums([])['qv'],0)
    def test_contracts(self):
        for n in (0,-1,True,1.5):
            with self.assertRaises(ValueError):brownian_errors(n)
        with self.assertRaises(ValueError):brownian_errors(1,-1)
        with self.assertRaises(ValueError):square_sums([0.5])
        with self.assertRaises(ValueError):ito_polynomial([],0,0,1)
        with self.assertRaises(ValueError):ito_polynomial((1,),True,0,1)

if __name__=='__main__':unittest.main()
