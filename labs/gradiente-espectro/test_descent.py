import unittest
from fractions import Fraction as Q
from itertools import product
from .descent import inspect,history,contraction,exact_line_step


class DescentTests(unittest.TestCase):
    def test_reference_and_line_search(self):
        self.assertEqual(history(Q(1,4),1)[-1]['point'],(Q(3,4),0))
        self.assertEqual(history(Q(1,4),1)[-1]['objective'],Q(9,32))
        self.assertEqual(exact_line_step((1,1)),Q(17,65))
        best=history(Q(17,65),1)[-1]
        self.assertEqual(best['point'],(Q(48,65),Q(-3,65)))
        self.assertEqual(best['objective'],Q(234,845))
        self.assertEqual(best['gradient'][0]+4*best['gradient'][1],0)
        self.assertLess(best['objective'],Q(9,32))
        self.assertGreater(history(Q(2,5),1)[-1]['objective'],Q(9,32))

    def test_closed_form_and_gradient_bounds(self):
        # 7 stepsizes x 9 starts x 9 states = 567 closed-form comparisons.
        for eta,x,y in product((Q(0),Q(1,10),Q(1,4),Q(2,5),Q(1,2),Q(3,4),Q(1)),(-1,0,2),(-2,0,1)):
            rows=history(eta,8,(x,y))
            for k,row in enumerate(rows):
                self.assertEqual(row['point'],(x*(1-eta)**k,y*(1-4*eta)**k))
                self.assertLessEqual(row['objective'],row['gradient_norm_squared']/2)
                self.assertGreaterEqual(row['objective'],row['gradient_norm_squared']/8)
        # Exact central differentiation of a quadratic, independent of coded gradient.
        h=Q(1,7)
        for x,y in product((-2,0,3),repeat=2):
            dfx=(inspect((x+h,y))['objective']-inspect((x-h,y))['objective'])/(2*h)
            dfy=(inspect((x,y+h))['objective']-inspect((x,y-h))['objective'])/(2*h)
            self.assertEqual((dfx,dfy),inspect((x,y))['gradient'])

    def test_uniform_contraction_optimum(self):
        self.assertEqual(contraction(Q(2,5)),Q(3,5))
        for j in range(101):self.assertGreaterEqual(contraction(Q(j,100)),Q(3,5))
        # These samples are sanity checks; lesson gives the all-real minimax argument.
        rows=history(Q(2,5),10)
        for k,row in enumerate(rows):self.assertEqual(row['objective'],Q(5,2)*Q(9,25)**k)

    def test_boundary_and_invariant_subspace(self):
        rows=history(Q(1,2),11);a,b=rows[10:]
        self.assertLess(a['objective']-b['objective'],Q(1,10**6))
        self.assertGreaterEqual(a['gradient_norm_squared'],16)
        self.assertEqual((rows[10]['point'][1],rows[11]['point'][1]),(1,-1))
        self.assertEqual(history(1,1,(1,0))[-1]['point'],(0,0))
        self.assertEqual(history(1,5,(1,1))[-1]['point'][1],-243)
        self.assertIsNone(exact_line_step((0,0)))

    def test_old_snippet_and_contracts(self):
        eta=.25;x,y=1.,1.
        for _ in range(40):x,y=x-eta*x,y-eta*4*y
        self.assertLess(abs(x),2e-5);self.assertEqual(y,0)
        for eta in (Q(-1),Q(3)):
            with self.assertRaises(ValueError):history(eta,2)
        for steps in (-1,201,True,1.):
            with self.assertRaises(ValueError):history(Q(1,4),steps)
        for eta in (True,.25,'1/4'):
            with self.assertRaises(TypeError):history(eta,2)
