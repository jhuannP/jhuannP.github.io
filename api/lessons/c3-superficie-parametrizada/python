"""Paraboloide z=a(x²+y²)/2 sobre disco de raio R.
Comprimentos em m, a em m^-1; densidade 2 kg/m² e campo (0,0,1) m/s.
"""
from math import sqrt, pi, isfinite


def geometry(a, radius, sign=1):
    for x in (a, radius):
        if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x):
            raise ValueError('Parâmetros finitos.')
    if a < 0 or radius <= 0 or isinstance(sign,bool) or sign not in (-1,1):
        raise ValueError('a não negativo, raio positivo e sinal ±1.')
    q=sqrt(1+(a*radius)**2)
    projected=pi*radius**2
    # Racionalização evita subtrair números quase iguais quando a≈0.
    area=2*projected*(q*q+q+1)/(3*(q+1))
    return dict(area=area,projected=projected,mass=2*area,
                flux=sign*projected,height=a*radius**2/2)


def normal(a,u,v,sign=1):
    """Normal unitária; parâmetros numéricos nas unidades do enunciado."""
    length=sqrt(1+a*a*(u*u+v*v))
    return tuple(sign*x/length for x in (-a*u,-a*v,1))


def simpson_area(a,radius,n=256):
    if isinstance(n,bool) or not isinstance(n,int) or n<2 or n%2:
        raise ValueError('n par e pelo menos 2.')
    h=radius/n
    def integrand(r):return 2*pi*r*sqrt(1+a*a*r*r)
    return h/3*(integrand(0)+integrand(radius)+sum((4 if i%2 else 2)*integrand(i*h) for i in range(1,n)))


if __name__=='__main__':
    for a in (0,.5,1):
        exact=geometry(a,1)
        print(a,exact,'área por Simpson:',simpson_area(a,1))
    print('Trocar orientação conserva área/massa e troca sinal do fluxo.')
