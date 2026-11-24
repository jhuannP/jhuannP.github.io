"""Círculo de raio 5: referências exatas e representações locais."""
from fractions import Fraction as Q


def point(x,y):
    if any(isinstance(v,bool) or not isinstance(v,(int,Q)) for v in (x,y)):
        raise ValueError('Use inteiros ou Fraction.')
    x,y=Q(x),Q(y)
    if x*x+y*y!=25:raise ValueError('Ponto fora do círculo de raio 5.')
    return x,y


def slope_y(x,y):
    x,y=point(x,y)
    if not y:raise ValueError('Tangente vertical; y não tem derivada finita em x.')
    return -x/y


def slope_x(x,y):
    x,y=point(x,y)
    if not x:raise ValueError('A representação inversa não tem derivada finita aqui.')
    return -y/x


def second_y(x,y):
    x,y=point(x,y)
    if not y:raise ValueError('A segunda derivada deste ramo exige y diferente de zero.')
    return -Q(25)/y**3


def tangent_vector(x,y):
    x,y=point(x,y)
    return -y,x


def rational_point(t):
    if isinstance(t,bool) or not isinstance(t,(int,Q)):raise ValueError('Parâmetro racional.')
    t=Q(t)
    return 5*(1-t*t)/(1+t*t),10*t/(1+t*t)


if __name__=='__main__':
    for x,y in ((3,4),(3,-4),(0,5),(5,0)):
        print('Ponto:',x,y,'vetor tangente:',tangent_vector(x,y))
        if y:print('y′=',slope_y(x,y),'y″=',second_y(x,y))
        else:print('Tangente vertical x=5; dx/dy=',slope_x(x,y))
    print('A fórmula de y′ não se aplica a pontos fora da curva.')
