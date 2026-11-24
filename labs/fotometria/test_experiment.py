import unittest
from math import isclose,log
from .experiment import photometry,apparent

class PhotometryTests(unittest.TestCase):
    def test_independent_flux_geometry(self):
        for M in (-3,0,4,8):
            for d in (1,10,100,1000):
                for A in (0,1,2.5):
                    m=apparent(M,d,A)
                    # Fluxo relativo ao ponto zero por geometria, sem usar módulo inverso.
                    flux=10**(-.4*M)*(10/d)**2*10**(-.4*A)
                    self.assertTrue(isclose(10**(-.4*m),flux,rel_tol=1e-12))
                    self.assertTrue(isclose(photometry(m,M,A)['distance'],d,rel_tol=1e-12))

    def test_exact_powers_and_extinction_sign(self):
        self.assertEqual(photometry(4,4,0)['distance'],10)
        self.assertEqual(photometry(9,4,0)['distance'],100)
        q=photometry(15,4,1);self.assertEqual(q['modulus'],10);self.assertEqual(q['distance'],1000)
        self.assertAlmostEqual(q['naive']/q['distance'],10**.2)
        self.assertAlmostEqual(photometry(15,4,2.5)['transmission'],.1)
        self.assertAlmostEqual(photometry(15,4,2.5)['bias'],10**.5)
        self.assertAlmostEqual(photometry(20,4,1)['distance']/q['distance'],10)

    def test_degeneracy_and_derivative(self):
        for m in (8,15,20):
            for M in (-2,4,8):
                q=photometry(m,M,1)
                # Mesmo m, mudando M e A com soma preservada: distância inalterada.
                self.assertAlmostEqual(q['distance'],photometry(m,M-1,2)['distance'])
                h=1e-5
                derivative=(photometry(m,M,1+h)['distance']-photometry(m,M,1-h)['distance'])/(2*h)
                self.assertTrue(isclose(derivative,-log(10)/5*q['distance'],rel_tol=1e-9))

    def test_invalid_data(self):
        for args in ((1,2,-1),(float('nan'),2,0),(1,float('inf'),0),(1,2,float('nan'))):
            with self.assertRaises(ValueError):photometry(*args)
        for args in ((1,0,0),(1,-1,0),(1,10,-1),(1,float('inf'),0)):
            with self.assertRaises(ValueError):apparent(*args)

if __name__=='__main__':unittest.main()
