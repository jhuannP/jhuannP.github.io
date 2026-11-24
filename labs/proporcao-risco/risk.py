"""Proporção Bernoulli iid: riscos exatos; não usa dados reais."""
from fractions import Fraction as Q
from math import comb


def size(n):
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=100:
        raise ValueError('n inteiro de1 a100.')
    return n


def estimates(n,k):
    size(n)
    if isinstance(k,bool) or not isinstance(k,int) or not 0<=k<=n:
        raise ValueError('k inteiro entre0 e n.')
    return Q(k,n),Q(k+1,n+2)


def risks(n,p):
    size(n)
    if isinstance(p,bool) or not isinstance(p,(int,Q)) or not 0<=p<=1:
        raise ValueError('p racional entre0 e1.')
    p=Q(p)
    weights=[comb(n,k)*p**k*(1-p)**(n-k) for k in range(n+1)]
    out={}
    for j,name in enumerate(('sample','shrink')):
        values=[estimates(n,k)[j] for k in range(n+1)]
        mean=sum(w*t for w,t in zip(weights,values)); bias=mean-p
        var=sum(w*(t-mean)**2 for w,t in zip(weights,values))
        mse=sum(w*(t-p)**2 for w,t in zip(weights,values))
        out[name]=dict(mean=mean,bias=bias,variance=var,mse=mse)
    return out


if __name__=='__main__':
    for p in (Q(0),Q(1,4),Q(1,2),Q(1)):
        print('n4,p=',p,risks(4,p))
    print('Risco usa p prescrito; não revela erro de uma estimativa real.')
