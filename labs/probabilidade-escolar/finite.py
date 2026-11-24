"""Probabilidade por pesos finitos; exemplos de dados ideais independentes."""
from fractions import Fraction as Q
from collections import defaultdict

def probability(weights,event):
    if type(weights) is not dict or not weights:
        raise ValueError('Mapa não vazio de pesos')
    if any(type(w) not in (int,Q) or w<0 for w in weights.values()):
        raise ValueError('Pesos int/Fraction não negativos, sem bool/float')
    total=sum(weights.values(),Q(0))
    if total==0:raise ValueError('Massa total deve ser positiva')
    event=set(event)
    if not event<=weights.keys():raise ValueError('Evento fora do espaço amostral')
    return sum((weights[x] for x in event),Q(0))/total

def dice_weights(sides=6):
    if type(sides) is not int or sides<1:raise ValueError('Número inteiro positivo de faces')
    return {(a,b):1 for a in range(1,sides+1) for b in range(1,sides+1)}

def sum_distribution(sides=6):
    w=dice_weights(sides);counts=defaultdict(int)
    for a,b in w:counts[a+b]+=1
    return {s:Q(n,len(w)) for s,n in sorted(counts.items())}

if __name__=='__main__':
    w=dice_weights();at_least_six={p for p in w if 6 in p}
    assert probability(w,at_least_six)==Q(11,36)
    print(sum_distribution())
    print('P(ao menos um 6) =',probability(w,at_least_six))
