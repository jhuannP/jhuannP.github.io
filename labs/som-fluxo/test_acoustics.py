import unittest
from math import pi,cos
from .acoustics import fields,means

class AcousticTests(unittest.TestCase):
    def test_single_direction_and_units(self):
        right=means(.3,a=2,b=0);left=means(.3,a=0,b=2)
        self.assertAlmostEqual(right['pressure2_Pa2'],2)
        self.assertAlmostEqual(right['net_W_m2'],.005)
        self.assertAlmostEqual(left['net_W_m2'],-.005)
        self.assertAlmostEqual(right['net_W_m2'],400*right['energy_J_m3'])
    def test_standing_counterexample(self):
        anti=means(0);node=means(pi/2)
        self.assertAlmostEqual(anti['pressure2_Pa2'],8)
        self.assertAlmostEqual(anti['net_W_m2'],0)
        self.assertAlmostEqual(anti['velocity2_m2_s2'],0)
        self.assertAlmostEqual(node['pressure2_Pa2'],0)
        self.assertAlmostEqual(anti['energy_J_m3'],.000025)
        self.assertAlmostEqual(node['energy_J_m3'],anti['energy_J_m3'])
        self.assertAlmostEqual(anti['pressure2_Pa2']/400,.02)
    def test_phase_and_amplitudes(self):
        for a in [0,1,2]:
            for b in [0,1,3]:
                for alpha in [0,.4,pi/2]:
                    for phi in [0,.7,pi]:
                        v=means(alpha,a,b,phi)
                        self.assertAlmostEqual(v['net_W_m2'],(a*a-b*b)/800)
                        self.assertAlmostEqual(v['energy_J_m3'],(a*a+b*b)/320000)
                        self.assertAlmostEqual(v['pressure2_Pa2'],(a*a+b*b+2*a*b*cos(2*alpha+phi))/2)
                        self.assertLessEqual(abs(v['net_W_m2']),400*v['energy_J_m3']+1e-14)
    def test_contracts(self):
        for kw in [dict(a=-1),dict(b=True),dict(rho=0),dict(c=0),dict(phi=float('nan')),dict(n=True),dict(n=7),dict(n=4097)]:
            with self.assertRaises(ValueError):means(0,**kw)
        with self.assertRaises(ValueError):fields(float('inf'),0)
if __name__=='__main__':unittest.main()
