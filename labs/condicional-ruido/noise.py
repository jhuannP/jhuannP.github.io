"""Modelo conhecido: X,E uniformes independentes em [0,1], Z=X+E.
Fraction: integrais analíticas exatas para entradas racionais; não estima dados.
"""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Use int ou Fraction.")
    return Q(x)

def support(z):
    z=rational(z)
    if not 0<z<2:return None
    return max(Q(0),z-1),min(Q(1),z)

def marginal(z):
    z=rational(z)
    return max(Q(0),min(z,2-z))

def conditional(z):
    interval=support(z)
    if interval is None:return None
    a,b=interval
    return dict(lower=a,upper=b,density=1/(b-a),mean=(a+b)/2,variance=(b-a)**2/12)

def tail(z,t):
    t=rational(t);r=conditional(z)
    if r is None:return None
    a,b=r['lower'],r['upper']
    return (b-min(b,max(a,t)))/(b-a)

def lower_bin(b):
    b=rational(b)
    if not 0<b<=1:raise ValueError("Faixa implementada: 0<b<=1.")
    return dict(evidence=b*b/2,mean=b/3,variance=b*b/18)

def bin_density(b,x):
    b=rational(b);x=rational(x);r=lower_bin(b)
    return (b-x)/r['evidence'] if 0<=x<=b else Q(0)

if __name__=='__main__':
    print(conditional(Q(1,2)));print(lower_bin(Q(1,2)))
