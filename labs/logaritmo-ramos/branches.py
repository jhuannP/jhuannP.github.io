"""Ângulos exatos em unidades de pi; ramo principal aberto, sem corte incluído."""
from fractions import Fraction as Q
from math import log,pi

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction')
    return Q(x)

def principal_angle(angle_pi):
    t=rational(angle_pi)
    if abs(t)>8:raise ValueError('Recorte de ângulo: -8..8 pi')
    wrapped=t-2*((t+1)//2)
    if wrapped==-1:raise ValueError('Sem valor no corte negativo neste ramo aberto')
    return wrapped

def product_defect(a,b):
    """[Arg(a)+Arg(b)-Arg(a*b)]/(2*pi), com a,b dados por seus ângulos/pi."""
    a=rational(a);b=rational(b)
    # Todas as três entradas precisam pertencer ao domínio do ramo.
    return (principal_angle(a)+principal_angle(b)-principal_angle(a+b))/2

def spiral_integral(start_radius,end_radius,angle_change_pi):
    """Integral de dz/z em z(t)=r0*exp(t*ln(r1/r0)+i*pi*q*t), t=0..1.
    Retorna (parte real float, coeficiente imaginário/pi exato).
    O caminho nunca atinge zero; ele pode cruzar o corte de Log principal.
    """
    r0=rational(start_radius);r1=rational(end_radius);q=rational(angle_change_pi)
    if not Q(1,16)<=r0<=16 or not Q(1,16)<=r1<=16 or abs(q)>8:
        raise ValueError('Recorte: raios 1/16..16, |q|<=8')
    return log(float(r1/r0)),q

if __name__=='__main__':
    print('Defeito do produto:',product_defect(Q(3,4),Q(3,4)))
    print('Caminho superior:',spiral_integral(1,2,Q(3,4)))
    print('Caminho inferior:',spiral_integral(1,2,Q(-5,4)))
