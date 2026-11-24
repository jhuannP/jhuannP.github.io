"""Aritmética racional para momentos finitos e contagem binomial."""
from fractions import Fraction as Q
from math import comb, fsum


def rational(x):
    if isinstance(x, bool) or not isinstance(x, (int, Q)):
        raise ValueError('Use int ou Fraction')
    return Q(x)


def moments(values, weights):
    if len(values) != len(weights) or not 1 <= len(values) <= 1000:
        raise ValueError('Listas de mesmo tamanho entre 1 e 1000')
    values, weights = list(map(rational, values)), list(map(rational, weights))
    if any(w < 0 for w in weights) or sum(weights) != 1:
        raise ValueError('Pesos não negativos com soma 1')
    mean = sum((x*w for x, w in zip(values, weights)), Q(0))
    second = sum((x*x*w for x, w in zip(values, weights)), Q(0))
    variance = sum(((x-mean)**2*w for x, w in zip(values, weights)), Q(0))
    return dict(mean=mean, second=second, variance=variance)


def binomial(n, p):
    p = rational(p)
    if isinstance(n, bool) or not isinstance(n, int) or not 0 <= n <= 100:
        raise ValueError('n inteiro entre 0 e 100 neste laboratório')
    if not 0 <= p <= 1:
        raise ValueError('p entre 0 e 1')
    # Expoentes zero retornam 1, inclusive nos casos p=0, p=1, n=0.
    return [Q(comb(n, k))*p**k*(1-p)**(n-k) for k in range(n+1)]


if __name__ == '__main__':
    r = moments([0, 2], [Q(1, 2), Q(1, 2)])
    assert r == dict(mean=Q(1), second=Q(2), variance=Q(1))
    print('Momentos do modelo {0,2}:', r)
    translated = moments([10**8-1, 10**8+1], [Q(1, 2), Q(1, 2)])
    assert translated['variance'] == 1
    x = [float(10**8-1), float(10**8+1)]; mean = fsum(x)/2
    raw = fsum(v*v for v in x)/2 - mean*mean
    centered = fsum((v-mean)**2 for v in x)/2
    print('Exato:', translated['variance'], 'float por diferença:', raw, 'float centrado:', centered)
    probabilities = binomial(3, Q(1, 2))
    assert probabilities == [Q(1, 8), Q(3, 8), Q(3, 8), Q(1, 8)]
    b = moments(list(range(4)), probabilities)
    assert b['mean'] == Q(3, 2) and b['variance'] == Q(3, 4)
    assert binomial(0, Q(1, 2)) == [1]
    print('Binomial n=3, p=1/2:', probabilities, b)
