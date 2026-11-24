"""Luminosidade de disco circular exponencial sintético; sem ajuste ou massa inferida."""
from math import exp,expm1,isfinite,pi

def fraction(x):
    if not isfinite(x) or x<0:raise ValueError('x deve ser finito e não negativo.')
    if x<.01:
        term=x*x/2;total=term
        for k in range(1,13):
            term*=-x*(k+1)/(k*(k+2));total+=term
        return total
    return -expm1(-x)-x*exp(-x)

def half_light_ratio():
    lo,hi=0.,10.
    for _ in range(70):
        mid=(lo+hi)/2
        if fraction(mid)<.5:lo=mid
        else:hi=mid
    return (lo+hi)/2

def disk(I0,h,R):
    if not all(isfinite(v) for v in (I0,h,R)) or I0<=0 or h<=0 or R<0:
        raise ValueError('I0,h positivos; R não negativo; todos finitos.')
    x=R/h;f=fraction(x);total=2*pi*I0*h*h
    return dict(x=x,local=I0*exp(-x),fraction=f,total=total,enclosed=total*f,
                missed=1-f,half_radius=h*half_light_ratio())

if __name__=='__main__':
    print('I0=2 unidades/kpc², h=3 kpc, R=6 kpc:',disk(2,3,6))
    print('Raio de meia-luz / h:',half_light_ratio())
