"""Amplitudes de Jones normalizadas e filtros ideais; sem instrumentos reais."""
from math import cos,sin,pi,isfinite,isclose,sqrt
from cmath import exp

def angle(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or abs(x)>100*pi:
        raise ValueError("ângulo finito em radianos, |ângulo|<=100*pi")
    return float(x)

def state(e):
    e=tuple(e)
    if len(e)!=2 or any(isinstance(z,bool) or not isinstance(z,(int,float,complex)) for z in e):
        raise ValueError("duas amplitudes numéricas")
    e=tuple(map(complex,e))
    if any(not isfinite(z.real) or not isfinite(z.imag) or abs(z)>1+1e-12 for z in e) or intensity(e)>1+1e-12:
        raise ValueError("estado normalizado ou atenuado necessário")
    return e

def intensity(e):return sum(abs(z)**2 for z in e)

def linear(theta):
    theta=angle(theta)
    return complex(cos(theta)),complex(sin(theta))

def project(e,theta):
    e=state(e);u=linear(theta)
    amplitude=sum(ui.conjugate()*zi for ui,zi in zip(u,e))
    return tuple(ui*amplitude for ui in u)

def plate(e,delta):
    e=state(e);delta=angle(delta)
    return e[0],e[1]*exp(1j*delta)

def chain(e,axes):
    e=state(e);axes=tuple(axes)
    if not isclose(intensity(e),1.,rel_tol=0.,abs_tol=1e-12) or len(axes)>12:
        raise ValueError("entrada unitária e até12 filtros")
    for theta in axes:e=project(e,theta)
    return intensity(e)

def mixture(components,axes):
    components=tuple(components);axes=tuple(axes)
    if not 1<=len(components)<=12:raise ValueError("1 a12 componentes")
    if any(isinstance(w,bool) or not isinstance(w,(int,float)) or not isfinite(w) or not 0<=w<=1 for w,_ in components):
        raise ValueError("pesos reais entre0 e1")
    if not isclose(sum(w for w,_ in components),1.,rel_tol=0.,abs_tol=1e-12):raise ValueError("pesos somam1")
    return sum(w*chain(e,axes) for w,e in components)

if __name__=='__main__':
    x,y=(1,0),(0,1);circ=(1/sqrt(2),1j/sqrt(2))
    print('cruzados:',chain(x,(0,pi/2)))
    print('intermediário45°:',chain(x,(0,pi/4,pi/2)))
    print('circular em45°:',chain(circ,(pi/4,)))
    print('circular com placa:',chain(plate(circ,-pi/2),(pi/4,)))
    print('mistura não polarizada:',mixture(((.5,x),(.5,y)),(pi/4,)))
