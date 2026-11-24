"""Intervalos racionais para sqrt(2), sem usar raiz de ponto flutuante."""
from fractions import Fraction as Q


def bracket(steps):
    if isinstance(steps,bool) or not isinstance(steps,int) or not 0<=steps<=40:
        raise ValueError('Número inteiro de etapas entre 0 e 40.')
    a,b=Q(1),Q(2)
    for _ in range(steps):
        mid=(a+b)/2
        if mid*mid<2:a=mid
        else:b=mid
    return dict(lower=a,upper=b,width=b-a)


def finite_sequence(n):
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=1000:
        raise ValueError('n inteiro entre 1 e 1000.')
    values=[1-Q(1,k) for k in range(1,n+1)]
    return dict(values=values,maximum=max(values),gap_to_one=Q(1,n))


def absolute_bounds(x,y):
    if any(isinstance(v,bool) or not isinstance(v,(int,Q)) for v in (x,y)):
        raise ValueError('Use inteiros ou Fraction.')
    x,y=Q(x),Q(y)
    return abs(x+y)<=abs(x)+abs(y),abs(abs(x)-abs(y))<=abs(x-y)


if __name__=='__main__':
    for n in (0,1,4,12):print('Intervalo racional:',n,bracket(n))
    for n in (1,5,20):
        r=finite_sequence(n)
        print('Conjunto finito:',n,'máximo=',r['maximum'],'distância até 1=',r['gap_to_one'])
    print('O supremo do conjunto infinito {1−1/n:n≥1} é 1, mas 1 não pertence a ele.')
    print('Isso é uma afirmação provada no texto, não inferida de uma lista finita.')
