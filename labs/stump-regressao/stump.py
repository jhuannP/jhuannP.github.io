"""Busca exata didática: um atributo, SSE, folhas mínimas e modelo constante."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError('Inteiro ou Fraction necessário')
    return Q(x)

def fit(x,y,min_leaf=1):
    x=tuple(map(rational,x));y=tuple(map(rational,y))
    if not x or len(x)!=len(y) or len(x)>100:raise ValueError('De 1 a 100 pares necessários')
    if type(min_leaf) is not int or not 1<=min_leaf<=100:raise ValueError('Folha mínima inteira de 1 a 100')
    def mean(v):return sum(v,Q(0))/len(v)
    def error(v):
        m=mean(v);return sum(((a-m)**2 for a in v),Q(0))
    value=mean(y);best=dict(threshold=None,left=value,right=value,cost=error(y))
    unique=sorted(set(x))
    for a,b in zip(unique,unique[1:]):
        t=(a+b)/2
        left=[v for z,v in zip(x,y) if z<=t];right=[v for z,v in zip(x,y) if z>t]
        if min(len(left),len(right))<min_leaf:continue
        cost=error(left)+error(right)
        if cost<best['cost']:
            best=dict(threshold=t,left=mean(left),right=mean(right),cost=cost)
    return best

def predict(model,x):
    x=rational(x)
    return model['left'] if model['threshold'] is None or x<=model['threshold'] else model['right']

if __name__=='__main__':
    model=fit([0,1,2,3],[0,1,2,5])
    print(model)
    assert model==dict(threshold=Q(5,2),left=Q(1),right=Q(5),cost=Q(2))
