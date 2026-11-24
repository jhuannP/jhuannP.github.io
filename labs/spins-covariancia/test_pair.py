import unittest
from fractions import Fraction as Q
from math import log
from itertools import product
from importlib import import_module
from statmech import canonical,ising_ring
from .pair import STATES,distribution,moments,response
INDEPENDENT=import_module('labs.paramagneto-finito.spin')


class CorrelationTests(unittest.TestCase):
    def test_three_zero_field_references(self):
        self.assertEqual(distribution(3),(Q(3,8),Q(1,8),Q(1,8),Q(3,8)))
        for a,cov,var,chi in [(Q(1,3),Q(-1,2),1,Q(1,2)),(Q(1),Q(0),2,Q(1)),(Q(3),Q(1,2),3,Q(3,2))]:
            r=moments(a)
            self.assertEqual(r['local_means'],(0,0));self.assertEqual(r['covariance'],cov);self.assertEqual(r['variance'],var)
            self.assertEqual(response(a,1,2)['total'],chi)
        self.assertEqual(response(Q(1,3),1,2)['off_diagonal'],Q(-1,4))

    def test_covariance_sum_and_field_reflection(self):
        for a,b in product((Q(1,5),Q(1,3),Q(1),Q(3),Q(7)),(Q(1,4),Q(1,2),Q(1),Q(2),Q(4))):
            r=moments(a,b);opposite=moments(a,1/b)
            self.assertEqual(sum(r['probabilities']),1)
            self.assertEqual(r['variance'],sum(r['local_variances'])+2*r['covariance'])
            self.assertEqual(r['mean'],-opposite['mean'])
            self.assertEqual(r['variance'],opposite['variance']);self.assertEqual(r['covariance'],opposite['covariance'])
            self.assertGreaterEqual(r['variance'],0)
            self.assertEqual(response(a,b,2)['per_spin'],response(a,b,2)['total']/2)

    def test_against_existing_canonical_and_field_derivative(self):
        for a,b,t in product((Q(1,3),Q(1),Q(3)),(Q(1,2),Q(1),Q(2)),(1.,2.,3.)):
            J=t*log(float(a))/2;h=t*log(float(b))/2
            def canonical_at(field):
                energies=[-J*s[0]*s[1]-field*sum(s) for s in STATES]
                prob=canonical(energies,t)['probabilities']
                return prob,sum(p*sum(s) for p,s in zip(prob,STATES))
            probabilities,mean=canonical_at(h);r=moments(a,b)
            for expected,observed in zip(r['probabilities'],probabilities):self.assertAlmostEqual(float(expected),observed,places=13)
            delta=1e-5;derivative=(canonical_at(h+delta)[1]-canonical_at(h-delta)[1])/(2*delta)
            self.assertAlmostEqual(derivative,float(response(a,b,Q(int(t)))['total']),delta=2e-9)

    def test_independent_limit_and_pair_topology(self):
        for b in (Q(1,4),Q(1,2),Q(1),Q(2),Q(4)):
            r=moments(1,b);mean,var=INDEPENDENT.moments(2,b)
            self.assertEqual((r['mean'],r['variance']),(mean,var));self.assertEqual(r['covariance'],0)
        with self.assertRaises(ValueError):ising_ring(2)
        ring=ising_ring(4);prob=canonical(ring['energies'],1)['probabilities']
        self.assertAlmostEqual(sum(p*m for p,m in zip(prob,ring['magnetizations'])),0,places=12)

    def test_old_example_challenge_and_contracts(self):
        self.assertEqual(Q(8,4*2),1);self.assertEqual(Q(8,2),4)
        N,T=4,2;self.assertEqual(N/(N*T),1/T);self.assertEqual(1/T,.5)
        for a,b in [(0,1),(1,0),(-1,1)]:
            with self.assertRaises(ValueError):distribution(a,b)
        for a in (True,1.,'1'):
            with self.assertRaises(TypeError):distribution(a)
        with self.assertRaises(ValueError):response(1,1,0)
