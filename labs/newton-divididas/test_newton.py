import unittest
from fractions import Fraction as F
from itertools import product,permutations
from .newton import coefficients,evaluate,append_node

def lagrange(xs,ys,x):
    total=F(0)
    for i,y in enumerate(ys):
        basis=F(1)
        for j,z in enumerate(xs):
            if i!=j:basis*=F(x-z,xs[i]-z)
        total+=y*basis
    return total

class NewtonTests(unittest.TestCase):
    def test_example_and_increment(self):
        xs=[-1,1,2];ys=[2,0,2];c=coefficients(xs,ys)
        self.assertEqual(c,(2,-1,1));self.assertEqual(evaluate(xs,c,F(3,2)),F(3,4))
        xx,cc=append_node(xs,c,3,8)
        self.assertEqual(cc,(2,-1,1,F(1,4)))
        self.assertEqual(cc,coefficients(xx,ys+[8]))
        self.assertEqual(evaluate(xx,cc,0),F(1,2))
        self.assertEqual(xs,[-1,1,2]);self.assertEqual(ys,[2,0,2])

    def test_against_independent_lagrange(self):
        xs=(-1,1,2)
        for ys in product((-1,0,1),repeat=3):
            for order in permutations(range(3)):
                xx=tuple(xs[i] for i in order);yy=tuple(ys[i] for i in order)
                c=coefficients(xx,yy)
                for x in (F(-2),F(-1),F(0),F(1,2),F(1),F(2),F(3)):
                    self.assertEqual(evaluate(xx,c,x),lagrange(xs,ys,x))
                xx2,c2=append_node(xx,c,4,3)
                self.assertEqual(c2,coefficients(xx2,yy+(3,)))

    def test_close_nodes_sensitivity_and_constant(self):
        eps=F(1,1000000);delta=F(1,1000000000)
        self.assertEqual(coefficients((0,delta),(0,eps)),(0,1000))
        self.assertEqual(coefficients((-1,1,2),(5,5,5)),(5,0,0))
        self.assertEqual(evaluate((7,),(4,),20),4)

    def test_contracts(self):
        for xs,ys in (((),()),((0,0),(1,2)),((True,),(1,)),((0.,),(1,)),((0,1),(1,))):
            with self.assertRaises(ValueError):coefficients(xs,ys)
        with self.assertRaises(ValueError):append_node((0,),(1,),0,2)
        with self.assertRaises(ValueError):evaluate((0,),(1,),float('nan'))

if __name__=='__main__':unittest.main()
