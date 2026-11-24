from decimal import Decimal,localcontext
from fractions import Fraction as Q
import unittest
from .bounds import harmonic_bounds,geometric_bounds,harmonic_bound_count,MAX_TERMS


def dec(q):return Decimal(q.numerator)/Decimal(q.denominator)


class AlternatingTests(unittest.TestCase):
    def test_harmonic_bounds_against_high_precision_log(self):
        with localcontext() as ctx:
            ctx.prec=80;reference=Decimal(2).ln()
            for n in list(range(101))+[199,200,998,999,1000]:
                out=harmonic_bounds(n)
                self.assertLess(dec(out["lower"]),reference)
                self.assertGreater(dec(out["upper"]),reference)
                error=reference-dec(out["partial"])
                self.assertEqual(error>0,n%2==0)
                self.assertLess(abs(error),dec(out["bound"]))
                # Neste caso há ainda a cota inferior da integral do resto.
                self.assertGreater(abs(error),dec(Q(1,2*(n+1))))

    def test_nested_intervals_and_even_odd_order(self):
        previous=harmonic_bounds(0)
        for n in range(1,101):
            current=harmonic_bounds(n)
            self.assertGreaterEqual(current["lower"],previous["lower"])
            self.assertLessEqual(current["upper"],previous["upper"])
            self.assertEqual(current["upper"]-current["lower"],Q(1,n+1))
            previous=current
        self.assertEqual(harmonic_bounds(9)["bound"],Q(1,10))

    def test_geometric_reference_and_bound_not_exact_error(self):
        for r in (Q(1,10),Q(1,2),Q(3,4),Q(9,10)):
            limit=1/(1+r)
            for n in range(31):
                out=geometric_bounds(n,r)
                self.assertEqual(limit-out["partial"],(-r)**n/(1+r))
                self.assertLessEqual(out["lower"],limit)
                self.assertGreaterEqual(out["upper"],limit)
                self.assertLess(abs(limit-out["partial"]),out["bound"])
        out=geometric_bounds(3)
        self.assertEqual(out["partial"],Q(3,4))
        self.assertEqual(abs(Q(2,3)-out["partial"]),Q(1,12))
        self.assertEqual(out["bound"],Q(1,8))

    def test_tolerance_counts_minimal_for_bound_only(self):
        for eps in (Q(1,1000),Q(1,10),Q(3,100),Q(1),Q(2),Q(7,13)):
            for strict in (False,True):
                n=harmonic_bound_count(eps,strict)
                condition=lambda m:Q(1,m+1)<eps if strict else Q(1,m+1)<=eps
                self.assertTrue(condition(n))
                if n:self.assertFalse(condition(n-1))
        self.assertEqual(harmonic_bound_count(Q(1,1000)),999)
        self.assertEqual(harmonic_bound_count(Q(1,1000),True),1000)
        # Não crescente permite resto zero ou igualdade com o próximo módulo.
        for m in range(1,31):
            terms=[Q(1,(k+1)//2) for k in range(1,2*m+1)]
            s=sum((v if k%2==0 else -v for k,v in enumerate(terms)),Q(0))
            self.assertEqual(s,0)
            self.assertEqual(terms[-1],Q(1,m))
        # Alternar e tender a zero, sem monotonicidade, pode divergir.
        for m in range(1,31):
            paired=sum((Q(1,k)-Q(1,2*k) for k in range(1,m+1)),Q(0))
            self.assertEqual(paired,sum((Q(1,k) for k in range(1,m+1)),Q(0))/2)

    def test_contracts_and_budget(self):
        for n in (-1,True,1.0,MAX_TERMS+1):
            with self.assertRaises(ValueError):harmonic_bounds(n)
        for r in (0,1,-1,Q(3,2)):
            with self.assertRaises(ValueError):geometric_bounds(3,r)
        for eps in (0,-1):
            with self.assertRaises(ValueError):harmonic_bound_count(eps)
        for bad in (.01,True,'1/100'):
            with self.assertRaises(TypeError):harmonic_bound_count(bad)
        with self.assertRaises(TypeError):harmonic_bound_count(Q(1,10),strict=1)
        self.assertGreater(harmonic_bound_count(Q(1,10**6)),MAX_TERMS)

if __name__=="__main__":unittest.main()
