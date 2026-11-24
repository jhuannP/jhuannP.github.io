"""Cilindro infinito, corrente axial uniforme, meio com permeabilidade mu0.
Valores reduzidos b=B/(mu0/(2*pi)), em A/m quando entradas estão em SI.
Não é simulação de circuito finito, materiais magnéticos ou corrente alternada.
"""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise TypeError("Use int ou Fraction para entradas exatas.")
    return Q(x)


def radius(a):
    a=rational(a)
    if a<=0:raise ValueError("Raio do fio deve ser positivo.")
    return a


def enclosed(current,a,r):
    current,a,r=rational(current),radius(a),rational(r)
    if r<0:raise ValueError("Distância radial não pode ser negativa.")
    return current*min(r*r/(a*a),Q(1))


def reduced_bphi(current,a,r):
    """Componente azimutal com sinal; no eixo define o limite zero."""
    current,a,r=rational(current),radius(a),rational(r)
    if r<0:raise ValueError("Distância radial não pode ser negativa.")
    return current*r/(a*a) if r<a else current/r


def reduced_field(current,a,x,y):
    """Componentes cartesianas (bx,by), sem precisar calcular raiz."""
    current,a,x,y=rational(current),radius(a),rational(x),rational(y)
    r2=x*x+y*y
    factor=current/(a*a) if r2<a*a else current/r2
    return (-factor*y,factor*x)


if __name__=="__main__":
    a=Q(1,500);current=6
    for r in (0,Q(1,1000),a,Q(1,250)):
        print("r/m",r,"I interna/A",enclosed(current,a,r),
              "bphi/(A/m)",reduced_bphi(current,a,r))
