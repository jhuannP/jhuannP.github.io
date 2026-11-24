import unittest
from fractions import Fraction as Q
from itertools import product
from .exact import distribution, unique_stationary

class TwoStateTests(unittest.TestCase):
    def test_path_enumeration(self):
        for a,b in product([Q(i,4) for i in range(5)], repeat=2):
            P=((1-a,a),(b,1-b))
            for initial,n in product((0,1),range(7)):
                result=[Q(0),Q(0)]
                for tail in product((0,1),repeat=n):
                    prev=initial; weight=Q(1)
                    for state in tail:
                        weight*=P[prev][state]; prev=state
                    result[prev]+=weight
                actual=distribution(a,b,int(initial==0),n)
                self.assertEqual(actual,tuple(result))
                self.assertEqual(sum(actual),1)
                self.assertTrue(all(x>=0 for x in actual))

    def test_closed_form_for_mixed_initial_distributions(self):
        for a,b,q,n in product([Q(i,4) for i in range(5)],repeat=4):
            # n above is reused only as a small integer index, not as probability.
            steps=int(4*n)
            expected=q if a+b==0 else b/(a+b)+(q-b/(a+b))*(1-a-b)**steps
            self.assertEqual(distribution(a,b,q,steps)[0],expected)

    def test_stationarity_and_nonconvergence(self):
        for a,b in product([Q(i,4) for i in range(5)],repeat=2):
            pi=unique_stationary(a,b)
            if pi is None:
                self.assertEqual((a,b),(0,0))
                self.assertEqual(distribution(a,b,Q(2,7),9),(Q(2,7),Q(5,7)))
            else:
                self.assertEqual(distribution(a,b,pi[0],1),pi)
        self.assertEqual(unique_stationary(1,1),(Q(1,2),Q(1,2)))
        self.assertEqual(distribution(1,1,1,8),(1,0))
        self.assertEqual(distribution(1,1,1,9),(0,1))

    def test_lesson_reference_and_dependence(self):
        a,b=Q(1,5),Q(1,10)
        self.assertEqual(distribution(a,b,1,2),(Q(33,50),Q(17,50)))
        self.assertEqual(distribution(a,b,1,3)[0],Q(281,500))
        self.assertNotEqual(Q(4,5)**2,distribution(a,b,1,2)[0])
        pi=unique_stationary(a,b)
        self.assertEqual(pi,(Q(1,3),Q(2,3)))
        self.assertNotEqual(pi[0]*Q(4,5),pi[0]**2)

    def test_invalid_inputs(self):
        for x in (True,0.2,float('nan'),-1,Q(3,2),'1/2'):
            for args in ((x,0,1),(0,x,1),(0,0,x)):
                with self.assertRaises(ValueError):distribution(*args,1)
        for n in (True,-1,201,1.5):
            with self.assertRaises(ValueError):distribution(0,0,1,n)
