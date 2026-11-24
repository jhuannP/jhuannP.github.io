"""Variações e escalas racionais para exemplos descritivos não negativos."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction; sem bool ou float')
    return Q(x)


def relative_change(initial,final):
    initial,final=map(rational,(initial,final))
    if initial<=0 or final<0:raise ValueError('Base positiva e valor final não negativo')
    return (final-initial)/initial


def bar_comparison(initial,final,baseline=0):
    initial,final,baseline=map(rational,(initial,final,baseline))
    relative=relative_change(initial,final)
    if not 0<=baseline<min(initial,final):raise ValueError('Origem abaixo dos dois valores positivos')
    return dict(absolute=final-initial,relative=relative,value_ratio=final/initial,
                drawn_ratio=(final-baseline)/(initial-baseline))


def rate_change(initial_percent,final_percent):
    initial_percent,final_percent=map(rational,(initial_percent,final_percent))
    if not 0<=initial_percent<=100 or not 0<=final_percent<=100:raise ValueError('Taxas entre0 e100%')
    return dict(points=final_percent-initial_percent,
                relative=(final_percent-initial_percent)/initial_percent if initial_percent else None)


def secant(t0,y0,t1,y1):
    t0,y0,t1,y1=map(rational,(t0,y0,t1,y1))
    if t1<=t0:raise ValueError('Tempo final maior que o inicial')
    return (y1-y0)/(t1-t0)


def histogram_density(edges,counts):
    if not isinstance(edges,(list,tuple)) or not isinstance(counts,(list,tuple)):
        raise ValueError('Bordas e contagens em listas/tuplas')
    edges=tuple(map(rational,edges))
    if len(edges)<2 or len(counts)!=len(edges)-1 or any(b<=a for a,b in zip(edges,edges[1:])):
        raise ValueError('Uma contagem por intervalo crescente')
    if any(type(n) is not int or n<0 for n in counts) or not sum(counts):
        raise ValueError('Contagens inteiras não negativas, total positivo')
    n=sum(counts)
    return tuple(Q(count,n)/(b-a) for a,b,count in zip(edges,edges[1:],counts))


if __name__=='__main__':
    print(bar_comparison(100,110,90))
    assert histogram_density([0,1,3],[2,2])==(Q(1,2),Q(1,4))
