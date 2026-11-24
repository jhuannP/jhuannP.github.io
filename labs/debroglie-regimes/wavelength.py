"""Modelo didático livre; energia em eV, lambda em nm, massa eletrônica arredondada."""
from math import sqrt, hypot, isfinite, asin, degrees
from fractions import Fraction as Q
import unittest

# Valores definidos pelo SI; cálculos float não têm aritmética exata.
H = 6.62607015e-34  # J s
C = 299792458.0  # m/s
EV = 1.602176634e-19  # J por eV
HC = H*C/EV*1e9  # eV nm
E0 = 511000.0  # eV: energia de repouso arredondada, não constante exata


def finite(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise ValueError('Número real finito')
    try: x = float(x)
    except OverflowError: raise ValueError('Número não representável') from None
    if not isfinite(x): raise ValueError('Número real finito')
    return x


def energy(x):
    x = finite(x)
    if not 1e-6 <= x <= 1e9:
        raise ValueError('Este laboratório usa energias de 1e-6 a 1e9 eV')
    return x


def electron_nm(k, relativistic=True):
    k = energy(k)
    if type(relativistic) is not bool: raise ValueError('Escolha booleana de regime')
    pc = sqrt(k*(k+2*E0)) if relativistic else sqrt(2*E0*k)
    return HC/pc


def relative_error(k):
    r = energy(k)/E0
    # Forma racionalizada da diferença sqrt(1+r/2)-1 para r pequeno.
    return r/(2*(sqrt(1+r/2)+1))


def limit_r(tolerance):
    tolerance = finite(tolerance)
    if not 0 <= tolerance <= 1:
        raise ValueError('Tolerância entre 0 e 1 neste laboratório')
    return 2*tolerance*(2+tolerance)


def photon_nm(e):
    return HC/energy(e)


def angle_deg(wavelength_nm, separation_nm, order):
    wavelength_nm, separation_nm = map(finite, (wavelength_nm, separation_nm))
    if wavelength_nm <= 0 or separation_nm <= 0 or type(order) is not int:
        raise ValueError('Comprimentos positivos; ordem inteira')
    arg = order*wavelength_nm/separation_nm
    if abs(arg) > 1: return None  # Sem direção real; não truncar silenciosamente.
    return degrees(asin(arg))  # Igualdade dá limite rasante de +/-90 graus.


class Checks(unittest.TestCase):
    def test_si_momentum_and_inverse(self):
        # Uma rota usa energia em eV; outra, massa/velocidade/momento em SI.
        mass = E0*EV/C**2
        for exponent in range(-6, 10):
            k = 10.**exponent
            r = k/E0
            gamma = 1+r
            beta = sqrt(r*(r+2))/(1+r)
            p_si = gamma*mass*beta*C
            self.assertAlmostEqual((H/p_si*1e9)/electron_nm(k), 1, delta=1e-12)
            # Reconstrução estável de K a partir de pc; evita subtrair energias próximas.
            pc = HC/electron_nm(k)
            reconstructed = pc**2/(hypot(E0, pc)+E0)
            self.assertAlmostEqual(reconstructed/k, 1, delta=1e-12)

    def test_examples(self):
        self.assertAlmostEqual(electron_nm(150), .10012981, delta=1e-8)
        self.assertAlmostEqual(electron_nm(100000), .00370143, delta=1e-8)
        self.assertAlmostEqual(100*relative_error(100000), 4.7782, delta=.0001)
        self.assertAlmostEqual(photon_nm(150), 8.26561323, delta=1e-8)
        self.assertGreater(photon_nm(150), 80*electron_nm(150))

    def test_scaling_and_regimes(self):
        for k in (1e-5, 1, 150, 100000, 1e7):
            self.assertAlmostEqual(electron_nm(4*k, False)/electron_nm(k, False), .5)
            # Lambda = h/p: dobrar pc, no mesmo sistema de unidades, divide lambda por 2.
            pc = HC/electron_nm(k)
            self.assertAlmostEqual((HC/(2*pc))/electron_nm(k), .5)
            ratio = electron_nm(k, False)/electron_nm(k)
            self.assertAlmostEqual(ratio, sqrt(1+k/(2*E0)))
            self.assertAlmostEqual(ratio-1, relative_error(k), delta=1e-12)
            self.assertGreater(electron_nm(k, False), electron_nm(k))

    def test_tolerance_by_exact_inequality(self):
        # A desigualdade ao quadrado é racional exata e não usa a rotina de erro.
        for tau in (Q(1, 100), Q(1, 20), Q(1, 10)):
            r_limit = 2*((1+tau)**2-1)
            self.assertAlmostEqual(limit_r(float(tau)), float(r_limit))
            for r in (r_limit/2, r_limit, r_limit+Q(1, 100000)):
                expected = 1+r/2 <= (1+tau)**2
                numerical = relative_error(float(r)*E0) <= float(tau)+1e-14
                self.assertEqual(numerical, expected)
        self.assertAlmostEqual(limit_r(.01), .0402)
        self.assertAlmostEqual(E0*limit_r(.01), 20542.2)

    def test_angle_and_impossibility(self):
        self.assertAlmostEqual(angle_deg(.1, .2, 1), 30)
        self.assertAlmostEqual(angle_deg(.1, .2, -1), -30)
        self.assertEqual(angle_deg(.1, .2, 0), 0)
        self.assertEqual(angle_deg(.1, .2, 2), 90)  # Limite geométrico, não intensidade.
        self.assertIsNone(angle_deg(.1, .2, 3))
        self.assertIsNone(angle_deg(.1, .2, -3))

    def test_contracts(self):
        for bad in (0, -1, True, float('nan'), float('inf'), 1e10, 1e-9, '150'):
            for function in (electron_nm, photon_nm, relative_error):
                with self.assertRaises(ValueError): function(bad)
        for bad in (-.01, 2, True, float('nan')):
            with self.assertRaises(ValueError): limit_r(bad)
        for args in ((0, 1, 1), (1, 0, 1), (1, 1, True), (1, 1, .5)):
            with self.assertRaises(ValueError): angle_deg(*args)
        with self.assertRaises(ValueError): electron_nm(150, relativistic=1)


if __name__ == '__main__':
    print('HC:', HC, 'eV nm; E0 adotado:', E0, 'eV')
    for k in (150, 100000):
        print(k, 'eV: lambda_nr=', electron_nm(k, False), 'nm; lambda_rel=', electron_nm(k),
              'nm; erro=', 100*relative_error(k), '%')
    print('Limite 1%:', E0*limit_r(.01), 'eV')
    unittest.main()
