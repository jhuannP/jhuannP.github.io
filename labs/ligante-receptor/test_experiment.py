import math,unittest
from decimal import Decimal,localcontext
from .experiment import binding,model


def decimal_root(total,receptors,kd):
    with localcontext() as ctx:
        ctx.prec=70
        L,R,K=map(lambda v:Decimal(str(v)),(total,receptors,kd))
        lo,hi=Decimal(0),min(L,R)
        for _ in range(240):
            c=(lo+hi)/2
            residual=(R-c)*(L-c)-K*c
            if residual>0:lo=c
            else:hi=c
        return float((lo+hi)/2)


class ReceptorTests(unittest.TestCase):
    def test_independent_decimal_root(self):
        for R in (.5,2,5):
            for K in (.5,1,4):
                for L in (0,.5,2,5,10):
                    s=binding(L,R,K)
                    self.assertAlmostEqual(s['complex'],decimal_root(L,R,K),places=13)
                    self.assertGreaterEqual(s['complex'],0)
                    self.assertLessEqual(s['complex'],min(L,R))
                    self.assertAlmostEqual(s['free_receptor']*s['free_ligand'],K*s['complex'],places=12)

    def test_half_occupancy_and_free_total_distinction(self):
        for R in (.5,1,2,5):
            for K in (.5,1,2,4):
                s=binding(K+R/2,R,K)
                self.assertAlmostEqual(s['fraction'],.5,places=14)
                self.assertAlmostEqual(s['free_ligand'],K,places=14)
                self.assertAlmostEqual(s['free_receptor'],R/2,places=14)
                self.assertGreater(s['approximation'],s['fraction'])
        self.assertEqual(model()['complex'],1)
        self.assertAlmostEqual(model()['approximation'],2/3)

    def test_inventories_monotonicity_and_dilute_receptors(self):
        for R,K in ((.5,.5),(2,1),(5,4)):
            previous=-1
            for i in range(101):
                L=i/10;s=binding(L,R,K)
                self.assertAlmostEqual(s['complex']+s['free_ligand'],L,places=14)
                self.assertAlmostEqual(s['complex']+s['free_receptor'],R,places=14)
                self.assertGreaterEqual(s['fraction']+1e-14,previous)
                self.assertGreaterEqual(s['approximation']+1e-14,s['fraction'])
                previous=s['fraction']
        self.assertGreater(binding(2,2,.5)['fraction'],binding(2,2,4)['fraction'])
        self.assertLess(binding(2,5,1)['free_ligand'],binding(2,.5,1)['free_ligand'])
        self.assertAlmostEqual(binding(2,1e-7,1)['fraction'],2/3,delta=2e-8)

    def test_kinetic_signs_and_contract(self):
        for L,R,K in ((2,2,1),(.5,5,4),(10,.5,.5)):
            c=binding(L,R,K)['complex']
            rate=lambda z:(R-z)*(L-z)-K*z # kon=1, koff=Kd, hypothetical units.
            self.assertAlmostEqual(rate(c),0,places=12)
            self.assertGreater(rate(c/2),0)
            self.assertLess(rate((c+min(L,R))/2),0)
        self.assertIsNone(binding(0,2,1)['depletion'])
        for args in ((-1,2,1),(2,0,1),(2,2,0)):
            with self.assertRaises(ValueError):binding(*args)
        with self.assertRaises(ValueError):model(11,2,1)
        with self.assertRaises(ValueError):binding(float('nan'),2,1)
