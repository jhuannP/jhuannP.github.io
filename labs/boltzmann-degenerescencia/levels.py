"""Prescribed finite two-level canonical system; no sampling or rate model."""
from fractions import Fraction as Q
from math import exp,isfinite,log,log1p,sqrt

def degeneracies(g0,g1):
    if any(isinstance(g,bool) or not isinstance(g,int) or not 1<=g<=1000000 for g in (g0,g1)):
        raise ValueError('positive integer degeneracies up to 1000000')

def probabilities(weight,g0=1,g1=1):
    degeneracies(g0,g1)
    if isinstance(weight,bool) or not isinstance(weight,(int,Q)) or not 0<=weight<=1:
        raise ValueError('rational Boltzmann weight in [0,1]')
    z=g0+g1*Q(weight)
    return Q(g0)/z,g1*Q(weight)/z

def thermodynamics(x,g0=1,g1=1):
    """x=gap/(kB*T)>0. Return logZ,p,U/gap,S/kB,C/kB,F/(kB*T)."""
    degeneracies(g0,g1)
    if isinstance(x,bool) or not isinstance(x,(int,float)):raise ValueError('positive finite x')
    try:x=float(x)
    except OverflowError:raise ValueError('positive finite x') from None
    if not isfinite(x) or x<=0:raise ValueError('positive finite x')
    a=log(g1)-log(g0)-x
    if a>=0:p=1/(1+exp(-a))
    else:
        w=exp(a);p=w/(1+w)
    logz=log(g0)+max(a,0)+log1p(exp(-abs(a)))
    c=(x*sqrt(p*(1-p)))**2
    return dict(p_exc=p,logz=logz,u_over_gap=p,s_over_k=logz+x*p,c_over_k=c,f_over_kt=-logz)

if __name__=='__main__':
    print('w1/3,g0=1,g1=3:',probabilities(Q(1,3),1,3))
    print('x=ln3:',thermodynamics(log(3),1,3))
