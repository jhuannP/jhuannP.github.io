"""Distribuição binária finita: enumeração de referência, não dinâmica física."""
from fractions import Fraction as Q
from itertools import product
from math import comb

def validate(n, p):
    if type(n) is not int or not 0 <= n <= 16:
        raise ValueError("N deve ser inteiro entre 0 e 16 nesta enumeração")
    if type(p) not in (int, Q) or not 0 <= p <= 1:
        raise ValueError("p deve ser inteiro ou Fraction no intervalo [0,1]")
    return Q(p)

def macro_distribution(n, p=Q(1, 2)):
    p = validate(n, p)
    return tuple(Q(comb(n, m)) * p**m * (1-p)**(n-m) for m in range(n+1))

def enumerate_distribution(n, p=Q(1, 2)):
    p = validate(n, p)
    totals = [Q(0) for _ in range(n+1)]
    for state in product((0, 1), repeat=n):
        weight = Q(1)
        for bit in state:
            weight *= p if bit else 1-p
        totals[sum(state)] += weight
    return tuple(totals)

def moments(probabilities):
    mean = sum((m*w for m, w in enumerate(probabilities)), Q(0))
    variance = sum(((m-mean)**2*w for m, w in enumerate(probabilities)), Q(0))
    return mean, variance

if __name__ == "__main__":
    for n, p in [(4, Q(1,2)), (8, Q(1,2)), (4, Q(1,4))]:
        distribution = macro_distribution(n, p)
        assert distribution == enumerate_distribution(n, p)
        print("N, p:", n, p, "P(M=m):", [str(x) for x in distribution])
        print("Média e variância:", moments(distribution))
