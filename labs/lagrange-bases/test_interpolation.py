import unittest,itertools
from fractions import Fraction as Q
from .interpolation import basis,weights,lagrange,barycentric,amplification

class LagrangeTests(unittest.TestCase):
    def test_cardinality_partition_and_polynomial_reproduction(self):
        count=0
        for xs in [[0],[0,1],[0,1,2],[-2,0,1,3]]:
            for i,x in enumerate(xs):self.assertEqual(basis(xs,x),tuple(Q(int(i==j)) for j in range(len(xs))))
            for coeff in itertools.product([-1,0,1],repeat=len(xs)):
                def poly(x):return sum((Q(c)*x**i for i,c in enumerate(coeff)),Q(0))
                ys=[poly(Q(x)) for x in xs]
                for x in [Q(-3,2),Q(1,2),Q(3,2),Q(5,2)]:
                    self.assertEqual(sum(basis(xs,x)),1)
                    self.assertEqual(lagrange(xs,ys,x),poly(x))
                    self.assertEqual(barycentric(xs,ys,x),poly(x));count+=1
        self.assertEqual(count,480) # (3+9+27+81)*4
    def test_original_example_and_weights(self):
        self.assertEqual(basis([0,1,2],Q(3,2)),(Q(-1,8),Q(3,4),Q(3,8)))
        self.assertEqual(lagrange([0,1,2],[0,1,4],Q(3,2)),Q(9,4))
        self.assertEqual(weights([0,1,2]),(Q(1,2),Q(-1),Q(1,2)))
        # Independent Newton divided differences for arbitrary integer data.
        for ys in itertools.product([-2,0,3],repeat=3):
            d0=ys[0];d1=ys[1]-ys[0];d2=Q(ys[2]-2*ys[1]+ys[0],2)
            for x in [Q(-1,2),Q(1,3),Q(3,2),3]:
                expected=d0+d1*x+d2*x*(x-1)
                self.assertEqual(lagrange([0,1,2],ys,x),expected)
    def test_data_perturbation_bounds_and_attainment(self):
        xs=[0,1,2];ys=[0,1,4];epsilon=Q(1,100)
        self.assertEqual(amplification(xs,Q(3,2)),Q(5,4))
        self.assertEqual(amplification(xs,3),7)
        for x in [Q(3,2),3]:
            base=lagrange(xs,ys,x);bound=epsilon*amplification(xs,x)
            errors=[]
            for signs in itertools.product([-1,1],repeat=3):
                perturbed=[Q(y)+s*epsilon for y,s in zip(ys,signs)]
                errors.append(abs(lagrange(xs,perturbed,x)-base))
            self.assertLessEqual(max(errors),bound);self.assertEqual(max(errors),bound)
        self.assertEqual(lagrange(xs,[0,Q(101,100),4],Q(3,2))-Q(9,4),Q(3,400))
    def test_shared_nodes_do_not_determine_target(self):
        def f(x,c):return x*x+c*x*(x-1)*(x-2)
        for c in [-100,-8,0,8,100]:
            self.assertEqual([f(x,c) for x in [0,1,2]],[0,1,4])
            x=Q(3,2);error=f(x,c)-lagrange([0,1,2],[0,1,4],x)
            self.assertEqual(error,Q(-3,8)*c)
            self.assertEqual(abs(error),abs(6*c)*Q(1,16))
    def test_permutation_affine_coordinate_and_contracts(self):
        xs=[0,1,2];ys=[0,1,4];x=Q(3,2)
        for order in itertools.permutations(range(3)):
            self.assertEqual(barycentric([xs[i] for i in order],[ys[i] for i in order],x),Q(9,4))
        self.assertEqual(lagrange([10+2*a for a in xs],ys,10+2*x),Q(9,4))
        for args in [([],[],0),([0,0],[1,2],1),([0,1],[1],0),([True],[1],0),([0],[1],.5)]:
            with self.assertRaises(ValueError):lagrange(*args)
        self.assertEqual(barycentric([0,1,2],[0,1,4],1),1)
