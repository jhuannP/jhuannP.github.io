import unittest
from fractions import Fraction as Q
from math import exp
from .experiment import pece,decay,stability

class PredictorCorrectorTests(unittest.TestCase):
    def test_rational_step_and_closed_recurrence(self):
        q=decay(1,2,final=1)
        self.assertEqual(q['trace'][1]['y'],.625)
        self.assertEqual(q['trace'][2]['predictor'],float(Q(13,32)))
        self.assertEqual(q['trace'][2]['y'],float(Q(47,128)))
        for rate in (Q(1,2),Q(1),Q(2),Q(4)):
            n=8;h=Q(4,n);z=-rate*h
            a=1+z+3*z*z/4;b=z*z/4
            values=[Q(1),1+z+z*z/2]
            for _ in range(1,n):values.append(a*values[-1]-b*values[-2])
            actual=decay(float(rate),n)['trace']
            for p,reference in zip(actual,values):self.assertAlmostEqual(p['y'],float(reference),places=11)

    def test_initialization_polynomial_reproduction_and_evaluation_count(self):
        for n in (2,4,16):
            for f,reference in ((lambda t,y:3,lambda t:1+3*t),(lambda t,y:2*t,lambda t:1+t*t)):
                q=pece(f,1,n)
                self.assertEqual(q['evaluations'],2*n+1)
                self.assertEqual(len(q['trace']),n+1)
                for p in q['trace']:self.assertAlmostEqual(p['y'],reference(p['t']),places=13)

    def test_convergence_local_defect_and_real_stability(self):
        errors=[decay(1,n,final=1)['final_error'] for n in (20,40,80)]
        for a,b in zip(errors,errors[1:]):self.assertGreater(a/b,3.6);self.assertLess(a/b,4.4)
        def defect(h):return abs(exp(h)-(1+h+3*h*h/4)+(h*h/4)*exp(-h))
        self.assertGreater(defect(.01)/defect(.005),7.5)
        self.assertLess(defect(.01)/defect(.005),8.5)
        for z in (-.1,-.5,-1,-1.5,-1.99):self.assertLess(stability(z),1)
        self.assertEqual(stability(-2),1)
        for z in (-2.01,-3,-4):self.assertGreater(stability(z),1)
        self.assertLess(stability(-4,'trap'),1)
        # Na fronteira, (r-1)^2: perturbação inicial produz crescimento linear.
        previous,current=Q(1),Q(1)+Q(1,1000)
        for _ in range(9):previous,current=current,2*current-previous
        self.assertEqual(current,1+Q(10,1000))
        self.assertEqual(decay(2,4)['trace'][-1]['y'],1)
        self.assertGreater(decay(4,4)['max_error'],100)

    def test_contract(self):
        for args in ((0,4),(-1,4),(True,4),(1,1),(1,2.),(1,True)):
            with self.assertRaises(ValueError):decay(*args)
        with self.assertRaises(ValueError):decay(1,4,'other')
        with self.assertRaises(ValueError):pece(lambda t,y:float('nan'))
        with self.assertRaises(ValueError):pece(lambda t,y:y,final=0)
