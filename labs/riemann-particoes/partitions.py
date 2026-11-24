"""Somas exatas para f(x)=x² em [0,1], não integrador genérico."""
from fractions import Fraction as Q

def rational(value):
    if type(value) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float/texto')
    return Q(value)

def partition(points):
    if type(points) not in (list,tuple) or len(points)<2:
        raise ValueError('Forneça lista/tupla de extremos')
    p=tuple(map(rational,points))
    if p[0]!=0 or p[-1]!=1 or any(a>=b for a,b in zip(p,p[1:])):
        raise ValueError('Partição estritamente crescente, de 0 a 1')
    return p

def bounds(points):
    p=partition(points);pairs=tuple(zip(p,p[1:]))
    return dict(lower=sum((a*a*(b-a) for a,b in pairs),Q(0)),
                upper=sum((b*b*(b-a) for a,b in pairs),Q(0)),
                mesh=max(b-a for a,b in pairs))

def tagged_sum(points,tags):
    p=partition(points)
    if type(tags) not in (list,tuple) or len(tags)!=len(p)-1:
        raise ValueError('Uma amostra por faixa')
    t=tuple(map(rational,tags))
    if any(not a<=x<=b for a,b,x in zip(p,p[1:],t)):
        raise ValueError('Cada amostra deve pertencer à sua faixa')
    return sum((x*x*(b-a) for a,b,x in zip(p,p[1:],t)),Q(0))

if __name__=='__main__':
    p=[0,Q(1,4),Q(1,2),1]
    print(bounds(p))
    assert bounds(p)==dict(lower=Q(9,64),upper=Q(37,64),mesh=Q(1,2))
