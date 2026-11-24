import json,math,unittest
from pathlib import Path
from .experiment import model,equilibrium,quotient,gibbs


class ProtonTransferTests(unittest.TestCase):
    def test_decimal_reference(self):
        rows=json.loads(Path(__file__).with_name('decimal_reference.json').read_text())
        self.assertEqual(len(rows),15)
        for row in rows:
            u=equilibrium(row['delta'],row['ratio'])
            self.assertAlmostEqual(u,float(row['ueq']),delta=8e-16)
            self.assertAlmostEqual(quotient(u,row['ratio']),row['delta'],delta=3e-9)

    def test_closed_forms_and_reversal(self):
        for delta in (-6,-4,-2,0,2,4,6):
            s=10**(delta/2);u=equilibrium(delta,1)
            self.assertAlmostEqual(u,s/(1+s),delta=3e-16)
            self.assertAlmostEqual(u+equilibrium(-delta,1),1,delta=3e-16)
        for r in (.25,.5,1,2,4):
            self.assertAlmostEqual(equilibrium(0,r),r/(1+r),delta=1e-15)
            for delta in (-6,0,6):
                self.assertAlmostEqual(equilibrium(delta,r)/min(1,r),equilibrium(delta,1/r)/min(1,1/r),delta=2e-15)

    def test_totals_and_dilution(self):
        for delta in (-6,0,2,6):
            for ratio in (.25,1,4):
                for f in (0,.25,.5,1):
                    a=model(delta,ratio,.005,f);b=model(delta,ratio,.01,f)
                    self.assertEqual(a['eq_fraction'],b['eq_fraction'])
                    self.assertEqual(a['logQ'],b['logQ'])
                    for amounts in (a['current'],a['final']):
                        HA,B,A,BH=amounts
                        self.assertTrue(all(x>=0 for x in amounts))
                        self.assertAlmostEqual(HA+A,.005,delta=2e-18)
                        self.assertAlmostEqual(B+BH,.005*ratio,delta=8*math.ulp(.005*ratio))
                        self.assertEqual(A,BH)
                    for x,y in zip(a['final'],b['final']):self.assertEqual(2*x,y)
        self.assertEqual(model(fraction=0)['direction'],'direto')
        self.assertEqual(model(fraction=1)['direction'],'inverso')
        self.assertEqual(model(0,1,.01,.5)['direction'],'equilíbrio')

    def test_gibbs_minimum_gradient_and_domain(self):
        for delta in (-2,0,2):
            for ratio in (.25,1,4):
                ue=equilibrium(delta,ratio);minimum=gibbs(ue,ratio,delta)
                for j in range(101):
                    u=min(1,ratio)*j/100
                    self.assertLessEqual(minimum,gibbs(u,ratio,delta)+1e-14)
                u=.3*min(1,ratio);h=1e-6
                gradient=(gibbs(u+h,ratio,delta)-gibbs(u-h,ratio,delta))/(2*h)
                expected=math.log(10)*(quotient(u,ratio)-delta)
                self.assertAlmostEqual(gradient,expected,delta=2e-9)
        for args in ((7,), (0,0), (0,1,0), (0,1,.01,1.1), (float('nan'),)):
            with self.assertRaises(ValueError):model(*args)
        for u in (0,1):
            with self.assertRaises(ValueError):quotient(u,1)
