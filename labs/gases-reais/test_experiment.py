import unittest
from fractions import Fraction as F
from .experiment import eos,model


class RealGasTests(unittest.TestCase):
    def test_physical_units_independent_equation(self):
        for theta in (F(2,5),F(3,5),F(1),F(2)):
            for x in (F(1,20),F(1,5),F(2,5),F(3,5)):
                for a in map(F,(2,5)):
                    for b in (F(1,10),F(1,5)):
                        R=F(3);T=theta*a/(R*b);Vm=b/x
                        p=R*T/(Vm-b)-a/(Vm*Vm)
                        s=eos(theta,x)
                        self.assertEqual(p*b*b/a,s['pressure'])
                        self.assertEqual(p*Vm/(R*T),s['z'])
                        self.assertEqual(s['z'],1+s['volume_correction']+s['attraction'])

    def test_virial_boyle_and_accidental_ideal_z(self):
        for theta in (F(2,5),F(3,5),F(1),F(2)):
            for x in (F(0),F(1,100),F(1,5),F(3,5)):
                s=eos(theta,x)
                self.assertEqual(s['z']-s['virial'],x*x/(1-x))
                if theta==1:self.assertEqual(s['z']-1,x*x/(1-x))
        s=eos(F(3,5),F(2,5))
        self.assertEqual(s['z'],1);self.assertEqual(s['pkappa'],F(9,13))
        self.assertNotEqual(s['pkappa'],1)
        self.assertEqual(eos(F(1),F(0))['z'],1)
        self.assertIsNone(eos(1,0)['volume_ratio'])

    def test_derivative_and_compressibility(self):
        h=1e-6
        for theta in (.4,.6,1,2):
            for x in (.05,.2,.4,.6):
                s=eos(theta,x)
                numeric=(eos(theta,x+h)['pressure']-eos(theta,x-h)['pressure'])/(2*h)
                self.assertAlmostEqual(s['slope'],numeric,places=8)
                # Differentiate pressure in volume coordinates v=Vm/b=1/x.
                v=1/x
                P=lambda w:theta/(w-1)-1/(w*w)
                dpdv=(P(v+h)-P(v-h))/(2*h)
                pk=-s['pressure']/(v*dpdv)
                self.assertAlmostEqual(s['pkappa'],pk,places=7)

    def test_mechanical_stability_critical_and_contract(self):
        critical=eos(F(8,27),F(1,3))
        self.assertEqual(critical['slope'],0);self.assertEqual(critical['second'],0)
        self.assertEqual(critical['pressure'],F(1,27))
        self.assertIsNone(critical['pkappa'])
        for j in range(20):
            x=F(j,20)
            gap=F(8,27)-2*x*(1-x)**2
            self.assertEqual(gap,2*(F(4,3)-x)*(x-F(1,3))**2)
            self.assertGreater(eos(F(2,5),x)['slope'],0)
        for args in ((.3,.2,0),(.6,-.1,0),(.6,.7,0),(.6,.2,2)):
            with self.assertRaises(ValueError):model(*args)
        with self.assertRaises(ValueError):eos(1,1)
