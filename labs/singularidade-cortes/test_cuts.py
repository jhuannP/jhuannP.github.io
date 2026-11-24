import unittest,math
from fractions import Fraction as Q
from decimal import Decimal,localcontext
from .cuts import power_cut,choose_cut,signed_cut

class SingularCutTests(unittest.TestCase):
    def test_transformed_integrals_and_tail(self):
        # x=u^d remove a singularidade x^(-1+1/d), deixando integrando d.
        for degree in (2,3):
            for k in range(21):
                r=power_cut(k,degree);u=Q(1,2**k)
                self.assertEqual(u**degree,r['epsilon'])
                self.assertEqual(degree*(1-u),r['integral'])
                self.assertEqual(degree*u,r['tail'])
                self.assertEqual(r['integral']+r['tail'],degree)
                self.assertGreater(r['tail'],0)
        self.assertEqual(power_cut(2)['integral'],Q(3,2))
        self.assertEqual(power_cut(2)['epsilon'],Q(1,16))

    def test_cut_selection_and_minimality(self):
        for degree in (2,3):
            for tolerance in [Q(10),Q(1),Q(1,10),Q(1,100),Q(1,1000)]:
                k,result=choose_cut(tolerance,degree)
                self.assertLessEqual(result['tail'],tolerance)
                if k:self.assertGreater(power_cut(k-1,degree)['tail'],tolerance)
        k,r=choose_cut(Q(1,100))
        self.assertEqual(k,8);self.assertEqual(r['epsilon'],Q(1,65536))
        self.assertEqual(r['tail'],Q(1,128))

    def test_symmetric_and_asymmetric_paths(self):
        for k in range(2,15):
            e=Q(1,2**k)
            symmetric=signed_cut(e,e)
            self.assertEqual(symmetric['combined'],0)
            self.assertAlmostEqual(symmetric['left']+symmetric['right'],0,places=13)
            other=signed_cut(2*e,e)
            self.assertAlmostEqual(other['combined'],math.log(2),places=14)
            self.assertAlmostEqual(signed_cut(e*e,e)['combined'],-k*math.log(2),places=12)
        self.assertLess(signed_cut(Q(1,1024),Q(1,32))['combined'],0)

    def test_logs_against_high_precision(self):
        with localcontext() as ctx:
            ctx.prec=60
            for left,right in [(Q(1,10),Q(1,100)),(Q(2,7),Q(1,13)),(Q(1,2**100),Q(1,2**40))]:
                ratio=left/right
                expected=(Decimal(ratio.numerator)/Decimal(ratio.denominator)).ln()
                self.assertAlmostEqual(signed_cut(left,right)['combined'],float(expected),delta=1e-12)

    def test_contracts(self):
        for a,b in [(0,1),(-1,1),(1,2)]:
            with self.assertRaises(ValueError):signed_cut(a,b)
        for v in [True,.1,'1']:
            with self.assertRaises(TypeError):signed_cut(v,1)
        for k in [-1,True,1.5,257]:
            with self.assertRaises(ValueError):power_cut(k)
        with self.assertRaises(ValueError):power_cut(1,4)
        with self.assertRaises(ValueError):choose_cut(0)
        with self.assertRaises(ValueError):choose_cut(Q(1,2**300))

if __name__=='__main__':unittest.main()
