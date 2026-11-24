import unittest
from fractions import Fraction as Q
from math import pi
from .plane import potential_field,surface,force_energy


def simpson(f,a,b,n=2000):
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,n)))


class PlaneTests(unittest.TestCase):
    def test_fixture(self):
        r=force_energy();self.assertEqual(r['fz'],Q(-9,8));self.assertEqual(r['energy'],Q(-9,4))
        self.assertEqual(r['induced_potential'],Q(-3,2));self.assertEqual(r['pair_energy'],Q(-9,2))
        phi,e=potential_field(0,0,4);self.assertAlmostEqual(phi,2);self.assertAlmostEqual(e[2],4/3)
        self.assertAlmostEqual(surface(1.5)['charge_in_disk'],-3/5)

    def test_boundary_and_surface_normal(self):
        for q in (-3,3):
            for x,y in [(0,0),(1,0),(1,2),(-3,4)]:
                phi,e=potential_field(x,y,0,q,2,2)
                self.assertEqual(phi,0);self.assertEqual(e[0],0);self.assertEqual(e[1],0)
                sigma=surface((x*x+y*y)**.5,q,2,2)['sigma_times_2pi']/(2*pi)
                epsilon=1/(4*pi*2)
                self.assertAlmostEqual(sigma,epsilon*e[2])

    def test_field_as_potential_gradient(self):
        h=1e-5
        for point in [(1,.5,.7),(-2,1,3),(.5,-1,4)]:
            _,e=potential_field(*point)
            for i in range(3):
                plus=list(point);minus=list(point);plus[i]+=h;minus[i]-=h
                numerical=-(potential_field(*plus)[0]-potential_field(*minus)[0])/(2*h)
                self.assertAlmostEqual(e[i],numerical,places=8)

    def test_induced_surface_integral_force(self):
        # Integra distribuição real: u=a/sqrt(rho²+a²), dQ=q du, de u1 para0.
        for q,a,k in [(3,2,2),(-3,2,2),(2,3,1)]:
            charge=simpson(lambda u:q,1,0)
            force=simpson(lambda u:k*q*q*u**3/a**2,1,0)
            self.assertAlmostEqual(charge,-q)
            self.assertAlmostEqual(force,float(force_energy(q,a,k)['fz']),places=10)

    def test_work_and_scales(self):
        initial=force_energy(3,2,2);final=force_energy(3,4,2)
        work=simpson(lambda height:9/(2*height**2),2,4)
        self.assertEqual(final['energy']-initial['energy'],Q(9,8))
        self.assertAlmostEqual(work,float(final['energy']-initial['energy']),places=10)
        self.assertEqual(initial['pair_energy'],2*initial['energy'])
        scaled=force_energy(6,2,2)
        self.assertEqual(scaled['fz'],4*initial['fz'])
        self.assertEqual(force_energy(-3,2,2)['fz'],initial['fz'])
        self.assertEqual(final['fz'],initial['fz']/4)
        self.assertEqual(final['energy'],initial['energy']/2)

    def test_contracts(self):
        for point in [(0,0,-1),(0,0,2),(True,0,1),(0,0,float('nan'))]:
            with self.assertRaises(ValueError):potential_field(*point)
        for args in [(0,2,2),(3,0,2),(3,2,-1),(3,2.0,2),(True,2,2)]:
            with self.assertRaises(ValueError):force_energy(*args)
        with self.assertRaises(ValueError):surface(-1)
