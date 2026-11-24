import unittest
from fractions import Fraction as Q
from .derivative import pair,add,subtract,multiply,divide,value,quotient,squared_norm

class DerivativeTests(unittest.TestCase):
    def test_rational_arithmetic_against_builtin(self):
        for a,b in ((0,0),(1,2),(-2,3),(Q(1,2),Q(-3,4))):
            for c,d in ((1,0),(0,2),(-1,1)):
                z,w=(a,b),(c,d);zc,wc=complex(a,b),complex(c,d)
                for fun,ref in ((add,zc+wc),(subtract,zc-wc),(multiply,zc*wc),(divide,zc/wc)):
                    actual=complex(*fun(z,w))
                    self.assertAlmostEqual(actual.real,ref.real)
                    self.assertAlmostEqual(actual.imag,ref.imag)
    def test_polynomial_quotient_identity_and_error(self):
        directions=((1,0),(0,1),(1,1),(2,-1),(-3,2))
        for z in ((0,0),(1,1),(2,-3),(Q(1,3),Q(2,5))):
            derivative=(2*z[0],2*z[1])
            for dx,dy in directions:
                for n in (1,10,100):
                    h=(Q(dx,n),Q(dy,n));r=quotient('square',z,h)
                    self.assertEqual(r,add(derivative,h))
                    self.assertEqual(squared_norm(subtract(r,derivative)),squared_norm(h))
        self.assertEqual(quotient('square',(1,1),(Q(1,10),0)),(Q(21,10),Q(2)))
    def test_conjugate_and_axis_trap(self):
        for n in (1,2,10,100):
            t=Q(1,n)
            for h,conj_expected,trap_expected in (
                ((t,0),(1,0),(1,0)),((0,t),(-1,0),(1,0)),((t,t),(0,-1),(-1,0))):
                self.assertEqual(quotient('conjugate',(2,-1),h),conj_expected)
                self.assertEqual(quotient('trap',(0,0),h),trap_expected)
            # Norm identity establishes the continuity bound algebraically.
            for h in ((t,t),(2*t,-3*t),(0,t)):
                self.assertEqual(squared_norm(value('trap',h)),squared_norm(h))
        # Independent Cartesian expression for conj(z)^2/z = conj(z)^3/|z|².
        for x,y in ((1,2),(-2,1),(Q(1,3),Q(1,2))):
            x,y=Q(x),Q(y)
            self.assertEqual(value('trap',(x,y)),((x**3-3*x*y*y)/(x*x+y*y),(y**3-3*x*x*y)/(x*x+y*y)))
    def test_radial_point_derivative_and_cr_axes(self):
        for n in (2,4,8,16):
            h=(Q(1,n),Q(2,n));r=quotient('radial',(0,0),h)
            self.assertEqual(r,(h[0],-h[1]))
            self.assertEqual(squared_norm(r),squared_norm(h))
        # Four real partials at zero from axes: ux=1, uy=0, vx=0, vy=1.
        for t in (Q(1,10),Q(-1,10)):
            fx=value('trap',(t,0));fy=value('trap',(0,t))
            ux,vx=fx[0]/t,fx[1]/t;uy,vy=fy[0]/t,fy[1]/t
            self.assertEqual((ux,uy,vx,vy),(1,0,0,1))
            self.assertEqual(ux,vy);self.assertEqual(uy,-vx)
        # Nonzero point of |z|² fails directional agreement.
        h=(Q(1,100),0);k=(0,Q(1,100))
        self.assertNotEqual(quotient('radial',(1,0),h),quotient('radial',(1,0),k))
    def test_contracts(self):
        for z in (1,(1,),(1,2,3),(True,0),(0.5,0)):
            with self.assertRaises(ValueError): pair(z)
        with self.assertRaises(ValueError): quotient('square',(0,0),(0,0))
        with self.assertRaises(ValueError): divide((1,0),(0,0))
        with self.assertRaises(ValueError): value('unknown',(0,0))
