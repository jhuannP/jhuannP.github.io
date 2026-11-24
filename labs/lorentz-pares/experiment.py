"""Boost exato em 1+1 para entradas racionais com gamma racional."""
from fractions import Fraction as Q
from math import isqrt

def boost(ct,x,beta):
    if any(type(z) not in (int,Q) for z in (ct,x,beta)):
        raise ValueError("Use int/Fraction, sem bool ou float.")
    ct,x,beta=map(Q,(ct,x,beta))
    if abs(beta)>=1:raise ValueError("O referencial exige |beta|<1.")
    s=1-beta*beta
    a,b=isqrt(s.numerator),isqrt(s.denominator)
    if a*a!=s.numerator or b*b!=s.denominator:
        raise ValueError("Este laboratório exato exige gamma racional; use o painel para outros beta.")
    gamma=Q(b,a)
    ctp=gamma*(ct-beta*x);xp=gamma*(x-beta*ct)
    before=ct*ct-x*x;after=ctp*ctp-xp*xp
    kind="coincidente" if ct==0 and x==0 else ("temporal" if before>0 else "espacial" if before<0 else "luz")
    return dict(ct=ctp,x=xp,beta=beta,gamma=gamma,interval=before,
                transformed_interval=after,kind=kind)

if __name__=="__main__":
    for pair in ((5,3),(1,2),(1,1),(0,0)):
        print(pair,"->",boost(*pair,Q(3,5)))
