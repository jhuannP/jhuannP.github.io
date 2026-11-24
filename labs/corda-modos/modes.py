"""Corda ideal: coordenadas racionais e perfil harmônico aproximado."""
from fractions import Fraction as Q
from math import sin, cos, pi

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int/Fraction; unidades SI não detectadas automaticamente')
    return Q(x)

def spectrum(length,speed,n):
    L=rational(length);v=rational(speed)
    if not Q(1,100)<=L<=10 or not Q(1,100)<=v<=1000:
        raise ValueError('Limites didáticos: .01<=L<=10 m e .01<=v<=1000 m/s')
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=20:
        raise ValueError('Modo inteiro de1 a20 necessário')
    return dict(wavelength=2*L/n,frequency=n*v/(2*L),
                nodes=tuple(j*L/n for j in range(n+1)),
                antinodes=tuple((2*j+1)*L/(2*n) for j in range(n)))

def profile(length,speed,n,x,time,amplitude):
    """amplitude=A de CADA componente; máximo resultante nos ventres é2A."""
    m=spectrum(length,speed,n);L=rational(length)
    x=rational(x);t=rational(time);A=rational(amplitude)
    if not 0<=x<=L or not 0<=t<=10 or not 0<A<=L/(100*n):
        raise ValueError('0<=x<=L,0<=t<=10 s,0<A<=L/(100n) necessários')
    # Redução exata de ciclos antes de trigonometria float.
    space=(Q(n)*x/(2*L))%1; clock=(m['frequency']*t)%1
    return 2*float(A)*sin(2*pi*float(space))*cos(2*pi*float(clock))

if __name__=='__main__':
    L=Q(6,5);v=48;n=3
    print(spectrum(L,v,n))
    for t in (Q(0),Q(1,240),Q(1,120)):
        print(t,profile(L,v,n,Q(1,5),t,Q(1,1000)))
