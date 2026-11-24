import unittest
from math import cos,sin,hypot,exp,pi
from .transient import apply,gain,maximizing_input,global_peak
from .experiment import state


class TransientTests(unittest.TestCase):
    def test_directions_and_attainment(self):
        for b in (-4,-2,-1,0,1,2,4):
            for t in (0,.1,.5,1,2,4):
                G=gain(b,t)
                for j in range(96):
                    theta=2*pi*j/96
                    z=apply(b,t,cos(theta),sin(theta))
                    self.assertLessEqual(hypot(*z),G+1e-12)
                v=maximizing_input(b,t)
                self.assertAlmostEqual(hypot(*v),1)
                self.assertAlmostEqual(hypot(*apply(b,t,*v)),G,places=12)
                self.assertAlmostEqual(gain(-b,t),G)

    def test_peak_and_threshold(self):
        for b in (-4,-3,-2,-1,0,1,2,3,4):
            tp,G=global_peak(b)
            for j in range(401):self.assertLessEqual(gain(b,j/20),G+1e-12)
            if abs(b)<=2:self.assertEqual((tp,G),(0,1))
            else:
                self.assertGreater(tp,0);self.assertGreater(G,1)
                self.assertLess(gain(b,tp-1e-3),G)
                self.assertLess(gain(b,tp+1e-3),G)
        self.assertAlmostEqual(global_peak(4)[0],.8660254037844386)
        self.assertAlmostEqual(global_peak(4)[1],1.5697753079149013)

    def test_trajectory_vs_operator_and_existing_family(self):
        self.assertAlmostEqual(hypot(*apply(4,1,0,1)),1.5168057934430552)
        self.assertLess(hypot(*apply(4,1,0,1)),gain(4,1))
        self.assertAlmostEqual(gain(0,1),exp(-1))
        for b in (-4,0,4):
            for t in (0,.5,1,2,4):
                old=state(-1,b,t,0,1)
                self.assertEqual(apply(b,t,0,1),(old['x'],old['y']))

    def test_contracts(self):
        for b,t in ((True,1),(5,1),(1,-1),(1,21),(float('nan'),1),(1,float('inf'))):
            for fn in (gain,maximizing_input):
                with self.assertRaises(ValueError):fn(b,t)
        with self.assertRaises(ValueError):apply(1,1,True,0)
        with self.assertRaises(ValueError):global_peak(5)


if __name__=='__main__':unittest.main()
