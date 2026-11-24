"""Enumeração racional de dropout invertido; operação isolada, não treino MLP."""
from fractions import Fraction as Q
from itertools import product

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Use int/Fraction.")
    return Q(x)

def values(xs):
    xs=tuple(map(rational,xs))
    if not 1<=len(xs)<=10:raise ValueError("Vetor com1 a10 componentes necessário.")
    return xs

def probability(p):
    p=rational(p)
    if not 0<=p<1:raise ValueError("0<=p<1 necessário.")
    return p

def apply(xs,p,mask=None,training=True):
    xs=values(xs);p=probability(p)
    if type(training) is not bool:raise ValueError("Modo booleano necessário.")
    if not training:return xs
    if mask is None:raise ValueError("Máscara explícita necessária no treino.")
    mask=tuple(mask)
    if len(mask)!=len(xs) or any(type(v) is not int or v not in (0,1) for v in mask):raise ValueError("Máscara inteira0/1 compatível necessária.")
    return tuple(v*m/(1-p) for v,m in zip(xs,mask))

def states(xs,p):
    xs=values(xs);p=probability(p);q=1-p;out=[]
    for mask in product((0,1),repeat=len(xs)):
        mass=q**sum(mask)*p**(len(mask)-sum(mask))
        if mass:out.append((mass,mask,apply(xs,p,mask)))
    return tuple(out)

def scalar_moments(xs,p,observable):
    data=[(mass,rational(observable(v))) for mass,_,v in states(xs,p)]
    mean=sum((mass*v for mass,v in data),Q(0))
    variance=sum((mass*(v-mean)**2 for mass,v in data),Q(0))
    return mean,variance

if __name__=='__main__':
    print(states([2,-1],Q(1,2)))
    print(scalar_moments([2,-1],Q(1,2),sum))
    print(scalar_moments([2,-1],Q(1,2),lambda v:max(0,sum(v))))
