import unittest
from fractions import Fraction as Q
from .refine import inverse,step,residual,norm,quantize

class RefinementTests(unittest.TestCase):
    def test_exact_fixture(self):
        A=((4,1),(1,3));b=(1,2);x=(Q(1,10),Q(3,5))
        self.assertEqual(residual(A,b,x),(0,Q(1,10)))
        self.assertEqual(step(A,b,x,inverse(A)),(Q(1,11),Q(7,11)))
        self.assertEqual(step(A,b,x,((Q(1,4),0),(0,Q(1,4)))),(Q(1,10),Q(5,8)))

    def test_contraction_and_failures(self):
        A=((4,1),(1,3));b=(1,2);star=(Q(1,11),Q(7,11));B=((Q(1,4),0),(0,Q(1,4)))
        for i in range(-8,9):
            for j in range(-8,9):
                e=(Q(i,20),Q(j,20));x=tuple(s-t for s,t in zip(star,e))
                y=step(A,b,x,B);new=tuple(s-t for s,t in zip(star,y))
                self.assertEqual(new,(-e[1]/4,(-e[0]+e[1])/4))
                self.assertLessEqual(norm(new),norm(e)/2)
        x=(star[0]-1,star[1]);bad=step(A,b,x,((1,0),(0,1)))
        self.assertEqual(tuple(s-t for s,t in zip(star,bad)),(-3,-1))
        noisy=step(A,b,star,inverse(A),(Q(1,100),0))
        self.assertEqual(tuple(s-t for s,t in zip(star,noisy)),(-Q(3,1100),Q(1,1100)))
        self.assertEqual(quantize(Q(1,1000),Q(1,100)),0)

    def test_direct_oracle_and_scaling(self):
        # Adjugada fornece oráculo escalar independente; inclui troca de linhas.
        count=0
        for a in range(1,5):
            for c in range(-2,3):
                for d in range(1,5):
                    det=a*d-c*c
                    if not det: continue
                    A=((a,c),(c,d));b=(2,-1);x=(Q(1,7),Q(-2,9))
                    want=(Q(2*d+c,det),Q(-a-2*c,det))
                    self.assertEqual(step(A,b,x,inverse(A)),want)
                    for scale in (Q(1,2),3):
                        As=tuple(tuple(scale*v for v in row) for row in A);bs=tuple(scale*v for v in b)
                        self.assertEqual(step(As,bs,x,inverse(As)),want)
                    count+=1
        self.assertGreater(count,60)

    def test_contracts(self):
        for bad in (True,0.1,'1'):
            with self.assertRaises(ValueError): quantize(bad,1)
        for a in (((1,2),(2,4)),((1,2),),((True,0),(0,1))):
            with self.assertRaises(ValueError): inverse(a)
        with self.assertRaises(ValueError): quantize(1,0)
        with self.assertRaises(ValueError): residual(((1,0),(0,1)),(1,2),(1,))
        with self.assertRaises(ValueError): inverse(((Q(1,1001),0),(0,1)))
