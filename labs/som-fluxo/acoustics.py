"""Duas ondas planas coerentes; fase temporal em radianos,grandezas SI."""
from math import cos,isfinite,pi,fsum

def _r(x,low,high):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or not low<=x<=high:raise ValueError('Parâmetro fora do domínio didático.')
    return float(x)

def fields(alpha,tau,a=2,b=2,phi=0,rho=1,c=400):
    alpha,tau,phi=(_r(x,-1e4,1e4) for x in (alpha,tau,phi))
    a,b=(_r(x,0,100) for x in (a,b));rho=_r(rho,.01,1e4);c=_r(c,1,1e4)
    right=a*cos(alpha-tau);left=b*cos(alpha+tau+phi)
    pressure=right+left;velocity=(right-left)/(rho*c)
    return pressure,velocity

def means(alpha,a=2,b=2,phi=0,rho=1,c=400,n=64):
    if isinstance(n,bool) or not isinstance(n,int) or not 8<=n<=4096:raise ValueError('Malha8–4096.')
    samples=[fields(alpha,2*pi*i/n,a,b,phi,rho,c) for i in range(n)]
    return {'pressure2_Pa2':fsum(p*p for p,u in samples)/n,
            'velocity2_m2_s2':fsum(u*u for p,u in samples)/n,
            'net_W_m2':fsum(p*u for p,u in samples)/n,
            'energy_J_m3':fsum(rho*u*u/2+p*p/(2*rho*c*c) for p,u in samples)/n}

if __name__=='__main__':
    for alpha,a,b in [(0,2,0),(0,2,2),(pi/2,2,2),(0,2,1)]:
        print('fase espacial/amplitudes:',alpha,a,b,means(alpha,a,b))
