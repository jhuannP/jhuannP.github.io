"""Synthetic coarse-grained carbon model; umol of six-carbon equivalents, minutes."""
from fractions import Fraction as F


def real(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):
        raise ValueError('int/Fraction required')
    return F(x)


def parameters(J=12,kg=2,kp=1,ks=1,km=1):
    J,kg,kp,ks,km=map(real,(J,kg,kp,ks,km))
    if min(J,kg,kp,ks)<0 or kg+kp<=0 or km<=0:
        raise ValueError('nonnegative input/rates, kg+kp>0 and km>0 required')
    return J,kg,kp,ks,km


def fluxes(a,y,p=(12,2,1,1,1)):
    a=real(a);y=real(y);J,kg,kp,ks,km=parameters(*p)
    if min(a,y)<0:raise ValueError('nonnegative pools required')
    g,pp,s,m=kg*a,kp*a,ks*a,km*y
    return dict(glycolysis=g,pentose=pp,storage=s,mobilization=m,
                da=J-g-pp-s+m,dy=s-m,
                pyruvate=2*g,pentose_product=pp,co2=pp,nadph=2*pp,
                carbon_input=6*J,carbon_output=6*(g+pp))


def steady(p=(12,2,1,1,1)):
    J,kg,kp,ks,km=parameters(*p)
    a=J/(kg+kp);y=ks*a/km
    return dict(a=a,y=y,fluxes=fluxes(a,y,p))


def step(a,y,h,p=(12,2,1,1,1)):
    """One explicit Euler step, conservative global positivity restriction."""
    h=real(h);J,kg,kp,ks,km=parameters(*p)
    if h<0 or h*(kg+kp+ks)>1 or h*km>1:
        raise ValueError('step outside sufficient positivity bound')
    f=fluxes(a,y,p)
    return real(a)+h*f['da'],real(y)+h*f['dy']


if __name__=='__main__':
    print('Prescribed base steady state:',steady())
    print('Same pools, double fluxes:',steady((24,4,2,2,2)))
    print('Half pools, same fluxes:',steady((12,4,2,2,2)))
    print('One positivity-preserving step from a=2,y=4:',step(2,4,F(1,4)))
    print('No measured cell, ATP budget, chemical potentials or physiological prediction.')
