import unittest
from itertools import product
from fractions import Fraction as F
from math import sin,pi
from .heat import evolve,diagnostic_step

class HeatTests(unittest.TestCase):
    def test_exact_counterexample_and_mode(self):
        u=(0,1,0,1,0)
        self.assertEqual(evolve(u,F(1,4),1)[-1],(0,F(1,2),F(1,2),F(1,2),0))
        self.assertEqual(diagnostic_step(u,F(3,5)),(0,F(-1,5),F(6,5),F(-1,5),0))
        for k,v in enumerate(evolve((0,1,0,-1,0),F(1,4),12)):
            self.assertEqual(v,(0,F(1,2)**k,0,-F(1,2)**k,0))
        with self.assertRaises(ValueError):evolve(u,F(3,5),1)

    def test_maximum_and_squared_norm(self):
        for interior in product((F(0),F(1,2),F(1)),repeat=3):
            u=(0,)+interior+(0,)
            for r in (F(0),F(1,10),F(1,4),F(1,2)):
                old=u
                for v in evolve(u,r,8)[1:]:
                    self.assertGreaterEqual(min(v),min(old));self.assertLessEqual(max(v),max(old))
                    self.assertLessEqual(sum(x*x for x in v),sum(x*x for x in old))
                    old=v

    def test_all_discrete_sine_modes(self):
        for M in (4,8,16):
            for j in range(1,M):
                for r in (F(1,4),F(1,2)):
                    values=[0.]+[sin(j*pi*i/M) for i in range(1,M)]+[0.]
                    actual=[(1-2*float(r))*values[i]+float(r)*(values[i-1]+values[i+1]) for i in range(1,M)]
                    gain=1-4*float(r)*sin(j*pi/(2*M))**2
                    self.assertLessEqual(abs(gain),1+1e-14)
                    for i,v in enumerate(actual,1):self.assertAlmostEqual(v,gain*values[i],places=13)

    def test_contracts(self):
        for u,r,n in (((1,0,0),F(1,4),1),((0,True,0),F(1,4),1),((0,1,0),.25,1),((0,1,0),F(-1),1),((0,1,0),F(1,4),True)):
            with self.assertRaises(ValueError):evolve(u,r,n)
        with self.assertRaises(ValueError):diagnostic_step((0,1,0),F(1,4))

if __name__=='__main__':unittest.main()
