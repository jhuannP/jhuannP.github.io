import unittest
from fractions import Fraction as F
from math import comb
from .curves import triangle,evaluate,split,derivative

P=((0,0),(1,2),(2,2),(3,0))


def bernstein(p,t):
    n=len(p)-1
    weights=[F(comb(n,i))*t**i*(1-t)**(n-i) for i in range(n+1)]
    return tuple(sum((w*q[j] for w,q in zip(weights,p)),F(0)) for j in range(len(p[0])))


class CurveTests(unittest.TestCase):
    def test_literal_triangle_and_polynomial(self):
        rows=triangle(P,F(1,2))
        self.assertEqual(rows[1],((F(1,2),1),(F(3,2),2),(F(5,2),1)))
        self.assertEqual(rows[2],((1,F(3,2)),(2,F(3,2))))
        self.assertEqual(rows[3],((F(3,2),F(3,2)),))
        for i in range(17):
            t=F(i,16)
            self.assertEqual(evaluate(P,t),(3*t,6*t*(1-t)))
        self.assertEqual(evaluate(P,0),P[0]);self.assertEqual(evaluate(P,1),P[-1])

    def test_independent_bernstein_reference(self):
        for n in range(7):
            p=tuple((i-n,i*i-n,(-1)**i*(i+1)) for i in range(n+1))
            for j in range(9):
                t=F(j,8);value=evaluate(p,t)
                self.assertEqual(value,bernstein(p,t))
                self.assertEqual(sum(F(comb(n,i))*t**i*(1-t)**(n-i) for i in range(n+1)),1)
                for k in range(3):self.assertTrue(min(q[k] for q in p)<=value[k]<=max(q[k] for q in p))

    def test_affine_invariance_and_perturbation(self):
        transform=lambda q:(2*q[0]+q[1]-2,-q[0]+3*q[1]+4)
        shifted=[(0,0),(1,3),(2,2),(3,0)] # Only P1_y changes by one.
        for j in range(9):
            t=F(j,8)
            self.assertEqual(evaluate([transform(p) for p in P],t),transform(evaluate(P,t)))
            before=evaluate(P,t);after=evaluate(shifted,t)
            self.assertEqual(after[1]-before[1],3*t*(1-t)**2)
        self.assertEqual(evaluate(shifted,F(1,3))[1]-evaluate(P,F(1,3))[1],F(4,9))
        self.assertEqual(evaluate(shifted,F(1,2))[1]-evaluate(P,F(1,2))[1],F(3,8))

    def test_subdivision_reparameterizes(self):
        for tau in [F(1,3),F(1,2),F(2,3)]:
            left,right=split(P,tau)
            self.assertEqual(left[-1],right[0])
            for i in range(9):
                s=F(i,8)
                self.assertEqual(evaluate(left,s),bernstein(P,tau*s))
                self.assertEqual(evaluate(right,s),bernstein(P,tau+(1-tau)*s))
            d=derivative(P,tau)
            self.assertEqual(derivative(left,1),tuple(tau*x for x in d))
            self.assertEqual(derivative(right,0),tuple((1-tau)*x for x in d))
        self.assertEqual(split(P,F(1,2)),
            (((0,0),(F(1,2),1),(1,F(3,2)),(F(3,2),F(3,2))),
             ((F(3,2),F(3,2)),(2,F(3,2)),(F(5,2),1),(3,0))))

    def test_derivatives_and_join(self):
        for i in range(9):
            t=F(i,8)
            self.assertEqual(derivative(P,t),(3,6-12*t))
        q=((3,0),(5,-4),(6,-4),(7,0))
        self.assertEqual(evaluate(P,1),evaluate(q,0))
        incoming=derivative(P,1);outgoing=derivative(q,0)
        self.assertNotEqual(incoming,outgoing)
        self.assertEqual(outgoing,tuple(2*x for x in incoming))
        self.assertEqual(tuple(x/2 for x in outgoing),incoming) # duration 2 versus 1
        self.assertEqual(derivative([(2,3)],F(1,3)),(0,0))

    def test_contracts_and_preservation(self):
        data=[[0,0],[1,2],[2,2],[3,0]];copy=[p[:] for p in data]
        triangle(data,F(1,3));split(data,F(1,3));self.assertEqual(data,copy)
        for p,t in [([],0),(P,-1),(P,2),(P,.5),([(0,0),(1,)],0),([(True,0)],0),([(1.0,0)],0),(list(P)*5,0)]:
            with self.assertRaises(ValueError):evaluate(p,t)

if __name__=='__main__':unittest.main()
