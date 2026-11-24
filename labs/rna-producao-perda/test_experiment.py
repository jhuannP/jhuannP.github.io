import math
import unittest
from decimal import Decimal as D,localcontext
from .experiment import model,solution

class RNATurnoverTests(unittest.TestCase):
    def test_high_precision_reference(self):
        with localcontext() as ctx:
            ctx.prec=65
            for fold in range(1,5):
                for initial in range(0,51,5):
                    for time in range(31):
                        r=model(fold,initial,time)
                        for key,a,d in [('a',D(2*fold),D(1)/5),('b',D(2),D(1)/(5*fold))]:
                            reference=a/d+(D(initial)-a/d)*(-d*time).exp()
                            self.assertAlmostEqual(r[key]['level'],float(reference),delta=1e-12)
    def test_independent_rk4_integration(self):
        for fold in (1,2,4):
            for initial in (0,10,20,50):
                for time in (1,10,30):
                    for a,d in ((2*fold,.2),(2,.2/fold)):
                        n=1000;h=time/n;m=float(initial)
                        for _ in range(n):
                            k1=a-d*m;k2=a-d*(m+h*k1/2);k3=a-d*(m+h*k2/2);k4=a-d*(m+h*k3)
                            m+=h*(k1+2*k2+2*k3+k4)/6
                        self.assertAlmostEqual(solution(a,d,initial,time),m,delta=1e-9)
    def test_stationary_family_and_relaxation(self):
        for fold in range(1,5):
            for initial in range(0,51,5):
                for time in range(31):
                    r=model(fold,initial,time);star=10*fold
                    for row in r.values():
                        self.assertAlmostEqual(row['stationary'],star)
                        self.assertGreaterEqual(row['level'],min(initial,star)-1e-12)
                        self.assertLessEqual(row['level'],max(initial,star)+1e-12)
                    self.assertGreaterEqual((r['a']['level']-r['b']['level'])*(star-initial),-1e-12)
                for a,d in ((2*fold,.2),(2,.2/fold)):
                    half=solution(a,d,initial,math.log(2)/d)
                    self.assertAlmostEqual(half,(initial+star)/2)
        self.assertEqual(solution(0,.2,5,0),5)
        self.assertAlmostEqual(solution(0,.2,5,math.log(2)/.2),2.5)
    def test_contract(self):
        for args in [(0,10,10),(5,10,10),(True,10,10),(2,3,10),(2,10,-1),(2,10,31),(2,10,.5)]:
            with self.assertRaises(ValueError):model(*args)
        for args in [(1,0,0,1),(-1,1,0,1),(1,1,-1,1),(1,1,0,-1),(True,1,0,1),(1,float('nan'),0,1),(1e300,1e-300,0,1)]:
            with self.assertRaises(ValueError):solution(*args)
