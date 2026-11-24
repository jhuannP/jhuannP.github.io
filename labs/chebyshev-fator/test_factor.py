from fractions import Fraction as Q
from math import cos,pi,prod
from pathlib import Path
import json
import unittest
from .factor import coefficients,monic,evaluate,fixture,error,interpolant,sup_error,mapped_error,base

class ChebyshevTests(unittest.TestCase):
    def test_coefficients(self):
        self.assertEqual(coefficients(0),(1,))
        self.assertEqual(coefficients(4),(1,0,-8,0,8))
        self.assertEqual(monic(4),(Q(1,8),0,-1,0,1))
    def test_trigonometric_reference(self):
        for n in range(1,13):
            self.assertEqual(monic(n)[-1],1)
            for j in range(21):
                theta=j*pi/20;x=cos(theta)
                # Horner float independente de recurrence em produção.
                value=sum(float(c)*x**k for k,c in enumerate(coefficients(n)))
                self.assertAlmostEqual(value,cos(n*theta),places=8)
        roots=[cos((2*k+1)*pi/8) for k in range(4)]
        for j in range(33):
            x=-1+j/16
            self.assertAlmostEqual(prod(x-r for r in roots),float(error(Q(j,16)-1,'roots')),places=13)
    def test_rational_interpolation_and_factor(self):
        for family in ('uniform','lobatto'):
            xs,c=fixture(family);ys=tuple(x**4 for x in xs)
            for j in range(33):
                x=Q(j,16)-1
                direct=base.lagrange(xs,ys,x)
                self.assertEqual(interpolant(x,family),direct)
                self.assertEqual(error(x,family),prod(x-node for node in xs))
    def test_uniform_norms_and_pointwise_counterexample(self):
        self.assertEqual(sup_error('uniform'),Q(16,81))
        self.assertEqual(sup_error('lobatto'),Q(1,4))
        self.assertEqual(sup_error('roots'),Q(1,8))
        self.assertGreater(sup_error('lobatto'),sup_error('uniform'))
        self.assertEqual(error(1,'uniform'),0)
        self.assertEqual(error(1,'roots'),Q(1,8))
        self.assertEqual(interpolant(0,'lobatto'),Q(-1,4))
        self.assertEqual(interpolant(0,'uniform'),Q(-1,9))
        for family in ('uniform','lobatto','roots'):
            for j in range(65):self.assertLessEqual(abs(error(Q(j,32)-1,family)),sup_error(family))
    def test_interval_mapping(self):
        for family in ('uniform','lobatto','roots'):
            for x in (2,3,4,5,6):
                self.assertEqual(mapped_error(x,family,2,6),16*error(Q(x-4,2),family))
        self.assertEqual(mapped_error(2,'roots',2,6),2)
        with self.assertRaises(ValueError):mapped_error(0,'roots',1,1)
    def test_preserved_material_and_contracts(self):
        ls=json.loads((Path(__file__).resolve().parents[2]/'content/lessons.json').read_text())
        l=next(x for x in ls if x['id']=='nos-chebyshev')
        exec(l['python'],{});exec(l['codingPractice']['solution'],{})
        for bad in (True,1.,-1,17):
            with self.assertRaises(ValueError):coefficients(bad)
        with self.assertRaises(ValueError):fixture('outro')
        with self.assertRaises(ValueError):error(.5,'roots')
if __name__=='__main__':unittest.main()
