import unittest
from math import isclose,log
from itertools import product
from .processes import expansion

KINDS=('isothermal_reversible','adiabatic_reversible','free_adiabatic')
class GasTests(unittest.TestCase):
    def test_two_paths_same_endpoints_different_work(self):
        iso=expansion(2,gamma=5/3,kind=KINDS[0]);free=expansion(2,gamma=5/3,kind=KINDS[2])
        self.assertEqual((iso['temperature_ratio'],iso['pressure_ratio']),(1,.5))
        self.assertEqual((free['temperature_ratio'],free['pressure_ratio']),(1,.5))
        self.assertEqual(free['work_over_nRT1'],0)
        self.assertTrue(isclose(iso['work_over_nRT1'],log(2),rel_tol=1e-14))
        self.assertEqual(free['heat_over_nRT1'],0)
        self.assertEqual(iso['heat_over_nRT1'],iso['work_over_nRT1'])

    def test_known_adiabatic_reference(self):
        r=expansion(4,gamma=1.5,kind=KINDS[1])
        self.assertTrue(isclose(r['temperature_ratio'],.5,rel_tol=1e-14))
        self.assertTrue(isclose(r['pressure_ratio'],.125,rel_tol=1e-14))
        self.assertTrue(isclose(r['work_over_nRT1'],1,rel_tol=1e-14))
        self.assertEqual(r['heat_over_nRT1'],0)

    def test_state_and_energy_balances(self):
        for ratio,gamma,kind in product((1,1.25,2,4,8),(1.25,1.5,5/3),KINDS):
            r=expansion(ratio,gamma=gamma,kind=kind)
            self.assertTrue(isclose(r['pressure_ratio']*ratio,r['temperature_ratio'],rel_tol=1e-13))
            self.assertTrue(isclose(r['du_over_nRT1'],r['heat_over_nRT1']-r['work_over_nRT1'],rel_tol=1e-13,abs_tol=1e-14))
            self.assertTrue(isclose(r['du_over_nRT1'],(r['temperature_ratio']-1)/(gamma-1),rel_tol=1e-13,abs_tol=1e-14))
            if ratio==1:self.assertEqual(r['work_over_nRT1'],0)

    def test_quadrature_is_only_for_reversible_curves(self):
        for exponent,kind in ((1,KINDS[0]),(5/3,KINDS[1])):
            expected=expansion(2,gamma=5/3,kind=kind)['work_over_nRT1']
            errors=[]
            for n in (50,100,200):
                h=1/n;estimate=h*sum((1+(j+.5)*h)**(-exponent) for j in range(n))
                errors.append(abs(estimate-expected))
            self.assertTrue(errors[1]<errors[0]/3 and errors[2]<errors[1]/3)
            self.assertLess(errors[-1],1e-5)
        # No attempt to integrate a fabricated p(V) equilibrium curve for free expansion.

    def test_near_gamma_one_stable_work(self):
        r=expansion(2,gamma=1+1e-12,kind=KINDS[1])
        self.assertTrue(isclose(r['work_over_nRT1'],log(2),rel_tol=1e-10))

    def test_contracts_and_representability(self):
        for bad in (True,'2',None,float('nan'),float('inf'),10**400):
            with self.assertRaises(ValueError):expansion(bad,gamma=5/3,kind=KINDS[0])
            with self.assertRaises(ValueError):expansion(2,gamma=bad,kind=KINDS[0])
        for ratio,gamma in ((0,1.5),(.5,1.5),(2,1),(2,0)):
            with self.assertRaises(ValueError):expansion(ratio,gamma=gamma,kind=KINDS[0])
        with self.assertRaises(ValueError):expansion(2,gamma=1.5,kind='unknown')
        with self.assertRaises(ArithmeticError):expansion(1e300,gamma=2,kind=KINDS[1])
