"""Experimento sintético exato: binomial e dois testes independentes."""
from fractions import Fraction as F
from math import comb

def law(n, probability):
    if type(n) is not int or not 1 <= n <= 20:
        raise ValueError("n inteiro entre 1 e 20")
    if not isinstance(probability, F) or not 0 <= probability <= 1:
        raise ValueError("probabilidade deve ser Fraction em [0, 1]")
    return tuple(F(comb(n, k))*probability**k*(1-probability)**(n-k) for k in range(n+1))

def upper_pvalues(null):
    if not null or any(not isinstance(q, F) or q < 0 for q in null) or sum(null) != 1:
        raise ValueError("lei discreta racional normalizada")
    return tuple(sum(null[k:], F(0)) for k in range(len(null)))

def rejection_mass(distribution, pvalues, alpha):
    if len(distribution) != len(pvalues) or not isinstance(alpha, F) or not 0 <= alpha <= 1:
        raise ValueError("comprimentos compatíveis e alpha racional em [0, 1]")
    upper_pvalues(distribution)
    if any(not isinstance(p, F) or not 0 <= p <= 1 for p in pvalues):
        raise ValueError("p-valores racionais em [0, 1]")
    return sum((q for q, p in zip(distribution, pvalues) if p <= alpha), F(0))

if __name__ == '__main__':
    null = law(5, F(1, 2))
    pv = upper_pvalues(null)
    size = rejection_mass(null, pv, F(1, 20))
    print("p-valores:", pv)
    print("tamanho:", size)
    print("poder em 3/4:", rejection_mass(law(5, F(3, 4)), pv, F(1, 20)))
    print("família independente:", 1-(1-size)**2)
