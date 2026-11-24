"""Original exact polynomial OU worksheet; transition indexed by rho, not a solver."""
from fractions import Fraction as F
from math import comb


def rational(x):
    if type(x) not in (int,F):raise ValueError('int or Fraction required')
    return F(x)


def polynomial(coeffs):
    if not isinstance(coeffs,(list,tuple)) or not 1<=len(coeffs)<=13:raise ValueError('degree<=12')
    c=tuple(map(rational,coeffs))
    while len(c)>1 and not c[-1]:c=c[:-1]
    return c


def params(theta,sigma):
    t,s=rational(theta),rational(sigma)
    if t<=0 or s<0:raise ValueError('theta>0,sigma>=0')
    return t,s


def evaluate(coeffs,x):
    x=rational(x);result=F(0)
    for c in reversed(polynomial(coeffs)):result=result*x+c
    return result


def apply(coeffs,theta=2,sigma=2):
    c=polynomial(coeffs);theta,sigma=params(theta,sigma);out=[F(0)]*len(c)
    for n,a in enumerate(c):
        out[n]-=theta*n*a
        if n>=2:out[n-2]+=sigma*sigma*n*(n-1)*a/2
    return polynomial(out)


def gaussian_moment(n,variance):
    if n%2:return F(0)
    result=F(1)
    for j in range(1,n,2):result*=j
    return result*variance**(n//2)


def transition(coeffs,rho,theta=2,sigma=2):
    """P_rho f(x)=E f(rho*x+sqrt(S*(1-rho²))*Z), Z standard normal.

    rho=exp(-theta*t); input rho rational in[0,1]. rho=0 is infinite-time limit.
    """
    c=polynomial(coeffs);theta,sigma=params(theta,sigma);rho=rational(rho)
    if not 0<=rho<=1:raise ValueError('0<=rho<=1')
    variance=sigma*sigma/(2*theta)*(1-rho*rho);out=[F(0)]*len(c)
    for n,a in enumerate(c):
        for k in range(n+1):out[k]+=a*comb(n,k)*rho**k*gaussian_moment(n-k,variance)
    return polynomial(out)


if __name__=='__main__':
    for f in [(1,),(0,1),(-1,0,1),(0,-3,0,1)]:
        print('f=',f,'Lf=',apply(f),'P_(1/2)f=',transition(f,F(1,2)))
    print('Prescribed OU theta=sigma=2; no sampled trajectories or inferred model.')
