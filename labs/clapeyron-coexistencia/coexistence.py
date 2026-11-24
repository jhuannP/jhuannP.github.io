"""Curvas sintéticas de coexistência; não são propriedades ajustadas de um fluido."""
from math import exp, log, isfinite
import unittest
R = 8.314  # J/(mol K), arredondado para o exemplo.


def finite(v):
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise ValueError('Real finito necessário')
    try: v = float(v)
    except OverflowError: raise ValueError('Real não representável') from None
    if not isfinite(v): raise ValueError('Real finito necessário')
    return v


def positive(v):
    v = finite(v)
    if v <= 0: raise ValueError('Valor positivo necessário')
    return v


def temperature(t):
    t = positive(t)
    if not 280 <= t <= 360: raise ValueError('Intervalo didático: 280 a 360 K')
    return t


def clapeyron(delta_h, t, delta_v):
    delta_h, t, delta_v = finite(delta_h), positive(t), finite(delta_v)
    if delta_v == 0: raise ValueError('Delta V não pode ser zero nesta forma')
    return delta_h/(t*delta_v)  # SI -> Pa/K; diferenças com sinais consistentes.


def parameters(t, t_ref, latent_ref, alpha):
    t, t_ref = temperature(t), temperature(t_ref)
    latent_ref, alpha = positive(latent_ref), finite(alpha)
    if latent_ref+alpha*(t-t_ref) <= 0:
        raise ValueError('Este modelo exige L positivo no segmento de integração')
    return t, t_ref, latent_ref, alpha


def log_ratio(t, t_ref=300, latent_ref=30000, alpha=0):
    t, t_ref, latent_ref, alpha = parameters(t, t_ref, latent_ref, alpha)
    value = ((latent_ref-alpha*t_ref)*(1/t_ref-1/t)+alpha*log(t/t_ref))/R
    if not isfinite(value): raise ValueError('Logaritmo não representável')
    return value


def pressure(t, p_ref=10000, t_ref=300, latent_ref=30000, alpha=0):
    p_ref = positive(p_ref)
    try: value = p_ref*exp(log_ratio(t, t_ref, latent_ref, alpha))
    except OverflowError: raise ValueError('Pressão não representável') from None
    if not isfinite(value) or value <= 0: raise ValueError('Pressão não representável')
    return value  # Mesma unidade de p_ref; padrão em Pa.


def inverse_pressure(p, p_ref=10000, t_ref=300, latent=30000):
    p, p_ref, t_ref, latent = positive(p), positive(p_ref), temperature(t_ref), positive(latent)
    reciprocal = 1/t_ref-R/latent*(log(p)-log(p_ref))
    if reciprocal <= 0: raise ValueError('Inversão sem temperatura positiva finita')
    return temperature(1/reciprocal)  # Apenas L constante; não extrapolar fora do intervalo.


def rk4_pressure(t, n=128, p_ref=10000, t_ref=300, latent_ref=30000, alpha=0):
    t, t_ref, latent_ref, alpha = parameters(t, t_ref, latent_ref, alpha)
    if type(n) is not int or n <= 0: raise ValueError('Número de passos inteiro positivo')
    p = positive(p_ref); h = (t-t_ref)/n
    def f(temp, value):
        latent = latent_ref+alpha*(temp-t_ref)
        return latent*value/(R*temp*temp)
    for k in range(n):
        temp = t_ref+k*h
        k1 = f(temp, p); k2 = f(temp+h/2, p+h*k1/2)
        k3 = f(temp+h/2, p+h*k2/2); k4 = f(temp+h, p+h*k3)
        p += h*(k1+2*k2+2*k3+k4)/6
    if not isfinite(p) or p <= 0: raise ValueError('Passo não produziu pressão positiva finita')
    return p


class Checks(unittest.TestCase):
    def test_local_slope_and_units(self):
        self.assertEqual(clapeyron(30000, 300, .002), 50000)
        self.assertEqual(clapeyron(6000, 300, -2e-6), -1e7)
        self.assertEqual(clapeyron(-30000, 300, -.002), 50000)
        # J/m^3 é Pa; reduzir ambas as diferenças molares pelo mesmo fator cancela.
        self.assertAlmostEqual(clapeyron(30, 300, 2e-6), 50000)

    def test_examples_and_tangent(self):
        self.assertAlmostEqual(log_ratio(330), 1.0934458853631341)
        self.assertAlmostEqual(pressure(330)/1000, 29.8454075881)
        slope = 30000*10000/(R*300**2)
        tangent = 10000+slope*30
        self.assertAlmostEqual(tangent/1000, 22.027904739)
        self.assertGreater(pressure(330), tangent)
        self.assertAlmostEqual(pressure(330, alpha=-40)/1000, 29.2200941132)

    def test_rk4_independent(self):
        for t in (280, 290, 300, 310, 320, 340, 360):
            for alpha in (-40, 0, 100):
                # A ODE usa dp/dT; não avalia a fórmula fechada de pressão nos estágios.
                self.assertAlmostEqual(rk4_pressure(t, 256, alpha=alpha), pressure(t, alpha=alpha), delta=1e-4)
        errors = [abs(rk4_pressure(340, n)-pressure(340)) for n in (16, 32, 64)]
        self.assertGreater(errors[0], errors[1]); self.assertGreater(errors[1], errors[2])
        self.assertLess(errors[2], .001)
        print('Erros RK4 em Pa, n=16/32/64:', errors)

    def test_derivative_and_latent_prescription(self):
        for t in (290, 310, 350):
            for alpha in (-40, 0, 100):
                h = .001
                derivative = (log_ratio(t+h, alpha=alpha)-log_ratio(t-h, alpha=alpha))/(2*h)
                target = (30000+alpha*(t-300))/(R*t*t)
                self.assertAlmostEqual(derivative, target, delta=1e-9)

    def test_inverse_and_scale(self):
        for t in (280, 290, 300, 310, 330, 350):
            self.assertAlmostEqual(inverse_pressure(pressure(t)), t)
            self.assertAlmostEqual(pressure(t, p_ref=10)*1000, pressure(t))
        self.assertAlmostEqual(inverse_pressure(20000), 318.3457081544)
        self.assertAlmostEqual(inverse_pressure(20, p_ref=10), inverse_pressure(20000))

    def test_contracts(self):
        for bad in (0, -1, True, float('inf'), float('nan'), 279, 361):
            with self.assertRaises(ValueError): pressure(bad)
        with self.assertRaises(ValueError): clapeyron(30000, 300, 0)
        with self.assertRaises(ValueError): pressure(330, alpha=-2000)
        with self.assertRaises(ValueError): inverse_pressure(0)
        with self.assertRaises(ValueError): inverse_pressure(1e100)
        for bad in (0, True, 1.5):
            with self.assertRaises(ValueError): rk4_pressure(330, bad)


if __name__ == '__main__':
    print('p(330K), L constante:', pressure(330)/1000, 'kPa')
    print('p(330K), L linear imposto:', pressure(330, alpha=-40)/1000, 'kPa')
    print('T para dobrar p:', inverse_pressure(20000), 'K')
    unittest.main()
