"""Exemplo original adimensional: p=1+x,q=0,w=1/(1+x),0<=x<=1,Dirichlet."""
from math import sin,cos,pi,log,log1p,sqrt,isfinite

LOG2=log(2)


def index(n):
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=12:
        raise ValueError('n inteiro de1 a12 neste laboratório didático.')
    return n


def coordinate(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or not 0<=x<=1:
        raise ValueError('x real finito em[0,1].')
    return float(x)


def eigenvalue(n):
    return (index(n)*pi/LOG2)**2


def mode(n,x,normalized=False):
    n=index(n);x=coordinate(x)
    if not isinstance(normalized,bool):raise ValueError('normalized deve ser bool.')
    factor=sqrt(2/LOG2) if normalized else 1
    return factor*sin(n*pi*log1p(x)/LOG2)


def derivative(n,x,normalized=False):
    n=index(n);x=coordinate(x)
    if not isinstance(normalized,bool):raise ValueError('normalized deve ser bool.')
    factor=sqrt(2/LOG2) if normalized else 1
    return factor*(n*pi/LOG2)*cos(n*pi*log1p(x)/LOG2)/(1+x)


def simpson(f,panels=4096):
    if isinstance(panels,bool) or not isinstance(panels,int) or not 2<=panels<=65536 or panels%2:
        raise ValueError('panels inteiro par entre2 e65536.')
    h=1/panels
    total=f(0)+f(1)
    total+=sum((4 if j%2 else 2)*f(j*h) for j in range(1,panels))
    return total*h/3


def inner(m,n,weighted=True,normalized=False,panels=4096):
    m=index(m);n=index(n)
    if not isinstance(weighted,bool) or not isinstance(normalized,bool):
        raise ValueError('weighted e normalized devem ser bool.')
    return simpson(lambda x: mode(m,x,normalized)*mode(n,x,normalized)/(1+x if weighted else 1),panels)


if __name__=='__main__':
    print('Modelo adimensional prescrito, sem material ou experimento real.')
    print('lambda1 =',eigenvalue(1),'norma quadrada exata = ln2/2 =',LOG2/2)
    print('Produto com peso dos modos1/2:',inner(1,2))
    print('Produto sem peso dos modos1/2:',inner(1,2,weighted=False))
