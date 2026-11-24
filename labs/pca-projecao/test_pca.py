import unittest
from math import sqrt,cos,sin,pi
from dataclasses import replace,FrozenInstanceError
from fractions import Fraction as Q
from .pca import fit,transform,inverse,explained_ratio,exact_covariance

DATA=((12,22),(8,18),(11,19),(9,21))

class PCATests(unittest.TestCase):
    def test_exact_covariance_and_reconstruction(self):
        mu,C=exact_covariance(DATA)
        self.assertEqual(mu,(10,20));self.assertEqual(C,((Q(5,2),Q(3,2)),(Q(3,2),Q(5,2))))
        m=fit(DATA);self.assertEqual(m.mean,(10,20));self.assertEqual(m.eigenvalues,(4,1))
        self.assertAlmostEqual(abs(m.direction[0]),1/sqrt(2),places=14)
        self.assertAlmostEqual(explained_ratio(m),.8,places=14)
        rec=inverse(m,transform(m,DATA))
        err=sum(sum((x-y)**2 for x,y in zip(p,q)) for p,q in zip(DATA,rec))/len(DATA)
        self.assertAlmostEqual(err,1,places=13)
        for p,q in zip(DATA,rec):
            self.assertAlmostEqual(sum((p[j]-q[j])*m.direction[j] for j in range(2)),0,places=13)

    def test_rayleigh_against_direct_projection(self):
        m=fit(DATA);mu,C=exact_covariance(DATA)
        for j in range(361):
            u=(cos(j*pi/180),sin(j*pi/180))
            var=sum(sum((p[k]-mu[k])*u[k] for k in range(2))**2 for p in DATA)/4
            matrix=sum(u[i]*float(C[i][k])*u[k] for i in range(2) for k in range(2))
            self.assertAlmostEqual(float(var),matrix,places=12)
            self.assertLessEqual(var,4+1e-12)
        self.assertAlmostEqual(sum(v*v for v in m.direction),1,places=14)

    def test_sign_translation_and_units(self):
        m=fit(DATA);neg=replace(m,direction=tuple(-v for v in m.direction))
        for a,b in zip(inverse(m,transform(m,DATA)),inverse(neg,transform(neg,DATA))):
            for x,y in zip(a,b):self.assertAlmostEqual(x,y,places=13)
        moved=tuple((x+100,y-7) for x,y in DATA);m2=fit(moved)
        for a,b in zip(transform(m,DATA),transform(m2,moved)):self.assertAlmostEqual(a,b,places=13)
        scaled=tuple((x,10*y) for x,y in DATA);m3=fit(scaled)
        self.assertGreater(abs(m3.direction[1]),.99)
        self.assertLess(abs(m3.direction[0]),.1)

    def test_frozen_fit_new_point_and_degeneracy(self):
        m=fit(DATA);score=transform(m,[(14,20)])[0]
        self.assertAlmostEqual(score,2*sqrt(2),places=13)
        self.assertEqual(m.mean,(10,20))
        for x,y in zip(inverse(m,[score])[0],(12,22)):self.assertAlmostEqual(x,y,places=13)
        with self.assertRaises(FrozenInstanceError):m.mean=(0,0)
        iso=fit(((1,0),(-1,0),(0,1),(0,-1)))
        self.assertTrue(iso.degenerate);self.assertEqual(iso.eigenvalues,(.5,.5))
        same=fit(((3,7),(3,7)));self.assertIsNone(explained_ratio(same))
        # Maior variância perde o alvo: mesma projeção, sinais distintos da segunda variável.
        unlabelled=((10,1),(10,-1),(-10,1),(-10,-1));u=fit(unlabelled)
        scores=transform(u,unlabelled)
        self.assertEqual(scores[0],scores[1]);self.assertEqual(scores[2],scores[3])
        self.assertAlmostEqual(explained_ratio(u),100/101,places=14)

    def test_contracts(self):
        for bad in ([],[(1,)],[(1,2,3)],[(True,1)],[(float('nan'),0)]):
            with self.assertRaises(ValueError):fit(bad)
        with self.assertRaises(ArithmeticError):fit(((1e308,0),(-1e308,0)))
        with self.assertRaises(TypeError):exact_covariance(((0.1,2),(1,3)))
        with self.assertRaises(ValueError):transform(fit(DATA),[(1,)])
        self.assertEqual(transform(fit(DATA),[]),())

if __name__=='__main__':unittest.main()
