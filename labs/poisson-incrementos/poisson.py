"""Poisson homogêneo: probabilidades limitadas e momentos exatos didáticos."""
from math import exp,isfinite,comb
from fractions import Fraction as Q

def integer(n):
    if type(n) is not int or not 0<=n<=1000:raise ValueError("Inteiro de0 a1000 necessário.")
    return n

def real(x):
    if isinstance(x,bool):raise ValueError("Real finito necessário.")
    try:x=float(x)
    except (ValueError,TypeError,OverflowError):raise ValueError("Real finito necessário.") from None
    if not isfinite(x):raise ValueError("Real finito necessário.")
    return x

def pmf(rate,duration,k):
    rate,duration=map(real,(rate,duration));k=integer(k)
    if rate<=0 or duration<0:raise ValueError("Taxa positiva e duração>=0 necessárias.")
    mu=rate*duration
    if not isfinite(mu) or mu>100:raise ValueError("Laboratório limitado a mu<=100.")
    value=exp(-mu)
    for j in range(1,k+1):value*=mu/j
    return value

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Use int/Fraction.")
    return Q(x)

def moments(rate,s,t):
    rate,s,t=map(rational,(rate,s,t))
    if rate<=0 or not 0<=s<=t:raise ValueError("lambda>0 e0<=s<=t necessários.")
    return dict(mean_s=rate*s,mean_t=rate*t,var_s=rate*s,var_t=rate*t,covariance=rate*s)

def conditional_count(total,s,t,k):
    total,k=integer(total),integer(k);s,t=map(rational,(s,t))
    if not 0<=s<=t or t<=0:raise ValueError("0<=s<=t e t>0 necessários.")
    if k>total:return Q(0)
    q=s/t
    return comb(total,k)*q**k*(1-q)**(total-k)

if __name__=='__main__':
    print(pmf(2,3,0),moments(2,1,3))
    print(conditional_count(6,1,3,0))
