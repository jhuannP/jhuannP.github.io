"""Oscilador normalizado: estágios reais, identidades de energia e tempo final fixo."""
from fractions import Fraction as Q
from math import cos, sin, sqrt, isfinite
from itertools import product
import unittest


def finite(x):
    if isinstance(x, bool) or not isinstance(x, (int, float, Q)):
        raise ValueError('Número real finito necessário')
    try: valid = isfinite(float(x))
    except OverflowError: valid = False
    if not valid: raise ValueError('Número não representável')
    return x


def state(y):
    if len(y) != 2: raise ValueError('Estado com posição e velocidade')
    return tuple(finite(v) for v in y)


def positive(x):
    x = finite(x)
    if x <= 0: raise ValueError('Valor positivo necessário')
    return x


def energy(y, omega=1):
    q, v = state(y); omega = positive(omega)
    return (v*v+omega*omega*q*q)/2


def advance(y, h, omega=1, method='rk4'):
    y, h, omega = state(y), positive(h), positive(omega)
    if method not in ('euler', 'heun', 'rk4'): raise ValueError('Método desconhecido')
    def f(z):
        q, v = state(z)
        return v, -omega*omega*q
    def shifted(z, k, scale): return tuple(a+scale*b for a, b in zip(z, k))
    k1 = f(y)
    if method == 'euler': result = shifted(y, k1, h)
    elif method == 'heun':
        k2 = f(shifted(y, k1, h))
        result = tuple(a+h*(b+c)/2 for a, b, c in zip(y, k1, k2))
    else:
        k2 = f(shifted(y, k1, h/2)); k3 = f(shifted(y, k2, h/2))
        k4 = f(shifted(y, k3, h))
        result = tuple(a+h*(b+2*c+2*d+e)/6 for a, b, c, d, e in zip(y, k1, k2, k3, k4))
    return state(result)


def energy_factor(method, z):
    z = finite(z)
    if method == 'euler': return 1+z*z
    if method == 'heun': return 1+z**4/4
    if method == 'rk4': return 1-z**6/72+z**8/576
    raise ValueError('Método desconhecido')


def exact(t, y=(1, 0), omega=1):
    t = finite(t); q, v = state(y); omega = positive(omega)
    return q*cos(omega*t)+v/omega*sin(omega*t), -omega*q*sin(omega*t)+v*cos(omega*t)


def simulate(final_time, n, method='rk4', y=(1, 0), omega=1):
    final_time, omega, y = positive(final_time), positive(omega), state(y)
    if type(n) is not int or not 1 <= n <= 100000: raise ValueError('Passos inteiros entre 1 e 100000')
    h = float(final_time)/n
    trace = [(0., y)]
    for k in range(n):
        y = advance(y, h, omega, method)
        trace.append(((k+1)*h, y))
    return trace


def scaled_error(y, target, omega=1):
    q, v = state(y); a, b = state(target); omega = positive(omega)
    return sqrt((omega*(q-a))**2+(v-b)**2)


class Checks(unittest.TestCase):
    def test_rational_energy_identity(self):
        count = 0
        for q, v, omega, h, method in product((Q(i, 2) for i in range(-3, 4)),
                (Q(i, 2) for i in range(-3, 4)), (Q(1, 2), Q(1), Q(2)),
                (Q(1, 8), Q(1, 2), Q(1)), ('euler', 'heun', 'rk4')):
            initial = (q, v)
            result = advance(initial, h, omega, method)
            self.assertEqual(energy(result, omega), energy_factor(method, omega*h)*energy(initial, omega))
            count += 1
        self.assertEqual(count, 1323)

    def test_one_step_examples(self):
        y, h, omega = (Q(1), Q(0)), Q(1), Q(1)
        self.assertEqual(advance(y, h, omega, 'euler'), (1, -1))
        self.assertEqual(advance(y, h, omega, 'heun'), (Q(1, 2), -1))
        self.assertEqual(advance(y, h, omega, 'rk4'), (Q(13, 24), Q(-5, 6)))
        self.assertEqual(energy_factor('rk4', Q(1)), Q(569, 576))
        self.assertEqual(energy_factor('rk4', Q(2)), Q(5, 9))
        self.assertGreater(energy_factor('rk4', Q(3)), 1)

    def test_fixed_final_time_convergence(self):
        target = exact(1)
        for method, bounds in (('euler', (1.7, 2.3)), ('heun', (3.7, 4.3)), ('rk4', (15, 17))):
            errors = [scaled_error(simulate(1, n, method)[-1][1], target) for n in (8, 16, 32, 64)]
            ratios = [a/b for a, b in zip(errors, errors[1:])]
            self.assertTrue(all(bounds[0] < r < bounds[1] for r in ratios), (method, ratios))
            print(method, 'erros no mesmo T=1:', errors)
        # Razão de energia acumulada de Euler, conferida também por iteração direta.
        trajectory = simulate(2, 20, 'euler')
        actual = energy(trajectory[-1][1])/energy((1, 0))
        self.assertAlmostEqual(actual, (1+.1**2)**20, delta=1e-12)

    def test_reference_energy_and_wrong_phase(self):
        for omega, q, v, t in product((.5, 1., 2.), (-1., 0., 1.), (-.5, 0., .5), (0., .25, 1., 3.)):
            self.assertAlmostEqual(energy(exact(t, (q, v), omega), omega), energy((q, v), omega), delta=1e-12)
        self.assertEqual(energy((0, 1)), energy((0, -1)))
        self.assertEqual(scaled_error((0, 1), (0, -1)), 2)
        self.assertEqual(advance((Q(0), Q(0)), Q(1), method='rk4'), (0, 0))

    def test_damped_identity(self):
        for q, v, omega, gamma in product((Q(-1), Q(0), Q(2)), (Q(-2), Q(0), Q(1)),
                                         (Q(1, 2), Q(1), Q(2)), (Q(0), Q(1, 4), Q(1))):
            acceleration = -omega*omega*q-2*gamma*v
            derivative = v*acceleration+omega*omega*q*v
            self.assertEqual(derivative, -2*gamma*v*v)
            self.assertLessEqual(derivative, 0)

    def test_contracts_and_input_preservation(self):
        y = [1., 0.]; advance(y, .1); self.assertEqual(y, [1., 0.])
        for bad in ((1,), (1, 0, 0), (float('nan'), 0), (True, 0)):
            with self.assertRaises(ValueError): advance(bad, .1)
        for bad in (0, -1, True, float('inf')):
            with self.assertRaises(ValueError): advance((1, 0), bad)
            with self.assertRaises(ValueError): advance((1, 0), .1, omega=bad)
        for bad in (0, True, 1.5, 100001):
            with self.assertRaises(ValueError): simulate(1, bad)
        with self.assertRaises(ValueError): advance((1, 0), .1, method='outro')


if __name__ == '__main__': unittest.main()
