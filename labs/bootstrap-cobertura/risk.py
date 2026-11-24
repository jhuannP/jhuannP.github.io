"""Cobertura exata de percentis da média: Bernoulli iid, n <= 5."""
from fractions import Fraction as Q
from math import comb


def rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise ValueError('Use int ou Fraction')
    return Q(value)


def size(n):
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 5:
        raise ValueError('n inteiro de 1 a 5')
    return n


def distribution(n, p):
    n = size(n); p = rational(p)
    if not 0 <= p <= 1:
        raise ValueError('p entre 0 e 1')
    return tuple(Q(comb(n, k))*p**k*(1-p)**(n-k) for k in range(n+1))


def interval(n, k, alpha=Q(1, 20)):
    n = size(n); alpha = rational(alpha)
    if isinstance(k, bool) or not isinstance(k, int) or not 0 <= k <= n:
        raise ValueError('k inteiro de 0 a n')
    if not 0 < alpha < 1:
        raise ValueError('0 < alpha < 1')
    masses = distribution(n, Q(k, n))
    def quantile(u):
        cumulative = Q(0)
        for j, mass in enumerate(masses):
            cumulative += mass
            if cumulative >= u:
                return Q(j, n)
        raise ArithmeticError('Distribuição não normalizada')
    return quantile(alpha/2), quantile(1-alpha/2)


def audit(n, p, alpha=Q(1, 20)):
    weights = distribution(n, p); p = rational(p)
    # Cada intervalo é uma função da contagem observada, não do p verdadeiro.
    intervals = tuple(interval(n, k, alpha) for k in range(n+1))
    coverage = sum((w for w, (lo, hi) in zip(weights, intervals) if lo <= p <= hi), Q(0))
    width = sum((w*(hi-lo) for w, (lo, hi) in zip(weights, intervals)), Q(0))
    return dict(coverage=coverage, expected_width=width, weights=weights, intervals=intervals)


if __name__ == '__main__':
    result = audit(3, Q(1, 4))
    assert result['coverage'] == Q(9, 16)
    assert result['intervals'] == ((0, 0), (0, 1), (0, 1), (1, 1))
    print(result)
