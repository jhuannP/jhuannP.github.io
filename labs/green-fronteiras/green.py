"""Integrais originais para estudo de Green: casos polinomiais e círculos."""
from fractions import Fraction as Q
from math import cos, sin, pi, isfinite
from itertools import product
import unittest


def field(kind, x, y):
    if kind == 'rotation': return -y, x
    if kind == 'polynomial': return x*x-y, x+y*y
    if kind == 'variable_curl': return 0, x*x
    if kind == 'gradient': return 2*x*y, x*x
    if kind == 'radial': return x, y
    if kind == 'vortex':
        r2 = x*x+y*y
        if r2 == 0: raise ValueError('G não está definido na origem')
        return -y/r2, x/r2
    raise ValueError('Campo desconhecido')


def orientation(s):
    if type(s) is not int or s not in (-1, 1):
        raise ValueError('Orientação +1 ou -1')
    return s


def edge(kind, start, end):
    x, y = map(Q, start); u, v = map(Q, end)
    dx, dy = u-x, v-y
    def integrand(t):
        p, q = field(kind, x+t*dx, y+t*dy)
        return p*dx+q*dy
    # Para os campos polinomiais aqui testados, o integrando tem grau <=2;
    # Simpson por lado é exato. Não é rotina geral de integração exata.
    return (integrand(Q(0))+4*integrand(Q(1, 2))+integrand(Q(1)))/6


def rectangle(kind, x0, y0, width, height, s=1):
    orientation(s)
    if width <= 0 or height <= 0: raise ValueError('Lados positivos')
    if kind not in ('rotation', 'polynomial', 'variable_curl', 'gradient'):
        raise ValueError('Somente os quatro campos polinomiais previstos')
    points = [(x0, y0), (x0+width, y0), (x0+width, y0+height), (x0, y0+height)]
    if s == -1: points.reverse()
    return sum(edge(kind, a, b) for a, b in zip(points, points[1:]+points[:1]))


def circle(kind, radius, s=1, n=128, flux=False):
    orientation(s)
    if isinstance(radius, bool) or not isinstance(radius, (int, float)) or not isfinite(radius) or radius <= 0:
        raise ValueError('Raio positivo finito')
    if type(n) is not int or n < 4: raise ValueError('Ao menos quatro pontos')
    if flux and s != 1: raise ValueError('Neste exemplo o fluxo externo usa somente a curva positiva')
    value = 0.
    for k in range(n):
        t = 2*pi*(k+.5)/n
        angle = s*t
        x, y = radius*cos(angle), radius*sin(angle)
        dx, dy = -s*radius*sin(angle), s*radius*cos(angle)
        p, q = field(kind, x, y)
        value += p*dy-q*dx if flux else p*dx+q*dy
    return value*2*pi/n


def annulus(kind, inner, outer, n=128):
    # circle valida cada raio e a malha; aqui verificamos a ordem.
    if not 0 < inner < outer: raise ValueError('Exige 0<a<R')
    return circle(kind, outer, 1, n)+circle(kind, inner, -1, n)


class Checks(unittest.TestCase):
    def test_rectangles_exact(self):
        count = 0
        for (x, y), w, h, s in product(((-2, 1), (0, 0), (3, -1)), (1, 2, 3), (1, 2, 4), (-1, 1)):
            expected = {'rotation': 2*w*h, 'polynomial': 2*w*h,
                        'variable_curl': h*((x+w)**2-x*x), 'gradient': 0}
            for kind, area in expected.items():
                self.assertEqual(rectangle(kind, x, y, w, h, s), s*area)
                count += 1
        self.assertEqual(count, 216)

    def test_circle_circulation(self):
        for radius, s, n in product((.25, 1., 3.), (-1, 1), (128, 1024)):
            for kind, expected in (('rotation', s*2*pi*radius**2), ('vortex', s*2*pi), ('radial', 0)):
                self.assertAlmostEqual(circle(kind, radius, s, n), expected, delta=1e-10)

    def test_annuli(self):
        for (a, r), n in product(((.25, 1), (.5, 2), (1, 3)), (128, 1024)):
            self.assertAlmostEqual(annulus('vortex', a, r, n), 0, delta=1e-10)
            self.assertAlmostEqual(annulus('rotation', a, r, n), 2*pi*(r*r-a*a), delta=1e-10)

    def test_flux_is_not_circulation(self):
        for r, n in product((.25, 1., 3.), (128, 1024)):
            self.assertAlmostEqual(circle('rotation', r, n=n, flux=True), 0, delta=1e-10)
            self.assertAlmostEqual(circle('radial', r, n=n, flux=True), 2*pi*r*r, delta=1e-10)

    def test_contracts(self):
        with self.assertRaises(ValueError): field('vortex', 0, 0)
        for bad in (0, -1, True, float('inf'), float('nan')):
            with self.assertRaises(ValueError): circle('vortex', bad)
        for bad in (0, True, .5):
            with self.assertRaises(ValueError): circle('rotation', 1, s=bad)
        for bad in (1, True, 4.5):
            with self.assertRaises(ValueError): circle('rotation', 1, n=bad)
        for a, r in ((0, 1), (2, 1), (1, 1)):
            with self.assertRaises(ValueError): annulus('vortex', a, r)
        with self.assertRaises(ValueError): rectangle('vortex', 0, 0, 1, 1)
        with self.assertRaises(ValueError): circle('radial', 1, s=-1, flux=True)


if __name__ == '__main__':
    print('G na coroa:', annulus('vortex', 1, 2))
    print('F na coroa, dividido por pi:', annulus('rotation', 1, 2)/pi)
    unittest.main()
