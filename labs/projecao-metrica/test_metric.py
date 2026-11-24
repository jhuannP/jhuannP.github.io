import unittest
from itertools import product
from fractions import Fraction as F
from .metric import inner,project,matrix

def mul(a,b):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2)) for i in range(2) for j in range(2))

def transpose(a):return a[0],a[2],a[1],a[3]

class MetricTests(unittest.TestCase):
    def test_fixture_and_euclidean_comparison(self):
        g=(1,0,0,4);u=(1,1);b=(2,0);v=project(b,u,g)
        self.assertEqual(v['alpha'],F(2,5));self.assertEqual(v['p'],(F(2,5),)*2)
        self.assertEqual(v['r'],(F(8,5),F(-2,5)));self.assertEqual(v['error_squared'],F(16,5))
        self.assertEqual(sum(v['r']),F(6,5)) # não ortogonal usual
        self.assertEqual(inner((1,-1),(1,-1),g),5) # resíduo da projeção usual
        self.assertEqual(matrix(u,g),(F(1,5),F(4,5),F(1,5),F(4,5)))
        self.assertEqual(project((2,0),(1,2),(1,0,0,1))['p'],(F(2,5),F(4,5)))

    def test_pythagoras_in_216_cases(self):
        for g in ((1,0,0,1),(1,0,0,4),(2,1,1,2)):
            for u in product((-1,0,1),repeat=2):
                if u==(0,0):continue
                for b in product((-1,0,1),repeat=2):
                    v=project(b,u,g)
                    self.assertEqual(inner(v['r'],u,g),0)
                    self.assertEqual(project(v['p'],u,g)['p'],v['p'])
                    for t in (-2,0,3):
                        residual=tuple(bi-t*ui for bi,ui in zip(b,u))
                        self.assertEqual(inner(residual,residual,g),v['error_squared']+(t-v['alpha'])**2*inner(u,u,g))
                    self.assertEqual(project(b,u,tuple(7*x for x in g))['p'],v['p'])

    def test_projector_identity_and_adjoint(self):
        for g in ((1,0,0,1),(1,0,0,4),(2,1,1,2)):
            for u in ((1,1),(1,0),(2,-1)):
                P=matrix(u,g)
                self.assertEqual(mul(P,P),P)
                self.assertEqual(mul(transpose(P),g),mul(g,P))
        self.assertNotEqual(transpose(matrix((1,1),(1,0,0,4))),matrix((1,1),(1,0,0,4)))

    def test_contracts(self):
        for g in ((1,0,0,0),(1,0,0,-1),(1,1,0,1),(0,0,0,1)):
            with self.assertRaises(ValueError):project((2,0),(1,1),g)
        for b,u in (((2.,0),(1,1)),((True,0),(1,1)),((2,0),(0,0)),((2,),(1,1))):
            with self.assertRaises(ValueError):project(b,u,(1,0,0,1))

if __name__=='__main__':unittest.main()
