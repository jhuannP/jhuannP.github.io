import unittest,itertools,math
from fractions import Fraction as Q
from .radial import lap_power,shell3

class RadialTests(unittest.TestCase):
    def test_cartesian_polynomial_oracle(self):
        # Expande (u+2*x*h+h²)^n por convolução, sem usar a fórmula radial.
        for d in (2,3):
            for point in itertools.product((1,2,3),repeat=d):
                u=sum(x*x for x in point)
                for n in range(5):
                    lap=0
                    for x in point:
                        coeff=[1]
                        for _ in range(n):
                            new=[0]*(len(coeff)+2)
                            for i,a in enumerate(coeff):
                                for j,b in enumerate((u,2*x,1)): new[i+j]+=a*b
                            coeff=new
                        lap+=2*(coeff[2] if len(coeff)>2 else 0)
                    # r^(2n-2)=u^(n-1), evitando raiz irracional.
                    expected=0 if n==0 else 2*n*(2*n+d-2)*u**(n-1)
                    self.assertEqual(lap,expected)
                    if math.isqrt(u)**2==u:
                        self.assertEqual(lap,lap_power(2*n,math.isqrt(u),d))
    def test_harmonic_powers(self):
        for d in range(3,11):
            for r in (Q(1,3),Q(3,2),Q(7,2)):
                self.assertEqual(lap_power(2-d,r,d),0)
                self.assertEqual(lap_power(0,r,d),0)
        self.assertEqual(lap_power(-1,2,2),Q(1,8))
        self.assertEqual(lap_power(2,2,3),6)
    def test_shell_and_flux(self):
        self.assertEqual(shell3(1),0);self.assertEqual(shell3(2),1)
        self.assertEqual(shell3(Q(3,2)),Q(2,3))
        for i in range(1,21):
            r=1+Q(i,20)
            self.assertEqual(r*r*(2/r**2),2)
            self.assertGreaterEqual(shell3(r),0);self.assertLessEqual(shell3(r),1)
    def test_contracts(self):
        for args in [(2,0,3),(2,-1,3),(2,1,1),(True,1,3),(2,1,True),(2,1.0,3),(101,1,3)]:
            with self.assertRaises(ValueError): lap_power(*args)
        for r in [0,Q(1,2),3,True,1.0]:
            with self.assertRaises(ValueError): shell3(r)
