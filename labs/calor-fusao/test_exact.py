import unittest
from fractions import Fraction as Q
from itertools import product
from .exact import solve

class FusionTests(unittest.TestCase):
    def setUp(self):self.args=dict(ice=Q(1,10),water=Q(1,5),Tw=20,c=4200,L=336000,Ccal=0)

    def test_partial_exact_and_boundary(self):
        r=solve(**self.args)
        self.assertEqual((r['available'],r['needed']),(16800,33600))
        self.assertEqual((r['Tf'],r['melted'],r['ice_remaining'],r['liquid']),(0,Q(1,20),Q(1,20),Q(1,4)))
        r=solve(**dict(self.args,Tw=40))
        self.assertEqual((r['regime'],r['Tf'],r['ice_remaining']),('liquid_at_zero',0,0))
        r=solve(**dict(self.args,Tw=60))
        self.assertEqual(r['Tf'],Q(40,3))
        self.assertEqual(r['ice_remaining'],0)

    def test_container_and_heat_sign_ledger(self):
        r=solve(**dict(self.args,Ccal=210))
        self.assertEqual(r['available'],21000)
        self.assertEqual((r['melted'],r['ice_remaining']),(Q(1,16),Q(3,80)))
        # Heat of the initially warm water and vessel, plus gain of original ice.
        for Tw,Ccal in product((0,20,40,60,99),(0,210,420)):
            r=solve(**dict(self.args,Tw=Tw,Ccal=Ccal));Tf=r['Tf']
            warm=Q(1,5)*4200*(Tf-Tw)
            vessel=Ccal*(Tf-Tw)
            original_ice=r['melted']*336000+r['melted']*4200*Tf
            self.assertEqual(warm+vessel+original_ice,0)

    def test_conservation_mass_energy_and_regimes(self):
        for ice,water,Tw,Ccal in product((Q(0),Q(1,20),Q(1,10)),(Q(1,10),Q(1,5)),(0,10,20,40,60,99),(0,210)):
            r=solve(**dict(self.args,ice=ice,water=water,Tw=Tw,Ccal=Ccal))
            self.assertEqual(r['H_initial'],r['H_final'])
            self.assertEqual(r['ice_remaining']+r['liquid'],ice+water)
            self.assertTrue(0<=r['melted']<=ice)
            self.assertTrue(0<=r['Tf']<=Tw)
            if r['ice_remaining']>0:self.assertEqual(r['Tf'],0)
            if r['Tf']>0:self.assertEqual(r['ice_remaining'],0)

    def test_near_threshold_and_scaling(self):
        for delta in (Q(-1,1000),Q(0),Q(1,1000)):
            r=solve(**dict(self.args,Tw=40+delta))
            if delta<0:self.assertGreater(r['ice_remaining'],0)
            if delta==0:self.assertEqual(r['regime'],'liquid_at_zero')
            if delta>0:self.assertGreater(r['Tf'],0)
        for Tw in (20,40,60):
            r=solve(**dict(self.args,Tw=Tw,Ccal=210))
            s=solve(**dict(self.args,Tw=Tw,ice=Q(1,5),water=Q(2,5),Ccal=420))
            self.assertEqual(s['Tf'],r['Tf'])
            self.assertEqual(s['melted'],2*r['melted'])

    def test_contracts(self):
        for key in self.args:
            for bad in (True,1.0,'1',float('nan')):
                with self.assertRaises(ValueError):solve(**dict(self.args,**{key:bad}))
        for changes in ({'ice':-1},{'water':0},{'Tw':-1},{'Tw':100},{'c':0},{'L':0},{'Ccal':-1}):
            with self.assertRaises(ValueError):solve(**dict(self.args,**changes))
