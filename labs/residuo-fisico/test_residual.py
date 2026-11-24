import itertools
import math
import unittest
from fractions import Fraction as F
from .residual import trial,residual,loss_gradient,step,alias

class ResidualTests(unittest.TestCase):
    def test_spatial_derivative_oracle(self):
        # Segunda diferença é exata para qualquer polinômio cúbico.
        h=F(1,100)
        for a,b in itertools.product((-1,0,F(1,2),1,2),repeat=2):
            self.assertEqual(trial(a,b,0),0);self.assertEqual(trial(a,b,1),0)
            for x in (F(1,4),F(1,2),F(3,4)):
                d2=(trial(a,b,x+h)-2*trial(a,b,x)+trial(a,b,x-h))/(h*h)
                self.assertEqual(-d2-2,residual(a,b,x))

    def test_parameter_gradients_independent_loss(self):
        h=F(1,1000)
        for xs in ((F(1,4),F(3,4)),(F(1,8),F(1,2),F(7,8))):
            for a,b in itertools.product((F(0),F(1,2),F(1)),repeat=2):
                # Loss from an independent spatial second-difference, not residual().
                def objective(A,B):
                    ds=[-(trial(A,B,x+h)-2*trial(A,B,x)+trial(A,B,x-h))/(h*h)-2 for x in xs]
                    return sum(z*z for z in ds)/len(xs)
                loss,g=loss_gradient(a,b,xs)
                self.assertEqual(loss,objective(a,b))
                self.assertEqual(g[0],(objective(a+h,b)-objective(a-h,b))/(2*h))
                self.assertEqual(g[1],(objective(a,b+h)-objective(a,b-h))/(2*h))

    def test_step_and_exact_reference(self):
        xs=(F(1,4),F(3,4));self.assertEqual(loss_gradient(0,0,xs),(F(4),(F(-8),F(-4))))
        a,b=step(0,0,xs,F(1,16));self.assertEqual((a,b),(F(1,2),F(1,4)))
        self.assertEqual(loss_gradient(a,b,xs)[0],F(45,64))
        self.assertEqual(loss_gradient(1,0,xs)[0],0)
        for j in range(9):
            x=F(j,8);self.assertEqual(trial(1,0,x),x-x*x)

    def test_aliasing_detected_off_grid(self):
        coarse=[alias(F(j,4)) for j in range(5)]
        self.assertLess(max(abs(v['residual']) for v in coarse),1e-11)
        for j,sgn in zip((1,3,5,7),(1,-1,1,-1)):
            z=alias(F(j,8));self.assertAlmostEqual(z['error'],sgn/8)
            self.assertAlmostEqual(z['residual'],sgn*2*math.pi**2)
        self.assertAlmostEqual(alias(F(1,8))['error'],.125)

    def test_contracts(self):
        for x in (-1,2,True,0.5,'1'):
            with self.assertRaises(ValueError):trial(1,0,x)
        with self.assertRaises(ValueError):loss_gradient(0,0,())
        with self.assertRaises(ValueError):step(0,0,(F(1,2),),0)
        with self.assertRaises(ValueError):alias(F(1,2),k=0)
