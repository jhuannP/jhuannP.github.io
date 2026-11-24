import unittest
from decimal import Decimal as D,localcontext,ROUND_DOWN
from fractions import Fraction as F
from .decimal_qr import factor,columns,diagnostics,analytic_columns

class RoundingTests(unittest.TestCase):
    def test_eight_digit_literal_cancellation(self):
        with localcontext() as ctx:
            ctx.prec=8
            self.assertEqual(D('1.00000001').sqrt(),D('1.0000000'))
        q,r=factor()
        self.assertEqual(q[0],(D(1),D('.0001'),D(0),D(0)))
        self.assertEqual(q[1],(D(0),D('-.70710676'),D('.70710676'),D(0)))
        self.assertEqual(q[2],(D(0),D('-.70710676'),D(0),D('.70710676')))
        self.assertEqual(diagnostics('.0001',q,r)['orthogonality_max'],D('.4999999700376976'))

    def test_independent_analytic_reference(self):
        for eps in ['1','0.5','.01','.0001','1e-8']:
            expected=analytic_columns(eps)
            for method in ['CGS','MGS','MGS2']:
                q,r=factor(eps,60,method)
                self.assertLess(max(abs(a-b) for x,y in zip(q,expected) for a,b in zip(x,y)),D('1e-40'))
                self.assertLess(diagnostics(eps,q,r)['reconstruction_max'],D('1e-55'))

    def test_exact_rational_diagnostics(self):
        # Decimal de saída é racional exato; oráculo não usa dot nem contexto decimal.
        for method in ['CGS','MGS','MGS2']:
            q,r=factor(method=method)
            Q=[[F(x) for x in col] for col in q];R=[[F(x) for x in row] for row in r]
            A=[[F(x) for x in col] for col in columns('.0001')]
            orth=max(abs(sum(Q[i][k]*Q[j][k] for k in range(4))-int(i==j)) for i in range(3) for j in range(3))
            resid=max(abs(A[j][k]-sum(Q[i][k]*R[i][j] for i in range(3))) for j in range(3) for k in range(4))
            stats=diagnostics('.0001',q,r)
            self.assertEqual(F(stats['orthogonality_max']),orth)
            self.assertEqual(F(stats['reconstruction_max']),resid)

    def test_specific_case_not_universal_ranking(self):
        stats=[diagnostics('.0001',*factor(method=m)) for m in ['CGS','MGS','MGS2']]
        for s in stats:self.assertLess(s['reconstruction_max'],D('1e-11'))
        self.assertGreater(stats[0]['orthogonality_max'],D('.49'))
        self.assertLess(stats[1]['orthogonality_max'],D('.0001'))
        self.assertLess(stats[2]['orthogonality_max'],D('1e-7'))
        # Ortogonalidade por fórmulas cruas em racionais.
        for e in [F(1,10),F(1,10000)]:
            raw=[(1,e,0,0),(e,-1,1+e*e,0),(e,-1,-1,2+e*e)]
            for i in range(3):
                for j in range(i):self.assertEqual(sum(a*b for a,b in zip(raw[i],raw[j])),0)

    def test_context_isolated(self):
        expected=factor(method='MGS2');stats=diagnostics('.0001',*expected)
        with localcontext() as ctx:
            ctx.prec=11;ctx.rounding=ROUND_DOWN
            self.assertEqual(factor(method='MGS2'),expected)
            self.assertEqual(diagnostics('.0001',*expected),stats)
            self.assertEqual(ctx.prec,11);self.assertEqual(ctx.rounding,ROUND_DOWN)

    def test_contracts(self):
        for eps in ['0','-1','NaN','Infinity','1e-9','2','bad']:
            with self.assertRaises(ValueError):factor(eps)
        for eps in [True,.0001,D('.0001')]:
            with self.assertRaises(TypeError):factor(eps)
        for p in [7,81,True,8.]:
            with self.assertRaises(ValueError):factor(precision=p)
        with self.assertRaises(ValueError):factor(method='Householder')
