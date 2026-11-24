"""Exemplos próprios: quadratura racional para polinômios em cubo/tetraedro."""
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
from math import factorial, pi, sin, isfinite
import unittest
NODES = tuple(Q(i, 4) for i in range(5))
WEIGHTS = tuple(Q(i, 90) for i in (7, 32, 12, 32, 7))  # Boole em [0,1], grau <=5.


def rational(v):
    if isinstance(v, bool) or not isinstance(v, (int, Q)):
        raise TypeError('Use int ou Fraction')
    return Q(v)


def quadrature(domain, f):
    if domain not in ('cube', 'tetra'): raise ValueError('Somente os dois domínios previstos')
    result = Q(0)
    for i, j, k in product(range(5), repeat=3):
        u, v, w = NODES[i], NODES[j], NODES[k]
        if domain == 'cube': x, y, z, jac = u, v, w, Q(1)
        else:
            x, y, z = u, (1-u)*v, (1-u)*(1-v)*w
            jac = (1-u)**2*(1-v)
        result += WEIGHTS[i]*WEIGHTS[j]*WEIGHTS[k]*jac*rational(f(x, y, z))
    return result


@lru_cache(maxsize=2)
def unit_moments(domain):
    volume = quadrature(domain, lambda x, y, z: 1)
    mass = quadrature(domain, lambda x, y, z: x+y+z)
    first = tuple(quadrature(domain, lambda x, y, z, axis=axis: (x, y, z)[axis]*(x+y+z))
                  for axis in range(3))
    return volume, mass, first


def properties(domain, length=Q(1), rho0=Q(1)):
    length, rho0 = rational(length), rational(rho0)
    if length <= 0 or rho0 < 0: raise ValueError('L positivo, rho0 não negativo')
    v, m, first = unit_moments(domain)
    volume, mass = length**3*v, rho0*length**3*m
    moments = tuple(rho0*length**4*a for a in first)
    center = tuple(a/mass for a in moments) if mass > 0 else None
    return dict(volume=volume, mass=mass, first=moments, center=center)


def sphere_simpson(radius, n=32):
    if isinstance(radius, bool) or not isinstance(radius, (int, float)) or not isfinite(radius) or not 0 < radius <= 1000:
        raise ValueError('Raio no intervalo didático (0,1000]')
    if type(n) is not int or n <= 0 or n % 2: raise ValueError('Passos pares positivos')
    h = pi/n
    angular = h/3*sum((1 if i in (0, n) else 4 if i % 2 else 2)*sin(i*h) for i in range(n+1))
    # f=1 é separável; a parte radial R³/3 e a azimutal 2pi são analíticas.
    return radius**3/3*angular*2*pi


class Checks(unittest.TestCase):
    def test_monomial_integrals(self):
        count = 0
        for a, b, c in product(range(4), repeat=3):
            if a+b+c > 3: continue
            f = lambda x, y, z: x**a*y**b*z**c
            self.assertEqual(quadrature('cube', f), Q(1, (a+1)*(b+1)*(c+1)))
            expected = Q(factorial(a)*factorial(b)*factorial(c), factorial(a+b+c+3))
            self.assertEqual(quadrature('tetra', f), expected)
            count += 1
        self.assertEqual(count, 20)

    def test_known_mass_and_moments(self):
        cube, tetra = properties('cube'), properties('tetra')
        self.assertEqual(cube, dict(volume=1, mass=Q(3, 2), first=(Q(5, 6),)*3, center=(Q(5, 9),)*3))
        self.assertEqual(tetra, dict(volume=Q(1, 6), mass=Q(1, 8), first=(Q(1, 30),)*3, center=(Q(4, 15),)*3))

    def test_scale_and_massless_case(self):
        for domain, length, rho in product(('cube', 'tetra'), (Q(1, 2), Q(1), Q(2), Q(3)),
                                           (Q(0), Q(1), Q(2), Q(5, 2))):
            base, changed = properties(domain), properties(domain, length, rho)
            self.assertEqual(changed['volume'], length**3*base['volume'])
            self.assertEqual(changed['mass'], rho*length**3*base['mass'])
            self.assertEqual(changed['first'], tuple(rho*length**4*m for m in base['first']))
            if rho:
                self.assertEqual(changed['center'], tuple(length*m for m in base['center']))
            else: self.assertIsNone(changed['center'])

    def test_spherical_quadrature(self):
        for radius in (.5, 1., 2., 3.):
            reference = 4*pi*radius**3/3
            errors = [abs(sphere_simpson(radius, n)/reference-1) for n in (8, 16, 32)]
            self.assertGreater(errors[0], errors[1]); self.assertGreater(errors[1], errors[2])
            self.assertLess(errors[-1], 1e-6)
        self.assertAlmostEqual(sphere_simpson(2)/sphere_simpson(1), 8)

    def test_domain_and_measure(self):
        # Seis monômios formam base dos polinômios unidimensionais de grau <=5.
        for degree in range(6):
            self.assertEqual(sum(w*x**degree for w, x in zip(WEIGHTS, NODES)), Q(1, degree+1))
        # Mudança triangular: cada ponto da malha mapeia para o tetraedro.
        for u, v, w in product(NODES, repeat=3):
            x, y, z = u, (1-u)*v, (1-u)*(1-v)*w
            self.assertGreaterEqual(min(x, y, z), 0)
            self.assertLessEqual(x+y+z, 1)
        self.assertEqual(quadrature('cube', lambda x, y, z: 1), 1)
        self.assertEqual(quadrature('tetra', lambda x, y, z: 1), Q(1, 6))

    def test_contracts(self):
        with self.assertRaises(ValueError): properties('outro')
        with self.assertRaises(ValueError): properties('cube', length=0)
        with self.assertRaises(ValueError): properties('cube', rho0=-1)
        with self.assertRaises(TypeError): properties('cube', length=1.)
        with self.assertRaises(TypeError): quadrature('cube', lambda x, y, z: 1.)
        for bad in (0, -1, True, float('nan'), 1001):
            with self.assertRaises(ValueError): sphere_simpson(bad)
        for bad in (0, 3, True):
            with self.assertRaises(ValueError): sphere_simpson(1, bad)


if __name__ == '__main__':
    for domain in ('cube', 'tetra'): print(domain, properties(domain))
    unittest.main()
