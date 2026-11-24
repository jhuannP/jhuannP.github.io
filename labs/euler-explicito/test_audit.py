import math
import unittest
from fractions import Fraction as Q
from decimal import Decimal, localcontext
from numerics4 import integrate
from .audit import exact_recurrence,regime,refinement

class EulerAuditTests(unittest.TestCase):
    def test_integrator_against_rational_closed_recurrence(self):
        for a in (1,2,5):
            for n in (1,2,4,8,16):
                trace=integrate(lambda t,y:[-a*y[0]],0,1,[1],n,'euler')
                self.assertEqual(len(trace),n+1)
                self.assertEqual(trace[-1][0],1)
                for i,(t,y) in enumerate(trace):
                    self.assertAlmostEqual(y[0],float(exact_recurrence(Q(a,n),i)),places=13)
                    self.assertEqual(t,i/n)
        self.assertEqual(exact_recurrence(Q(1,2),2),Q(1,4))

    def test_regime_boundaries(self):
        samples=(Q(1,2),1,Q(3,2),2,Q(5,2))
        names=("decaimento positivo","anulacao em um passo","alternancia com decaimento",
               "alternancia sem decaimento","alternancia com crescimento")
        for q,name in zip(samples,names):self.assertEqual(regime(q),name)
        self.assertEqual([exact_recurrence(2,n) for n in range(4)],[1,-1,1,-1])
        self.assertEqual(exact_recurrence(1,1),0)
        self.assertGreater(abs(exact_recurrence(Q(5,2),4)),1)
        self.assertLess(exact_recurrence(Q(3,2),1),0)

    def test_local_defect_scaling_and_global_refinement(self):
        with localcontext() as ctx:
            ctx.prec=60
            defects=[]
            for n in (10,20,40,80):
                h=Decimal(1)/n
                defects.append((-h).exp()-(1-h))
            for a,b in zip(defects,defects[1:]):
                self.assertGreater(a/b,Decimal('3.8'))
                self.assertLess(a/b,4)
        rows=refinement()
        for first,second in zip(rows,rows[1:]):
            self.assertGreater(first[2],second[2])
            self.assertGreater(first[2]/second[2],1.9)
            self.assertLess(first[2]/second[2],2.2)

    def test_global_bound_and_exact_solution_underestimate(self):
        # Independent continuous reference exp(-1), with y''<=1 and Lipschitz L=1.
        for n in (2,4,8,16,32,64,128):
            y=integrate(lambda t,y:[-y[0]],0,1,[1],n,'euler')[-1][1][0]
            self.assertLess(y,math.exp(-1))
            self.assertLessEqual(abs(y-math.exp(-1)),(math.e-1)/(2*n))

    def test_contracts_and_existing_engine_validation(self):
        for q in (True,.5,'1/2'):
            with self.assertRaises(TypeError):exact_recurrence(q,2)
        for q in (0,-1):
            with self.assertRaises(ValueError):regime(q)
        with self.assertRaises(TypeError):exact_recurrence(1,True)
        with self.assertRaises(ValueError):exact_recurrence(1,-1)
        with self.assertRaises(ValueError):integrate(lambda t,y:[-y[0]],0,1,[1],0,'euler')
        with self.assertRaises(ValueError):integrate(lambda t,y:[float('nan')],0,1,[1],2,'euler')
        with self.assertRaises(ValueError):integrate(lambda t,y:[1,2],0,1,[1],2,'euler')

if __name__ == "__main__":unittest.main()
