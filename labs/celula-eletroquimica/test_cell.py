import math
import unittest
from decimal import Decimal, localcontext
from .cell import R,F,state,log_quotient

class CellTests(unittest.TestCase):
    def test_standard_case_and_equilibrium(self):
        s=state(.60,2,300.,0.)
        self.assertEqual(s['E_V'],.60)
        self.assertAlmostEqual(s['delta_r_G_J_mol'],-115782.398544,places=6)
        equilibrium=state(.60,2,300.,s['ln_K'])
        self.assertAlmostEqual(equilibrium['E_V'],0.,places=14)
        self.assertAlmostEqual(equilibrium['delta_r_G_J_mol'],0.,places=8)
        self.assertGreater(state(.60,2,300.,s['ln_K']-1)['E_V'],0)
        self.assertLess(state(.60,2,300.,s['ln_K']+1)['E_V'],0)

    def test_decimal_oracle_for_chemical_gibbs_route(self):
        # Independent route: chemical free energy, Decimal logarithm, then work/charge.
        with localcontext() as ctx:
            ctx.prec=50
            for t in (275,300,350):
                for n in (1,2,4):
                    for e0 in (-.2,0.,.6):
                        for am,an in ((1,1),(100,1),(1,100),(3,7)):
                            s=state(e0,n,t,log_quotient(am,an))
                            rd,fd=Decimal(str(R)),Decimal(str(F))
                            dg0=-Decimal(n)*fd*Decimal(str(e0))
                            dg=dg0+rd*Decimal(t)*(Decimal(am)/Decimal(an)).ln()
                            self.assertAlmostEqual(s['delta_r_G_J_mol'],float(dg),delta=1e-8)
                            self.assertAlmostEqual(s['E_V'],float(-dg/(Decimal(n)*fd)),places=13)

    def test_reverse_and_rescale_reaction(self):
        for lq in (-20.,0.,10.,100.):
            a=state(.6,2,300,lq)
            reverse=state(-.6,2,300,-lq)
            self.assertAlmostEqual(reverse['E_V'],-a['E_V'])
            self.assertAlmostEqual(reverse['delta_r_G_J_mol'],-a['delta_r_G_J_mol'])
            for factor in (2,3,5):
                b=state(.6,2*factor,300,factor*lq)
                self.assertAlmostEqual(b['E_V'],a['E_V'])
                self.assertAlmostEqual(b['delta_r_G_J_mol'],factor*a['delta_r_G_J_mol'])
                self.assertAlmostEqual(b['ln_K'],factor*a['ln_K'])

    def test_log_activities_without_forming_ratio(self):
        lq=log_quotient(1e300,1e-300)
        self.assertTrue(math.isfinite(lq))
        self.assertAlmostEqual(lq,600*math.log(10),places=10)
        self.assertTrue(math.isfinite(state(.6,2,300,lq)['E_V']))
        for scale in (.001,2,1e100):
            self.assertAlmostEqual(log_quotient(3*scale,7*scale),math.log(3/7),places=12)

    def test_contracts(self):
        for n in (True,2.,'2'):
            with self.assertRaises(TypeError):state(.6,n,300,0)
        for n in (0,-2):
            with self.assertRaises(ValueError):state(.6,n,300,0)
        for t in (0,-273.,float('nan'),float('inf')):
            with self.assertRaises(ValueError):state(.6,2,t,0)
        for a in (0.,-1.,float('nan'),float('inf')):
            with self.assertRaises(ValueError):log_quotient(a,1.)
        with self.assertRaises(TypeError):log_quotient(True,1.)
        with self.assertRaises(TypeError):state('0.6',2,300,0)
        with self.assertRaises(ValueError):state(.6,2,300,float('inf'))
        with self.assertRaises(ValueError):state(.6,2,10**1000,0)
        with self.assertRaises(ValueError):state(.6,10**1000,300,0)

if __name__ == "__main__":unittest.main()
