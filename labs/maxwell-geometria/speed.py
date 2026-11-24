"""Classical isotropic Maxwell model; dimensionless u=v/s, s=sqrt(theta/m)."""
from math import exp,sqrt,pi,erfc,isfinite


def real(value,lo,hi):
    if type(value) not in (int,float):raise ValueError('Finite int/float required')
    value=float(value)
    if not isfinite(value) or not lo<=value<=hi:raise ValueError('Outside didactic numeric domain')
    return value


def component_density(x):
    x=real(x,-32,32)
    return exp(-x*x/2)/sqrt(2*pi)


def speed_density(u):
    u=real(u,0,32)
    return sqrt(2/pi)*u*u*exp(-u*u/2)


def tails(u):
    """Return omitted probability and unnormalized second moment above u."""
    u=real(u,0,32);base=sqrt(2/pi)*exp(-u*u/2);e=erfc(u/sqrt(2))
    return dict(probability=e+u*base,second_moment=3*e+(u**3+3*u)*base)


def scales(theta,mass):
    theta=real(theta,1e-4,1e4);mass=real(mass,1e-4,1e4);s=sqrt(theta/mass)
    return dict(s=s,mode=sqrt(2)*s,mean=sqrt(8/pi)*s,rms=sqrt(3)*s,mean_square=3*theta/mass)


def physical_speed_density(v,theta,mass):
    s=scales(theta,mass)['s'];v=real(v,0,32*s)
    return speed_density(v/s)/s


if __name__=='__main__':
    print('theta2,m1',scales(2,1))
    for u in (0,1,2,4,8):print('u',u,'component',component_density(u),'speed',speed_density(u),'tails',tails(u))
