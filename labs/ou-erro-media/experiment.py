"""Variância da média de amostras estacionárias;sem simulação ou ajuste."""
from math import exp,sqrt,isfinite
from fractions import Fraction as F

def variance_ratio(n,rho):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:
        raise ValueError('n inteiro positivo')
    if isinstance(rho,bool) or not isinstance(rho,(int,float,F)) or not isfinite(rho) or not 0<=rho<=1:
        raise ValueError('rho em[0,1]')
    rho=float(rho)
    return (n+2*sum((n-k)*rho**k for k in range(1,n)))/(n*n)

def inspect(n=20,alpha_level=10):
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=40 or isinstance(alpha_level,bool) or not isinstance(alpha_level,int) or not 5<=alpha_level<=200:
        raise ValueError('n1..40 e alpha_level5..200 inteiros')
    a=alpha_level/100;rho=exp(-a);variance=variance_ratio(n,rho)
    return dict(rho=rho,variance=variance,iid_variance=1/n,
                sem=sqrt(variance),iid_sem=1/sqrt(n),neff=1/variance,
                asym_neff=n*(1-rho)/(1+rho),inflation=sqrt(n*variance),horizon=(n-1)*a)

if __name__=='__main__':
    assert abs(variance_ratio(2,F(1,2))-F(3,4))<1e-14
    z=inspect();assert 1<=z['neff']<=20 and z['sem']>z['iid_sem']
    print(z)
