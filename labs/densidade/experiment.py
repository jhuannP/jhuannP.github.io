"""Uniforme e exponencial: referências analíticas, sem dados externos."""
from math import exp, expm1, log1p, isfinite


def finite(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x):
        raise ValueError('Use número real finito')
    return float(x)


def uniform_cdf(x, origin=0, width=.5):
    x, origin, width = map(finite, (x, origin, width))
    if width <= 0 or not isfinite(origin+width) or origin+width == origin:
        raise ValueError('Largura positiva e extremo representável distintos')
    if x <= origin: return 0.
    if x >= origin+width: return 1.
    return (x-origin)/width


def uniform_interval(lo, hi, origin=0, width=.5):
    lo, hi = map(finite, (lo, hi))
    # Valide os parâmetros mesmo quando o evento descrito é vazio.
    lower, upper = uniform_cdf(lo, origin, width), uniform_cdf(hi, origin, width)
    return 0. if lo > hi else max(0., upper-lower)


def rate_value(rate):
    rate = finite(rate)
    if not .01 <= rate <= 100:
        raise ValueError('Taxa entre 0,01 e 100 neste laboratório')
    return rate


def exponential_cdf(t, rate=2):
    t, rate = finite(t), rate_value(rate)
    return 0. if t < 0 else -expm1(-rate*t)


def exponential_survival(t, rate=2):
    t, rate = finite(t), rate_value(rate)
    return 1. if t < 0 else exp(-rate*t)


def exponential_interval(lo, hi, rate=2):
    lo, hi, rate = finite(lo), finite(hi), rate_value(rate)
    if lo > hi or hi <= 0: return 0.
    lo = max(0., lo)
    # Forma estável em intervalos curtos e afastados da origem.
    return exp(-rate*lo)*(-expm1(-rate*(hi-lo)))


def exponential_quantile(u, rate=2):
    u, rate = finite(u), rate_value(rate)
    if not 0 <= u < 1: raise ValueError('u entre 0 inclusive e 1 exclusivo')
    return -log1p(-u)/rate


if __name__ == '__main__':
    assert uniform_cdf(.1) == .2
    assert abs(uniform_interval(.4, .8)-.2) < 1e-12
    assert uniform_interval(.8, .4) == 0
    print('Uniforme [0;0,5]: densidade 2; P([0;0,1])=', uniform_interval(0, .1))
    rate, elapsed, remaining = 2., .3, .4
    ratio = exponential_survival(elapsed+remaining, rate)/exponential_survival(elapsed, rate)
    assert abs(ratio-exponential_survival(remaining, rate)) < 1e-12
    print('Média exponencial:', 1/rate, 'sobrevivência adicional:', ratio)
    for u in (0, .1, .5, .9):
        t = exponential_quantile(u, rate)
        assert abs(exponential_cdf(t, rate)-u) < 1e-12
    print('Mediana com taxa 2:', exponential_quantile(.5, rate))
