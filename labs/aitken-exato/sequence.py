"""Aitken para dados racionais exatos; sem recuperação de erro de medição."""
from fractions import Fraction as Q

def rational(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise ValueError('Use inteiro ou Fraction; floats não são entradas exatas.')
    return Q(value)

def aitken(x0, x1, x2):
    x0, x1, x2 = map(rational, (x0, x1, x2))
    delta = x1-x0
    delta2 = x2-2*x1+x0
    if delta2 == 0:
        raise ArithmeticError('Segunda diferença zero; não concluir divergência.')
    return x0-delta*delta/delta2

def two_modes(n, limit=Q(2), a=Q(1), q=Q(1,2), b=Q(1), r=Q(1,4)):
    if isinstance(n, bool) or not isinstance(n, int) or not 0 <= n <= 100:
        raise ValueError('Índice inteiro entre0 e100.')
    limit,a,q,b,r=map(rational,(limit,a,q,b,r))
    return limit+a*q**n+b*r**n

if __name__ == '__main__':
    values=[two_modes(n) for n in range(3)]
    print('Dois modos:', values, 'estimativa:', aitken(*values))
    print('Original:', aitken(Q(1),Q(101,100),Q(10199,10000)))
    print('Perturbado:', aitken(Q(1),Q(101,100),Q(20399,20000)))
