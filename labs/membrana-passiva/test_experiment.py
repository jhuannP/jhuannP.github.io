import unittest
from fractions import Fraction as Q
from itertools import product
from decimal import Decimal,localcontext
from .experiment import stationary,transient

class PassiveMembraneTests(unittest.TestCase):
    def test_reference_stationary_and_initial_slope(self):
        self.assertEqual(stationary(4,1),dict(Vinf=-60,tau=20,G=5,IK=120,INa=-120))
        r=transient(4,1,t=0)
        self.assertEqual((r["V"],r["IK"],r["INa"],r["dV"]),(-80,40,-140,1))
        with localcontext() as ctx:
            ctx.prec=50
            expected=Decimal(-60)-Decimal(20)*Decimal(-1).exp()
        self.assertAlmostEqual(transient(4,1,t=20)["V"],float(expected),places=12)
    def test_grid_balance_and_single_ion_limits(self):
        for gk,gna,C,I in product(range(4),range(4),(50,100,200),(-100,0,100)):
            if not gk+gna:continue
            r=stationary(gk,gna,C,I)
            self.assertEqual(r["IK"]+r["INa"],I)
            if I==0:self.assertTrue(-90<=r["Vinf"]<=60)
            if I==0 and gna==0:self.assertEqual(r["Vinf"],-90)
            if I==0 and gk==0:self.assertEqual(r["Vinf"],60)
    def test_transient_residual_derivative_and_time_composition(self):
        h=Q(1,1000)
        for gk,gna,C,I,t in product((1,4),(0,1),(50,100),(-50,0,50),(1,20,80)):
            r=transient(gk,gna,C,I,t=t)
            self.assertAlmostEqual(C*r["dV"]+r["IK"]+r["INa"],I,places=10)
            diff=(transient(gk,gna,C,I,t=t+h)["V"]-transient(gk,gna,C,I,t=t-h)["V"])/(2*float(h))
            self.assertAlmostEqual(diff,r["dV"],places=7)
            # Composition checked via analytic state, with rounded initial value converted to a rational.
            at10=transient(gk,gna,C,I,t=10)["V"]
            after=transient(gk,gna,C,I,V0=Q.from_float(at10),t=t)["V"]
            self.assertAlmostEqual(after,transient(gk,gna,C,I,t=t+10)["V"],places=11)
    def test_scales_and_capacitance_does_not_change_stationary_voltage(self):
        a=stationary(4,1,100,25);b=stationary(4,1,200,25)
        self.assertEqual(a["Vinf"],b["Vinf"]);self.assertEqual(b["tau"],2*a["tau"])
        for t in (0,10,20,100):
            fast=transient(8,2,100,50,t=t)
            original=transient(4,1,100,25,t=2*t)
            self.assertAlmostEqual(fast["V"],original["V"],places=12)
    def test_contracts(self):
        for args in [(0,0,100,0),(-1,1,100,0),(1,1,0,0),(True,1,100,0),(1.,1,100,0)]:
            with self.assertRaises(ValueError):stationary(*args)
        with self.assertRaises(ValueError):transient(4,1,t=-1)
