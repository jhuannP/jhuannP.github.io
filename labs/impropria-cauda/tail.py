"""Prescribed f(x)=x**(-3/2)+3*x**(-2), x>=1; exact square cutoffs."""
from fractions import Fraction as Q
from importlib import import_module
from numerics import trapezio
RULES=import_module('labs.quadratura-erro.experiment')


def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise TypeError('Use int/Fraction without bool/float')
    return Q(x)


def cutoff(n):
    if type(n) is not int or not 1<=n<=10000:raise ValueError('n must be int 1..10000')
    remaining=Q(2,n)+Q(3,n*n)
    return dict(R=n*n,tail=remaining,partial=Q(5)-remaining)


def minimum_cutoff(tolerance):
    tolerance=number(tolerance)
    if tolerance<=0 or tolerance<cutoff(10000)['tail']:
        raise ValueError('Positive tolerance attainable in the didactic n domain required')
    lo,hi=1,10000
    while lo<hi:
        mid=(lo+hi)//2
        if cutoff(mid)['tail']<=tolerance:hi=mid
        else:lo=mid+1
    return cutoff(lo)|dict(n=lo)


def regularized(t):
    """After x=1/t**2 with Jacobian; analytic continuous extension at zero."""
    t=number(t)
    if not 0<=t<=1:raise ValueError('0<=t<=1')
    return 2+6*t


def first_transform_at_square(t):
    """g(u)=u**(-1/2)+3 evaluated only at u=t**2>0, for identity tests."""
    t=number(t)
    if not 0<t<=1:raise ValueError('0<t<=1')
    return 1/t+3


def finite_comparison(n,panels):
    info=cutoff(n)
    if n==1:raise ValueError('Need R>1 for finite-interval quadrature')
    if type(panels) is not int or not 1<=panels<=100000:raise ValueError('1..100000 panels')
    q=trapezio(lambda x:x**(-1.5)+3/x**2,1,info['R'],panels)
    return dict(quadrature=q,quadrature_error=q-float(info['partial']),
                signed_total_error=5-q,tail=float(info['tail']))


if __name__=='__main__':
    for n in (5,10,20):print('cutoff',n,cutoff(n))
    print('minimum exact tail <=1/100',minimum_cutoff(Q(1,100)))
    for panels in (10,100,1000):print('R100',panels,finite_comparison(10,panels))
    print('regularized trapezoid and Simpson',RULES.rules(regularized,2))
