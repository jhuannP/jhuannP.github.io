from fractions import Fraction as Q
from itertools import product
import unittest
from .experiment import inspect

class SlidingWork(unittest.TestCase):
    def test_newton_kinematics_independent(self):
        # t escolhido antes da parada; posição/velocidade calculadas por Newton.
        for m,v,force,friction in product(range(1,5),range(1,7),range(9),range(9)):
            a=Q(force-friction,m)
            stop_time=-Q(v)/a if a<0 else None
            t=min(Q(1,4),stop_time/2) if stop_time else Q(1,4)
            x=v*t+a*t*t/2;velocity=v+a*t
            self.assertEqual(Q(m,2)*(velocity**2-v*v),(force-friction)*x)
            if a<0:
                distance=v*stop_time+a*stop_time**2/2
                self.assertEqual(distance,inspect(m,v,force,friction,0)['stop'])

    def test_balances_and_reachable_domain(self):
        for m,v,force,friction,d in product([1,2,4],[1,3,6],[0,2,8],[0,5,8],range(13)):
            r=inspect(m,v,force,friction,d)
            self.assertEqual(r['applied']+r['friction_work'],r['k']-r['k0'])
            self.assertEqual(r['k']-r['k0']+r['internal'],r['applied'])
            self.assertGreaterEqual(r['k'],0)
            if r['reachable']:self.assertEqual(r['end'],d)
            else:
                self.assertIsNone(r['query_k']);self.assertEqual(r['k'],0)
                self.assertLess(r['end'],d)

    def test_exact_boundary_and_zero_resultant(self):
        self.assertEqual(inspect(distance=3)['query_k'],0)
        self.assertFalse(inspect(distance=4)['reachable'])
        r=inspect(force=5,friction=5,distance=4)
        self.assertEqual(r['k'],9);self.assertEqual(r['applied'],20)
        self.assertEqual(r['internal'],20);self.assertIsNone(r['stop'])
        self.assertEqual(inspect(distance=0)['net_work'],0)
        self.assertEqual(inspect(v0=6,distance=0)['k0'],4*inspect(v0=3,distance=0)['k0'])

    def test_contracts(self):
        for field,values in {'m':[0,5,True,1.5],'v0':[0,7],'force':[-1,9],'friction':[-1,9],'distance':[-1,13,'2']}.items():
            for value in values:
                with self.assertRaises(ValueError):inspect(**{field:value})
