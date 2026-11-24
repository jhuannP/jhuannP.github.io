import unittest
from fractions import Fraction as Q
from .states import cycle,law,metrics

class StateTests(unittest.TestCase):
    def test_reference_and_three_observables(self):
        self.assertEqual(law(1,Q(1,2)),(Q(1,2),Q(1,2),0))
        s=law(2,Q(1,2));self.assertEqual(s,(Q(3,8),Q(3,8),Q(1,4)))
        self.assertEqual(metrics(s),dict(fully=Q(3,8),any_mark=Q(3,4),marked_targets=Q(9,16)))

    def test_independent_strand_and_daughter_enumeration(self):
        # Explicit strand states; select one of two daughters before hypothetical maintenance.
        for state,strands in (((1,0,0),(1,1)),((0,1,0),(1,0)),((0,0,1),(0,0))):
            for p in (Q(0),Q(1,3),Q(1,2),Q(1)):
                result=[Q(0)]*3
                for old in strands:
                    if old:
                        result[0]+=p/2;result[1]+=(1-p)/2
                    else:result[2]+=Q(1,2)
                self.assertEqual(cycle(state,p),tuple(result))

    def test_normalization_and_closed_moment_recursion(self):
        states=((1,0,0),(0,1,0),(0,0,1),(Q(1,3),Q(1,6),Q(1,2)))
        for s in states:
            m0=metrics(s)['marked_targets']
            for p in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
                for n in range(11):
                    r=law(n,p,s);self.assertEqual(sum(r),1);self.assertGreaterEqual(min(r),0)
                    self.assertEqual(metrics(r)['marked_targets'],m0*((1+p)/2)**n)

    def test_no_maintenance_and_perfect_initial_full_state(self):
        for n in range(1,21):
            self.assertEqual(law(n,0),(0,Q(1,2)**(n-1),1-Q(1,2)**(n-1)))
            self.assertEqual(law(n,1),(1,0,0))
        # Same bulk fraction, distinct dyad states; no inference of all dyads from mean.
        a=metrics((0,1,0));b=metrics((Q(1,2),0,Q(1,2)))
        self.assertEqual(a['marked_targets'],b['marked_targets'])
        self.assertNotEqual(a['fully'],b['fully'])
        self.assertEqual(law(1,1,(0,1,0)),(Q(1,2),0,Q(1,2)))

    def test_contracts(self):
        for state in ((1,1,0),(-1,1,1),(True,0,0),(1.0,0,0),(1,0)):
            with self.assertRaises(ValueError):cycle(state,Q(1,2))
        for p in (-1,2,True,.5):
            with self.assertRaises(ValueError):law(2,p)
        for n in (-1,101,True,2.0):
            with self.assertRaises(ValueError):law(n,Q(1,2))
