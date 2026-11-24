"""Duas leis artificiais para discutir média e dispersão; não ajusta o artigo."""
from fractions import Fraction as F
from math import comb

def probability(p):
    if isinstance(p,bool) or not isinstance(p,(int,F)) or not 0<=p<=1:
        raise ValueError('Probabilidade racional em [0,1]')
    return F(p)

def independent(n=15,p=F(1,8)):
    p=probability(p)
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=30:
        raise ValueError('n inteiro de 1 a 30')
    return tuple(F(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1))

def families(weights=(1,2,4,8),p=F(1,8)):
    p=probability(p);weights=tuple(weights)
    if not weights or len(weights)>15 or any(isinstance(w,bool) or not isinstance(w,int) or w<1 for w in weights) or sum(weights)>100:
        raise ValueError('Pesos inteiros positivos; no máximo 15 eventos e soma100')
    law=[F(1)]
    for w in weights:
        new=[F(0)]*(len(law)+w)
        for k,q in enumerate(law):
            new[k]+=q*(1-p);new[k+w]+=q*p
        law=new
    return tuple(law)

def moments(law):
    law=tuple(law)
    if not law or any(not isinstance(q,(int,F)) or isinstance(q,bool) or q<0 for q in law) or sum(law)!=1:
        raise ValueError('Lei racional normalizada e não negativa')
    mean=sum((k*q for k,q in enumerate(law)),F(0))
    variance=sum(((k-mean)**2*q for k,q in enumerate(law)),F(0))
    return mean,variance

if __name__=='__main__':
    for name,law in [('independentes',independent()),('pesos',families())]:
        print(name,'média/variância=',moments(law),'P0=',law[0],'P>=8=',sum(law[8:]))
