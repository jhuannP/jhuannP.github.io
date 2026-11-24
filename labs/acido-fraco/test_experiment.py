import unittest
from decimal import Decimal,localcontext
from math import sqrt
from .experiment import solve

class WeakAcidTests(unittest.TestCase):
    def test_balances_and_equilibria(self):
        for C in (0,1e-10,1e-7,1e-4,.01):
            for Ka in (1e-8,1e-5,.01):
                r=solve(C,Ka)
                self.assertAlmostEqual(r['charge']/r['h'],0,delta=1e-12)
                self.assertAlmostEqual(r['h']*r['oh']/1e-14,1,places=12)
                if C:
                    self.assertAlmostEqual((r['acid']+r['anion'])/C,1,places=12)
                    self.assertAlmostEqual(r['h']*r['anion']/r['acid']/Ka,1,places=12)
                    self.assertTrue(0<r['alpha']<1)
                self.assertGreaterEqual(r['h'],1e-7*(1-1e-14))

    def test_independent_decimal_cubic_newton(self):
        with localcontext() as ctx:
            ctx.prec=80
            kw=Decimal('1e-14')
            for C in ('1e-10','1e-7','1e-4','.01'):
                for Ka in ('1e-8','1e-5','.01'):
                    c,k=Decimal(C),Decimal(Ka);h=c+kw.sqrt()
                    for _ in range(250):
                        p=h**3+k*h*h-(kw+k*c)*h-k*kw
                        dp=3*h*h+2*k*h-(kw+k*c)
                        new=h-p/dp
                        if abs(new-h)<h*Decimal('1e-65'):h=new;break
                        h=new
                    self.assertLess(abs(Decimal(str(solve(float(c),float(k))['h']))/h-1),Decimal('1e-13'))

    def test_approximation_regimes_and_dilution(self):
        concentrated=solve(.1,1e-5)
        self.assertLess(abs(concentrated['quadratic']/concentrated['h']-1),1e-6)
        self.assertLess(abs(concentrated['square_root']/concentrated['h']-1),.006)
        dilute=solve(1e-10,1e-5)
        self.assertGreater(dilute['pH_quadratic'],7)
        self.assertLess(dilute['pH'],7)
        self.assertGreater(dilute['h'],1e-10)
        self.assertLess(dilute['anion'],1e-10)
        self.assertGreater(dilute['alpha'],.98)
        previous=0
        for C in (1e-10,1e-8,1e-6,1e-4,.01):
            h=solve(C,1e-5)['h'];self.assertGreater(h,previous);previous=h

    def test_water_limit_constants_and_invalid_inputs(self):
        r=solve(0,1e-5)
        self.assertEqual(r['pH'],7);self.assertIsNone(r['alpha'])
        self.assertIsNone(r['pH_quadratic'])
        # Kw diferente é apenas uma constante de teste, não uma temperatura atribuída.
        self.assertEqual(solve(0,1e-5,1e-12)['pH'],6)
        for args in [(-1,1e-5),(1,0),(1,-1),(float('nan'),1),(1,float('inf'))]:
            with self.assertRaises(ValueError):solve(*args)
        with self.assertRaises(ValueError):solve(1,1,0)

if __name__=='__main__':unittest.main()
