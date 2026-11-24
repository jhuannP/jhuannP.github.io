"""Faixas racionais para duas séries com hipóteses demonstradas nas notas.
Não certifica monotonicidade/limite de uma sequência arbitrária por amostragem.
"""
from fractions import Fraction as Q
MAX_TERMS=5000


def count(n):
    if type(n) is not int or not 0<=n<=MAX_TERMS:
        raise ValueError("N deve ser inteiro entre0 e5000; limite didático de trabalho.")
    return n


def rational(value):
    if isinstance(value,bool) or not isinstance(value,(int,Q)):
        raise TypeError("Use int ou Fraction, sem float/bool.")
    return Q(value)


def enclosure(partial,next_term):
    return dict(partial=partial,lower=min(partial,partial+next_term),
                upper=max(partial,partial+next_term),bound=abs(next_term))


def harmonic_bounds(n):
    n=count(n)
    partial=sum((Q(1 if k%2 else -1,k) for k in range(1,n+1)),Q(0))
    return enclosure(partial,Q(1 if n%2==0 else -1,n+1))


def geometric_bounds(n,ratio=Q(1,2)):
    n=count(n);r=rational(ratio)
    if not 0<r<1:raise ValueError("Use0<r<1 para magnitudes r**(n-1).")
    partial=sum(((-r)**k for k in range(n)),Q(0))
    return enclosure(partial,(-r)**n)


def harmonic_bound_count(epsilon,strict=False):
    """Menor N>=0 com cota1/(N+1)<=epsilon, ou< se strict=True.
    Não é o menor N necessário para o erro real, apenas para a cota escolhida.
    Não executa a soma nem contorna MAX_TERMS.
    """
    eps=rational(epsilon)
    if eps<=0:raise ValueError("Tolerância deve ser positiva.")
    if type(strict) is not bool:raise TypeError("strict deve ser bool.")
    q=1/eps
    floor=q.numerator//q.denominator
    ceil=(q.numerator+q.denominator-1)//q.denominator
    return max(0,floor if strict else ceil-1)


if __name__=="__main__":
    print("Faixa após9termos",harmonic_bounds(9))
    eps=Q(1,1000)
    print("Cota<=epsilon",harmonic_bound_count(eps))
    print("Cota<epsilon",harmonic_bound_count(eps,strict=True))
