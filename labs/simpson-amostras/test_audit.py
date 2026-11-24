import unittest,json,math
from fractions import Fraction as Q
from pathlib import Path
from .audit import compare,hidden,value

class AuditTests(unittest.TestCase):
    def test_quartic_reference(self):
        r=compare((0,0,0,0,1))
        self.assertEqual((r['coarse'],r['fine'],r['indicator']),(Q(5,24),Q(77,384),Q(1,1920)))
        self.assertEqual((r['corrected'],r['exact'],r['true_error']),(Q(1,5),Q(1,5),0))
        self.assertEqual(r['evaluations'],5)

    def test_degree_five_exactness_on_multiple_intervals(self):
        # Corrected rule has degree5; primitives of monomials are independent references.
        for degree in range(6):
            for a,b in ((Q(0),Q(1)),(Q(-2),Q(3)),(Q(1,3),Q(7,6))):
                r=compare((0,)*degree+(1,),a,b)
                primitive=(b**(degree+1)-a**(degree+1))/(degree+1)
                self.assertEqual(r['corrected'],primitive)
                if degree<4:self.assertEqual(r['indicator'],0)

    def test_hidden_positive_polynomial(self):
        c=hidden();r=compare(c)
        for k in range(5):self.assertEqual(value(c,Q(k,4)),0)
        self.assertGreater(value(c,Q(1,8)),0)
        self.assertEqual((r['coarse'],r['fine'],r['corrected'],r['indicator']),(0,0,0,0))
        self.assertEqual((r['exact'],r['true_error']),(1,1))
        # Evaluate factored expression independently of expanded coefficients.
        for k in range(33):
            x=Q(k,32);q=Q(1)
            for root in (0,Q(1,4),Q(1,2),Q(3,4),1):q*=x-root
            self.assertEqual(value(c,x),Q(1419264,5)*q*q)

    def test_existing_adaptive_routine_and_budget_failure(self):
        root=Path(__file__).resolve().parents[2]
        lesson=next(l for l in json.loads((root/'content/lessons.json').read_text()) if l['id']=='quadratura-adaptativa')
        ns={};exec(lesson['python'],ns);f=ns['simpson_adaptativo']
        def invisible(x):
            q=1.0
            for r in (0,.25,.5,.75,1):q*=x-r
            return (1419264/5)*q*q
        r=f(invisible,0,1,tol=1e-12)
        self.assertEqual((r['valor'],r['erro_estimado'],r['avaliacoes'],r['atingiu_criterio']),(0,0,5,True))
        fail=f(math.exp,0,1,tol=1e-20,max_depth=0)
        self.assertFalse(fail['atingiu_criterio']);self.assertEqual(fail['avaliacoes'],5)
        # Supplying a split reveals nonzero information; no claim of universal cure.
        split=f(invisible,0,.5,tol=1e-10)['valor']+f(invisible,.5,1,tol=1e-10)['valor']
        self.assertAlmostEqual(split,1,places=7)
        exec(lesson['codingPractice']['solution'],{})

    def test_contracts(self):
        for coeff in ((),(True,),(1.,),(0,)*22):
            with self.assertRaises(ValueError):compare(coeff)
        for a,b in ((1,0),(1,1),(True,2),(0.,1)):
            with self.assertRaises(ValueError):compare((1,),a,b)
