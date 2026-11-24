"""Órbita relativa elíptica prescrita; sem efemérides ou unidades implícitas."""
from math import sin, cos, sqrt, atan2, pi, isfinite

def real(value):
    if isinstance(value,bool) or not isinstance(value,(int,float)):
        raise TypeError('número real finito requerido')
    try: out=float(value)
    except OverflowError: raise ValueError('fora do domínio numérico') from None
    if not isfinite(out): raise ValueError('número finito requerido')
    return out

def eccentricity(e):
    e=real(e)
    if not 0<=e<=.99: raise ValueError('recorte 0 <= e <= 0.99')
    return e

def solve(mean,e):
    """Uma volta [0,2π]; bisseção fixa, não intervalo certificado em float."""
    mean=real(mean);e=eccentricity(e)
    if not 0<=mean<=2*pi: raise ValueError('M em [0,2π] rad')
    if mean==0 or mean==2*pi or e==0:
        return {'E':mean,'residual':0.,'half_width':0.,'iterations':0}
    lo,hi=0.,2*pi
    for _ in range(48):
        mid=(lo+hi)/2
        if mid-e*sin(mid)<mean: lo=mid
        else: hi=mid
    E=(lo+hi)/2
    return {'E':E,'residual':E-e*sin(E)-mean,'half_width':(hi-lo)/2,'iterations':48}

def state(E,e,a=1.,mu=1.):
    """a em L, mu em L³/T²; posição relativa ao foco e velocidade d/dt."""
    E=real(E);e=eccentricity(e);a=real(a);mu=real(mu)
    if not 0<=E<=2*pi: raise ValueError('E em [0,2π]')
    if not 1e-6<=a<=1e6 or not 1e-12<=mu<=1e12:
        raise ValueError('recorte: a em [1e-6,1e6], mu em [1e-12,1e12]')
    b=a*sqrt(1-e*e);den=1-e*cos(E);n=sqrt(mu/a**3)
    x=a*(cos(E)-e);y=b*sin(E);r=a*den
    nu=atan2(y,x)%(2*pi)
    if E==2*pi: nu=2*pi
    return {'x':x,'y':y,'r':r,'nu':nu,'vx':-a*sin(E)*n/den,
            'vy':b*cos(E)*n/den,'n':n,'period':2*pi/n,
            'area':a*b*(E-e*sin(E))/2}
