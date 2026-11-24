import unittest
from fractions import Fraction as Q
from .experiment import value_derivative,divide_linear,cauchy_bound,newton,family

class PolynomialZerosTests(unittest.TestCase):
    def test_horner_against_direct_powers(self):
        for c in ([-2,1,1],[2,-3,0,1],[1,-2,1],[3,0,-2,0,5]):
            for x in map(Q,(-3,-1,0,1,2,3)):
                p,dp=value_derivative(c,x)
                self.assertEqual(p,sum(a*x**j for j,a in enumerate(c)))
                self.assertEqual(dp,sum(j*c[j]*x**(j-1) for j in range(1,len(c))))

    def test_division_reconstructs_coefficients_and_values(self):
        for c in ([-2,1,1],[2,-3,0,1],[1,-2,1]):
            for r in (Q(-2),Q(1),Q(101,100),Q(2)):
                q,rem=divide_linear(c,r)
                rebuilt=[rem-r*q[0]]+[q[j-1]-r*q[j] for j in range(1,len(q))]+[q[-1]]
                self.assertEqual(rebuilt,c)
                self.assertEqual(rem,value_derivative(c,r)[0])
        q,rem=divide_linear([1,-2,1],Q(101,100))
        self.assertEqual(q,[-Q(99,100),1]);self.assertEqual(rem,Q(1,10000))
        self.assertEqual(cauchy_bound(family(2)),4)

    def test_multiplicity_and_stop_diagnostics(self):
        # Referência algébrica: erro do Newton de (x-1)^2 é dividido por 2.
        trace=newton([1,-2,1],2,6)['trace']
        for k,row in enumerate(trace):self.assertEqual(row['x']-1,2**(-k))
        r=newton([1,-2,1],2,6,2)
        self.assertEqual(r['trace'][-1]['x'],1);self.assertEqual(r['status'],'computedZero')
        self.assertEqual(newton([1,0,1],0,3)['status'],'derivativeZero')
        self.assertEqual(newton(family(2),2,0)['status'],'limit')
        for m in (1,2):
            for x0 in (1.25,1.5,2,2.5):
                a=newton(family(m),x0,3,1)['trace'][-1]['x']
                b=newton(family(m),x0,3,m)['trace'][-1]['x']
                self.assertLessEqual(abs(b-1),abs(a-1)+1e-12)
                self.assertLessEqual(abs(a-1),abs(x0-1))

    def test_sensitivity_scaling_and_invalid_inputs(self):
        # Perturbação exata: (x-1)^2 - 10^-8 tem raízes 1 +/- 10^-4.
        eps=Q(1,10**8)
        for r in (1-Q(1,10000),1+Q(1,10000)):
            self.assertEqual(value_derivative([1-eps,-2,1],r)[0],0)
        p,dp=value_derivative(family(2),Q(3,2))
        ps,dps=value_derivative([7*a for a in family(2)],Q(3,2))
        self.assertEqual(ps/dps,p/dp)
        for c in ([],[1,0],[float('nan'),1]):
            with self.assertRaises(ValueError):value_derivative(c,1)
        with self.assertRaises(ValueError):newton(family(2),2,-1)
        with self.assertRaises(ValueError):divide_linear([1],1)

if __name__=='__main__':unittest.main()
