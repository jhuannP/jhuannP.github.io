"""Referências analíticas: normal e média de Bernoullis iid ou repetidas."""
from fractions import Fraction as Q
from math import comb, erfc, sqrt, isfinite


def finite(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x):
        raise ValueError('Use número real finito')
    return float(x)


def normal_cdf(x, mean=0, sd=1):
    x, mean, sd = map(finite, (x, mean, sd))
    if sd <= 0: raise ValueError('Desvio padrão positivo')
    return .5*erfc(-(x-mean)/(sd*sqrt(2)))


def normal_survival(x, mean=0, sd=1):
    x, mean, sd = map(finite, (x, mean, sd))
    if sd <= 0: raise ValueError('Desvio padrão positivo')
    return .5*erfc((x-mean)/(sd*sqrt(2)))


def mean_bernoulli(n, p, epsilon=Q(1, 5)):
    if isinstance(n, bool) or not isinstance(n, int) or not 1 <= n <= 100:
        raise ValueError('n inteiro entre 1 e 100 neste laboratório')
    if isinstance(p, bool) or not isinstance(p, (int, Q)) or not 0 < p < 1:
        raise ValueError('p racional estritamente entre 0 e 1')
    if isinstance(epsilon, bool) or not isinstance(epsilon, (int, Q)) or epsilon <= 0:
        raise ValueError('epsilon racional positivo')
    p, epsilon = Q(p), Q(epsilon)
    masses = [Q(comb(n, k))*p**k*(1-p)**(n-k) for k in range(n+1)]
    mean = sum(Q(k, n)*mass for k, mass in enumerate(masses))
    variance = sum((Q(k, n)-mean)**2*mass for k, mass in enumerate(masses))
    tail = sum(mass for k, mass in enumerate(masses) if abs(Q(k, n)-p) >= epsilon)
    return dict(masses=masses, mean=mean, variance=variance, tail=tail,
                chebyshev=min(Q(1), p*(1-p)/(n*epsilon**2)))


if __name__ == '__main__':
    assert normal_cdf(10, 10, 2) == .5
    z = (14-10)/2
    assert z == 2
    print('x=14, média 10, desvio 2: z=', z, 'CDF=', normal_cdf(14, 10, 2))
    print('Cauda superior em z=8, por erfc:', normal_survival(8))
    for n in (4, 16, 64):
        result = mean_bernoulli(n, Q(1, 2))
        assert result['mean'] == Q(1, 2)
        assert result['variance'] == Q(1, 4*n)
        assert result['tail'] <= result['chebyshev']
        print('n=', n, 'Var(média)=', result['variance'], 'cauda exata=', result['tail'])
    # Se todos os dados repetem a mesma Bernoulli, a média é a própria variável.
    p = Q(1, 2)
    repeated_variance = p*(1-p)
    assert repeated_variance == Q(1, 4)  # Não encolhe com n.
    print('Dados perfeitamente dependentes: Var(média)=', repeated_variance)
