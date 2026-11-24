import unittest
from fractions import Fraction as F
from .experiment import model

def norm_inf_matrix(A):return max(sum(abs(v) for v in row) for row in A)

class SensitivityTests(unittest.TestCase):
    def test_fraction_inverse_and_bounds(self):
        for e in range(1,7):
            d=F(1,10**e);A=[[F(1),F(1)],[F(1),1+d]]
            inverse=[[(1+d)/d,-1/d],[-1/d,1/d]]
            for i in range(2):
                for j in range(2):self.assertEqual(sum(A[i][k]*inverse[k][j] for k in range(2)),int(i==j))
            cond=norm_inf_matrix(A)*norm_inf_matrix(inverse)
            for direction in (0,1):
                for s in (F(i,4) for i in range(-4,5)):
                    m=model(e,float(s),direction,0);xh=[1+s,1+(-s if direction==0 else s)];b=[F(2),2+d]
                    r=[b[i]-sum(A[i][j]*xh[j] for j in range(2)) for i in range(2)]
                    relative=max(abs(v) for v in r)/max(abs(v) for v in b)
                    self.assertAlmostEqual(m['kappa']/float(cond),1,places=14)
                    self.assertAlmostEqual(m['residual_relative'],float(relative),places=14)
                    self.assertAlmostEqual(m['error_relative'],float(abs(s)),places=14)
                    self.assertLessEqual(relative/cond,abs(s));self.assertLessEqual(abs(s),cond*relative)
                    # Exatamente a solução do RHS perturbado b-r, sem resolver por código do modelo.
                    br=[b[i]-r[i] for i in range(2)]
                    self.assertEqual([sum(inverse[i][j]*br[j] for j in range(2)) for i in range(2)],xh)

    def test_scale_and_direction(self):
        for e in (1,3,6):
            for direction in (0,1):
                for q in range(-3,4):
                    m=model(e,.5,direction,q);base=model(e,.5,direction,0)
                    self.assertAlmostEqual(m['residual_relative'],base['residual_relative'],places=14)
                    self.assertEqual(m['kappa'],base['kappa']);self.assertEqual(m['error_relative'],.5)
                    self.assertAlmostEqual(m['residual_abs']/base['residual_abs'],10.**q,places=10)
        self.assertEqual(model(6,1,1)['residual_relative'],1)
        self.assertLess(model(6,1,0)['residual_relative'],1e-6)

    def test_float_evaluation_and_original_example(self):
        m=model();self.assertEqual(m['xhat'],[2,0]);self.assertEqual(m['r'],[0,.001]);self.assertEqual(m['error_relative'],1)
        for e in range(1,7):
            for d in (0,1):
                for q in (-3,0,3):
                    m=model(e,.25,d,q)
                    # Outra ordem de operações, tolerância proporcional à escala dos dados.
                    raw=[m['b'][i]-(m['A'][i][0]*m['xhat'][0]+m['A'][i][1]*m['xhat'][1]) for i in range(2)]
                    for a,b in zip(raw,m['residual_float']):self.assertLessEqual(abs(a-b),2e-12*m['c'])
                    for a,b in zip(m['r'],m['residual_float']):self.assertLessEqual(abs(a-b),2e-12*m['c'])
        zero=model(s=0);self.assertEqual(zero['residual_relative'],0);self.assertEqual(zero['bound'],0)

    def test_domain(self):
        for args in ((0,1,0,0),(7,1,0,0),(3,2,0,0),(3,1,2,0),(3,1,0,4),(True,1,0,0),(3,float('nan'),0,0)):
            with self.assertRaises(ValueError):model(*args)
