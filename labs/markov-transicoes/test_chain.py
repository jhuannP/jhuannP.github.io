import unittest
from itertools import product
from fractions import Fraction as F
from .chain import step,orbit,two_state,stationary_two,first_hit_tail,first_hit_mean,P

class ChainTests(unittest.TestCase):
    def test_path_enumeration(self):
        # Independent sum over explicit state paths, not repeated vector multiplication.
        for start in ((F(1),F(0)),(F(1,3),F(2,3))):
            for n in range(7):
                totals=[F(0),F(0)]
                for states in product(range(2),repeat=n+1):
                    weight=start[states[0]]
                    for i,j in zip(states,states[1:]):weight*=P[i][j]
                    totals[states[-1]]+=weight
                self.assertEqual(orbit(start,P,n)[-1],tuple(totals))
                self.assertEqual(sum(totals),1)

    def test_closed_form_grid(self):
        for alpha,beta in product((F(0),F(1,4),F(1,2),F(3,4),F(1)),repeat=2):
            Q=two_state(alpha,beta)
            for a0 in (F(0),F(1,2),F(1)):
                values=orbit((a0,1-a0),Q,8)
                for n,v in enumerate(values):
                    expected=a0 if alpha+beta==0 else beta/(alpha+beta)+(1-alpha-beta)**n*(a0-beta/(alpha+beta))
                    self.assertEqual(v,(expected,1-expected))
                    self.assertTrue(all(x>=0 for x in v));self.assertEqual(sum(v),1)
            if alpha+beta>0:
                pi=stationary_two(alpha,beta)
                self.assertEqual(step(pi,Q),pi)
        vals=orbit((1,0),P,4)
        self.assertGreater(vals[3][0]-F(2,3),F(1,100))
        self.assertLess(vals[4][0]-F(2,3),F(1,100))

    def test_periodicity_and_hitting(self):
        flip=two_state(1,1)
        self.assertEqual(stationary_two(1,1),(F(1,2),F(1,2)))
        self.assertEqual(orbit((1,0),flip,3),((1,0),(0,1),(1,0),(0,1)))
        for pi in ((1,0),(0,1),(F(1,3),F(2,3))):self.assertEqual(step(pi,two_state(0,0)),pi)
        self.assertEqual(first_hit_mean(F(1,5)),5)
        self.assertEqual(first_hit_mean(F(1,10)),10)
        self.assertEqual(stationary_two(F(1,5),F(2,5)),stationary_two(F(1,10),F(1,5)))
        # First-hit mass through step 10 plus survival after 10 is exactly one.
        alpha=F(1,5)
        self.assertEqual(sum(first_hit_tail(alpha,n-1)*alpha for n in range(1,11))+first_hit_tail(alpha,10),1)
        self.assertEqual(first_hit_tail(alpha,3),F(64,125))

    def test_contract_and_input_preservation(self):
        p=[1,0];q=[[F(4,5),F(1,5)],[F(2,5),F(3,5)]]
        before=(p.copy(),[row.copy() for row in q]);step(p,q);self.assertEqual((p,q),before)
        for bad in ([[1,1],[0,1]],[[1,0],[1]],[[F(-1,2),F(3,2)],[0,1]]):
            with self.assertRaises(ValueError):step((1,0),bad)
        with self.assertRaises(ValueError):step((1,),P)
        with self.assertRaises(TypeError):two_state(0.2,F(2,5))
        with self.assertRaises(TypeError):orbit((1,0),P,True)
        with self.assertRaises(ValueError):orbit((1,0),P,101)
        with self.assertRaises(ValueError):stationary_two(0,0)
        with self.assertRaises(ValueError):first_hit_mean(0)
