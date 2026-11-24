"""Modelo original: sítio único, repressor livre fixo, média linear de RNA."""
from fractions import Fraction as Q
from itertools import product
from math import exp, expm1, isfinite
import unittest


def rational(v):
    if isinstance(v, bool) or not isinstance(v, (int, Q)):
        raise TypeError('Use int ou Fraction para os parâmetros exatos')
    return Q(v)


def steady(r, kon=Q(1, 10), koff=Q(1), alpha=Q(8), decay=Q(1, 2), binds=True):
    r, kon, koff, alpha, decay = map(rational, (r, kon, koff, alpha, decay))
    if r < 0 or alpha < 0 or min(kon, koff, decay) <= 0 or type(binds) is not bool:
        raise ValueError('Parâmetros de ligação/remoção positivos; r e alpha não negativos')
    kd = koff/kon
    bound = r/(kd+r) if binds else Q(0)
    free = 1-bound
    synthesis = alpha*free
    return dict(kd=kd, bound=bound, free=free, synthesis=synthesis, rna=synthesis/decay)


def transient(t, r=Q(30), kon=Q(1, 10), koff=Q(1), alpha=Q(8), decay=Q(1, 2), theta0=0., m0=16.):
    params = steady(r, kon, koff, alpha, decay)
    t, theta0, m0 = state(t, theta0, m0)
    b, d, a = float(kon*r+koff), float(decay), float(alpha)
    equilibrium = float(params['bound']); mean = float(params['rna'])
    theta = equilibrium+(theta0-equilibrium)*exp(-b*t)
    # Convolução positiva e estável, inclusive quando as duas taxas são iguais.
    if b == d: convolution = t*exp(-d*t)
    else:
        low, gap = min(b, d), abs(b-d)
        convolution = exp(-low*t)*(-expm1(-gap*t))/gap
    m = mean+(m0-mean)*exp(-d*t)-a*(theta0-equilibrium)*convolution
    return theta, m


def state(t, theta0, m0):
    for value in (t, theta0, m0):
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value):
            raise ValueError('Tempo e estado reais finitos')
    if not 0 <= t <= 20 or not 0 <= theta0 <= 1 or m0 < 0:
        raise ValueError('Tempo didático entre 0 e 20 min; ocupação em [0,1], RNA não negativo')
    return float(t), float(theta0), float(m0)


def rk4(t, n=512, r=Q(30), kon=Q(1, 10), koff=Q(1), alpha=Q(8), decay=Q(1, 2), theta0=0., m0=16.):
    steady(r, kon, koff, alpha, decay)  # Contrato dos parâmetros antes de converter.
    t, theta, m = state(t, theta0, m0)
    if type(n) is not int or n <= 0: raise ValueError('Passos inteiros positivos')
    on, off, a, d = map(float, (kon*r, koff, alpha, decay))
    def f(x, y): return on*(1-x)-off*x, a*(1-x)-d*y
    h = t/n
    for _ in range(n):
        a1, b1 = f(theta, m)
        a2, b2 = f(theta+h*a1/2, m+h*b1/2)
        a3, b3 = f(theta+h*a2/2, m+h*b2/2)
        a4, b4 = f(theta+h*a3, m+h*b3)
        theta += h*(a1+2*a2+2*a3+a4)/6
        m += h*(b1+2*b2+2*b3+b4)/6
        if not isfinite(theta) or not isfinite(m) or not -1e-12 <= theta <= 1+1e-12 or m < -1e-12:
            raise ArithmeticError('Passo não preservou estado admissível; não truncar a saída')
    return theta, m


class Checks(unittest.TestCase):
    def test_exact_stationary_balances(self):
        count = 0
        for r, kon, koff, d in product((Q(0), Q(1), Q(10), Q(30), Q(100)),
                                      (Q(1, 10), Q(1, 5)), (Q(1), Q(2)), (Q(1, 2), Q(2))):
            s = steady(r, kon, koff, decay=d)
            self.assertEqual(s['free']+s['bound'], 1)
            self.assertEqual(kon*r*s['free'], koff*s['bound'])
            self.assertEqual(8*s['free'], d*s['rna'])
            self.assertTrue(0 <= s['bound'] <= 1)
            count += 1
        self.assertEqual(count, 40)

    def test_cis_trans_and_ambiguity(self):
        a, b = steady(Q(30)), steady(Q(30), binds=False)
        self.assertEqual((a['kd'], a['bound'], a['synthesis'], a['rna']), (10, Q(3, 4), 2, 4))
        self.assertEqual(b['rna'], 16); self.assertEqual(a['rna']/b['rna'], Q(1, 4))
        self.assertEqual(steady(Q(0))['rna'], 16)
        self.assertEqual(steady(Q(30), kon=Q(1, 30))['rna'], 8)
        same = steady(Q(0), decay=Q(2))
        self.assertEqual(same['rna'], a['rna'])
        self.assertNotEqual(same['synthesis'], a['synthesis'])

    def test_response_scales_and_initial_derivative(self):
        self.assertEqual(1/(Q(1, 10)*30+1), Q(1, 4))
        self.assertEqual(1/Q(1, 2), 2)
        self.assertEqual(transient(0), (0, 16))
        self.assertEqual(8*(1-0)-.5*16, 0)
        self.assertEqual(8*(1-.75)-.5*16, -6)  # Supor ocupação instantânea muda a derivada inicial.
        for t in (.25, .5, 1., 2., 5.):
            expected, observed = transient(t), rk4(t)
            for exact, numerical in zip(expected, observed):
                self.assertAlmostEqual(exact, numerical, delta=1e-7)
        self.assertLess(abs(transient(20)[1]-4), .001)

    def test_equal_and_near_equal_rates(self):
        # kon*r+koff=0.5=decay: evita divisão 0/0 na solução de convolução.
        for t in (.25, 1., 2., 5.):
            params = dict(r=Q(4), koff=Q(1, 10))
            analytical, numerical = transient(t, **params), rk4(t, **params)
            for a, b in zip(analytical, numerical): self.assertAlmostEqual(a, b, delta=1e-7)
            close = transient(t, r=Q(4), koff=Q(100000001, 10**9))
            self.assertAlmostEqual(close[1], analytical[1], delta=1e-7)

    def test_monotonicity_and_zero_production(self):
        points = [steady(Q(r)) for r in range(101)]
        self.assertTrue(all(a['bound'] < b['bound'] for a, b in zip(points, points[1:])))
        self.assertTrue(all(a['rna'] > b['rna'] for a, b in zip(points, points[1:])))
        self.assertEqual(steady(Q(30), alpha=Q(0))['rna'], 0)
        for r in (Q(0), Q(1), Q(100)):
            self.assertEqual(steady(r, binds=False)['rna'], 16)

    def test_contracts(self):
        for kwargs in (dict(r=Q(-1)), dict(r=Q(30), kon=Q(0)), dict(r=Q(30), decay=Q(0)),
                       dict(r=Q(30), koff=Q(-1)), dict(r=Q(30), binds=1)):
            with self.assertRaises(ValueError): steady(**kwargs)
        with self.assertRaises(TypeError): steady(30.)
        with self.assertRaises(TypeError): steady(True)
        for t in (-1, 21, True, float('nan')):
            with self.assertRaises(ValueError): transient(t)
        for n in (0, True, 1.5):
            with self.assertRaises(ValueError): rk4(1, n)


if __name__ == '__main__':
    print('A:', steady(Q(30)), '; B:', steady(Q(30), binds=False))
    print('Depois de 1 min, ocupação e RNA médio:', transient(1))
    unittest.main()
