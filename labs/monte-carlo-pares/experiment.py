"""Integração polinomial exata e comparação de estimadores com 2M avaliações."""
from fractions import Fraction as Q
from math import comb,sqrt
from random import Random
from statistics import mean,stdev
FAMILIES=((0,0,1),(Q(1,4),-1,1),(0,1))

def coefficients(c):
    if not isinstance(c,(list,tuple)) or not c or any(type(x) not in (int,Q) for x in c):
        raise ValueError("Coeficientes int/Fraction numa sequência não vazia")
    return tuple(map(Q,c))

def product(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def integral(c):return sum((a/Q(i+1) for i,a in enumerate(c)),Q(0))

def moments(c):
    c=coefficients(c);mirror=[Q(0)]*len(c)
    for i,a in enumerate(c):
        for j in range(i+1):mirror[j]+=a*comb(i,j)*(-1)**j
    paired=[(a+b)/2 for a,b in zip(c,mirror)]
    mu=integral(c);var=integral(product(c,c))-mu*mu
    vp=integral(product(paired,paired))-mu*mu
    cov=integral(product(c,mirror))-mu*mu
    return dict(mean=mu,var=var,pair_var=vp,cov=cov)

def model(family=0,k=4):
    if type(family) is not int or family not in range(3) or type(k) is not int or k not in range(2,11):
        raise ValueError("Família0..2, k2..10 inteiros")
    s=moments(FAMILIES[family]);m=2**k;n=2*m
    vi=s["var"]/n;va=s["pair_var"]/m
    return dict(family=family,k=k,m=m,n=n,mean=s["mean"],var_ind=vi,var_anti=va,
                se_ind=sqrt(vi),se_anti=sqrt(va),gain=None if va==0 else vi/va)

def sample(family=0,m=16,seed=42):
    if type(family) is not int or family not in range(3) or type(m) is not int or m<2 or type(seed) is not int or seed<0:
        raise ValueError("Família0..2; M≥2 e semente não negativa, inteiros")
    c=FAMILIES[family];f=lambda u:sum(float(a)*u**i for i,a in enumerate(c))
    rng=Random(seed);plain=[f(rng.random()) for _ in range(2*m)]
    paired=[]
    for _ in range(m):
        u=rng.random();paired.append((f(u)+f(1-u))/2)
    return dict(plain=mean(plain),paired=mean(paired),se_plain=stdev(plain)/sqrt(2*m),
                se_paired=stdev(paired)/sqrt(m),evaluations_each=2*m)

if __name__=="__main__":
    s=model(0,4);assert s["gain"]==8
    assert model(1,4)["gain"]==Q(1,2)
    assert model(2,4)["var_anti"]==0
    print(s);print(sample())
