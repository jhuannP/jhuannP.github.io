import unittest
from fractions import Fraction as Q
from itertools import product
from .layers import affine,collapse,relu,xor_score

class Tests(unittest.TestCase):
    def test_fixture_and_affine_identity(self):
        W1=[[1,2],[-1,1]];b1=[1,-2];W2=[[3,-2]];b2=[4]
        W,b=collapse(W1,b1,W2,b2);self.assertEqual(W,[[5,4]]);self.assertEqual(b,[11])
        self.assertEqual(affine(W,b,[2,-1]),[17])
        for x in product([Q(-2),Q(-1,2),Q(0),Q(1,3),Q(2)],repeat=2):
            nested=affine(W2,b2,affine(W1,b1,x))
            self.assertEqual(nested,affine(W,b,x));self.assertEqual(nested,[5*x[0]+4*x[1]+11])
    def test_various_shapes_and_composition_associativity(self):
        for d,h,o in product(range(1,5),repeat=3):
            W1=[[Q(i-j,3) for j in range(d)] for i in range(h)];b1=[Q(i,2) for i in range(h)]
            W2=[[Q(i+j+1,5) for j in range(h)] for i in range(o)];b2=[-i for i in range(o)]
            x=[Q(j-1,2) for j in range(d)]
            W,b=collapse(W1,b1,W2,b2)
            self.assertEqual(affine(W,b,x),affine(W2,b2,affine(W1,b1,x)))
        A,a=[[2,-1],[1,0]],[1,2];B,b=[[1,2],[0,3]],[0,-1];C,c=[[2,-2]],[3]
        BA,ba=collapse(A,a,B,b);CB,cb=collapse(B,b,C,c)
        self.assertEqual(collapse(BA,ba,C,c),collapse(A,a,CB,cb))
    def test_relu_xor_and_domain(self):
        for i,j in product(range(21),repeat=2):
            x=[Q(i,20),Q(j,20)]
            self.assertEqual(xor_score(x),2*abs(x[0]-x[1])-1)
        for x in product([0,1],repeat=2):
            self.assertEqual(int(xor_score(x)>0),x[0]^x[1])
        # Não afim: valor no ponto médio não é a média dos extremos.
        self.assertNotEqual(relu(0),(relu(-1)+relu(1))/2)
        # Retirar ativação da construção faz as duas linhas se cancelarem.
        W,b=collapse([[1,-1],[-1,1]],[0,0],[[2,2]],[-1])
        self.assertEqual(W,[[0,0]]);self.assertEqual(b,[-1])
        # Não linearidade não garante saída não afim: cancelamento possível.
        for t in (Q(-2),Q(-1,3),0,Q(1,3),2):self.assertEqual(relu(t)-relu(-t),t)
    def test_contracts(self):
        for W,b,x in [([],[],[]),([[]],[0],[]),([[1],[2,3]],[0,0],[1]),
                      ([[1,2]],[0],[1]),([[1]],[],[1]),([[True]],[0],[1]),
                      ([[1.]],[0],[1]),([[1]],[0],[True])]:
            with self.assertRaises(ValueError):affine(W,b,x)
        with self.assertRaises(ValueError):collapse([[1]],[0],[[1,2]],[0])
        for x in ([0],[0,0,0],[-1,0],[0,2],[True,0],[.5,0]):
            with self.assertRaises(ValueError):xor_score(x)
