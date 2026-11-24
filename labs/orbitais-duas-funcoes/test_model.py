import unittest
from fractions import Fraction as F
from .model import levels,filling
class TwoSiteTests(unittest.TestCase):
    def test_example_and_filling(self):
        x=levels(-1,F(-2,5),F(1,5))
        self.assertEqual(x['plus'],F(-7,6));self.assertEqual(x['minus'],F(-3,4))
        self.assertEqual(x['minus']-x['plus'],F(5,12))
        self.assertEqual(x['norm_plus_squared'],F(12,5))
        for n,target in enumerate([F(0),F(1,2),F(1),F(1,2),F(0)]):
            b,a,order=filling(n);self.assertEqual(b+a,n);self.assertEqual(order,target)

    def test_generalized_eigen_equations_and_metric(self):
        # 125 models, both eigenvectors, two rows and metric orthogonality.
        for a in range(-2,3):
            for b in range(-2,3):
                for s in [F(-2,3),F(-1,4),F(0),F(1,4),F(2,3)]:
                    x=levels(a,b,s)
                    for sign,key in [(1,'plus'),(-1,'minus')]:
                        e=x[key];c=(F(1),F(sign))
                        h=(a*c[0]+b*c[1],b*c[0]+a*c[1])
                        sc=(c[0]+s*c[1],s*c[0]+c[1])
                        self.assertEqual(h,tuple(e*v for v in sc))
                        norm=c[0]*sc[0]+c[1]*sc[1]
                        self.assertEqual(norm,x['norm_'+key+'_squared']);self.assertGreater(norm,0)
                    # v+^T S v- = 0, despite a nonorthogonal atomic basis.
                    self.assertEqual((1-s)+(s-1),0)

    def test_energy_origin_and_order_condition(self):
        for s in [F(-1,2),F(0),F(1,2)]:
            for a in [-2,-1,1]:
                for b in [F(-2),F(-1,3),F(1)]:
                    original=levels(a,b,s);delta=F(7,3)
                    shifted=levels(a+delta,b+delta*s,s)
                    for key in ['plus','minus']:self.assertEqual(shifted[key],original[key]+delta)
                    self.assertEqual(original['plus']<original['minus'],b-a*s<0)
        x=levels(-1,F(-2,5),F(1,5))
        wrong=levels(0,F(-2,5),F(1,5))
        self.assertNotEqual(x['minus']-x['plus'],wrong['minus']-wrong['plus'])

    def test_contracts(self):
        for s in [-1,1,2]:
            with self.assertRaises(ValueError):levels(-1,-1,s)
        for x in [True,0.2,'0']:
            with self.assertRaises(TypeError):levels(-1,-1,x)
        for n in [-1,5]:
            with self.assertRaises(ValueError):filling(n)
        for n in [True,2.0]:
            with self.assertRaises(TypeError):filling(n)
if __name__=='__main__':unittest.main()
