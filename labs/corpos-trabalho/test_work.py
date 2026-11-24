import unittest
from math import log,sqrt
from .work import compare,path

class Tests(unittest.TestCase):
    def test_fixture_and_balance(self):
        r=compare(400,100,2)
        self.assertEqual(r['reversible_k'],200)
        self.assertEqual(r['contact_k'],250)
        self.assertAlmostEqual(r['maximum_j'],200)
        self.assertEqual(r['heat_hot_j'],400)
        self.assertEqual(r['heat_cold_j'],200)
        self.assertAlmostEqual(r['entropy_contact_jk'],2*log(25/16))
        self.assertNotAlmostEqual(r['maximum_j'],r['efficiency_initial']*r['heat_hot_j'])
    def test_entropy_and_scale(self):
        for h,c in ((400,100),(600,300),(300,300),(1000,80)):
            r=compare(h,c,2)
            self.assertLessEqual(r['reversible_k'],r['contact_k'])
            self.assertGreaterEqual(r['entropy_contact_jk'],-1e-12)
            self.assertAlmostEqual(2*log(r['reversible_k']/h)+2*log(r['reversible_k']/c),0,places=12)
            self.assertAlmostEqual(2*(h+c-2*r['reversible_k']),r['maximum_j'],places=10)
            self.assertAlmostEqual(r['heat_hot_j']-r['heat_cold_j'],r['maximum_j'],places=10)
            self.assertAlmostEqual(compare(h,c,6)['maximum_j'],3*r['maximum_j'],places=10)
        self.assertEqual(compare(300,300,2)['maximum_j'],0)
    def test_path_and_independent_quadrature(self):
        for h,c,C in ((400,100,2),(600,300,3),(1000,80,1)):
            states=path(h,c,C,40)
            for H,K in states:
                self.assertAlmostEqual(H*K,h*c,places=8)
                self.assertGreaterEqual(H+1e-10,K)
            # Integrar C(1-h*c/T²)dT por Simpson, separadamente do balanço.
            lo=sqrt(h*c);hi=h;n=4000;dx=(hi-lo)/n
            f=lambda t:C*(1-h*c/t**2)
            integral=dx/3*(f(lo)+f(hi)+sum((4 if j%2 else 2)*f(lo+j*dx)for j in range(1,n)))
            self.assertAlmostEqual(integral,compare(h,c,C)['maximum_j'],places=8)
    def test_contracts(self):
        for args in ((100,400,2),(0,0,2),(400,100,0),(400,100,True),(float('inf'),100,2),(10**1000,100,2),(400,100,'2')):
            with self.assertRaises(ValueError):compare(*args)
        for n in (0,201,True,1.5):
            with self.assertRaises(ValueError):path(400,100,2,n)
