import unittest
from math import pi,sin,cos,isclose,nan,inf
from cmath import exp
from .experiment import wave,probability,model

def simpson(f,a,b,n=2048):
    h=(b-a)/n
    return h*(f(a)+f(b)+4*sum(f(a+i*h) for i in range(1,n,2))+2*sum(f(a+i*h) for i in range(2,n,2)))/3

class BornPhaseTests(unittest.TestCase):
    def test_normalization_and_intervals_against_amplitudes(self):
        for k in range(9):
            for a,b in ((0,1),(0,.5),(.5,1),(.1,.4),(.2,.2)):
                integral=simpson(lambda x:abs(wave(x,k))**2,a,b)
                self.assertAlmostEqual(integral,probability(a,b,k),delta=2e-11)
            self.assertAlmostEqual(probability(0,1,k),1,delta=1e-12)
    def test_mean_and_symmetry(self):
        for k in range(9):
            mean=simpson(lambda x:x*abs(wave(x,k))**2,0,1)
            self.assertAlmostEqual(mean,model(k)["mean_u"],delta=2e-11)
            self.assertAlmostEqual(model(k)["left"]+model(k)["right"],1)
            for j in range(101):
                u=j/100
                self.assertGreaterEqual(abs(wave(u,k))**2,0)
                self.assertAlmostEqual(abs(wave(u,k))**2,abs(wave(1-u,(k+4)%8))**2,delta=1e-12)
    def test_global_relative_phase_and_mixture(self):
        for j in range(101):
            u=j/100
            mixture=sin(pi*u)**2+sin(2*pi*u)**2
            self.assertAlmostEqual(abs(wave(u,2))**2,mixture,delta=1e-12)
            for alpha in (.2,1.3,4.):self.assertAlmostEqual(abs(exp(1j*alpha)*wave(u,0))**2,abs(wave(u,0))**2)
        self.assertGreater(model(0)["left"],.9)
        self.assertLess(model(4)["left"],.1)
        # Projetor no próprio estado (1,i)/sqrt(2): puro 1; mistura 1/2.
        pure=abs((1+(-1j)*1j)/2)**2
        mixed=.5*abs(1/2**.5)**2+.5*abs(-1j/2**.5)**2
        self.assertAlmostEqual(pure,1);self.assertAlmostEqual(mixed,.5)
    def test_scaling_and_boundaries(self):
        for L in (.5,2.,4.):
            for k in (0,2,4):
                self.assertAlmostEqual(probability(0,L/2,k,L),model(k)["left"])
                self.assertAlmostEqual(L*abs(wave(L*.3,k,L))**2,abs(wave(.3,k))**2)
        self.assertEqual(wave(-1),0j);self.assertEqual(wave(2),0j)
        self.assertAlmostEqual(abs(wave(1)),0,delta=1e-14)
    def test_contract(self):
        for k in (-1,9,True,2.):
            with self.assertRaises(ValueError):model(k)
        for L in (0,-1,True,nan,inf):
            with self.assertRaises(ValueError):wave(.1,0,L)
        for a,b in ((-.1,.5),(.5,1.1),(.7,.3),(False,.5)):
            with self.assertRaises(ValueError):probability(a,b)
