import unittest
from math import pi,log,sqrt
from .modes import mode,derivative,eigenvalue,inner,simpson


class WeightedModes(unittest.TestCase):
    def test_landmarks_zero_count_and_eigenvalue_scaling(self):
        for n in range(1,7):
            self.assertAlmostEqual(eigenvalue(n)/eigenvalue(1),n*n,places=12)
            for j in range(n+1):
                x=2**(j/n)-1
                self.assertLess(abs(mode(n,x)),1e-13)
            for j in range(n):
                x=2**((j+.5)/n)-1
                self.assertAlmostEqual(mode(n,x),(-1)**j,places=13)
        self.assertAlmostEqual(mode(1,sqrt(2)-1),1,places=14)

    def test_gram_matrix_and_omitted_weight_counterexample(self):
        a=log(2)
        for m in range(1,5):
            for n in range(1,5):
                self.assertAlmostEqual(inner(m,n),a/2 if m==n else 0,delta=3e-10)
                self.assertAlmostEqual(inner(m,n,normalized=True),1 if m==n else 0,delta=1e-9)
        # Independent closed integral: substitution x=exp(a*t)-1,
        # then product-to-sum and endpoint values of integral exp(a*t)cos(k*pi*t).
        ordinary=-3*a*a/2*(1/(a*a+pi*pi)-1/(a*a+9*pi*pi))
        self.assertAlmostEqual(inner(1,2,weighted=False),ordinary,delta=1e-10)
        self.assertLess(ordinary,-.05)
        self.assertGreater(ordinary,-.07)

    def test_flux_residual_refines_in_physical_coordinate(self):
        # A conservative difference uses only samples of mode, not derivative().
        errors=[]
        for h in [.02,.01,.005]:
            err=0
            for n in [1,2,3]:
                for x in [.2,.45,.75]:
                    right=(1+x+h/2)*(mode(n,x+h)-mode(n,x))/h
                    left=(1+x-h/2)*(mode(n,x)-mode(n,x-h))/h
                    A=-(right-left)/h*(1+x)
                    err=max(err,abs(A-eigenvalue(n)*mode(n,x)))
            errors.append(err)
        for coarse,fine in zip(errors,errors[1:]):
            self.assertGreater(coarse/fine,3.8)
            self.assertLess(coarse/fine,4.2)

    def test_rayleigh_and_derivative_from_independent_differences(self):
        for n in range(1,5):
            mass=simpson(lambda x:mode(n,x)**2/(1+x))
            energy=simpson(lambda x:(1+x)*derivative(n,x)**2)
            self.assertAlmostEqual(energy/mass,eigenvalue(n),delta=3e-7)
            for x in [.2,.5,.8]:
                h=1e-5
                numeric=(mode(n,x+h)-mode(n,x-h))/(2*h)
                self.assertAlmostEqual(derivative(n,x),numeric,delta=3e-7)

    def test_boundary_bilinear_form_for_non_eigenfunctions(self):
        # f=x(1-x),g=x²(1-x),p=1+x; exact polynomials evaluated by quadrature.
        f=lambda x:x-x*x;df=lambda x:1-2*x;ddf=lambda x:-2
        g=lambda x:x*x-x**3;dg=lambda x:2*x-3*x*x;ddg=lambda x:2-6*x
        Lf=lambda x:-df(x)-(1+x)*ddf(x)
        Lg=lambda x:-dg(x)-(1+x)*ddg(x)
        nodes=[(.5-sqrt(15)/10,5/18),(.5,4/9),(.5+sqrt(15)/10,5/18)]
        difference=sum(w*(f(x)*Lg(x)-Lf(x)*g(x)) for x,w in nodes)
        boundary=lambda x:(1+x)*(df(x)*g(x)-f(x)*dg(x))
        self.assertAlmostEqual(difference,boundary(1)-boundary(0),places=13)
        # Removing Dirichlet for f=1,g=x makes a nonzero boundary obstruction.
        f0=lambda x:1;df0=lambda x:0;g0=lambda x:x;dg0=lambda x:1
        obstruction=lambda x:(1+x)*(df0(x)*g0(x)-f0(x)*dg0(x))
        self.assertEqual(obstruction(1)-obstruction(0),-1)
        self.assertAlmostEqual(simpson(lambda x:-1,panels=4),obstruction(1)-obstruction(0))

    def test_contracts(self):
        for n in [0,-1,13,True,1.0,'1']:
            with self.assertRaises(ValueError):eigenvalue(n)
        for x in [-.1,1.1,float('nan'),float('inf'),True,'0']:
            with self.assertRaises(ValueError):mode(1,x)
            with self.assertRaises(ValueError):derivative(1,x)
        for panels in [0,3,65538,True,2.0]:
            with self.assertRaises(ValueError):inner(1,2,panels=panels)
        with self.assertRaises(ValueError):inner(1,2,weighted=1)
        with self.assertRaises(ValueError):mode(1,.5,normalized=1)
        with self.assertRaises(ValueError):derivative(1,.5,normalized=1)
