"""A=[[-1,b],[0,-1]], norma euclidiana, tempo adimensional não negativo."""
from math import exp, hypot, sqrt, isfinite


def checked(x, low, high):
    if type(x) not in (int,float) or not isfinite(x) or not low<=x<=high:
        raise ValueError('Parâmetro real finito fora do contrato.')
    return float(x)


def apply(b,t,x,y):
    b=checked(b,-4,4);t=checked(t,0,20)
    x=checked(x,-4,4);y=checked(y,-4,4)
    return exp(-t)*(x+b*t*y),exp(-t)*y


def gain(b,t):
    b=checked(b,-4,4);t=checked(t,0,20)
    k=abs(b*t)
    return exp(-t)*(hypot(k,2)+k)/2


def maximizing_input(b,t):
    b=checked(b,-4,4);t=checked(t,0,20)
    k=b*t
    sigma=(hypot(k,2)+abs(k))/2
    y=sigma if k>=0 else -sigma
    scale=hypot(1,y)
    return 1/scale,y/scale


def global_peak(b):
    b=abs(checked(b,-4,4))
    t=sqrt(b*b-4)/b if b>2 else 0.0
    return t,gain(b,t)


if __name__=='__main__':
    z=apply(4,1,0,1)
    print('Estado de (0,1) em t1:',z,'norma',hypot(*z))
    print('Ganho ótimo em t1:',gain(4,1))
    print('Pico da norma do operador: t,G=',global_peak(4))
    print('Norma e tempo adimensionais; sem energia física ou expm geral.')
