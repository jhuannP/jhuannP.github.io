import math
import unittest
from .well import phi,density,probability,energy,midpoint_norm,MAX_MODE


def simpson(f,a,b,cells=2400):
    h=(b-a)/cells
    return h/3*(f(a)+f(b)+sum((4 if j%2 else 2)*f(a+j*h) for j in range(1,cells)))


class WellTests(unittest.TestCase):
    def test_interval_formula_against_independent_quadrature(self):
        grid=[j/4 for j in range(5)]
        for n in range(1,8):
            for a in grid:
                for b in grid:
                    if a>b:continue
                    expected=simpson(lambda s:2*math.sin(n*math.pi*s)**2,a,b)
                    bound=(b-a)/180*((b-a)/2400)**4*(2*n*math.pi)**4
                    self.assertLessEqual(abs(probability(n,a,b)-expected),bound+2e-13)
                    self.assertAlmostEqual(probability(n,a,b),expected,places=10)
        # Intervalo minúsculo junto à parede: probabilidade>0, sem cancelamento grosseiro.
        small=1e-8
        reference=simpson(lambda s:2*math.sin(math.pi*s)**2,0,small,200)
        actual=probability(1,0,small)
        self.assertGreater(actual,0)
        self.assertAlmostEqual(actual/reference,1,places=12)

    def test_normalization_orthogonality_and_nodes(self):
        for n in range(1,8):
            self.assertEqual(phi(n,0),0);self.assertEqual(phi(n,1),0)
            self.assertEqual(phi(n,-.1),0);self.assertEqual(phi(n,1.1),0)
            self.assertAlmostEqual(probability(n,0,1),1,places=13)
            for j in range(1,n):self.assertLess(abs(phi(n,j/n)),1e-12)
            self.assertEqual(len([j for j in range(1,n)]),n-1)
            for m in range(1,8):
                overlap=simpson(lambda s:phi(n,s)*phi(m,s),0,1)
                self.assertAlmostEqual(overlap,float(n==m),places=11)

    def test_probabilities_symmetry_and_classical_interval_limit(self):
        self.assertAlmostEqual(probability(1,.25,.75),.5+1/math.pi,places=13)
        self.assertAlmostEqual(probability(2,.25,.75),.5,places=13)
        self.assertAlmostEqual(probability(3,.25,.75),.5-1/(3*math.pi),places=13)
        for n in (1,2,3,10,50,100):
            for a,b in ((0,.13),(.13,.7),(.2,.8)):
                actual=probability(n,a,b)
                self.assertAlmostEqual(actual,probability(n,1-b,1-a),places=12)
                self.assertLessEqual(abs(actual-(b-a)),1/(n*math.pi)+1e-14)
            self.assertAlmostEqual(probability(n,0,.37)+probability(n,.37,1),1,places=13)
        self.assertAlmostEqual(density(1,.5),2,places=13)
        self.assertLess(density(2,.5),1e-28)
        self.assertEqual(probability(1,.5,.5),0)

    def test_energy_scaling_and_sampling_alias(self):
        for n in (1,2,3,7):
            self.assertAlmostEqual(energy(n)/energy(1),n*n,places=12)
            self.assertAlmostEqual(energy(n,L=2)/energy(n),.25,places=13)
            self.assertAlmostEqual(energy(n,m=2)/energy(n),.5,places=13)
            self.assertAlmostEqual(energy(n,hbar=2)/energy(n),4,places=13)
            self.assertAlmostEqual(midpoint_norm(n,n),2,places=12)
            self.assertAlmostEqual(midpoint_norm(n,1000),1,places=12)
        self.assertAlmostEqual((energy(3)-energy(2))/energy(1),5,places=13)

    def test_contracts(self):
        for n in (0,-1,True,1.,MAX_MODE+1):
            with self.assertRaises(ValueError):phi(n,.5)
        for s in (True,'0.5',None):
            with self.assertRaises(TypeError):phi(1,s)
        for s in (math.nan,math.inf):
            with self.assertRaises(ValueError):phi(1,s)
        for args in ((.5,.4),(-.1,.5),(0,1.1)):
            with self.assertRaises(ValueError):probability(1,*args)
        with self.assertRaises(ValueError):energy(1,m=0)
        with self.assertRaises(ArithmeticError):energy(1,L=1e-300)
        for cells in (0,True,1.,100001):
            with self.assertRaises(ValueError):midpoint_norm(1,cells)

if __name__=="__main__":unittest.main()
