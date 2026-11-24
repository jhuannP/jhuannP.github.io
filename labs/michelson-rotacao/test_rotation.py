import unittest
from decimal import Decimal as D, localcontext
from fractions import Fraction as Q
from math import sqrt
from .rotation import gap, ether_times, rotation_change, fringe_shift, relativistic_proper_times

class RotationTests(unittest.TestCase):
    def test_rational_fixture_from_intercepts(self):
        # c=1, v=3/5: parallel interception times L/(c-v), L/(c+v).
        # Transverse interception solves (c*t)^2=L^2+(v*t)^2; sqrt=4/5.
        before, after = ether_times(3, 2, 1, .6)
        expected = ((Q(15,2)+Q(15,8), Q(5)), (Q(15,2), Q(5)+Q(5,4)))
        for a,b in zip(before+after, expected[0]+expected[1]):
            self.assertAlmostEqual(a,float(b),places=13)
        self.assertAlmostEqual(rotation_change(3,2,1,.6),-25/8)
        self.assertAlmostEqual(fringe_shift(3,2,.5,.6),25/4)

    def test_independent_decimal_times(self):
        with localcontext() as ctx:
            ctx.prec=80
            for b in ('0','0.6','-0.8','0.01','0.0001','0.000000001'):
                v=D(b);r=(1-v*v).sqrt()
                for l1,l2 in ((2,2),(3,2),(1,7)):
                    # Independent time-of-flight expressions; not the rationalized gap.
                    parallel1=D(l1)/(1-v)+D(l1)/(1+v)
                    parallel2=D(l2)/(1-v)+D(l2)/(1+v)
                    transverse1=2*D(l1)/r;transverse2=2*D(l2)/r
                    change=(transverse1-parallel2)-(parallel1-transverse2)
                    actual=rotation_change(l1,l2,1,float(b))
                    if change==0:self.assertEqual(actual,0)
                    else:self.assertLess(abs(D(str(actual))/change-1),D('2e-14'))

    def test_quadratic_limit_and_cancellation(self):
        # Exact / leading order tends to 1 with error O(beta**2).
        for b in (1e-2,1e-3,1e-4):
            ratio=gap(b)/(b*b/2)
            self.assertGreater(ratio,1)
            self.assertLess(abs((ratio-1)/(b*b)-1.25),.001)
        self.assertAlmostEqual(fringe_shift(4,4,500e-9,1e-4),0.160000002,places=12)
        self.assertAlmostEqual(2*4*1e-8/500e-9,.16,places=14)
        b=1e-9
        self.assertEqual(1/(1-b*b)-1/sqrt(1-b*b),0)
        self.assertAlmostEqual(gap(b)/(b*b/2),1,places=14)

    def test_invariance_scales_and_evenness(self):
        for b in (0,.1,.6,.9):
            self.assertEqual(gap(b),gap(-b))
            self.assertAlmostEqual(fringe_shift(3,2,.5,b),fringe_shift(2,3,.5,b))
            for k in (.001,7,1e6):
                self.assertAlmostEqual(fringe_shift(3*k,2*k,.5*k,b),fringe_shift(3,2,.5,b),places=10)
                self.assertAlmostEqual(rotation_change(3,2,2*k,b)*k,rotation_change(3,2,2,b),places=10)

    def test_proper_times_and_labelled_rotation(self):
        self.assertEqual(relativistic_proper_times(3,2,1),(6,4))
        for b in (.1,.6,.8):
            before,after=ether_times(3,2,1,b)
            direct=(after[0]-after[1])-(before[0]-before[1])
            self.assertAlmostEqual(direct,rotation_change(3,2,1,b))
        self.assertEqual(rotation_change(3,2,1,0),0)
        self.assertEqual(ether_times(3,2,1,0),((6,4),(6,4)))

    def test_contracts(self):
        for b in (True,'0.1',None):
            with self.assertRaises(TypeError):gap(b)
        for b in (1,-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):gap(b)
        for params in ((0,2,1,.1),(2,-1,1,.1),(2,2,0,.1),(2,2,1,2)):
            with self.assertRaises(ValueError):ether_times(*params)
        with self.assertRaises(ValueError):fringe_shift(2,2,0,.1)

if __name__=='__main__':unittest.main()
