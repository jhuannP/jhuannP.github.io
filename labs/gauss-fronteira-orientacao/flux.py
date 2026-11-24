"""Fluxo por faces com quadratura racional e divergência por momentos.
Domínio exato: campos polinomiais de grau total≤3,cubo/tetraedro unitários.
"""
from fractions import Fraction as Q
from itertools import product
from math import factorial,sin,cos,pi,sqrt
import unittest

NODES=tuple(Q(i,4) for i in range(5))
WEIGHTS=tuple(Q(i,90) for i in (7,32,12,32,7))


def polynomial(terms):
    out=[]
    for axis,powers,coefficient in terms:
        if type(axis) is not int or axis not in range(3) or len(powers)!=3:
            raise ValueError('Componente e expoentes tridimensionais')
        if any(type(x) is not int or x<0 for x in powers) or sum(powers)>3:
            raise ValueError('Grau total de0 a3 neste laboratório')
        if isinstance(coefficient,bool) or not isinstance(coefficient,(int,Q)):
            raise TypeError('Coeficiente racional exato')
        out.append((axis,tuple(powers),Q(coefficient)))
    return tuple(out)


def value(terms,point,axis):
    return sum((coefficient*point[0]**p[0]*point[1]**p[1]*point[2]**p[2]
                for component,p,coefficient in terms if component==axis),Q(0))


def integrate_square(function):
    return sum((wu*wv*function(u,v) for u,wu in zip(NODES,WEIGHTS)
                for v,wv in zip(NODES,WEIGHTS)),Q(0))


def integrate_triangle(function):
    # u=s,v=(1-s)t,Jacobiano1-s. Graus transformados≤4 em s e≤3 em t.
    return integrate_square(lambda s,t:(1-s)*function(s,(1-s)*t))


def face_fluxes(kind,raw_terms):
    terms=polynomial(raw_terms)
    if kind=='cube':
        faces=[]
        for axis in range(3):
            others=[i for i in range(3) if i!=axis]
            for side,sign in ((Q(0),-1),(Q(1),1)):
                def f(u,v):
                    point=[Q(0)]*3;point[axis]=side
                    point[others[0]]=u;point[others[1]]=v
                    return sign*value(terms,point,axis)
                faces.append(integrate_square(f))
        return tuple(faces)
    if kind=='tetra':
        faces=[]
        for axis in range(3):
            others=[i for i in range(3) if i!=axis]
            def f(u,v):
                point=[Q(0)]*3;point[others[0]]=u;point[others[1]]=v
                return -value(terms,point,axis)
            faces.append(integrate_triangle(f))
        faces.append(integrate_triangle(lambda u,v:sum(value(terms,(u,v,1-u-v),axis) for axis in range(3))))
        return tuple(faces)
    raise ValueError('Use cube ou tetra')


def volume_divergence(kind,raw_terms):
    terms=polynomial(raw_terms)
    if kind not in ('cube','tetra'):raise ValueError('Use cube ou tetra')
    total=Q(0)
    for axis,p,coefficient in terms:
        if not p[axis]:continue
        powers=list(p);powers[axis]-=1
        if kind=='cube':
            moment=Q(1,(powers[0]+1)*(powers[1]+1)*(powers[2]+1))
        else:
            moment=Q(factorial(powers[0])*factorial(powers[1])*factorial(powers[2]),factorial(sum(powers)+3))
        total+=coefficient*p[axis]*moment
    return total


def radial_sphere_flux(radius,orientation=1):
    if radius<=0 or orientation not in (-1,1):raise ValueError('Raio positivo e orientação±1')
    n=256;m=16;h=pi/n
    def latitude(theta):
        total=0.
        for j in range(m):
            phi=2*pi*(j+.5)/m
            point=(radius*sin(theta)*cos(phi),radius*sin(theta)*sin(phi),radius*cos(theta))
            norm=sqrt(sum(x*x for x in point))
            field=tuple(x/norm**3 for x in point)
            normal=tuple(orientation*x/radius for x in point)
            total+=sum(x*y for x,y in zip(field,normal))*radius**2*sin(theta)
        return total*(2*pi/m)
    return h/3*(latitude(0)+latitude(pi)+sum((4 if k%2 else 2)*latitude(k*h) for k in range(1,n)))


class Checks(unittest.TestCase):
    def test_quadrature_and_contracts(self):
        for degree in range(6):
            self.assertEqual(sum(w*x**degree for x,w in zip(NODES,WEIGHTS)),Q(1,degree+1))
        for terms in ([(3,(0,0,0),1)],[(0,(-1,0,0),1)],[(0,(4,0,0),1)]):
            with self.assertRaises(ValueError):polynomial(terms)
        with self.assertRaises(TypeError):polynomial([(0,(0,0,0),.5)])
        with self.assertRaises(ValueError):face_fluxes('sphere',[])
        with self.assertRaises(ValueError):radial_sphere_flux(0)

    def test_original_and_tetrahedron(self):
        identity=[(0,(1,0,0),1),(1,(0,1,0),1),(2,(0,0,1),1)]
        self.assertEqual(face_fluxes('cube',identity),(0,1,0,1,0,1))
        field=[(0,(2,0,0),1),(1,(0,1,0),1),(2,(0,0,1),1)]
        self.assertEqual(face_fluxes('tetra',field),(0,0,0,Q(5,12)))
        self.assertEqual(volume_divergence('tetra',field),Q(5,12))

    def test_every_polynomial_basis_up_to_three(self):
        cases=0
        for p in product(range(4),repeat=3):
            if sum(p)>3:continue
            for axis in range(3):
                terms=[(axis,p,1)]
                for kind in ('cube','tetra'):
                    self.assertEqual(sum(face_fluxes(kind,terms)),volume_divergence(kind,terms))
                cases+=1
        self.assertEqual(cases,60)
        print('Campos de base conferidos nos dois sólidos:',cases)

    def test_open_face_needs_other_parts(self):
        constant=[(2,(0,0,0),1)]
        faces=face_fluxes('tetra',constant)
        self.assertEqual(faces,(0,0,Q(-1,2),Q(1,2)))
        self.assertEqual(sum(faces),0)
        self.assertEqual(volume_divergence('tetra',constant),0)
        self.assertNotEqual(faces[-1],0)

    def test_punctured_field_and_shell(self):
        for radius in (.5,1.,3.):
            outer=radial_sphere_flux(radius)
            inner=radial_sphere_flux(radius,-1)
            self.assertAlmostEqual(outer,4*pi,delta=1e-8)
            self.assertAlmostEqual(inner,-4*pi,delta=1e-8)
        total=radial_sphere_flux(3.)+radial_sphere_flux(.5,-1)
        self.assertAlmostEqual(total,0.,delta=1e-12)


if __name__=='__main__':
    unittest.main()
