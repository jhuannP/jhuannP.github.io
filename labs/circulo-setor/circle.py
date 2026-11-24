"""Coeficientes racionais de pi separados de aproximações poligonais float."""
from fractions import Fraction as Q
from math import sin,tan,pi

def rational(x):
    if isinstance(x,bool)or not isinstance(x,(int,Q)):raise ValueError('Use inteiro ou Fraction')
    return Q(x)

def radius(r):
    r=rational(r)
    if not Q(1,1000)<=r<=1000:raise ValueError('Raio didático 1/1000..1000')
    return r

def sector(r,turn):
    """turn em fração de uma volta, não graus nem radianos.
    Saída: área=area_pi*pi; arco=arc_pi*pi;
    perímetro=perimeter_plain+arc_pi*pi, com caso especial de disco completo.
    Unidades lineares consistentes fornecidas pelo usuário.
    """
    r=radius(r);turn=rational(turn)
    if not 0<turn<=1:raise ValueError('Fração de volta em (0,1]')
    return {'area_pi':r*r*turn,'arc_pi':2*r*turn,
            'perimeter_plain':Q(0)if turn==1 else 2*r}

def annulus_area_pi(outer,inner):
    outer=radius(outer);inner=rational(inner)
    if not 0<=inner<outer:raise ValueError('Use 0<=raio interno<externo')
    return outer*outer-inner*inner

def polygon_bounds(r,n):
    """Polígono inscrito de circunraio r e circunscrito de apótema r."""
    r=float(radius(r))
    if isinstance(n,bool)or type(n)is not int or not 3<=n<=256:
        raise ValueError('Inteiro 3..256 lados')
    return (n*r*r*sin(2*pi/n)/2,n*r*r*tan(pi/n))

if __name__=='__main__':
    print('Setor r=6, 120 graus:',sector(6,Q(1,3)))
    print('Coroa R=5,r=3: coeficiente de pi',annulus_area_pi(5,3))
    print('Áreas poligonais em torno do disco r=1:',polygon_bounds(1,64))
