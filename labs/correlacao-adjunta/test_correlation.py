import unittest
from fractions import Fraction as F
from itertools import product
from .correlation import correlate,pullback,squared_loss

class CorrelationTests(unittest.TestCase):
    def test_fixtures(self):
        self.assertEqual(correlate((2,-1,3,0),(1,2)),(0,5,3))
        self.assertEqual(pullback((2,-1,3,0),(1,2),(1,-2,1)),((1,0,-3,2),(7,-7)))
        self.assertEqual(squared_loss((2,-1,3,0),(1,2),(1,1,1)),(F(21,2),((-1,2,10,4),(0,13))))
        self.assertEqual(correlate((1,2,3,4),(1,0,-1)),(-2,-2))

    def test_matrix_adjoint_and_kernel_identity(self):
        # Matriz construída por diagonais; não chama o forward para formar o oráculo.
        for x in product((-1,0,1),repeat=3):
            for k in product((-1,0,1),repeat=2):
                A=((k[0],k[1],0),(0,k[0],k[1]));g=(1,-2)
                y=tuple(sum(a*b for a,b in zip(row,x)) for row in A)
                dx=tuple(sum(A[i][j]*g[i] for i in range(2)) for j in range(3))
                actual_dx,dk=pullback(x,k,g)
                self.assertEqual(correlate(x,k),y);self.assertEqual(actual_dx,dx)
                gy=sum(a*b for a,b in zip(g,y))
                self.assertEqual(gy,sum(a*b for a,b in zip(x,actual_dx)))
                self.assertEqual(gy,sum(a*b for a,b in zip(k,dk)))

    def test_quadratic_loss_differences(self):
        x=(F(2),F(-1),F(3),F(0));k=(F(1),F(2));target=(1,1,1)
        loss,(dx,dk)=squared_loss(x,k,target)
        for h in (F(1,10),F(1,7)):
            for values,grads,is_x in ((x,dx,True),(k,dk,False)):
                for j,grad in enumerate(grads):
                    a=list(values);b=list(values);a[j]+=h;b[j]-=h
                    plus=squared_loss(a,k,target)[0] if is_x else squared_loss(x,a,target)[0]
                    minus=squared_loss(b,k,target)[0] if is_x else squared_loss(x,b,target)[0]
                    self.assertEqual((plus-minus)/(2*h),grad)
        # Somar as contribuições é necessário: x1 participa de duas janelas.
        self.assertEqual(dx[1],2)

    def test_contracts(self):
        for x,k in (((),(1,)),((1,),()),((1,),(1,2)),((True,),(1,)),((.5,),(1,))):
            with self.assertRaises(ValueError):correlate(x,k)
        with self.assertRaises(ValueError):pullback((1,2),(1,),(1,))
        with self.assertRaises(ValueError):squared_loss((1,2),(1,),(1,))
