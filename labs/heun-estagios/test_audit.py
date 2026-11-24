import math
import unittest
from decimal import Decimal,localcontext
from fractions import Fraction as Q
from numerics4 import step,integrate
from .audit import factor,experiment

class HeunAuditTests(unittest.TestCase):
    def test_actual_stage_arguments_and_nonlinear_distinction(self):
        calls=[]
        def rhs(t,y):
            calls.append((t,tuple(y)))
            return [y[0]**2]
        result=step(rhs,0,[1],.5,'heun')[0]
        self.assertEqual(calls,[(0.,(1.,)),(.5,(1.5,))])
        self.assertEqual(result,29/16)
        midpoint=1+.5*(1+.25)**2
        self.assertEqual(midpoint,57/32)
        self.assertNotEqual(result,midpoint)
        self.assertNotEqual(result,2)  # continuous solution at t=1/2

    def test_every_node_against_exact_linear_recurrence(self):
        for a in (1,2,5):
            for n in (1,2,4,8,16):
                trace=integrate(lambda t,y:[-a*y[0]],0,1,[1],n,'heun')
                for i,(t,y) in enumerate(trace):
                    self.assertAlmostEqual(y[0],float(factor(Q(a,n))**i),places=12)
        self.assertEqual(factor(Q(3,2)),Q(5,8))
        self.assertEqual(factor(2),1)
        self.assertGreater(factor(Q(5,2)),1)
        for j in range(1,41):self.assertGreater(factor(Q(j,10)),0)

    def test_nonautonomous_affine_rhs_integrated_exactly(self):
        # Trapezoidal integration of a linear-in-time derivative is exact.
        # This catches using the wrong time in the second derivative evaluation.
        for m in (-2,0,3):
            for b in (-1,2):
                for n in (1,2,4,8):
                    trace=integrate(lambda t,y:[m*t+b],0,1,[2],n,'heun')
                    for t,y in trace:
                        self.assertAlmostEqual(y[0],2+m*t*t/2+b*t,places=13)

    def test_local_defect_global_order_and_cost(self):
        with localcontext() as ctx:
            ctx.prec=60
            defects=[]
            for n in (10,20,40):
                h=Decimal(1)/n
                defects.append(abs((-h).exp()-(1-h+h*h/2)))
            for a,b in zip(defects,defects[1:]):
                self.assertGreater(a/b,Decimal('7.8'))
                self.assertLess(a/b,8)
        rows=[experiment(n,'heun') for n in (10,20,40,80)]
        for row in rows:self.assertEqual(row['evaluations'],2*row['n'])
        for a,b in zip(rows,rows[1:]):
            self.assertGreater(a['error']/b['error'],3.8)
            self.assertLess(a['error']/b['error'],4.3)
        euler=experiment(20,'euler');heun=experiment(10,'heun')
        self.assertEqual(euler['evaluations'],heun['evaluations'])
        self.assertLess(heun['error'],euler['error'])  # this IVP, not universal

    def test_contracts_and_existing_engine(self):
        for q in (True,.5,'1/2'):
            with self.assertRaises(TypeError):factor(q)
        for q in (0,-1):
            with self.assertRaises(ValueError):factor(q)
        with self.assertRaises(ValueError):experiment(0,'heun')
        with self.assertRaises(ValueError):step(lambda t,y:[math.inf],0,[1],.1,'heun')
        with self.assertRaises(ValueError):step(lambda t,y:[1,2],0,[1],.1,'heun')
        with self.assertRaises(ValueError):step(lambda t,y:[-y[0]],0,[1],0,'heun')

if __name__ == "__main__":unittest.main()
