"""Enumeração exata e Monte Carlo bootstrap com gerador didático compartilhado."""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import ceil, sqrt

PRESETS = ([0,2], [0,0,2], [0,1,1,4], [2,2,2])


def validate_data(data):
    if not 1 <= len(data) <= 5:
        raise ValueError('Entre 1 e 5 dados neste laboratório de enumeração')
    if any(isinstance(x,bool) or not isinstance(x,(int,Q)) for x in data):
        raise ValueError('Use int ou Fraction')
    return list(map(Q,data))


def statistic(data, kind='mean'):
    if kind=='mean':return sum(data)/len(data)
    if kind=='median':
        values=sorted(data); n=len(values)
        return values[n//2] if n%2 else (values[n//2-1]+values[n//2])/2
    raise ValueError('Use mean ou median')


def percentile(values, probability):
    if isinstance(probability,bool) or not isinstance(probability,(int,Q)) or not 0<=probability<=1:
        raise ValueError('Probabilidade racional entre 0 e 1')
    if not values:raise ValueError('Lista de réplicas não vazia')
    values=sorted(values)
    # Inversa da CDF empírica, sem interpolação: menor valor cuja acumulada atinge u.
    index=max(0,ceil(Q(probability)*len(values))-1)
    return values[index]


def summarize(values, observed):
    n=len(values);mean=sum(values)/n
    variance=sum((x-mean)**2 for x in values)/n
    return dict(mean=mean, bias=mean-observed, variance=variance,
                sample_variance=None if n==1 else variance*Q(n,n-1),
                lower=percentile(values,Q(1,40)), upper=percentile(values,Q(39,40)),
                masses={x:Q(count,n) for x,count in sorted(Counter(values).items())})


def exact_bootstrap(data, kind='mean'):
    data=validate_data(data); n=len(data)
    observed=statistic(data,kind)
    # Enumera posições, preservando a multiplicidade de valores repetidos.
    values=[statistic([data[i] for i in indices],kind) for indices in product(range(n),repeat=n)]
    result=summarize(values,observed)
    del result['sample_variance']  # Enumeração é a distribuição completa, não uma amostra de réplicas.
    return result


def monte_carlo(data, repetitions=200, seed=42, kind='mean'):
    data=validate_data(data);n=len(data);observed=statistic(data,kind)
    if isinstance(repetitions,bool) or not isinstance(repetitions,int) or not 2<=repetitions<=10000:
        raise ValueError('Entre 2 e 10000 réplicas')
    if isinstance(seed,bool) or not isinstance(seed,int) or not 0<=seed<2**32:
        raise ValueError('Semente inteira de 32 bits')
    state=seed;bucket=2**32//n;limit=bucket*n
    def index():
        nonlocal state
        while True:
            state=(1664525*state+1013904223)%(2**32)
            if state<limit:return state//bucket
    values=[statistic([data[index()] for _ in range(n)],kind) for _ in range(repetitions)]
    return summarize(values,observed)


if __name__=='__main__':
    exact=exact_bootstrap([0,2])
    assert exact['masses']=={Q(0):Q(1,4),Q(1):Q(1,2),Q(2):Q(1,4)}
    assert exact['mean']==1 and exact['variance']==Q(1,2)
    print('Exato [0,2]:',exact)
    for data in PRESETS:
        exact=exact_bootstrap(data);mc=monte_carlo(data)
        n=len(data);mean=Q(sum(data),n);v=sum((Q(x)-mean)**2 for x in data)/n
        assert exact['mean']==mean and exact['variance']==v/n
        print('Dados:',data,'SE exato:',sqrt(float(exact['variance'])),
              'SE Monte Carlo:',sqrt(float(mc['sample_variance'])))
    median=exact_bootstrap([0,0,2],'median')
    assert median['mean']==Q(14,27) and median['variance']==Q(560,729)
    print('Mediana [0,0,2]: viés bootstrap condicional=',median['bias'])
