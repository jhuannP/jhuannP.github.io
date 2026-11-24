"""Região entre y=x e y=2−x: fatores racionais de área/volume sobre pi.
Coordenadas em uma mesma unidade de comprimento; x em [0,2].
"""
from fractions import Fraction as Q

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(v)

def axis_value(axis):
    axis=rational(axis)
    if axis not in (0,1,3):raise ValueError("Eixos implementados: y=0, y=1, y=3.")
    return axis

def section(x,axis=0):
    x=rational(x);axis=axis_value(axis)
    if not 0<=x<=2:raise ValueError("Corte x em [0,2].")
    lo,hi=sorted((x,2-x))
    outer=max(abs(lo-axis),abs(hi-axis))
    inner=Q(0) if lo<=axis<=hi else min(abs(lo-axis),abs(hi-axis))
    return outer,inner,outer*outer-inner*inner

def riemann(n,side='left',axis=0):
    """Soma de áreas/pi vezes dx somente em [0,1], uniforme."""
    axis=axis_value(axis)
    if type(n) is not int or not 1<=n<=4096:raise ValueError("n inteiro 1..4096.")
    if side not in ('left','right','mid'):raise ValueError("left/right/mid.")
    offset={'left':Q(0),'right':Q(1),'mid':Q(1,2)}[side]
    return sum((section((i+offset)/n,axis)[2] for i in range(n)),Q(0))/n

def exact_volume_factor(axis=0,stop=1):
    axis=axis_value(axis);stop=rational(stop)
    if stop not in (1,2):raise ValueError("Extensão implementada: [0,1] ou [0,2].")
    return {Q(0):Q(2),Q(1):Q(1,3),Q(3):Q(4)}[axis]*stop

if __name__=='__main__':
    for axis in (0,1,3):
        print('eixo y=',axis,'volume/pi=',exact_volume_factor(axis),'limites n=8:',riemann(8,'right',axis),riemann(8,'left',axis))
