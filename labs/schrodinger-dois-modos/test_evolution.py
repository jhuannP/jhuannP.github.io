import cmath
import math
import unittest
from .evolution import amplitudes,wave,left_probability,current_tau

def simpson(f,a,b,n):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))

class EvolutionTests(unittest.TestCase):
    def test_integrated_amplitude_against_region_formula(self):
        for i in range(25):
            tau=i*math.pi/18
            density=lambda s:abs(wave(s,tau))**2
            for endpoint,expected in ((1,1),(.5,left_probability(tau))):
                coarse=simpson(density,0,endpoint,100)
                fine=simpson(density,0,endpoint,1000)
                self.assertLess(abs(fine-expected),2e-11)
                self.assertLessEqual(abs(fine-expected),abs(coarse-expected)+1e-14)
            self.assertAlmostEqual(abs(wave(0,tau)),0,places=14)
            self.assertAlmostEqual(abs(wave(1,tau)),0,places=14)

    def test_stationary_modulus_and_energy_weights(self):
        for tau in (-2,0,.3,2,8):
            c=amplitudes(tau)
            weights=[abs(x)**2 for x in c]
            self.assertAlmostEqual(sum(weights),1)
            self.assertAlmostEqual(weights[0]+4*weights[1],2.5)
            self.assertAlmostEqual(weights[0]+16*weights[1]-2.5**2,2.25)
            for phi in (1,1+2j,-.3j):
                self.assertAlmostEqual(abs(phi*cmath.exp(-3j*tau))**2,abs(phi)**2)

    def test_global_phase_energy_shift_and_recurrence(self):
        for tau in (0,.1,1,2):
            for s in (.1,.3,.5,.7,.9):
                for shift in (-2,3.7):
                    self.assertAlmostEqual(abs(wave(s,tau,shift))**2,abs(wave(s,tau))**2)
                recurrent=wave(s,tau+2*math.pi/3)
                self.assertAlmostEqual(abs(recurrent-cmath.exp(-2j*math.pi/3)*wave(s,tau)),0,places=13)
        initial=amplitudes(0);later=amplitudes(math.pi/3)
        overlap=sum(a.conjugate()*b for a,b in zip(initial,later))
        self.assertAlmostEqual(abs(overlap),0,places=14)

    def test_local_continuity_by_independent_finite_difference(self):
        for tau in (.1,.3,.7,1.2):
            step=1e-5
            derivative=(left_probability(tau+step)-left_probability(tau-step))/(2*step)
            self.assertLess(abs(derivative+current_tau(.5,tau)),3e-10)
            self.assertAlmostEqual(current_tau(0,tau),0,places=14)
            self.assertAlmostEqual(current_tau(1,tau),0,places=14)

    def test_schrodinger_residual_reduces_with_resolution(self):
        # i dPsi/dtau = -(1/pi^2) d2Psi/ds2, checked without modal eigenvalues.
        for s,tau in ((.2,.3),(.4,.7),(.6,1.1)):
            residual=[]
            for h in (.01,.005):
                dt=(wave(s,tau+h)-wave(s,tau-h))/(2*h)
                dxx=(wave(s+h,tau)-2*wave(s,tau)+wave(s-h,tau))/(h*h)
                residual.append(abs(1j*dt+dxx/math.pi**2))
            self.assertLess(residual[1],residual[0]/3.8)

    def test_contracts(self):
        for x in (True,'0',None):
            with self.assertRaises(TypeError):wave(x,0)
        for x in (-.1,1.1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):wave(x,0)
        for x in (float('nan'),float('inf')):
            with self.assertRaises(ValueError):amplitudes(x)
        with self.assertRaises(ValueError):amplitudes(1e308,1e308)

if __name__=='__main__':unittest.main()
