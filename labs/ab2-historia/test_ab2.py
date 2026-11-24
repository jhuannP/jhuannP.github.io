import unittest
from fractions import Fraction as Q
import numerics4 as shared
from .ab2 import integrate,heun_start,test_sequence,characteristic

class Ab2Tests(unittest.TestCase):
    def test_reference_and_affine_slope(self):
        r=integrate(lambda t,y:-y,1,Q(9,10),Q(1,10),2)
        self.assertEqual(r[-1][1],Q(163,200))
        for n in (2,4,8,16):
            h=Q(1,n);f=lambda t,y:2*t
            start=heun_start(f,1,h)
            trace=integrate(f,1,start,h,n)
            for t,y in trace:self.assertEqual(y,1+t*t)
        calls=[]
        trace=integrate(lambda t,y:(calls.append((t,y)) or 2),0,Q(1,5),Q(1,10),6)
        self.assertEqual(len(calls),6)
        self.assertEqual([t for t,_ in calls],[Q(i,10) for i in range(6)])
        self.assertEqual(trace[-1][1],Q(6,5))
    def test_one_euler_start_keeps_second_order_here(self):
        errors=[]
        for n in (4,8,16):
            h=Q(1,n);r=integrate(lambda t,y:2*t,1,1,h,n)
            for t,y in r[1:]:self.assertEqual(y-(1+t*t),-h*h)
            errors.append(abs(r[-1][1]-2))
        self.assertEqual(errors[0]/errors[1],4)
        self.assertEqual(errors[1]/errors[2],4)
    def test_boundary_parasitic_mode_and_growth(self):
        r=test_sequence(-1,1,0,30)
        for n,y in enumerate(r):self.assertEqual(y,Q(2,3)*Q(1,2)**n+Q(1,3)*(-1)**n)
        self.assertEqual(characteristic(Q(1,2),-1),0)
        self.assertEqual(characteristic(-1,-1),0)
        self.assertEqual(r[2:5],[Q(1,2),Q(-1,4),Q(3,8)])
        stable=test_sequence(Q(-1,2),1,Q(5,8),60)
        self.assertLess(abs(stable[-1]),Q(1,10**10))
        unstable=test_sequence(-2,1,0,16)
        self.assertGreater(abs(unstable[-1]),10000)
        self.assertEqual(test_sequence(0,1,1,10),[1]*11)
        # Signs at -1,0,1 bracket both roots for -1<z<0.
        for j in range(1,20):
            z=Q(-j,20)
            self.assertGreater(characteristic(-1,z),0)
            self.assertLess(characteristic(0,z),0)
            self.assertGreater(characteristic(1,z),0)
    def test_shared_cache_preserves_vector_results_and_reduces_calls(self):
        calls=[]
        def rhs(t,y):
            calls.append(t)
            return [t-y[0]+y[1]*y[1],-y[1]]
        n=20;new=shared.adams_bashforth2(rhs,0,1,[1,.2],n)
        self.assertEqual(len(calls),n+4) # Four RK4 stages, old derivative once, n-1 current.
        def pure(t,y):return [t-y[0]+y[1]*y[1],-y[1]]
        h=1/n;prev=[1,.2];current=shared.step(pure,0,prev,h)
        old_trace=[(0,list(prev)),(h,list(current))]
        for i in range(1,n):
            now=shared.slope(pure,i*h,current);old=shared.slope(pure,(i-1)*h,prev)
            nxt=[a+h*(3*b-c)/2 for a,b,c in zip(current,now,old)]
            prev,current=current,nxt;old_trace.append(((i+1)*h,list(current)))
        self.assertEqual(new,old_trace)
    def test_contracts(self):
        for n in (0,-1,1001,True,2.0):
            with self.assertRaises(ValueError): integrate(lambda t,y:y,1,1,1,n)
        for h in (0,-1,True,0.1):
            with self.assertRaises(ValueError): integrate(lambda t,y:y,1,1,h,2)
        with self.assertRaises(ValueError): integrate(lambda t,y:0.5,1,1,1,2)
        with self.assertRaises(ValueError): integrate(None,1,1,1,2)
