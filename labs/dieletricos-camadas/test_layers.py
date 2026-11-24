import unittest
from fractions import Fraction as Q
from itertools import product
from .layers import solve,potential


class LayeredCapacitor(unittest.TestCase):
    def test_original_examples(self):
        a=solve(2,5,1,2,Q(9,5))
        for key,val in dict(D1=2,D2=2,E1=1,E2=Q(2,5),phi_interface=Q(4,5),
                            capacity=Q(10,9),energy=Q(9,5),bound_interface=Q(-3,5)).items():
            self.assertEqual(a[key],val,key)
        b=solve(2,5,1,2,Q(9,5),1)
        for key,val in dict(D1=Q(14,9),D2=Q(23,9),E1=Q(7,9),E2=Q(23,45),
                            phi_interface=Q(46,45),energy=Q(86,45),
                            bound_interface=Q(-19,15)).items():
            self.assertEqual(b[key],val,key)
        self.assertNotEqual(b['energy'],b['free_bottom']*b['voltage']/2)
        self.assertEqual(b['energy']-b['free_bottom']*b['voltage']/2,Q(23,45))

    def test_nodal_potential_oracle_and_charge_ledgers(self):
        # Different unknown: nodal phi, derived from incoming/outgoing free flux.
        for k1,k2,d1,d2,V,s in product([1,2,5],[1,3,7],[1,2],[1,3],[-2,0,3],[-1,0,1]):
            a=solve(k1,k2,d1,d2,V,s)
            phi=(Q(s)+Q(k1*V,d1))/(Q(k1,d1)+Q(k2,d2))
            E1=(V-phi)/d1; E2=phi/d2
            self.assertEqual((a['E1'],a['E2'],a['phi_interface']),(E1,E2,phi))
            self.assertEqual(k2*E2-k1*E1,s)
            self.assertEqual(a['free_bottom']+s+a['free_top'],0)
            self.assertEqual(a['bound_bottom']+a['bound_interface']+a['bound_top'],0)
            self.assertEqual(s+a['bound_interface'],E2-E1)
            self.assertEqual(a['bound_bottom']+a['free_bottom'],E1)
            self.assertEqual(a['bound_top']+a['free_top'],-E2)
            self.assertEqual(potential(a,0),V)
            self.assertEqual(potential(a,d1),phi)
            self.assertEqual(potential(a,d1+d2),0)
            for z in [Q(d1,3),Q(2*d1,3)]:
                h=Q(d1,10)
                self.assertEqual(-(potential(a,z+h)-potential(a,z-h))/(2*h),E1)

    def test_energy_by_independent_linear_potential_integral(self):
        # For a linear potential, U=1/2 sum(surface free charge * potential).
        # No constitutive expression for energy used on this side of the equality.
        for V,s in product([-3,-1,0,2,4],[-2,0,1,3]):
            a=solve(2,5,1,2,V,s)
            by_charges=(a['free_bottom']*V+s*a['phi_interface'])/2
            self.assertEqual(a['energy'],by_charges)
            self.assertGreaterEqual(a['energy'],0)
            if V or s:self.assertGreater(a['energy'],0)
            else:self.assertEqual(a['energy'],0)

    def test_homogeneous_split_and_order_without_free_sheet(self):
        for k,L,a,V in product([1,2,5],[2,4],[Q(1,4),Q(3,4)],[-3,0,2]):
            d1=a*L;d2=L-d1
            x=solve(k,k,d1,d2,V)
            self.assertEqual(x['capacity'],Q(k,L))
            self.assertEqual((x['E1'],x['E2']),(Q(V,L),Q(V,L)))
            self.assertEqual(x['bound_interface'],0)
        for k1,k2,d1,d2 in product([1,2,5],[1,3],[1,2],[1,3]):
            x=solve(k1,k2,d1,d2,3);y=solve(k2,k1,d2,d1,3)
            self.assertEqual((x['capacity'],x['D1'],x['energy']),
                             (y['capacity'],y['D1'],y['energy']))
            self.assertEqual(x['phi_interface']+y['phi_interface'],3)

    def test_affine_response_at_fixed_sheet_and_sign_reversal(self):
        for s in [-2,0,1,3]:
            a=solve(2,5,1,2,-1,s);b=solve(2,5,1,2,2,s)
            self.assertEqual((b['free_bottom']-a['free_bottom'])/3,Q(10,9))
            r=solve(2,5,1,2,1,-s)
            for key in ['D1','D2','E1','E2','P1','P2','phi_interface',
                        'free_bottom','free_top','bound_bottom','bound_interface','bound_top']:
                self.assertEqual(r[key],-a[key],key)
            self.assertEqual(r['energy'],a['energy'])
        zero=solve(2,5,1,2,0,1)
        self.assertNotEqual(zero['free_bottom'],0)
        self.assertGreater(zero['energy'],0)

    def test_contracts(self):
        good=[2,5,1,2,Q(9,5),0]
        for i in range(6):
            for bad in [True,1.0,'2',None]:
                args=good.copy();args[i]=bad
                with self.assertRaises(ValueError):solve(*args)
        for i in range(4):
            for bad in [0,-1]:
                args=good.copy();args[i]=bad
                with self.assertRaises(ValueError):solve(*args)
        x=solve(*good)
        for z in [-1,4,True,.5]:
            with self.assertRaises(ValueError):potential(x,z)
