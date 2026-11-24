"""Exact prescribed binomial probabilities and explicit Gaussian approximations."""
from fractions import Fraction as F
from math import comb,erf,erfc,inf,sqrt


def parameters(n,p):
    if type(n) is not int or not 1<=n<=256:raise ValueError('integer n in 1..256 required')
    if isinstance(p,bool) or not isinstance(p,(int,F)):raise ValueError('exact p required')
    p=F(p)
    if not 0<=p<=1 or p.denominator>1000:raise ValueError('p in [0,1], denominator<=1000 required')
    return n,p


def masses(n,p):
    n,p=parameters(n,p)
    return tuple(F(comb(n,k))*p**k*(1-p)**(n-k) for k in range(n+1))


def exact(n,p,lower=None,upper=None):
    values=masses(n,p)
    if any(v is not None and type(v) is not int for v in (lower,upper)):
        raise ValueError('integer bounds or None required')
    if lower is not None and upper is not None and lower>upper:raise ValueError('ordered bounds required')
    return sum((q for k,q in enumerate(values) if (lower is None or k>=lower) and (upper is None or k<=upper)),F(0))


def normal_area(a,b):
    """Integral of standard Gaussian density; floats can underflow at extreme tails."""
    if a>=0:return (erfc(a/sqrt(2))-erfc(b/sqrt(2)))/2
    if b<=0:return (erfc(-b/sqrt(2))-erfc(-a/sqrt(2)))/2
    return (erf(b/sqrt(2))-erf(a/sqrt(2)))/2


def approximate(n,p,lower=None,upper=None,corrected=True):
    n,p=parameters(n,p)
    if not 0<p<1:raise ValueError('positive variance required for normal approximation')
    if type(corrected) is not bool or any(v is not None and type(v) is not int for v in (lower,upper)):
        raise ValueError('integer bounds or None, bool correction required')
    if lower is not None and upper is not None and lower>upper:raise ValueError('ordered bounds required')
    mean=float(n*p);sd=sqrt(float(n*p*(1-p)));offset=.5 if corrected else 0
    a=-inf if lower is None else (lower-offset-mean)/sd
    b=inf if upper is None else (upper+offset-mean)/sd
    return normal_area(a,b)


if __name__=='__main__':
    print('Balanced n=16,p=1/2,event 6..10:',exact(16,F(1,2),6,10))
    print('Uncorrected:',approximate(16,F(1,2),6,10,False))
    print('Corrected:',approximate(16,F(1,2),6,10))
    print('Rare n=100,p=1/100,event K<=0:',float(exact(100,F(1,100),upper=0)))
    print('Rare corrected:',approximate(100,F(1,100),upper=0))
    print('Prescribed laws, exact probabilities; no sampled data or universal error guarantee.')
