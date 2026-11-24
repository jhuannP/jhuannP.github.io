from fractions import Fraction as Q
from itertools import product
import unittest
from .experiment import poly,value,primitive,derivative,integral,dirichlet,neumann

def direct_value(a,x):
    return sum(Q(c)*x**i for i,c in enumerate(a))

def direct_integral(a,L):
    return sum(Q(c)*L**(i+1)/Q(i+1) for i,c in enumerate(a))

def multiply(a,b):
    result=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):result[i+j]+=x*y
    return result

class PoissonBoundaryTests(unittest.TestCase):
    def test_hand_examples_and_mean_choice(self):
        self.assertEqual(dirichlet([1]),(Q(0),Q(1,2),Q(-1,2)))
        self.assertIsNone(neumann([1]))
        self.assertEqual(dirichlet([-1,2]),(Q(0),Q(-1,6),Q(1,2),Q(-1,3)))
        u=neumann([-1,2])
        self.assertEqual(u,(Q(-1,12),Q(0),Q(1,2),Q(-1,3)))
        self.assertEqual((value(u,0),value(u,1)),(Q(-1,12),Q(1,12)))
    def test_sources_against_exact_five_point_curvature(self):
        for g in product((-2,-1,0,1,2),repeat=4):
            for L in (Q(1,2),Q(1),Q(3,2)):
                d=dirichlet(g,L);n=neumann(g,L)
                self.assertEqual(direct_value(d,Q(0)),0)
                self.assertEqual(direct_value(d,L),0)
                self.assertEqual(n is None,direct_integral(g,L)!=0)
                for u in (d,n):
                    if u is None:continue
                    # Stencil exato para polinômios de grau até cinco; sem usar derivative.
                    h=L/20
                    for x in (L/3,L/2,2*L/3):
                        dd=(-direct_value(u,x+2*h)+16*direct_value(u,x+h)-30*direct_value(u,x)
                            +16*direct_value(u,x-h)-direct_value(u,x-2*h))/(12*h*h)
                        self.assertEqual(-dd,direct_value(g,x))
                if n is not None:
                    du=derivative(n)
                    self.assertEqual((value(du,0),value(du,L)),(0,0))
                    self.assertEqual(direct_integral(n,L),0)
    def test_energy_identity_and_constant_kernel(self):
        for L in (Q(1,2),Q(1),Q(2)):
            for scale in range(-3,4):
                # g=scale*(2x-L) é compatível em [0,L].
                g=[-scale*L,2*scale]
                for u in (dirichlet(g,L),neumann(g,L)):
                    du=derivative(u)
                    energy=direct_integral(multiply(du,du),L)
                    self.assertEqual(direct_integral(multiply(u,g),L),energy)
                    self.assertGreaterEqual(energy,0)
                n=neumann(g,L)
                for shift in (-4,1,7):
                    shifted=list(n);shifted[0]+=shift
                    self.assertEqual(derivative(derivative(shifted)),derivative(derivative(n)))
                    self.assertEqual(direct_integral(shifted,L)/L,shift)
        self.assertEqual(derivative([3]),(0,))
        self.assertNotEqual(value([3],0),0)  # Constante não nula viola Dirichlet homogêneo.
    def test_polynomial_helpers_on_rational_values(self):
        for coeffs in ((0,),(Q(1,3),Q(-2,7),Q(3,5)),(1,0,0)):
            self.assertEqual(derivative(primitive(coeffs)),poly(coeffs))
            for x in (Q(0),Q(1,3),Q(-2)):
                self.assertEqual(value(coeffs,x),direct_value(coeffs,x))
        self.assertEqual(poly([1,0,0]),(1,))
    def test_contracts_and_incompatible_is_not_silently_projected(self):
        for source in ([],None,[True],[1.0],["1"]):
            for solve in (dirichlet,neumann):
                with self.assertRaises(ValueError):solve(source)
        for L in (0,-1,True,1.0,"1"):
            for solve in (dirichlet,neumann):
                with self.assertRaises(ValueError):solve([0],L)
        self.assertIsNone(neumann([1,0,0]))
        self.assertEqual(neumann([0]),(0,))
