"""Bootstrap IID exato da média para até seis posições observadas."""
from fractions import Fraction as Q
from itertools import product
from collections import Counter


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool ou float.')
    return Q(x)


def distribution(values):
    if type(values) not in (list,tuple) or not 1<=len(values)<=6:
        raise ValueError('Use lista/tupla com uma a seis observações.')
    x=tuple(map(rational,values));n=len(x)
    counts=Counter(sum((x[i] for i in indices),Q(0))/n
                   for indices in product(range(n),repeat=n))
    total=n**n
    mean=sum((v*c for v,c in counts.items()),Q(0))/total
    variance=sum(((v-mean)**2*c for v,c in counts.items()),Q(0))/total
    empirical_variance=sum(((v-mean)**2 for v in x),Q(0))/n
    return {'counts':dict(sorted(counts.items())),'total':total,
            'mean':mean,'variance':variance,'empirical_variance':empirical_variance}


def quantile(counts,p):
    p=rational(p)
    if not 0<=p<=1 or type(counts) is not dict or not counts:
        raise ValueError('Distribuição e probabilidade inválidas.')
    if any(type(v) not in (int,Q) or type(c) is not int or c<1
           for v,c in counts.items()):raise ValueError('Valores racionais e contagens positivas.')
    total=sum(counts.values());acc=0
    for value,count in sorted(counts.items()):
        acc+=count
        if Q(acc,total)>=p:return value


if __name__=='__main__':
    r=distribution([1,1,4])
    print(r)
    print('Quantis 2,5% e 97,5%:',quantile(r['counts'],Q(1,40)),quantile(r['counts'],Q(39,40)))
    print('População sintética P(1)=99/100,P(100)=1/100:')
    print('Média=',Q(199,100),'chance de três valores1=',Q(99,100)**3)
    print('Se observarmos [1,1,1],bootstrap:',distribution([1,1,1]))
