"""Contraexemplo clássico; integral no retângulo truncado [a,1]×[b,1]."""
from math import atan,atan2,pi,isfinite,log


def cutoff(x):
    if isinstance(x,bool):raise ValueError('Corte real em(0,1].')
    try:x=float(x)
    except (ValueError,TypeError,OverflowError):raise ValueError('Corte real em(0,1].') from None
    if not isfinite(x) or not 0<x<=1:raise ValueError('Corte real em(0,1].')
    return x


def rectangle(a,b):
    a,b=map(cutoff,(a,b))
    return pi/4-atan(a)-atan2(1,b)+atan2(a,b)


def midpoint_x(a,b,n):
    """Integral em y analítica, seguida por ponto médio em x; sem quadratura2D."""
    a,b=map(cutoff,(a,b))
    if type(n) is not int or not 1<=n<=100000:raise ValueError('n inteiro1..100000.')
    h=(1-a)/n
    return h*sum(1/(1+x*x)-b/(x*x+b*b) for x in (a+(k+.5)*h for k in range(n)))


def annulus_absolute(epsilon):
    e=cutoff(epsilon)
    return -log(e) # angular integral ∫_0^(pi/2)|cos(2theta)| dtheta =1


if __name__=='__main__':
    for scale in (1.,2.,.5):
        for b in (1e-2,1e-3,1e-4):
            print('a/b=',scale,'b=',b,'I=',rectangle(scale*b,b))
        print('Limite do caminho:',atan(scale)-pi/4)
    print('Limites iterados: y primeiro',pi/4,'x primeiro',-pi/4)
    print('Integral absoluta em quarto de anel epsilon=.01:',annulus_absolute(.01))
