"""Cadeia homogênea de dois estados, aritmética racional e vetor linha."""
from fractions import Fraction as Q

def probability(x):
    if type(x) not in (int, Q) or not 0 <= x <= 1:
        raise ValueError("Use int ou Fraction entre zero e um")
    return Q(x)

def distribution(alpha, beta, q, n):
    a, b, q = map(probability, (alpha, beta, q))
    if type(n) is not int or not 0 <= n <= 200:
        raise ValueError("Passos inteiros entre 0 e 200")
    for _ in range(n):
        q = q*(1-a) + (1-q)*b
    return q, 1-q

def unique_stationary(alpha, beta):
    a, b = map(probability, (alpha, beta))
    if a+b == 0:
        return None  # identidade: há muitas distribuições estacionárias
    return b/(a+b), a/(a+b)

if __name__ == "__main__":
    a, b = Q(1,5), Q(1,10)
    print("Dois passos a partir de A:", distribution(a,b,1,2))
    print("Estacionária única:", unique_stationary(a,b))
