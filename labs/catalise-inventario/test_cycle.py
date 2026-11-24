import unittest
from fractions import Fraction as Q
from .cycle import stationary,drift,flux,step

class CycleTests(unittest.TestCase):
    def test_fixture(self):
        y=stationary();self.assertEqual(y,(Q(1,4000),Q(1,2000),Q(1,4000)))
        self.assertEqual(flux(y),Q(1,1000));self.assertEqual(flux(y)/sum(y),1)
        self.assertEqual(drift(y),(0,0,0))
        self.assertEqual(flux(stationary(0,3))/Q(1,1000),2)
        self.assertEqual(flux(stationary(2,9))/Q(1,1000),2)

    def test_inventory_stationarity_and_scaling(self):
        for L in range(5):
            for S in range(5):
                y=stationary(L,S);self.assertEqual(sum(y),Q(1,1000))
                self.assertEqual(drift(y,L,S),(0,0,0))
                self.assertEqual(y[1],L*y[0]);self.assertEqual(6*y[2],2*S*y[0])
                double=stationary(L,S,Q(1,500))
                self.assertEqual(double,tuple(2*x for x in y))
                self.assertEqual(flux(double),2*flux(y))

    def test_trajectory_and_initial_transient(self):
        target=stationary();total=sum(target);y=(Q(0),total,Q(0))
        self.assertEqual(flux(y),0)
        for _ in range(80):
            dy=drift(y);self.assertEqual(sum(dy),0)
            y=step(y,Q(1,8));self.assertEqual(sum(y),total)
            self.assertTrue(all(v>=0 for v in y))
        self.assertLess(max(abs(a-b) for a,b in zip(y,target)),Q(1,10**7))
        self.assertEqual(step(target,Q(1,8)),target)

    def test_contracts(self):
        for L,S in ((True,1),(0.5,1),(-1,1),(1,13)):
            with self.assertRaises(ValueError):stationary(L,S)
        for y,h in (((0,0),Q(1,8)),((-1,0,1),Q(1,8)),((0,1,0),1),((0,1,0),0)):
            with self.assertRaises(ValueError):step(y,h)
        with self.assertRaises(ValueError):stationary(total=0)
