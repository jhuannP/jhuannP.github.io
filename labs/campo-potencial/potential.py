"""Exemplos fixos de campo e potencial; não decide conservatividade geral."""
from fractions import Fraction as Q
from math import isfinite

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Use int/Fraction.")
    return Q(x)

def point(v):
    v=tuple(map(rational,v))
    if len(v)!=2:raise ValueError("Ponto de duas componentes necessário.")
    return v

def phi(v):
    x,y=point(v);return x*x*y+3*x+y*y

def field(v):
    x,y=point(v);return 2*x*y+3,x*x+2*y

def segment(a,b):
    # Simpson em t é exato: o integrando polinomial tem grau<=2.
    a,b=point(a),point(b);dx,dy=b[0]-a[0],b[1]-a[1]
    def integrand(t):
        u,v=field((a[0]+dx*t,a[1]+dy*t))
        return u*dx+v*dy
    return (integrand(Q(0))+4*integrand(Q(1,2))+integrand(Q(1)))/6

def path(vertices):
    vertices=tuple(map(point,vertices))
    if len(vertices)<2:raise ValueError("Pelo menos dois vértices necessários.")
    return sum((segment(a,b) for a,b in zip(vertices,vertices[1:])),Q(0))

def vortex(x,y):
    if isinstance(x,bool) or isinstance(y,bool):raise ValueError("Reais finitos necessários.")
    try:x,y=float(x),float(y)
    except (TypeError,ValueError,OverflowError):raise ValueError("Reais finitos necessários.") from None
    if not isfinite(x) or not isfinite(y):raise ValueError("Reais finitos necessários.")
    r2=x*x+y*y
    if r2<=0 or not isfinite(r2):raise ValueError("Ponto fora do domínio/resolução float.")
    out=(-y/r2,x/r2)
    if not all(map(isfinite,out)):raise ValueError("Campo não resolvido em float.")
    return out

if __name__=='__main__':
    print(path([(0,0),(1,2)]),path([(0,0),(1,0),(1,2)]))
    print(phi((1,2))-phi((0,0)))
