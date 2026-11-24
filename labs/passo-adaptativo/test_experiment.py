import unittest, math
from decimal import Decimal, localcontext
from .experiment import step, adaptive_rk4
import numerics4

class AdaptiveDiagnosticsTests(unittest.TestCase):
    def test_decimal_one_step_and_asymptotic_estimate(self):
        # Referência de 70 dígitos: polinômio de estabilidade, sem integrar estágios.
        def R(z):
            return 1+z+z*z/2+z**3/6+z**4/24
        with localcontext() as ctx:
            ctx.prec=70
            errors=[]
            for divisor in (2,4,8,16):
                h=Decimal(1)/divisor
                whole=R(-h);twice=R(-h/2)**2;real=abs(twice-(-h).exp())
                estimate=abs(whole-twice)/15
                w=step(lambda t,y:[-y[0]],0,[1],float(h))[0]
                mid=step(lambda t,y:[-y[0]],0,[1],float(h/2))
                f=step(lambda t,y:[-y[0]],float(h/2),mid,float(h/2))[0]
                self.assertAlmostEqual(w,float(whole),places=14)
                self.assertAlmostEqual(f,float(twice),places=14)
                self.assertLess(abs(float(estimate/real)-1),float(h))
                errors.append(real)
            # Reduzir h pela metade reduz o defeito local aproximadamente por 32.
            self.assertLess(abs(float(errors[-2]/errors[-1])-32),2)
    def test_rejections_trace_and_evaluation_cost(self):
        calls=[]
        def f(t,y):
            calls.append((t,tuple(y)))
            return [-y[0]]
        r=adaptive_rk4(f,0,3,[1],h0=1,atol=1e-6,rtol=0,record_attempts=True)
        self.assertEqual(len(calls),12*len(r['attempts']))
        self.assertGreater(r['rejected'],0)
        accepted=[a for a in r['attempts'] if a['accepted']]
        self.assertEqual((len(accepted),len(r['attempts'])-len(accepted)),(r['accepted'],r['rejected']))
        self.assertEqual(len(r['trace']),len(accepted)+1)
        trace_index=0
        for a in r['attempts']:
            t,y=r['trace'][trace_index]
            self.assertEqual((a['t'],a['before']),(t,y))
            self.assertEqual(a['accepted'],a['ratio']<=1)
            self.assertTrue(.2<=a['factor']<=2)
            self.assertAlmostEqual(a['estimate'][0],abs(a['whole'][0]-a['twice'][0])/15)
            if a['accepted']:
                trace_index+=1
                self.assertEqual(r['trace'][trace_index][1],a['twice'])
        self.assertAlmostEqual(sum(a['h'] for a in accepted),3)
        self.assertEqual(r['trace'][-1][0],3)
        self.assertLess(abs(r['trace'][-1][1][0]-math.exp(-3)),2e-6)
    def test_compatibility_and_global_error_is_distinct(self):
        for sign in (-1,1):
            f=lambda t,y:[sign*y[0]]
            args=dict(h0=1,atol=1e-6,rtol=0)
            plain=adaptive_rk4(f,0,3,[1],**args)
            logged=adaptive_rk4(f,0,3,[1],record_attempts=True,**args)
            self.assertEqual(set(plain),{'trace','accepted','rejected'})
            self.assertEqual(plain,{k:logged[k] for k in plain})
            self.assertEqual(logged,numerics4.adaptive_rk4(f,0,3,[1],record_attempts=True,**args))
            if sign==1:
                # Não é uma cota universal: um caso basta para refutar a promessa.
                self.assertGreater(abs(logged['trace'][-1][1][0]-math.exp(3)),1e-6)
                self.assertTrue(all(a['ratio']<=1 for a in logged['attempts'] if a['accepted']))
    def test_zero_defect_budget_resolution_and_validation(self):
        r=adaptive_rk4(lambda t,y:[0],0,1,[2],h0=.25,record_attempts=True)
        self.assertTrue(all(a['ratio']==0 and a['factor']==2 for a in r['attempts']))
        self.assertEqual(r['trace'][-1],(1,[2]))
        with self.assertRaises(RuntimeError): adaptive_rk4(lambda t,y:[-y[0]],0,3,[1],h0=3,atol=1e-12,rtol=0,max_trials=1)
        with self.assertRaises(ArithmeticError): adaptive_rk4(lambda t,y:[0],1e20,1e20+1e6,[1],h0=1)
        with self.assertRaises(ValueError): adaptive_rk4(lambda t,y:[float('nan')],0,1,[1])
        with self.assertRaises(ValueError): adaptive_rk4(lambda t,y:[1,2],0,1,[1])
        with self.assertRaises(ValueError): adaptive_rk4(lambda t,y:[0],0,1,[1],record_attempts=1)
