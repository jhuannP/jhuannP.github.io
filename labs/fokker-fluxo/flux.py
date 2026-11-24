"""Original periodic constant-coefficient finite-volume step; not a general PDE solver."""
from fractions import Fraction as F
import math


def rational(x):
    if type(x) not in (int,F):raise ValueError('int/Fraction required')
    return F(x)


def weights(c,d,dt,dx):
    c,d,dt,dx=map(rational,(c,d,dt,dx))
    if d<0 or dt<0 or dx<=0:raise ValueError('D>=0,dt>=0,dx>0')
    adv=abs(c)*dt/dx;diff=d*dt/(dx*dx)
    return 1-adv-2*diff,max(c,0)*dt/dx+diff,max(-c,0)*dt/dx+diff


def step(densities,c,d,dt,dx):
    if not isinstance(densities,(list,tuple)) or not 3<=len(densities)<=256:
        raise ValueError('3..256 cell means')
    r=tuple(map(rational,densities));c,d,dt,dx=map(rational,(c,d,dt,dx))
    if min(r)<0:raise ValueError('input densities must be nonnegative')
    weights(c,d,dt,dx) # validates coefficients, no clipping or silent stability enforcement
    flux=tuple(max(c,0)*r[i]+min(c,0)*r[(i+1)%len(r)]-d*(r[(i+1)%len(r)]-r[i])/dx for i in range(len(r)))
    out=tuple(r[i]-dt/dx*(flux[i]-flux[i-1]) for i in range(len(r)))
    return out,flux


def periodic_density(x,t,c=1,d=.1,a=.5,length=1):
    values=(x,t,c,d,a,length)
    if any(type(v) not in (int,float) for v in values):raise ValueError('finite reals')
    try:x,t,c,d,a,length=map(float,values)
    except OverflowError as e:raise ValueError('representable values') from e
    if not all(math.isfinite(v) for v in (x,t,c,d,a,length)) or t<0 or d<0 or abs(a)>1 or length<=0:
        raise ValueError('t,D>=0,|a|<=1,L>0')
    try:
        k=2*math.pi/length
        decay=math.exp(-d*k*k*t)
        phase=k*(x-c*t)
        result=(1+a*decay*math.cos(phase))/length
    except (ValueError,OverflowError,ZeroDivisionError) as e:
        raise ValueError('analytic evaluation outside representable range') from e
    if not math.isfinite(result):raise ValueError('density not representable')
    return result


if __name__=='__main__':
    r=(4,0,0,0);c=F(1,4);d=F(1,32);dx=F(1,4)
    for dt in (F(1,4),F(1)):
        out,j=step(r,c,d,dt,dx)
        print('dt=',dt,'weights=',weights(c,d,dt,dx),'out=',out,'mass=',dx*sum(out))
    print('Second step example intentionally violates positivity condition; no clipping.')
