import unittest
from fractions import Fraction as Q
from math import cos,pi
from .nested import trapezoid_column,extrapolate,romberg,cosine_coarse_samples

def direct_trapezoid(f,a,b,n):
    h=(b-a)/n
    return h*(f(a)/2+sum((f(a+i*h) for i in range(1,n)),Q(0))+f(b)/2)

class RombergTests(unittest.TestCase):
    def test_nested_matches_full_rule_and_unique_evaluations(self):
        for a,b in [(Q(0),Q(1)),(Q(-2),Q(3))]:
            calls=[]
            def f(x):calls.append(x);return x**4-2*x+1
            column=trapezoid_column(f,a,b,7)
            self.assertEqual(len(calls),65)
            self.assertEqual(len(set(calls)),65)
            for k,t in enumerate(column):self.assertEqual(t,direct_trapezoid(lambda x:x**4-2*x+1,a,b,2**k))

    def test_polynomial_degree_exactness(self):
        # Independent monomial antiderivatives, 20 applicable column-degree pairs.
        for j in range(4):
            for power in range(2*j+2):
                table=romberg(lambda x:x**power,0,1,j+1)
                self.assertEqual(table[j][j],Q(1,power+1))
        table=romberg(lambda x:x*x,0,1,3)
        self.assertEqual(table[0][0],Q(1,2));self.assertEqual(table[1][0],Q(3,8));self.assertEqual(table[1][1],Q(1,3))

    def test_quartic_error_expansion_and_columns(self):
        table=romberg(lambda x:x**4,0,1,6)
        for k,row in enumerate(table):
            h=Q(1,2**k)
            self.assertEqual(row[0],Q(1,5)+h*h/3-h**4/30)
            if k>=1:self.assertEqual(row[1],Q(1,5)+Q(2,15)*h**4)
            if k>=2:self.assertEqual(row[2],Q(1,5))
        self.assertEqual(table[1][1],Q(5,24))
        self.assertEqual(table[2][1],Q(77,384))

    def test_kink_interpolation_error_oracle(self):
        a=Q(1,5);exact=Q(17,50)
        table=romberg(lambda x:abs(x-a),0,1,7)
        for k,row in enumerate(table):
            n=2**k;h=Q(1,n);theta=a*n-int(a*n)
            self.assertEqual(row[0]-exact,h*h*theta*(1-theta))
        self.assertNotEqual(table[2][2],exact)

    def test_smooth_alias_false_stability(self):
        table=romberg(cosine_coarse_samples,0,1,5)
        for k in range(4):
            self.assertTrue(all(x==1 for x in table[k]))
            for i in range(2**k+1):
                self.assertAlmostEqual(cos(16*pi*i/2**k),1,places=13)
        # Integral sin(16*pi)/(16*pi)-sin(0)/(16*pi)=0 analytically.
        self.assertEqual(table[3][-1]-table[2][-1],0)
        self.assertEqual(table[4][0],0)
        self.assertNotEqual(table[4][-1],0)
        with self.assertRaises(ValueError):cosine_coarse_samples(Q(1,32))

    def test_contracts(self):
        for args in ((0,0,2),(1,0,2),(0,1,0),(0,1,11)):
            with self.assertRaises(ValueError):trapezoid_column(lambda x:x,*args)
        for lev in (True,2.0):
            with self.assertRaises(TypeError):trapezoid_column(lambda x:x,0,1,lev)
        with self.assertRaises(TypeError):trapezoid_column(lambda x:float(x),0,1,2)
        for bad in ([],None,'x'):
            with self.assertRaises(TypeError):extrapolate(bad)

if __name__=='__main__':unittest.main()
