import unittest
from math import isclose,log,nan,inf
from .experiment import state,entropy_isotherm,R

class MaxwellThermodynamicsTests(unittest.TestCase):
    def test_free_energy_derivatives_against_equation_of_state(self):
        for T in (250.,300.,500.):
            for V in (.005,.01,.03):
                for n in (.5,1.,2.):
                    q=state(T,V,n);ht=T*1e-4;hv=V*1e-4
                    minus_F_T=-(state(T+ht,V,n)["F"]-state(T-ht,V,n)["F"])/(2*ht)
                    minus_F_V=-(state(T,V+hv,n)["F"]-state(T,V-hv,n)["F"])/(2*hv)
                    self.assertAlmostEqual(minus_F_T,q["S"],delta=1e-6)
                    self.assertTrue(isclose(minus_F_V,n*R*T/V,rel_tol=1e-8))
                    self.assertAlmostEqual(q["F"]+T*q["S"],q["U"],delta=1e-9)
    def test_mixed_derivatives_and_maxwell_relation(self):
        for T in (260.,330.,480.):
            for V in (.008,.02):
                ht,hv=T*1e-3,V*1e-3
                f=lambda t,v:state(t,v)["F"]
                mixed=(f(T+ht,V+hv)-f(T+ht,V-hv)-f(T-ht,V+hv)+f(T-ht,V-hv))/(4*ht*hv)
                ds=(state(T,V+hv)["S"]-state(T,V-hv)["S"])/(2*hv)
                dp=(state(T+ht,V)["p"]-state(T-ht,V)["p"])/(2*ht)
                self.assertTrue(isclose(-mixed,R/V,rel_tol=2e-6))
                self.assertTrue(isclose(ds,dp,rel_tol=2e-6))
                self.assertAlmostEqual(T*dp-state(T,V)["p"],0,delta=1e-6)
    def test_entropy_by_independent_quadrature_and_composition(self):
        for v1,v2 in ((.01,.02),(.02,.01),(.006,.027),(.01,.01)):
            for n in (.5,1.,2.):
                count=1024;h=(v2-v1)/count
                terms=[n*R/(v1+i*h) for i in range(count+1)]
                integral=h*(terms[0]+terms[-1]+4*sum(terms[1:-1:2])+2*sum(terms[2:-1:2]))/3
                self.assertAlmostEqual(entropy_isotherm(v1,v2,n),integral,delta=1e-9)
                self.assertAlmostEqual(entropy_isotherm(v1,v2,n),-entropy_isotherm(v2,v1,n),delta=1e-12)
        self.assertAlmostEqual(entropy_isotherm(.01,.02)+entropy_isotherm(.02,.03),entropy_isotherm(.01,.03),delta=1e-12)
    def test_contract_and_reference_not_absolute_entropy(self):
        self.assertEqual(state(300,.01)["S"],0)
        self.assertAlmostEqual(entropy_isotherm(.01,.02),R*log(2),delta=1e-12)
        for i in range(4):
            for bad in (0,-1,True,nan,inf,'300',None):
                args=[300,.01,1,20];args[i]=bad
                with self.assertRaises(ValueError):state(*args)
