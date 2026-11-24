"""Exact rational models in SI, with prescribed forces. No measured motor data."""
from fractions import Fraction as F


def real(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):
        raise ValueError('exact int or Fraction required')
    return F(x)


def dot(a,b):
    if not isinstance(a,(tuple,list)) or not isinstance(b,(tuple,list)) or not 1<=len(a)==len(b)<=3:
        raise ValueError('matching vectors of dimension 1..3 required')
    return sum((real(x)*real(y) for x,y in zip(a,b)),F(0))


def cart(mass=2,v0=1,drive=6,resistance=2,t=2,boost=0):
    """Track-frame speed remains nonnegative; boost changes only observer, not force law."""
    mass,v0,drive,resistance,t,boost=map(real,(mass,v0,drive,resistance,t,boost))
    if mass<=0 or v0<0 or resistance<0 or drive<resistance or t<0:
        raise ValueError('mass>0, v0>=0, drive>=resistance>=0, t>=0 required')
    net=drive-resistance;a=net/mass
    v=v0+a*t;observed_v=v-boost
    x=v0*t+a*t*t/2-boost*t
    initial_k=mass*(v0-boost)**2/2;k=mass*observed_v**2/2
    return dict(acceleration=a,velocity=observed_v,displacement=x,
                drive_power=drive*observed_v,resistance_power=-resistance*observed_v,
                net_power=net*observed_v,drive_work=drive*x,resistance_work=-resistance*x,
                net_work=net*x,delta_k=k-initial_k,kinetic=k)


def nonlinear(t):
    """Separate SI example: mass 2kg, v=1+t^2 m/s, F=4t N, elapsed t>=0."""
    t=real(t)
    if t<0:raise ValueError('t>=0 required')
    v=1+t*t;force=4*t
    return dict(velocity=v,force=force,power=force*v,work=2*t*t+t**4,
                delta_k=v*v-1)


if __name__=='__main__':
    print('Track frame at 2s:',cart())
    print('Observer moving at +2m/s:',cart(boost=2))
    print('Separate nonlinear example at 1s:',nonlinear(1))
    print('Prescribed classical particle models only; no electrical efficiency or measured equipment.')
