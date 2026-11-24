"""Duas superfícies quadráticas adimensionais; não é diagnóstico geral."""
import math


def plane(kind, a, b, h, k):
    if kind not in (0, 1) or not all(math.isfinite(v) for v in (a,b,h,k)):
        raise ValueError('Função 0/1 e coordenadas finitas')
    sign = 1 if kind == 0 else -1
    base = a*a + 2*sign*b*b
    g = (2*a, 4*sign*b)
    linear = base + g[0]*h + g[1]*k
    exact = (a+h)**2 + 2*sign*(b+k)**2
    remainder = h*h + 2*sign*k*k
    rho = math.hypot(h,k)
    return dict(base=base,g=g,normal=(-g[0],-g[1],1),linear=linear,
                exact=exact,remainder=remainder,rho=rho,
                scaled=abs(remainder)/rho if rho else None,bound=2*rho*rho)


def model(kind=0, point=0, angle=45, refinements=2):
    if kind not in (0,1) or point not in (0,1,2) or not math.isfinite(angle) or not 0<=angle<=360 or not isinstance(refinements,int) or not 0<=refinements<=6:
        raise ValueError('Função 0/1, ponto 0..2, ângulo 0..360, n inteiro 0..6')
    a,b=((1,1),(0,0),(-1,1))[point]
    u={0:(1.,0.),90:(0.,1.),180:(-1.,0.),270:(0.,-1.),360:(1.,0.)}.get(angle,(math.cos(math.radians(angle)),math.sin(math.radians(angle))))
    rho=2.**(-refinements)
    return dict(plane(kind,a,b,rho*u[0],rho*u[1]),a=a,b=b,u=u)


if __name__=='__main__':
    s=plane(0,1,1,.1,.2)
    assert abs(s['linear']-4)<1e-14
    assert abs(s['exact']-4.09)<1e-14
    for n in (0,2,4,6):
        print(n,model(refinements=n))
