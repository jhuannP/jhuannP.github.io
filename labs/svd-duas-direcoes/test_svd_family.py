import unittest
from fractions import Fraction as Q
from .svd_family import V1,V2,matrix,apply,pseudoinverse,fit,norm_squared

def transpose(a):return tuple(tuple(row) for row in zip(*a))
def multiply(a,b):
    return tuple(tuple(sum((x*y for x,y in zip(row,col)),Q(0)) for col in zip(*b)) for row in a)

class SvdFamilyTests(unittest.TestCase):
    def test_directions_reconstruction_and_gram(self):
        self.assertEqual(norm_squared(V1),1);self.assertEqual(norm_squared(V2),1)
        self.assertEqual(sum(x*y for x,y in zip(V1,V2)),0)
        for eta in (0,Q(1,100),Q(1,2),1,3):
            a=matrix(eta)
            self.assertEqual(apply(eta,V1),(3,0,0));self.assertEqual(apply(eta,V2),(0,eta,0))
            gram=multiply(transpose(a),a)
            for v,eigenvalue in ((V1,9),(V2,eta*eta)):
                self.assertEqual(tuple(sum(x*y for x,y in zip(row,v)) for row in gram),tuple(eigenvalue*x for x in v))
            for x in ((1,0),(0,1),(Q(2,3),Q(-5,4))):
                c1=sum(u*v for u,v in zip(V1,x));c2=sum(u*v for u,v in zip(V2,x))
                self.assertEqual(apply(eta,x),(3*c1,eta*c2,0))
    def test_moore_penrose_identities(self):
        for eta in (0,Q(1,100),1,3):
            a=matrix(eta);pinv=pseudoinverse(eta);ap=multiply(a,pinv);pa=multiply(pinv,a)
            self.assertEqual(multiply(ap,a),a);self.assertEqual(multiply(pa,pinv),pinv)
            self.assertEqual(transpose(ap),ap);self.assertEqual(transpose(pa),pa)
    def test_least_squares_and_minimum_norm_at_rank_drop(self):
        b=(3,1,2);r=fit(1,b)
        self.assertEqual(r['x'],(Q(-1,5),Q(7,5)))
        self.assertEqual(r['residual_squared'],4)
        for dx in range(-2,3):
            for dy in range(-2,3):
                x=(r['x'][0]+dx,r['x'][1]+dy)
                residual=tuple(t-y for t,y in zip(b,apply(1,x)))
                self.assertGreaterEqual(norm_squared(residual),r['residual_squared'])
        base=fit(0,b)
        for t in (Q(-2),Q(-1,2),Q(0),Q(3,2)):
            x=tuple(u+t*v for u,v in zip(base['x'],V2))
            self.assertEqual(apply(0,x),base['prediction'])
            self.assertEqual(norm_squared(x),base['norm_squared']+t*t)
        self.assertIsNone(base['condition'])
    def test_rank_one_error_and_noise_bias_tradeoff(self):
        for eta in (0,Q(1,100),1,3):
            a,a1=matrix(eta),matrix(eta,True)
            difference=tuple(tuple(x-y for x,y in zip(r,s)) for r,s in zip(a,a1))
            self.assertEqual(sum(norm_squared(row) for row in difference),eta*eta)
            for x in ((1,0),(0,1),V1,V2):
                err=tuple(sum(a*b for a,b in zip(row,x)) for row in difference)
                self.assertLessEqual(norm_squared(err),eta*eta*norm_squared(x))
        eta=Q(1,100);truth=tuple(x+y for x,y in zip(V1,V2));clean=apply(eta,truth)
        observed=(clean[0],clean[1]+Q(1,50),clean[2])
        full,truncated=fit(eta,observed),fit(eta,observed,True)
        self.assertEqual(full['condition'],300)
        self.assertEqual(norm_squared(tuple(x-y for x,y in zip(full['x'],truth))),4)
        self.assertEqual(norm_squared(tuple(x-y for x,y in zip(truncated['x'],truth))),1)
        self.assertEqual(full['residual_squared'],0)
        self.assertEqual(truncated['residual_squared'],Q(9,10000))
        self.assertEqual(fit(eta,clean)['x'],truth) # Without the chosen noise, truncation adds bias.
        self.assertEqual(fit(1,(3,1,2),True)['residual_squared'],5)
    def test_contracts(self):
        for eta in (-1,4,True,0.1):
            with self.assertRaises(ValueError):matrix(eta)
        for b in ((1,2),(1,2,3,4),(1,True,2),(1,0.5,2)):
            with self.assertRaises(ValueError):fit(1,b)
        with self.assertRaises(ValueError):fit(1,(1,2,3),1)
        with self.assertRaises(ValueError):matrix(1,1)
