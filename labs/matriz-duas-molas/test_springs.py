import unittest,itertools
from fractions import Fraction as Q
from .springs import fixed_displacement,fixed_force

class MicroenvironmentSpringTests(unittest.TestCase):
    def test_reference_protocols(self):
        a=fixed_displacement(2,2,2);b=fixed_displacement(8,2,2);c=fixed_force(8,2,2)
        self.assertEqual((a['force'],a['total_energy']),(2,2))
        self.assertEqual((b['force'],b['matrix_extension'],b['cell_extension'],b['total_energy']),(Q(16,5),Q(2,5),Q(8,5),Q(16,5)))
        self.assertEqual((c['force'],c['total_extension'],c['total_energy']),(2,Q(5,4),Q(5,4)))
    def test_balance_hooke_and_energy_on_grid(self):
        count=0
        for km,kc,delta in itertools.product([Q(1,2),2,8],[1,2,4],[0,1,2]):
            r=fixed_displacement(km,kc,delta)
            self.assertEqual(r['matrix_extension']+r['cell_extension'],delta)
            self.assertEqual(km*r['matrix_extension'],r['force'])
            self.assertEqual(kc*r['cell_extension'],r['force'])
            self.assertEqual(r['total_energy'],r['matrix_energy']+r['cell_energy'])
            self.assertEqual(r['total_energy'],r['effective_stiffness']*delta*delta/2);count+=1
        self.assertEqual(count,27)
    def test_independent_constrained_energy_minimum(self):
        # At fixed total extension, vary matrix extension by z and cell by -z.
        for km,kc,delta in itertools.product([1,2,8],[1,3],[1,2]):
            r=fixed_displacement(km,kc,delta);xm,xc=r['matrix_extension'],r['cell_extension']
            for z in [Q(-1,4),Q(-1,10),Q(1,10),Q(1,4)]:
                energy=km*(xm+z)**2/2+kc*(xc-z)**2/2
                self.assertEqual(energy-r['total_energy'],(km+kc)*z*z/2)
                self.assertGreater(energy,r['total_energy'])
    def test_protocol_roundtrip_and_stiff_limit(self):
        for km in [1,2,8,100,10000]:
            a=fixed_displacement(km,2,2);b=fixed_force(km,2,a['force'])
            self.assertEqual(a,b)
        forces=[fixed_displacement(k,2,2)['force'] for k in [1,2,8,100,10000]]
        self.assertEqual(forces,sorted(forces))
        self.assertTrue(all(f<4 for f in forces))
        self.assertLess(4-forces[-1],Q(1,1000))
        for km in [1,2,8]:self.assertEqual(fixed_force(km,2,2)['cell_extension'],1)
    def test_units_scaling_zero_and_contracts(self):
        r=fixed_displacement(2,2,2);b=fixed_displacement(2,2,4)
        self.assertEqual(b['force'],2*r['force']);self.assertEqual(b['total_energy'],4*r['total_energy'])
        self.assertEqual(fixed_displacement(2,2,0)['total_energy'],0)
        for args in [(0,1,1),(1,-1,1),(1,1,-1),(True,1,1),(.5,1,1)]:
            with self.assertRaises(ValueError):fixed_displacement(*args)
        with self.assertRaises(ValueError):fixed_force(1,1,-1)
