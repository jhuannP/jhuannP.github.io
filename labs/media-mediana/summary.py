"""Resumos descritivos racionais; sem inferência populacional."""
from fractions import Fraction as Q
from collections import Counter


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use inteiro/Fraction, sem bool ou float')
    return Q(x)


def data(values):
    if not isinstance(values,(list,tuple)) or not values:raise ValueError('Dados não vazios em lista/tupla')
    return tuple(map(rational,values))


def frequency_summary(frequencies):
    if not isinstance(frequencies,dict) or not frequencies:raise ValueError('Tabela não vazia exigida')
    pairs=[]
    for x,count in frequencies.items():
        x=rational(x)
        if type(count) is not int or count<0:raise ValueError('Frequência inteira não negativa')
        if count:pairs.append((x,count))
    pairs.sort()
    n=sum(count for x,count in pairs)
    if not n:raise ValueError('Nenhuma observação com frequência positiva')
    total=sum((x*count for x,count in pairs),Q(0))
    ranks=((n-1)//2,n//2)  # Posições centrais indexadas desde zero.
    central=[]
    for rank in ranks:
        cumulative=0
        for x,count in pairs:
            cumulative+=count
            if cumulative>rank:
                central.append(x);break
    return dict(n=n,total=total,mean=total/n,median=sum(central)/2,
                minimum=pairs[0][0],maximum=pairs[-1][0],
                range=pairs[-1][0]-pairs[0][0])


def summarize(values):
    return frequency_summary(dict(Counter(data(values))))


def combine_means(groups):
    """Grupos não vazios, disjuntos e da mesma variável/unidade devem ser garantidos pelo chamador."""
    if not isinstance(groups,(list,tuple)) or not groups:raise ValueError('Forneça grupos')
    count_total=0;total=Q(0)
    for group in groups:
        if not isinstance(group,(list,tuple)) or len(group)!=2:raise ValueError('Grupo=(n,média)')
        count,mean=group
        if type(count) is not int or count<1:raise ValueError('Grupo com n inteiro positivo')
        mean=rational(mean);count_total+=count;total+=count*mean
    return total/count_total


def losses(values,center):
    xs=data(values);center=rational(center)
    return dict(absolute=sum((abs(x-center) for x in xs),Q(0)),
                squared=sum(((x-center)**2 for x in xs),Q(0)))


if __name__=='__main__':
    a=[1,2,3,4,10];b=[1,2,3,4,100]
    assert summarize(a)['mean']==4 and summarize(a)['median']==3
    assert summarize(b)['mean']==22 and summarize(b)['median']==3
    assert combine_means([(2,3),(6,10)])==Q(33,4)
    print(summarize(a),summarize(b))
