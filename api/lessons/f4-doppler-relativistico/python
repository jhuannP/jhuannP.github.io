"""Doppler longitudinal: luz em +x, fonte em repouso, receptor v=βc.
β>0 é afastamento; frequências próprias; grandezas retornadas são razões.
"""
from math import sqrt,isfinite


def doppler(beta):
    if isinstance(beta,bool) or not isinstance(beta,(int,float)) or not isfinite(beta) or abs(beta)>=1:
        raise ValueError('β real finito com |β|<1.')
    gamma=1/sqrt((1-beta)*(1+beta))
    ratio=sqrt((1-beta)/(1+beta))
    return dict(gamma=gamma,ratio=ratio,arrival_period=1/(1-beta),
                proper_period=1/ratio,wavelength_ratio=1/ratio,z=1/ratio-1)


def beta_from_ratio(ratio):
    if isinstance(ratio,bool) or not isinstance(ratio,(int,float)) or not isfinite(ratio) or ratio<=0:
        raise ValueError('Razão de frequências positiva e finita.')
    # Evita elevar uma razão muito grande ao quadrado.
    if ratio<=1:
        q=ratio*ratio;return (1-q)/(1+q)
    q=(1/ratio)**2;return (q-1)/(q+1)


def receptions(beta):
    """Unidades T_emit=1 e c=1; distância inicial 3cT_emit.
    Duas cristas emitidas em t=0 e t=1, recebidas antes de cruzar a fonte.
    """
    q=doppler(beta)
    t0=3/(1-beta);t1=4/(1-beta)
    x0=t0;x1=t1-1  # posições dos dois raios no encontro
    dt=t1-t0;dx=x1-x0
    dt_prime=q['gamma']*(dt-beta*dx)
    dx_prime=q['gamma']*(dx-beta*dt)
    return dict(t0=t0,t1=t1,x0=x0,x1=x1,dt=dt,dx=dx,dt_prime=dt_prime,dx_prime=dx_prime)


if __name__=='__main__':
    for beta in (-.6,0,.6):
        q=doppler(beta);print('β=',beta,q)
        print('Recepções normalizadas:',receptions(beta))
        print('Linha sintética 600 THz ->',600*q['ratio'],'THz')
    print('Sem gravidade, expansão cosmológica ou efeito transversal.')
