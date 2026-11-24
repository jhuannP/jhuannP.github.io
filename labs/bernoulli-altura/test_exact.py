import unittest
from fractions import Fraction as Q
from itertools import product
from .exact import sections

class BernoulliTests(unittest.TestCase):
    def setUp(self):
        self.params=dict(A1=Q(4,10000),A2=Q(1,10000),v1=1,rho=1000,g=10,z1=0,z2=1,p1=200000)

    def test_reference_and_pressure_work(self):
        r=sections(**self.params)
        self.assertEqual(r['flow'],Q(1,2500))
        self.assertEqual(r['v2'],4)
        self.assertEqual((r['dp_kinetic'],r['dp_height'],r['dp']),(-7500,-10000,-17500))
        self.assertEqual(r['p2'],182500)
        self.assertEqual((r['B1'],r['B2']),(200500,200500))
        # Independent unit-volume work balance.
        pressure_work=self.params['p1']-r['p2']
        gain_kinetic=1000*(r['v2']**2-1)/2
        gain_potential=1000*10*(1-0)
        self.assertEqual(pressure_work,gain_kinetic+gain_potential)

    def test_reverse_sections_and_conserve_mass(self):
        for A1,A2,v1,dz in product((Q(1,10000),Q(2,10000),Q(4,10000)),repeat=4):
            args=dict(self.params,A1=A1,A2=A2,v1=v1,z2=dz)
            r=sections(**args)
            reverse=sections(**dict(args,A1=A2,A2=A1,v1=r['v2'],z1=dz,z2=0,p1=r['p2']))
            self.assertEqual(A1*v1,A2*r['v2'])
            self.assertEqual(reverse['p2'],args['p1'])
            self.assertEqual(reverse['v2'],v1)

    def test_pressure_and_height_reference_shifts(self):
        r=sections(**self.params)
        for offset in (-100000,0,75000):
            shifted=sections(**dict(self.params,p1=self.params['p1']+offset))
            self.assertEqual(shifted['dp'],r['dp'])
            self.assertEqual(shifted['p2'],r['p2']+offset)
        shifted=sections(**dict(self.params,z1=7,z2=8))
        self.assertEqual(shifted['dp'],r['dp'])
        self.assertEqual(shifted['B1'],r['B1']+70000)

    def test_static_horizontal_and_descending_limits(self):
        rest=sections(**dict(self.params,v1=0))
        self.assertEqual(rest['flow'],0)
        self.assertEqual(rest['dp'],-10000)
        flat=sections(**dict(self.params,z2=0))
        self.assertEqual(flat['dp'],-7500)
        same=sections(**dict(self.params,A2=self.params['A1'],z2=-1))
        self.assertEqual(same['v2'],1)
        self.assertEqual(same['dp'],10000)
        wider=sections(**dict(self.params,A2=4*self.params['A1'],z2=0))
        self.assertGreater(wider['dp'],0)

    def test_contracts(self):
        for key in self.params:
            for bad in (True,1.0,'1',float('inf')):
                with self.assertRaises(ValueError):sections(**dict(self.params,**{key:bad}))
        for key in ('A1','A2','rho','g'):
            for bad in (0,-1):
                with self.assertRaises(ValueError):sections(**dict(self.params,**{key:bad}))
        with self.assertRaises(ValueError):sections(**dict(self.params,v1=-1))
