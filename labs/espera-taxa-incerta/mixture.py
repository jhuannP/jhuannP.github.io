"""Exemplo próprio. q_i=exp(-lambda_i * 1 dia); tempos inteiros em dias."""
from fractions import Fraction as Q
from itertools import product
from math import log, exp, isclose
import unittest


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Q)):
        raise TypeError('Use int ou Fraction; floats não são racionais exatos aqui')
    return Q(x)


def parameters(p, q):
    p = rational(p)
    q = tuple(rational(v) for v in q)
    if not 0 <= p <= 1 or len(q) != 2 or not all(0 < v < 1 for v in q):
        raise ValueError('Peso entre 0 e 1 e duas sobrevivências estritamente entre 0 e 1')
    return p, q


def day(n):
    if type(n) is not int or n < 0:
        raise ValueError('Use número inteiro não negativo de dias')
    return n


def survival(t, p=Q(1, 2), q=(Q(1, 2), Q(1, 4))):
    p, q = parameters(p, q)
    t = day(t)
    return p*q[0]**t + (1-p)*q[1]**t


def posterior(t, p=Q(1, 2), q=(Q(1, 2), Q(1, 4))):
    p, q = parameters(p, q)
    t = day(t)
    masses = (p*q[0]**t, (1-p)*q[1]**t)
    # Denominador positivo para tempos inteiros finitos e parâmetros aceitos.
    return tuple(m/sum(masses) for m in masses)


def additional(t, s, p=Q(1, 2), q=(Q(1, 2), Q(1, 4))):
    day(t); day(s)
    return survival(t+s, p, q)/survival(t, p, q)


def simpson(f, hi=32, n=4096):
    # Quadratura aproximada; não é uma prova do limite de integração infinito.
    h = hi/n
    return h/3*(f(0)+f(hi)+sum((4 if k % 2 else 2)*f(k*h) for k in range(1, n)))


class Checks(unittest.TestCase):
    def test_example(self):
        self.assertEqual(survival(1), Q(3, 8))
        self.assertEqual(survival(2), Q(5, 32))
        self.assertEqual(posterior(1), (Q(2, 3), Q(1, 3)))
        self.assertEqual(posterior(2), (Q(4, 5), Q(1, 5)))
        self.assertEqual(additional(1, 1), Q(5, 12))
        self.assertNotEqual(additional(1, 1), survival(1))

    def test_joint_table_and_updates(self):
        # K=floor(T/dia), bins 0..11 e cauda 12+. Diferenças de sobrevivências
        # geram uma tabela conjunta normalizada; os eventos são somas de células.
        configs = 0
        for p, q in product((Q(0), Q(1, 5), Q(1, 2), Q(4, 5), Q(1)),
                            ((Q(1, 2), Q(1, 4)), (Q(3, 4), Q(1, 4)), (Q(1, 2), Q(1, 2)))):
            table = [(i, k, w*v**k*(1-v)) for i, (w, v) in enumerate(zip((p, 1-p), q)) for k in range(12)]
            table += [(i, 12, w*v**12) for i, (w, v) in enumerate(zip((p, 1-p), q))]
            self.assertEqual(sum(m for _, _, m in table), 1)
            for t, s in product(range(7), range(5)):
                known = sum(m for _, k, m in table if k >= t)
                slow = sum(m for i, k, m in table if i == 0 and k >= t)
                future = sum(m for _, k, m in table if k >= t+s)
                w = posterior(t, p, q)
                self.assertEqual(w, (slow/known, 1-slow/known))
                self.assertEqual(additional(t, s, p, q), future/known)
                self.assertEqual(additional(t, s, p, q), sum(a*b**s for a, b in zip(w, q)))
                self.assertEqual(posterior(s, w[0], q), posterior(t+s, p, q))
                configs += 1
        self.assertEqual(configs, 525)

    def test_single_rate_limits(self):
        for t, s in product(range(8), range(6)):
            for p in (Q(0), Q(1, 3), Q(1)):
                self.assertEqual(additional(t, s, p, (Q(2, 3), Q(2, 3))), Q(2, 3)**s)
            self.assertEqual(additional(t, s, Q(1)), Q(1, 2)**s)
            self.assertEqual(additional(t, s, Q(0)), Q(1, 4)**s)

    def test_density_and_remaining_mean(self):
        rates = (log(2), 2*log(2))  # dia^-1
        for t in (0, 1, 2):
            w = tuple(float(v) for v in posterior(t))
            density = lambda u: sum(a*b*exp(-b*u) for a, b in zip(w, rates))
            tail = sum(a*exp(-b*32) for a, b in zip(w, rates))
            self.assertAlmostEqual(simpson(density)+tail, 1, delta=2e-8)
            mean_tail = sum(a*(32+1/b)*exp(-b*32) for a, b in zip(w, rates))
            actual = simpson(lambda u: u*density(u))+mean_tail
            expected = sum(a/b for a, b in zip(w, rates))
            self.assertAlmostEqual(actual, expected, delta=2e-8)
        self.assertTrue(isclose(sum(a/b for a, b in zip((2/3, 1/3), rates)), 5/(6*log(2))))

    def test_hazard_derivative(self):
        def hazard(t):
            masses = [exp(-r*t)/2 for r in (log(2), 2*log(2))]
            return sum(m*r for m, r in zip(masses, (log(2), 2*log(2))))/sum(masses)
        for t in (0, 1, 2, 4):
            h = hazard(t)
            a = 1/(1+2**(-t))
            var = a*(log(2)-h)**2+(1-a)*(2*log(2)-h)**2
            derivative = (hazard(t+1e-4)-hazard(t-1e-4))/(2e-4)
            self.assertAlmostEqual(derivative, -var, delta=1e-8)
        self.assertAlmostEqual(hazard(1)/log(2), 4/3)

    def test_contracts(self):
        for t in (-1, True, Q(1, 2), float('nan')):
            with self.assertRaises(ValueError): posterior(t)
        for p, q in ((Q(-1), (Q(1, 2), Q(1, 4))), (Q(2), (Q(1, 2), Q(1, 4))),
                     (Q(1, 2), (Q(0), Q(1, 4))), (Q(1, 2), (Q(1), Q(1, 4))),
                     (Q(1, 2), (Q(1, 4),))):
            with self.assertRaises(ValueError): parameters(p, q)
        with self.assertRaises(TypeError): parameters(.5, (Q(1, 2), Q(1, 4)))


if __name__ == '__main__':
    print('Após um dia:', posterior(1), '; mais um dia:', additional(1, 1))
    unittest.main()
