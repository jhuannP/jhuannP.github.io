import unittest
from decimal import Decimal,localcontext
from .experiment import distribution

class AminoAcidTests(unittest.TestCase):
    def test_fractions_mass_action_and_concentration(self):
        for pH in (0,2.34,3.34,5.97,7,9.6,10.6,14):
            r=distribution(pH)
            self.assertAlmostEqual(r['plus']+r['zero']+r['minus'],1,places=14)
            self.assertTrue(all(0<=r[k]<=1 for k in ('plus','zero','minus')))
            self.assertAlmostEqual(r['zero']/r['plus'],10**(pH-2.34),delta=1e-12*10**(pH-2.34))
            self.assertAlmostEqual(r['minus']/r['zero'],10**(pH-9.6),delta=1e-12*10**(pH-9.6))
            self.assertAlmostEqual(r['bound_protons'],1+r['charge'],places=14)
            for C in (1e-6,.001,.1):self.assertAlmostEqual(C*(r['plus']+r['zero']+r['minus']),C,places=14)

    def test_independent_decimal_mass_action(self):
        with localcontext() as ctx:
            ctx.prec=80
            ten=Decimal(10);k1=ten**Decimal('-2.34');k2=ten**Decimal('-9.60')
            for pH in ('0','2.34','3.34','5.97','7','9.60','10.60','14'):
                h=ten**(-Decimal(pH));D=h*h+k1*h+k1*k2
                refs=[h*h/D,k1*h/D,k1*k2/D];r=distribution(float(pH))
                for key,ref in zip(('plus','zero','minus'),refs):
                    self.assertLess(abs(Decimal(str(r[key]))/ref-1),Decimal('1e-13'))

    def test_isoelectric_symmetry_and_nonzero_minor_forms(self):
        for pk1,pk2 in [(2.34,9.6),(2,4),(5,9)]:
            pI=(pk1+pk2)/2;r=distribution(pI,pk1,pk2)
            self.assertAlmostEqual(r['charge'],0,places=14)
            self.assertGreater(r['plus'],0);self.assertGreater(r['minus'],0)
            self.assertLess(r['zero'],1)
            for d in (.5,1,2):
                left=distribution(pI-d,pk1,pk2);right=distribution(pI+d,pk1,pk2)
                self.assertAlmostEqual(left['plus'],right['minus'],places=14)
                self.assertAlmostEqual(left['charge'],-right['charge'],places=14)
        self.assertAlmostEqual(distribution(2.34)['plus'],distribution(2.34)['zero'],places=14)
        self.assertAlmostEqual(distribution(9.6)['zero'],distribution(9.6)['minus'],places=14)

    def test_charge_slope_limits_and_domain(self):
        for pH in (1,3,5.97,8,10,13):
            h=1e-5;r=distribution(pH)
            numerical=(distribution(pH+h)['charge']-distribution(pH-h)['charge'])/(2*h)
            self.assertAlmostEqual(numerical,r['slope'],delta=2e-10)
            self.assertLessEqual(r['slope'],0)
        self.assertGreater(distribution(-20)['charge'],.999999999)
        self.assertLess(distribution(40)['charge'],-.999999999)
        for args in [(float('nan'),),(0,3,2),(101,)]:
            with self.assertRaises(ValueError):distribution(*args)

if __name__=='__main__':unittest.main()
