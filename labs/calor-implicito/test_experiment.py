import unittest
from fractions import Fraction as Q
from math import sin,pi,exp
from .experiment import step,heat

class ImplicitHeatTests(unittest.TestCase):
    def test_independent_rational_dense_solve_and_boundary_terms(self):
        # Eliminação Gaussiana racional independente de Thomas.
        for m in (1,2,4,7):
            for r in (Q(0),Q(1,4),Q(1),Q(8)):
                u=[Q(i+1,3) for i in range(m)];left,right=Q(2),Q(-1)
                A=[[Q(1)+2*r if i==j else -r if abs(i-j)==1 else Q(0) for j in range(m)] for i in range(m)]
                rhs=u[:];rhs[0]+=r*left;rhs[-1]+=r*right
                aug=[row+[v] for row,v in zip(A,rhs)]
                for j in range(m):
                    pivot=aug[j][j];aug[j]=[x/pivot for x in aug[j]]
                    for i in range(m):
                        if i!=j:
                            factor=aug[i][j];aug[i]=[a-factor*b for a,b in zip(aug[i],aug[j])]
                actual=step([float(v) for v in u],float(r),left=float(left),right=float(right))
                for a,row in zip(actual,aug):self.assertAlmostEqual(a,float(row[-1]),places=12)
        self.assertAlmostEqual(step([1.],1)[0],1/3)
        for r in (.1,1,10):
            linear=[1+2*j/8 for j in range(1,8)]
            for a,b in zip(step(linear,r,left=1,right=3),linear):self.assertAlmostEqual(a,b,places=12)

    def test_modal_reference_stability_and_triangle_bound(self):
        for n in (4,8,16):
            for nt in (4,16,40):
                for method in ('implicit','explicit'):
                    for high in (False,True):
                        q=heat(n,nt,method,high)
                        for j,v in enumerate(q['numerical']):
                            expected=0.
                            for k,a in [(1,1.)]+([(n-1,.1)] if high else []):
                                z=-4*q['r']*sin(k*pi/(2*n))**2
                                factor=1/(1-z) if method=='implicit' else 1+z
                                expected+=a*sin(k*pi*j/n)*factor**nt
                            if j in (0,n):expected=0.
                            # Sem modo alto explícito, arredondamento pode semear o modo instável.
                            if high or q['radius']<=1:
                                self.assertLess(abs(v-expected),2e-10*max(1,max(map(abs,q['numerical']))))
                        self.assertLessEqual(q['total'],q['temporal']+q['spatial']+1e-10)
                        if method=='implicit':
                            self.assertLess(q['radius'],1)
                            self.assertGreaterEqual(min(q['numerical']),-1e-14)
        self.assertGreater(heat(8,16,'explicit')['radius'],1)
        self.assertGreater(heat(8,16,'explicit')['total'],100)

    def test_temporal_and_spatial_refinement_separately(self):
        es=[heat(16,nt,high=False)['temporal'] for nt in (20,40,80)]
        for a,b in zip(es,es[1:]):self.assertTrue(1.85<a/b<2.15)
        es=[heat(n,80,high=False)['spatial'] for n in (8,16,32)]
        for a,b in zip(es,es[1:]):self.assertTrue(3.8<a/b<4.2)
        # Monotonicidade e contração: dois dados ordenados sob mesmas bordas.
        for r in (.01,.5,8):
            a=step([0,1,0,1],r);b=step([1,2,1,2],r)
            self.assertTrue(all(x<=y for x,y in zip(a,b)))
            self.assertLessEqual(max(abs(x-y) for x,y in zip(a,b)),1+1e-14)
            self.assertLessEqual(max(a),1+1e-14)

    def test_contracts(self):
        for args in ((3,4),(4,0),(True,4),(4,2.5),(65,4)):
            with self.assertRaises(ValueError):heat(*args)
        for kwargs in ({'method':'cn'},{'high':1}):
            with self.assertRaises(ValueError):heat(**kwargs)
        for u,r in (([],1),([1],-1),([float('nan')],1),([1],True),([1],1e308)):
            with self.assertRaises(ValueError):step(u,r)
