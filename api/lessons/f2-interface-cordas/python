"""Pulso compacto entre cordas ideais; SI, sem atrito ou massa na junção."""
from math import isfinite
A=.02
WIDTH=.5  # segundos, duração total do pulso=1s
TENSION=1.0
MU1=1.0

def pulse(s):
    z=s/WIDTH
    return A*(1-z*z)**3 if abs(z)<1 else 0.0

def prime(s):
    z=s/WIDTH
    return -6*A*z*(1-z*z)**2/WIDTH if abs(z)<1 else 0.0

def cumulative(t):
    z=(t-2)/WIDTH
    if z<=-1:return 0.0
    if z>=1:return 1.0
    def h(u):return u**3/3-4*u**5/5+6*u**7/7-4*u**9/9+u**11/11
    return (h(z)+128/3465)/(256/3465)

def coefficients(ratio=8):
    if isinstance(ratio,bool) or not isinstance(ratio,int) or not 2<=ratio<=8:
        raise ValueError('Razão Z2/Z1 em quartos: inteiro2..8')
    q=ratio/4
    r=(1-q)/(1+q);tau=2/(1+q)
    return dict(q=q,c1=1.0,c2=1/q,mu1=MU1,mu2=q*q,Z1=1.0,Z2=q,
                r=r,tau=tau,R=r*r,transmission=q*tau*tau)

def field(side,x,t,ratio=8):
    c=coefficients(ratio)
    if side not in ('left','right') or not all(isfinite(v) for v in (x,t)) or t<0:
        raise ValueError('Lado left/right, x e t finitos, t>=0')
    if (side=='left' and x>0) or (side=='right' and x<0):raise ValueError('x no lado escolhido')
    if side=='left':
        a=t-x-2;b=t+x-2
        inc=pulse(a);ref=c['r']*pulse(b)
        y=inc+ref;velocity=prime(a)+c['r']*prime(b);slope=-prime(a)+c['r']*prime(b);mu=MU1
    else:
        s=t-x/c['c2']-2
        inc=ref=0.0;y=c['tau']*pulse(s)
        velocity=c['tau']*prime(s);slope=-velocity/c['c2'];mu=c['mu2']
    return dict(y=y,incident=inc,reflected=ref,velocity=velocity,slope=slope,
                density=.5*mu*velocity**2+.5*TENSION*slope**2,power=-TENSION*velocity*slope)

def model(ratio=8,time=3.5):
    c=coefficients(ratio)
    if isinstance(time,bool) or not isinstance(time,(int,float)) or not isfinite(time) or not 0<=time<=5:raise ValueError('Tempo entre0 e5s')
    f=cumulative(time);e0=1024*A*A/(385*WIDTH)
    return dict(**c,time=time,passed=f,energy0=e0,
                energy_left=e0*(1-f+c['R']*f),energy_right=e0*c['transmission']*f,
                left=field('left',0,time,ratio),right=field('right',0,time,ratio))

if __name__=='__main__':
    for ratio in (2,4,8):
        c=model(ratio,3.5)
        print('q=',c['q'],'r=',c['r'],'tau=',c['tau'],'R=',c['R'],'T_E=',c['transmission'])
    assert abs(model(8,2)['energy_right']/model(8,2)['energy0']-4/9)<1e-12
