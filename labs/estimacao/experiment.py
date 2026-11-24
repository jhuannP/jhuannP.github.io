"""Divisores de variância, riscos exatos e intervalo normal com sigma conhecido."""
from fractions import Fraction as Q
from math import comb, sqrt, isfinite
from statistics import NormalDist


def sample_variances(values):
    if not 2 <= len(values) <= 1000:
        raise ValueError('Amostra de 2 a 1000 números racionais')
    if any(isinstance(x, bool) or not isinstance(x, (int, Q)) for x in values):
        raise ValueError('Use int ou Fraction')
    n = len(values); mean = sum(map(Q, values))/n
    ss = sum((Q(x)-mean)**2 for x in values)
    return dict(mean=mean, ss=ss, divisor_n=ss/n, divisor_n_minus_1=ss/(n-1))


def variance_risks(n, p):
    if isinstance(n, bool) or not isinstance(n, int) or not 2 <= n <= 100:
        raise ValueError('n inteiro entre 2 e 100 neste laboratório')
    if isinstance(p, bool) or not isinstance(p, (int, Q)) or not 0 <= p <= 1:
        raise ValueError('p racional entre 0 e 1')
    p = Q(p); target = p*(1-p)
    masses = [Q(comb(n, k))*p**k*(1-p)**(n-k) for k in range(n+1)]
    def risk(divisor):
        estimates = [Q(k*(n-k), n*divisor) for k in range(n+1)]
        mean = sum(x*w for x, w in zip(estimates, masses))
        bias = mean-target
        variance = sum((x-mean)**2*w for x, w in zip(estimates, masses))
        mse = sum((x-target)**2*w for x, w in zip(estimates, masses))
        return dict(mean=mean, bias=bias, variance=variance, mse=mse)
    return dict(target=target, divisor_n=risk(n), divisor_n_minus_1=risk(n-1))


def normal_interval(mean, sd, n, level=.95):
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError('n inteiro positivo')
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x) for x in (mean, sd, level)):
        raise ValueError('Parâmetros numéricos finitos')
    if sd <= 0 or not 0 < level < 1:
        raise ValueError('sigma positivo e nível entre 0 e 1')
    critical = NormalDist().inv_cdf((1+level)/2)
    margin = critical*sd/sqrt(n)
    return dict(lower=mean-margin, upper=mean+margin, margin=margin, critical=critical)


if __name__ == '__main__':
    r = sample_variances([1, 2, 3])
    assert r['divisor_n'] == Q(2, 3) and r['divisor_n_minus_1'] == 1
    print('Uma amostra observada sintética:', r)
    risks = variance_risks(4, Q(1, 2))
    assert risks['divisor_n_minus_1']['bias'] == 0
    assert risks['divisor_n']['mse'] < risks['divisor_n_minus_1']['mse']
    print('Riscos sob Bernoulli iid:', risks)
    interval = normal_interval(5, 2, 4)
    assert 1.95 < interval['margin'] < 1.97
    print('Intervalo normal de 95%, sigma conhecido:', interval)
