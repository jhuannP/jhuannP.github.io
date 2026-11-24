import unittest
from math import pi,sqrt,cos
from cmath import exp
from .polarization import linear,intensity,project,plate,chain,mixture

class PolarizationTests(unittest.TestCase):
    def test_malus_projection_and_global_phase(self):
        for a in (0.,.2,.7,pi/2):
            for b in (0.,.3,pi/4,pi/2,pi):
                e=linear(a);out=project(e,b)
                self.assertAlmostEqual(intensity(out),cos(a-b)**2,places=13)
                self.assertLessEqual(intensity(out),1+1e-12)
                again=project(out,b)
                for x,y in zip(out,again):self.assertAlmostEqual(abs(x-y),0,places=13)
                rotated=tuple(z*exp(.7j) for z in e)
                self.assertAlmostEqual(chain(rotated,(b,)),chain(e,(b,)),places=13)

    def test_crossed_and_intermediate(self):
        x=(1,0)
        self.assertAlmostEqual(chain(x,(0,pi/2)),0,places=13)
        self.assertAlmostEqual(chain(x,(0,pi/4,pi/2)),.25,places=13)
        self.assertAlmostEqual(mixture(((.5,(1,0)),(.5,(0,1))),(0,pi/4,pi/2)),.125,places=13)

    def test_circular_and_incoherent_mixture(self):
        c=(1/sqrt(2),1j/sqrt(2));mix=((.5,(1,0)),(.5,(0,1)))
        for theta in (0.,.2,.7,pi/4,pi/2):
            self.assertAlmostEqual(chain(c,(theta,)),.5,places=13)
            self.assertAlmostEqual(mixture(mix,(theta,)),.5,places=13)
        corrected=plate(c,-pi/2)
        self.assertAlmostEqual(intensity(corrected),1,places=13)
        self.assertAlmostEqual(chain(corrected,(pi/4,)),1,places=13)
        mixed_corrected=tuple((w,plate(e,-pi/2)) for w,e in mix)
        self.assertAlmostEqual(mixture(mixed_corrected,(pi/4,)),.5,places=13)

    def test_contracts(self):
        for e in ((True,0),(1,1),(1e300,0),(float('nan'),0),(1,)):
            with self.assertRaises(ValueError):chain(e,(0,))
        with self.assertRaises(ValueError):chain((0,0),(0,))
        with self.assertRaises(ValueError):project((1,0),float('inf'))
        with self.assertRaises(ValueError):mixture(((.4,(1,0)),),())
        with self.assertRaises(ValueError):chain((1,0),(0,)*13)
        with self.assertRaises(ValueError):mixture(((.5000000005,(1,0)),(.5,(0,1))),())

if __name__=='__main__':unittest.main()
