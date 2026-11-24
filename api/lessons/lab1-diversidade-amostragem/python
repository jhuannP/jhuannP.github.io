"""Riqueza esperada numa coleção finita; categorias e ordens inteiramente sintéticas."""
from fractions import Fraction as F
from math import comb
POPULATIONS=((6,3,2,1),(3,3,3,3),(9,1,1,1))

def expectation(counts,n):
    if not isinstance(counts,(tuple,list)) or not 1<=len(counts)<=8 or any(type(k) is not int or k<0 for k in counts) or sum(counts)<=0:
        raise ValueError('Uma a oito contagens inteiras não negativas, total positivo')
    total=sum(counts)
    if type(n) is not int or not 0<=n<=total:raise ValueError('Tamanho inteiro entre zero e total')
    denominator=comb(total,n)
    detection=tuple(1-F(comb(total-k,n) if n<=total-k else 0,denominator) for k in counts)
    return dict(detection=detection,expected=sum(detection,F(0)),total_subsets=denominator)

def model(population=0,n=4,order=0):
    if type(population) is not int or population not in range(3) or type(order) is not int or order not in range(3):raise ValueError('Coleção e ordem 0..2')
    counts=POPULATIONS[population]
    r=expectation(counts,n);labels=tuple(i for i,k in enumerate(counts) for _ in range(k))
    if order==0:indices=tuple(range(12))
    elif order==1:
        offsets=[sum(counts[:i]) for i in range(4)]
        indices=tuple(offsets[i]+j for j in range(max(counts)) for i in range(4) if j<counts[i])
    else:indices=(0,6,1,9,7,2,11,3,8,10,4,5)
    selected=tuple(labels[i] for i in indices[:n])
    observed=tuple(selected.count(i) for i in range(4))
    return dict(counts=counts,indices=indices,selected=selected,observed=observed,
                richness=sum(k>0 for k in observed),rare_in_sample=observed[3]>0,
                rare_probability=r['detection'][3],expected=r['expected'],total_subsets=r['total_subsets'])

if __name__=='__main__':
    r=model();assert r['expected']==F(433,165) and r['rare_probability']==F(1,3)
    assert r['richness']==1 and model(order=1)['richness']==4
    print('Riqueza observada/esperada:',r['richness'],r['expected'])
    print('P(D aparecer) no sorteio uniforme:',r['rare_probability'])
