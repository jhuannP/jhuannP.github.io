"""Resistor e balanço térmico sintéticos. SI; Δ em K, sem dados reais.
O limite de 60 K é hipótese didática, não faixa validada de material.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt, isfinite
import unittest


def finite(x, positive=False):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x):
        raise ValueError('Número real finito necessário')
    if x < 0 or (positive and x == 0):
        raise ValueError('Número positivo necessário' if positive else 'Número não negativo necessário')
    return float(x)


class Thermal:
    def __init__(self, r0=10., alpha=.01, conductance=.2, ceiling=60.):
        self.r0 = finite(r0, True)
        self.alpha = finite(alpha)
        self.g = finite(conductance, True)
        self.ceiling = finite(ceiling, True)

    def resistance(self, delta):
        delta = finite(delta)
        if delta > self.ceiling:
            raise ValueError('Temperatura fora da faixa adotada')
        return self.r0*(1+self.alpha*delta)

    def voltage_balance(self, delta, voltage):
        voltage = finite(voltage)
        return voltage**2/self.resistance(delta)-self.g*delta

    def voltage_formal_root(self, voltage):
        # Raiz algébrica; o chamador ainda precisa conferir a faixa de validade.
        voltage = finite(voltage)
        b = voltage**2/(self.r0*self.g)
        # Forma racionalizada inclui alpha=0 sem cancelamento subtrativo.
        return 2*b/(1+sqrt(1+4*self.alpha*b))

    def voltage_bisection(self, voltage):
        # Só procura dentro da faixa; None NÃO significa inexistência global.
        voltage = finite(voltage)
        if voltage == 0: return 0.
        hi = self.ceiling
        if self.voltage_balance(hi, voltage) > 0: return None
        lo = 0.
        for _ in range(80):
            mid = (hi+lo)/2
            if self.voltage_balance(mid, voltage) > 0: lo = mid
            else: hi = mid
        return (hi+lo)/2

    def current_equilibrium(self, current):
        current = finite(current)
        drive = current**2*self.r0
        restoring = self.g-drive*self.alpha
        if restoring <= 0:
            return {'status': 'sem raiz não negativa', 'delta': None,
                    'linear_growth': -restoring}
        root = drive/restoring
        return {'status': 'na faixa' if root <= self.ceiling else 'fora da faixa',
                'delta': root, 'linear_growth': -restoring}


class Checks(unittest.TestCase):
    def test_geometry_units_and_power(self):
        rho, length, area = Q(15, 10**9), Q(2), Q(1, 10**6)
        self.assertEqual(rho*length/area, Q(3, 100))
        # Aritmética racional exata: sinais passivos, unidades SI.
        for r, v in product((Q(1, 2), Q(2), Q(10)), (Q(-6), Q(0), Q(6))):
            i = v/r
            self.assertEqual(v*i, i*i*r)
            self.assertEqual(v*i, v*v/r)
            self.assertGreaterEqual(v*i, 0)
            self.assertEqual(v*v/(2*r), (v*v/r)/2)
            self.assertEqual(i*i*(2*r), 2*(i*i*r))
        self.assertEqual(Q(18)*Q(5), 90)

    def test_voltage_roots_by_independent_search(self):
        checked = outside = 0
        for r0, alpha, g, v in product((2., 10., 25.), (0., .004, .01), (.1, .2, 1.), (0., 2., 10., 30.)):
            model = Thermal(r0, alpha, g)
            root = model.voltage_formal_root(v)
            found = model.voltage_bisection(v)
            if root <= model.ceiling:
                self.assertIsNotNone(found)
                self.assertAlmostEqual(found, root, delta=1e-10)
                self.assertAlmostEqual(model.voltage_balance(root, v), 0., delta=1e-10)
                # Derivada analítica negativa: C_th>0 implica retorno local.
                slope = -v*v*alpha/(r0*(1+alpha*root)**2)-g
                self.assertLess(slope, 0)
                checked += 1
            else:
                self.assertIsNone(found)
                self.assertGreater(model.voltage_balance(model.ceiling, v), 0)
                outside += 1
        self.assertEqual(checked+outside, 108)
        self.assertGreater(checked, 0); self.assertGreater(outside, 0)

    def test_current_range_and_feedback(self):
        m = Thermal()
        low = m.current_equilibrium(.5)
        self.assertEqual(low['status'], 'na faixa')
        self.assertAlmostEqual(low['delta'], 100/7)
        self.assertAlmostEqual(.5**2*m.resistance(low['delta'])-m.g*low['delta'], 0)
        medium = m.current_equilibrium(1.)
        self.assertEqual(medium['status'], 'fora da faixa')
        self.assertAlmostEqual(medium['delta'], 100.)
        high = m.current_equilibrium(2.)
        self.assertEqual(high['status'], 'sem raiz não negativa')
        self.assertGreater(high['linear_growth'], 0)
        # Caso exatamente crítico por constantes binárias: força constante positiva.
        critical = Thermal(2., .25, .5).current_equilibrium(1.)
        self.assertEqual(critical['status'], 'sem raiz não negativa')
        self.assertEqual(critical['linear_growth'], 0)
        self.assertEqual(m.current_equilibrium(0.)['delta'], 0.)

    def test_example_and_temperature(self):
        m = Thermal()
        root = m.voltage_bisection(10.)
        self.assertAlmostEqual(root, (sqrt(3)-1)/.02)
        self.assertAlmostEqual(m.resistance(root), 13.660254037844386)
        self.assertAlmostEqual(100/m.resistance(root), 7.320508075688773)
        self.assertAlmostEqual(Thermal(alpha=.004).resistance(50.), 12.)
        self.assertAlmostEqual(Thermal(alpha=0).voltage_formal_root(10.), 50.)

    def test_contracts(self):
        for kwargs in ({'r0':0}, {'alpha':-.01}, {'conductance':0}, {'ceiling':0}, {'alpha':True}):
            with self.assertRaises(ValueError): Thermal(**kwargs)
        for value in (-1., float('inf'), float('nan'), True):
            with self.assertRaises(ValueError): Thermal().resistance(value)
        with self.assertRaises(ValueError): Thermal().resistance(61.)
        with self.assertRaises(ValueError): Thermal().voltage_bisection(-1.)
        with self.assertRaises(ValueError): Thermal().current_equilibrium(-1.)


if __name__ == '__main__':
    m = Thermal()
    print('Tensão fixa, Δ* em K:', m.voltage_bisection(10.))
    for i in (.5, 1., 2.): print('Corrente em A:', i, m.current_equilibrium(i))
    unittest.main()
