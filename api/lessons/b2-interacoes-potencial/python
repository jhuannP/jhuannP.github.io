"""Lennard-Jones12-6 integral,sem corte: par prescrito,não modelo de proteína completa."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction, não bool/float.')
    return Q(x)


def parameters(r,epsilon,sigma):
    vals=tuple(map(rational,(r,epsilon,sigma)))
    if min(vals)<=0:raise ValueError('Distância,epsilon e sigma positivos.')
    return vals


def potential(r,epsilon=1,sigma=1):
    r,epsilon,sigma=parameters(r,epsilon,sigma)
    a=(sigma/r)**6
    return 4*epsilon*(a*a-a)


def force(r,epsilon=1,sigma=1):
    """F_r positivo aumenta r; força no corpo2 é F_r*n, no1 é -F_r*n."""
    r,epsilon,sigma=parameters(r,epsilon,sigma)
    return 24*epsilon/r*(2*(sigma/r)**12-(sigma/r)**6)


def curvature(r,epsilon=1,sigma=1):
    r,epsilon,sigma=parameters(r,epsilon,sigma)
    return 24*epsilon/r**2*(26*(sigma/r)**12-7*(sigma/r)**6)


def minimum_bracket(steps=60):
    """Intervalo racional para r_min/sigma; raiz de s**6=2 em[1,3/2]."""
    if isinstance(steps,bool) or not isinstance(steps,int) or not 1<=steps<=128:
        raise ValueError('steps inteiro de1 a128.')
    lo,hi=Q(1),Q(3,2)
    for _ in range(steps):
        mid=(lo+hi)/2
        if mid**6<2:lo=mid
        else:hi=mid
    return lo,hi


def work(a,b,epsilon=1,sigma=1,panels=64):
    """Integral de F_r dr por Simpson racional; erro de quadratura ainda existe."""
    a,epsilon,sigma=parameters(a,epsilon,sigma);b=rational(b)
    if b<=a:raise ValueError('Exige 0<a<b.')
    if isinstance(panels,bool) or not isinstance(panels,int) or not 2<=panels<=512 or panels%2:
        raise ValueError('panels par entre2 e512.')
    h=(b-a)/panels
    result=force(a,epsilon,sigma)+force(b,epsilon,sigma)
    result+=sum((4 if j%2 else 2)*force(a+j*h,epsilon,sigma) for j in range(1,panels))
    return result*h/3


if __name__=='__main__':
    print('Entrada fictícia:epsilon1 unidade de energia,sigma1 unidade de comprimento.')
    for r in [1,2]:print('r=',r,'U=',potential(r),'F_r=',force(r))
    lo,hi=minimum_bracket();print('Intervalo racional para r_min/sigma:',lo,hi)
    print('Aproximação:',float((lo+hi)/2),'largura exata:',hi-lo)
    print('Trabalho1→2 por Simpson64:',float(work(1,2)))
    print('Referência por diferença de energia:',float(potential(1)-potential(2)))
