"""Exact finite identities and Gaussian moment formulas; no sampled Brownian path."""
from fractions import Fraction as Q

def q(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('int/Fraction required')
    return Q(x)

def square_sums(increments,x0=0):
    if not isinstance(increments,(list,tuple)) or len(increments)>4096:raise ValueError('finite grid up to 4096 increments')
    x=q(x0);left=Q(0);variation=Q(0)
    for dx in increments:
        dx=q(dx);left+=x*dx;variation+=dx*dx;x+=dx
    return dict(final=x,left=left,right=left+variation,midpoint=left+variation/2,qv=variation)

def brownian_errors(n,horizon=1):
    horizon=q(horizon)
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=1000000 or horizon<0:raise ValueError('n positive integer, horizon nonnegative')
    return dict(mean_qv=horizon,var_qv=2*horizon*horizon/n,mse_left=horizon*horizon/(2*n))

def ito_polynomial(coeffs,x,b,sigma):
    if not isinstance(coeffs,(tuple,list)) or not 1<=len(coeffs)<=9:raise ValueError('coefficients of degree up to eight')
    coeffs=tuple(map(q,coeffs));x,b,sigma=map(q,(x,b,sigma))
    first=sum((i*a*x**(i-1) for i,a in enumerate(coeffs) if i>=1),Q(0))
    second=sum((i*(i-1)*a*x**(i-2) for i,a in enumerate(coeffs) if i>=2),Q(0))
    return b*first+sigma*sigma*second/2,sigma*first

if __name__=='__main__':
    for n in (4,16,64):print(n,brownian_errors(n))
    print('OU quadrado,estado X=2:',ito_polynomial((0,0,1),2,-4,3))
