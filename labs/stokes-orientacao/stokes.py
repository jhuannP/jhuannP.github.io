"""Comparação independente de linha e fluxo para campos polinomiais de grau <=2."""
from fractions import Fraction as Q
from itertools import product
from math import sin, cos, pi
import unittest

NODES = tuple(Q(i,4) for i in range(5))
WEIGHTS = tuple(Q(w,90) for w in (7,32,12,32,7))


def integral(f):
    return sum(w*f(t) for t,w in zip(NODES,WEIGHTS))


def monomial(exps, xyz):
    result = Q(1)
    for n,x in zip(exps,xyz):
        result *= x**n
    return result


def derivative(exps, xyz, axis):
    n = exps[axis]
    if n == 0:
        return Q(0)
    reduced = list(exps)
    reduced[axis] -= 1
    return n*monomial(reduced,xyz)


def graph(coeffs,u,v):
    a,b,c,d,e,f = coeffs
    z = a*u*u+b*u*v+c*v*v+d*u+e*v+f
    return (u,v,z), 2*a*u+b*v+d, b*u+2*c*v+e


def line(component, exps, coeffs):
    # Four CCW edges of the unit parameter square; dz follows the graph.
    def edge(k,t):
        u,v,du,dv = ((t,Q(0),1,0),(Q(1),t,0,1),
                     (1-t,Q(1),-1,0),(Q(0),1-t,0,-1))[k]
        xyz,zu,zv = graph(coeffs,u,v)
        tangent = (du,dv,zu*du+zv*dv)
        return monomial(exps,xyz)*tangent[component]
    return sum(integral(lambda t:edge(k,t)) for k in range(4))


def flux(component, exps, coeffs):
    def integrand(u,v):
        xyz,zu,zv = graph(coeffs,u,v)
        dx,dy,dz = (derivative(exps,xyz,k) for k in range(3))
        # Curl of a field with only the specified component nonzero.
        curl = ((0,dz,-dy),(-dz,0,dx),(dy,-dx,0))[component]
        normal_area = (-zu,-zv,1)
        return sum(a*b for a,b in zip(curl,normal_area))
    return integral(lambda u:integral(lambda v:integrand(u,v)))


def circle(field,radius=1,orientation=1,n=256):
    # Midpoint quadrature. Used only for the smooth circle, never at the axis.
    total = 0.
    for k in range(n):
        t = orientation*2*pi*(k+.5)/n
        x,y = radius*cos(t),radius*sin(t)
        f = field(x,y)
        total += f[0]*(-radius*sin(t))+f[1]*(radius*cos(t))
    return orientation*2*pi*total/n


class Checks(unittest.TestCase):
    def test_quadrature_degree(self):
        for k in range(6):
            self.assertEqual(integral(lambda t:t**k),Q(1,k+1))

    def test_ninety_basis_graph_comparisons(self):
        graphs = ((0,0,0,0,0,0),(1,0,1,0,0,0),(1,-2,3,2,-1,1))
        basis = [e for e in product(range(3),repeat=3) if sum(e)<=2]
        self.assertEqual(len(basis),10)
        for g,c,e in product(graphs,range(3),basis):
            with self.subTest(graph=g,component=c,exponents=e):
                self.assertEqual(line(c,e,g),flux(c,e,g))

    def test_known_curved_square(self):
        g = (1,0,1,0,0,0)  # z=u²+v², normal area=(-2u,-2v,1)
        # F=(-y/2,x/2,0) gives curl=(0,0,1), square-projection flux=1.
        for method in (line,flux):
            self.assertEqual(-method(0,(0,1,0),g)/2+method(1,(1,0,0),g)/2,1)
            # G=(z,0,0): curl=(0,1,0), flux=integral -2v = -1.
            self.assertEqual(method(0,(0,0,1),g),-1)

    def test_circle_and_annulus(self):
        original = lambda x,y:(-y/2,x/2)
        singular = lambda x,y:(-y/(x*x+y*y),x/(x*x+y*y))
        for r in (.5,1.,3.):
            for sign in (-1,1):
                self.assertAlmostEqual(circle(original,r,sign),sign*pi*r*r,places=11)
                self.assertAlmostEqual(circle(singular,r,sign),sign*2*pi,places=11)
        self.assertAlmostEqual(circle(singular,2,1)+circle(singular,1,-1),0,places=11)
        self.assertAlmostEqual(circle(original,2,1)+circle(original,1,-1),3*pi,places=11)


if __name__ == '__main__':
    unittest.main()
