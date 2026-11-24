"""Exact AR(1) moment recurrences with prescribed coefficients; no sampling."""
from fractions import Fraction as Q

def q(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('int/Fraction required')
    return Q(x)

def evolve(r,noise,mean,var,n):
    r,noise,mean,var=map(q,(r,noise,mean,var))
    if noise<0 or var<0 or isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=10000:raise ValueError('nonnegative variances; integer n0..10000')
    for _ in range(n):mean=r*mean;var=r*r*var+noise
    return mean,var

def stationary(r,noise):
    r,noise=map(q,(r,noise))
    if abs(r)>=1 or noise<0:raise ValueError('strictly stable coefficient required')
    return noise/(1-r*r)

def euler(theta,diffusion_variance,h):
    theta,diffusion_variance,h=map(q,(theta,diffusion_variance,h))
    if theta<=0 or diffusion_variance<0 or h<=0:raise ValueError('theta,h positive; sigma squared nonnegative')
    return 1-theta*h,diffusion_variance*h

if __name__=='__main__':
    for h in (Q(1,2),Q(1),Q(3,2)):
        r,noise=euler(1,2,h)
        print('h,r,variância estacionária Euler:',h,r,stationary(r,noise))
    print('kernel exato prescrito rho1/2,q3/4,após2:',evolve(Q(1,2),Q(3,4),2,0,2))
