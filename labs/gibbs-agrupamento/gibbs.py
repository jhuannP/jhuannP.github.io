"""Ensembles discretos finitos: massas racionais, entropias em float, kB=1."""
from fractions import Fraction as Q
from math import log,fsum,inf

def distribution(values):
    values=tuple(values)
    if not values or any(isinstance(v,bool) or not isinstance(v,(int,Q)) for v in values):
        raise TypeError("Distribuição não vazia de int/Fraction.")
    values=tuple(Q(v) for v in values)
    if min(values)<0 or sum(values)!=1:raise ValueError("Massas não negativas com soma exata 1.")
    return values

def logq(v):
    return log(v.numerator)-log(v.denominator)

def entropy(values):
    p=distribution(values)
    return -fsum(float(v)*logq(v) for v in p if v)

def relative_entropy(p,q):
    p,q=distribution(p),distribution(q)
    if len(p)!=len(q):raise ValueError("Mesmo espaço rotulado necessário.")
    if any(a and not b for a,b in zip(p,q)):return inf
    return fsum(float(a)*(logq(a)-logq(b)) for a,b in zip(p,q) if a)

def grouping(values,groups):
    p=distribution(values);groups=tuple(tuple(g) for g in groups)
    flat=[i for g in groups for i in g]
    if not groups or any(not g for g in groups) or any(type(i) is not int for i in flat) or sorted(flat)!=list(range(len(p))):
        raise ValueError("Grupos não vazios devem particionar os índices sem repetição.")
    masses=tuple(sum((p[i] for i in g),Q(0)) for g in groups)
    conditional=tuple(tuple(p[i]/mass for i in g) if mass else None for g,mass in zip(groups,masses))
    macro=entropy(masses)
    within=fsum(float(mass)*entropy(c) for mass,c in zip(masses,conditional) if mass)
    uniform=[Q(0)]*len(p)
    for g,mass in zip(groups,masses):
        for i in g:uniform[i]=mass/len(g)
    return dict(masses=masses,conditional=conditional,micro=entropy(p),macro=macro,
                within=within,uniform_within=tuple(uniform),max_given_groups=entropy(uniform))

if __name__=='__main__':
    p=[Q(1,2),Q(1,4),Q(1,8),Q(1,8)]
    result=grouping(p,[[0,1],[2,3]])
    print(result)
    print('D(p||q):',relative_entropy(p,result['uniform_within']))
