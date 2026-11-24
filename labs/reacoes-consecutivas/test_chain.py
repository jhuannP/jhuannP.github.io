import unittest
from math import exp,expm1,log
from .chain import integrate,rhs

def reference(k1,k2,a0,t):
    a=a0*exp(-k1*t);delta=(k2-k1)*t
    if delta==0:i=a*k1*t
    else:i=a*k1*t*(-expm1(-delta))/delta
    return a,i,a0-a-i

class ChainTests(unittest.TestCase):
    def test_against_exact_solution(self):
        # 60 estados em escalas moderadas; referência não é derivada do RK4.
        for k1,k2 in ((1,1),(1,10),(2,1),(1,1.000001)):
            for a0 in (.25,1,3):
                for t in (.1,.5,1,2,4):
                    got=integrate(k1,k2,a0,t,max_step=.01)
                    for v,w in zip((got.a,got.intermediate,got.product),reference(k1,k2,a0,t)):
                        self.assertLess(abs(v-w),2e-9*a0)
                    self.assertLess(abs(got.mass_error),2e-13*a0)
                    self.assertGreaterEqual(min(got.a,got.intermediate,got.product),0)

    def test_equal_rates_and_peak(self):
        z=integrate(1,1,1,1,max_step=.01)
        self.assertAlmostEqual(z.intermediate,1/exp(1),places=9)
        self.assertAlmostEqual(z.product,1-2/exp(1),places=9)
        for t in (.9,1.1):self.assertLess(integrate(1,1,1,t).intermediate,z.intermediate)
        tm=log(10)/9;peak=integrate(1,10,1,tm,max_step=.01)
        self.assertLess(abs(rhs((peak.a,peak.intermediate,peak.product),1,10)[1]),1e-9)

    def test_initial_layer_and_stationary_approximation(self):
        z=integrate(1,10,1,0)
        self.assertEqual(z.intermediate,0)
        self.assertEqual(rhs((1,0,0),1,10),( -1,1,0))
        # i/(k1*a/k2)=10/9*(1-exp(-9t)); não vale1 nem no limite tardio.
        for t in (.1,.5,1):
            z=integrate(1,10,1,t,max_step=.01)
            self.assertAlmostEqual(z.intermediate/(z.a/10),10/9*(1-exp(-9*t)),places=8)

    def test_refinement_and_units_rescaling(self):
        exact=reference(1,1,1,1);errors=[]
        for h in (.25,.125,.0625):
            z=integrate(1,1,1,1,max_step=h)
            errors.append(max(abs(v-w) for v,w in zip((z.a,z.intermediate,z.product),exact)))
        self.assertLess(errors[1],errors[0]/10);self.assertLess(errors[2],errors[1]/10)
        z=integrate(1,10,1,2);seconds=integrate(1/60,10/60,1,120)
        for a,b in zip((z.a,z.intermediate,z.product),(seconds.a,seconds.intermediate,seconds.product)):
            self.assertAlmostEqual(a,b,places=13)
        scaled=integrate(1,10,3,2)
        self.assertAlmostEqual(scaled.product,3*z.product,places=13)

    def test_contracts_and_budget(self):
        for bad in (True,'1',None):
            with self.assertRaises(TypeError):integrate(bad,1,1,1)
        for args in ((0,1,1,1),(1,-1,1,1),(1,1,0,1),(1,1,1,-1),(float('inf'),1,1,1)):
            with self.assertRaises(ValueError):integrate(*args)
        with self.assertRaises(ValueError):integrate(1,1,1,1,max_step=1)
        with self.assertRaises(ValueError):integrate(1,1e8,1,1)
        self.assertEqual(integrate(1,1,1,0).steps,0)

if __name__=='__main__':unittest.main()
