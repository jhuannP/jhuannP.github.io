import unittest
from math import log10
from decimal import Decimal,localcontext
from .experiment import solve

class BufferTests(unittest.TestCase):
    def test_mass_charge_and_henderson_equilibrium_identity(self):
        for C in (1e-8,.001,.01):
            for ratio in (.1,.5,.9):
                for dose in (-1.2,-.3,0,.3,1.2):
                    r=solve(C*(1-ratio),C*ratio,C*dose)
                    scale=r['h']+r['sodium']+r['anion']+r['oh']+r['chloride']
                    self.assertLess(abs(r['charge'])/scale,1e-12)
                    self.assertAlmostEqual((r['acid']+r['anion'])/C,1,places=12)
                    self.assertAlmostEqual(r['h']*r['oh']/1e-14,1,places=12)
                    self.assertAlmostEqual(r['pH'],5+log10(r['anion']/r['acid']),places=12)

    def test_independent_decimal_cubic(self):
        with localcontext() as ctx:
            ctx.prec=80;Ka=Decimal('1e-5');Kw=Decimal('1e-14')
            for ca,cs in [('0.005','0.005'),('0','0.01'),('0.000000005','0.000000005')]:
                for dose in ('-1.2','0','.3','1.2'):
                    Ca,Cs=Decimal(ca),Decimal(cs);C=Ca+Cs;q=C*Decimal(dose);S=Cs+q
                    b=S-C;h=(-b+(b*b+4*Kw).sqrt())/2
                    for _ in range(300):
                        p=h**3+(Ka+S)*h*h+(Ka*(S-C)-Kw)*h-Ka*Kw
                        dp=3*h*h+2*(Ka+S)*h+Ka*(S-C)-Kw
                        new=h-p/dp
                        if abs(new-h)<h*Decimal('1e-60'):h=new;break
                        h=new
                    r=solve(float(Ca),float(Cs),float(q))
                    self.assertLess(abs(Decimal(str(r['h']))/h-1),Decimal('2e-12'))

    def test_capacity_is_local_and_dilution_limits_hh(self):
        for q in (-.003,0,.003):
            r=solve(.005,.005,q);step=1e-8
            dpdq=(solve(.005,.005,q+step)['pH']-solve(.005,.005,q-step)['pH'])/(2*step)
            self.assertAlmostEqual(r['beta'],1/dpdq,delta=2e-10)
        self.assertLess(abs(solve(.005,.005)['pH']-5),.002)
        self.assertGreater(abs(solve(5e-9,5e-9)['pH']-5),1.9)
        self.assertIsNone(solve(.005,.005,.006)['hh'])
        self.assertIsNone(solve(.005,.005,-.006)['hh'])
        self.assertGreater(solve(.005,.005,.006)['pH'],10)

    def test_salt_acid_water_and_domain(self):
        self.assertGreater(solve(0,.01)['pH'],7)
        self.assertAlmostEqual(solve(.01,0)['pH'],3.506866489839185,places=12)
        self.assertEqual(solve(0,0)['pH'],7)
        acid=solve(0,0,-.001);base=solve(0,0,.001)
        self.assertAlmostEqual(acid['pH'],3,places=7)
        self.assertAlmostEqual(base['pH'],11,places=7)
        self.assertGreater(solve(.005,.005,.001)['pH'],solve(.005,.005)['pH'])
        for args in [(-1,0),(0,-1),(0,0,float('nan'))]:
            with self.assertRaises(ValueError):solve(*args)
        with self.assertRaises(ValueError):solve(0,0,Ka=0)

if __name__=='__main__':unittest.main()
