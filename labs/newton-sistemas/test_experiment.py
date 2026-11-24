import unittest
from fractions import Fraction as Q
from math import sqrt
from .experiment import system,jacobian,solve2,newton,norm

class NewtonSystemTests(unittest.TestCase):
    def test_step_against_rational_elimination(self):
        for x in (Q(-3,2),Q(-1,2),Q(0),Q(1,2),Q(3,2)):
            for y in (Q(-1),Q(0),Q(1)):
                if x+y==0:continue
                F=system(x,y);A=jacobian(x,y);d=solve2(A,[-v for v in F])
                target=(x*x+y*y+1)/(2*(x+y))
                self.assertAlmostEqual(float(x)+d[0],float(target),places=11)
                self.assertAlmostEqual(float(y)+d[1],float(target),places=11)
                for row,rhs in zip(A,F):self.assertAlmostEqual(sum(float(a)*b for a,b in zip(row,d)),-float(rhs),places=11)
        self.assertEqual(solve2([[2,0],[1,-1]],[0,-1]),(0,1))

    def test_jacobian_and_known_roots(self):
        for x,y in ((1,0),(-.5,1),(.25,.5)):
            h=1e-5;A=jacobian(x,y)
            for j in range(2):
                plus=system(x+(h if j==0 else 0),y+(h if j else 0))
                minus=system(x-(h if j==0 else 0),y-(h if j else 0))
                for i in range(2):self.assertAlmostEqual((plus[i]-minus[i])/(2*h),A[i][j],places=9)
        for start,sign in (((1,0),1),((-1,0),-1),((.25,.5),1)):
            q=newton(*start,max_steps=8)
            self.assertEqual(q['status'],'residual');last=q['trace'][-1]
            self.assertLessEqual(last['residual'],1e-10)
            self.assertAlmostEqual(last['x'],sign/sqrt(2),places=9)
            self.assertAlmostEqual(last['y'],sign/sqrt(2),places=9)

    def test_stopping_reasons_do_not_certify_roots(self):
        for point in ((0,0),(1,-1),(-.5,.5)):
            q=newton(*point);self.assertEqual(q['status'],'pivot')
            self.assertGreater(q['trace'][-1]['residual'],.1)
        self.assertEqual(newton(1,0,max_steps=0)['status'],'limit')
        self.assertEqual(newton(1,.5,steptol=10)['status'],'smallStep')
        self.assertEqual(newton(1,-1+1e-14)['status'],'pivot')
        self.assertEqual(newton(1,-1+1e-8)['status'],'bound')
        q=newton(1,0,max_steps=1)
        self.assertEqual(q['trace'][0]['residual'],q['trace'][1]['residual'])
        self.assertEqual(q['status'],'limit')

    def test_input_contract(self):
        for args in ((True,0),(float('inf'),0),(0,0,True),(1e7,0),(0,0,13),(0,0,1,-1)):
            with self.assertRaises(ValueError):newton(*args)
