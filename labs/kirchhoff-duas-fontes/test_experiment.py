import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import solve

class KirchhoffNetworkTests(unittest.TestCase):
    def test_lesson_case(self):
        x=solve(12,6,2,3,6)
        self.assertEqual((x['u'],x['i1'],x['i2'],x['i3']),(8,2,Q(-2,3),Q(4,3)))
        self.assertEqual(x['dissipated'],(8,Q(4,3),Q(32,3)))
        self.assertEqual(x['delivered'],(24,-4))

    def test_independent_two_mesh_solution(self):
        for e1,e2 in product((-6,0,6,12),repeat=2):
            for r1,r2,r3 in product((Q(1,2),Q(2),Q(3)),repeat=3):
                x=solve(e1,e2,r1,r2,r3)
                det=(r1+r3)*(r2+r3)-r3*r3
                a=(e1*(r2+r3)-r3*e2)/det
                b=((r1+r3)*e2-r3*e1)/det
                self.assertEqual(x['i1'],a)
                self.assertEqual(x['i2'],b)
                self.assertEqual(x['i3'],a+b)
                self.assertEqual(x['u'],r3*(a+b))

    def test_conservation_and_oriented_loops(self):
        for e1,e2 in product((-12,0,6,12),repeat=2):
            for r1,r2,r3 in product((1,2,3),repeat=3):
                x=solve(e1,e2,r1,r2,r3)
                self.assertEqual(x['i1']+x['i2']-x['i3'],0)
                self.assertEqual(e1-r1*x['i1']-x['u'],0)
                self.assertEqual(e2-r2*x['i2']-x['u'],0)
                self.assertEqual(sum(x['delivered']),sum(x['dissipated']))
                self.assertTrue(all(p>=0 for p in x['dissipated']))

    def test_scaling_swapping_and_zero_sources(self):
        x=solve(12,6,2,3,6);y=solve(24,12,2,3,6);z=solve(12,6,4,6,12)
        self.assertEqual(y['u'],2*x['u'])
        for key in ('i1','i2','i3'):self.assertEqual(y[key],2*x[key]);self.assertEqual(z[key],x[key]/2)
        self.assertEqual(z['u'],x['u'])
        swapped=solve(6,12,3,2,6)
        self.assertEqual(swapped['i1'],x['i2']);self.assertEqual(swapped['i2'],x['i1'])
        zero=solve(0,0,2,3,6)
        self.assertTrue(all(zero[k]==0 for k in ('u','i1','i2','i3')))

    def test_contract(self):
        for args in [(12,6,0,3,6),(12,6,-2,3,6),(12,6,2,3,0),(True,6,2,3,6),(12.,6,2,3,6),(12,6,2,3,None)]:
            with self.assertRaises(ValueError):solve(*args)
