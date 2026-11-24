import unittest
from fractions import Fraction as Q
from itertools import product
from .induction import force,dot,fixed_loop,mean_emf


class InductionTests(unittest.TestCase):
    def test_force_sign_and_orthogonality(self):
        self.assertEqual(force(1,(2,0,0),(0,0,3)),(0,-6,0))
        self.assertEqual(force(-1,(2,0,0),(0,0,3)),(0,6,0))
        vectors=list(product((-1,0,1),repeat=3))
        for v in vectors:
            for b in vectors:
                f=force(2,v,b)
                self.assertEqual(dot(f,v),0);self.assertEqual(dot(f,b),0)
                self.assertEqual(force(-2,v,b),tuple(-x for x in f))
                self.assertEqual(force(2,b,v),tuple(-x for x in f))

    def test_flux_projection_and_unchanging_field(self):
        a=(0,0,Q(1,5))
        r=fixed_loop(a,(0,0,3),(0,0,0),4)
        self.assertEqual(r['flux'],Q(3,5));self.assertEqual(r['emf'],0)
        self.assertEqual(fixed_loop(a,(3,0,0),(2,0,0),4)['emf'],0)
        self.assertEqual(dot((1,2,3),(4,5,6)),32)

    def test_affine_derivative_from_independent_endpoints(self):
        for a,b0,rate in product((Q(-2),Q(1,5),Q(3)),repeat=3):
            for start,dt in [(0,Q(1,2)),(2,3),(5,Q(7,3))]:
                r=fixed_loop((0,0,a),(0,0,b0),(0,0,rate),4,start,3)
                first=(b0+rate*start)*a;last=(b0+rate*(start+dt))*a
                self.assertEqual(r['flux'],first)
                self.assertEqual(r['emf'],mean_emf(first,last,dt,3))
                self.assertEqual(r['emf']*r['current'],r['power'])

    def test_orientation_and_rotation(self):
        a=(Q(1,5),Q(1,3),Q(1,2));b=(1,2,3);rate=(2,-1,4)
        r=fixed_loop(a,b,rate,4)
        rev=fixed_loop(tuple(-x for x in a),b,rate,4)
        for key in ('flux','flux_rate','emf','current'):self.assertEqual(rev[key],-r[key])
        self.assertEqual(rev['power'],r['power'])
        rotate=lambda v:(-v[1],v[0],v[2])
        self.assertEqual(fixed_loop(rotate(a),rotate(b),rotate(rate),4),r)
        up=fixed_loop((0,0,Q(1,5)),(0,0,1),(0,0,2),4)
        down=fixed_loop((0,0,Q(1,5)),(0,0,1),(0,0,-2),4)
        self.assertEqual(up['current'],Q(-1,10));self.assertEqual(down['current'],Q(1,10))
        self.assertEqual(up['power'],Q(1,25))

    def test_original_and_contracts(self):
        self.assertEqual(mean_emf(0,6,3),-2)
        self.assertEqual(mean_emf(5,5,2),0)
        for args in [(0,6,0,1),(0,6,1,True),(0,6,1,0),(0.0,6,1,1)]:
            with self.assertRaises(ValueError):mean_emf(*args)
        for a,r,t in [((0,0,0),4,0),((0,0,1),0,0),((0,0,1),4,-1),((0,1),4,0),((0,0,True),4,0)]:
            with self.assertRaises(ValueError):fixed_loop(a,(0,0,1),(0,0,2),r,t)
