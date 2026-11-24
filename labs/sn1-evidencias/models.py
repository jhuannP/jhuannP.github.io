"""Prescribed first-order decay and illustrative stereochemical mixtures."""
from math import exp, isfinite
from fractions import Fraction as Q

def nonnegative(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or x<0:
        raise ValueError('finite nonnegative real required')
    return float(x)

def decay(initial,k,t):
    """Concentration for an irreversible first-order model; no fitted chemistry."""
    initial,k,t=map(nonnegative,(initial,k,t))
    return initial*exp(-k*t)

def stereo(free):
    """(inversion,retention); free fraction has equiprobable faces, rest all inversion."""
    if isinstance(free,bool) or not isinstance(free,(int,Q)) or not 0<=free<=1:
        raise ValueError('int/Fraction in [0,1] required')
    free=Q(free)
    return 1-free/2,free/2

if __name__=='__main__':
    from math import log
    for t in (0,8,16): print(t,'s:',decay(0.16,log(2)/8,t),'mol/L')
    inv,ret=stereo(Q(3,5))
    print('inversão,retenção,excesso normalizado:',inv,ret,inv-ret)
