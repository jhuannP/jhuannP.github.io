import unittest
from itertools import product
from fractions import Fraction as Q
from .exact import moments

class CovarianceTests(unittest.TestCase):
    def test_affine_two_time_reference(self):
        mu,C=moments([(9,1),(10,3),(11,5)],[1,1,1])
        self.assertEqual(mu,(10,3))
        self.assertEqual(C,((Q(2,3),Q(4,3)),(Q(4,3),Q(8,3))))
        raw=sum(Q(x*y,3) for x,y in [(9,1),(10,3),(11,5)])
        self.assertEqual(raw,Q(94,3))
        self.assertEqual(raw-mu[0]*mu[1],C[0][1])
        self.assertEqual(4*C[0][0]-4*C[0][1]+C[1][1],0)

    def test_zero_covariance_and_dependence(self):
        mu,C=moments([(-1,1),(0,0),(1,1)],[1,1,1])
        self.assertEqual(mu,(0,Q(2,3)))
        self.assertEqual(C,((Q(2,3),0),(0,Q(2,9))))
        rows=[(-1,1),(0,0),(1,1)]
        given=[x for x,y in rows if y==0]
        self.assertEqual(Q(given.count(0),len(given)),1)
        self.assertNotEqual(Q(given.count(0),len(given)),Q(1,3))

    def test_weighting_scaling_translation_and_zero_variance(self):
        rows=[(-1,1),(0,0),(1,1)]
        mu,C=moments(rows,[1,2,1])
        self.assertEqual(C[0][0],Q(1,2))
        moved=[(7-3*x,5+2*y,17) for x,y in rows]
        mu2,C2=moments(moved,[2,4,2])
        self.assertEqual(mu2,(7-3*mu[0],5+2*mu[1],17))
        self.assertEqual(C2[0][0],9*C[0][0])
        self.assertEqual(C2[1][1],4*C[1][1])
        self.assertEqual(C2[0][1],-6*C[0][1])
        self.assertEqual(C2[2],(0,0,0))

    def test_projected_variance_and_invalid_matrix_witnesses(self):
        rows=[(-2,1,3),(0,4,-1),(1,0,2),(3,-1,0)];weights=[1,2,0,3]
        _,C=moments(rows,weights)
        for a in product(range(-2,3),repeat=3):
            values=[sum(ai*xi for ai,xi in zip(a,row)) for row in rows]
            mean=sum(Q(w)*v for w,v in zip(weights,values))/sum(weights)
            direct=sum(Q(w)*(v-mean)**2 for w,v in zip(weights,values))/sum(weights)
            quadratic=sum(Q(a[i])*C[i][j]*a[j] for i in range(3) for j in range(3))
            self.assertEqual(quadratic,direct)
            self.assertGreaterEqual(quadratic,0)
        for bad,a,expected in [(((1,2),(2,1)),(1,-1),-2),
                              (((1,Q(9,10),Q(9,10)),(Q(9,10),1,Q(-9,10)),(Q(9,10),Q(-9,10),1)),(1,-1,-1),Q(-12,5))]:
            witness=sum(Q(a[i])*bad[i][j]*a[j] for i in range(len(a)) for j in range(len(a)))
            self.assertEqual(witness,expected)

    def test_contracts(self):
        for rows,w in [([],[]),([[]],[1]),([(1,),(2,3)],[1,1]),([(1,)],[0]),([(1,)],[True]),([(True,)],[1]),([(1.5,)],[1]),([(1,)],[-1]),([(1,)],[])]:
            with self.assertRaises(ValueError):moments(rows,w)
