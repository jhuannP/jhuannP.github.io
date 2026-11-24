import unittest
from math import atan,pi,log
from .cutoff import rectangle,midpoint_x,annulus_absolute


class CutoffTests(unittest.TestCase):
    def test_analytic_against_midpoint(self):
        for a,b in ((.1,.2),(.2,.1),(.3,.3),(.6,.2)):
            e1=abs(midpoint_x(a,b,100)-rectangle(a,b))
            e2=abs(midpoint_x(a,b,200)-rectangle(a,b))
            self.assertLess(e2,2e-5)
            if a!=b:self.assertLess(e2,e1/3)

    def test_symmetry_and_distinct_cutoffs(self):
        for a,b in ((.1,.2),(.01,.3),(.25,.5)):
            self.assertAlmostEqual(rectangle(a,b),-rectangle(b,a),14)
        for e in (.5,.1,.01,1e-4):self.assertAlmostEqual(rectangle(e,e),0,14)
        for scale in (.5,1,2):
            b=1e-6
            self.assertAlmostEqual(rectangle(scale*b,b),atan(scale)-pi/4,delta=4e-6)
        self.assertGreater(rectangle(.002,.001),.3)
        self.assertLess(rectangle(.001,.002),-.3)

    def test_iterated_and_absolute_limits(self):
        e=1e-6
        self.assertAlmostEqual(rectangle(e,e*e),pi/4,delta=3e-6)
        self.assertAlmostEqual(rectangle(e*e,e),-pi/4,delta=3e-6)
        self.assertAlmostEqual(annulus_absolute(.25)-annulus_absolute(.5),log(2),14)
        self.assertGreater(annulus_absolute(1e-6),annulus_absolute(1e-3))
        self.assertEqual(annulus_absolute(1),0)

    def test_contracts(self):
        for x in (0,-1,True,float('nan'),float('inf'),2):
            with self.assertRaises(ValueError):rectangle(x,.1)
        with self.assertRaises(ValueError):midpoint_x(.1,.2,0)


if __name__=='__main__':unittest.main()
