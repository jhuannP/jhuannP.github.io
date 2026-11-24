"""Faixas uniformes de Y=max(0,X-a), X uniforme [0,1]. Exemplo original.
Uma mensagem corresponde ao intervalo, não ao seu extremo nem ao ponto médio de Y.
"""
from fractions import Fraction as Q

def intervals(a, m):
    if type(a) not in (int,Q) or not 0<a<1:
        raise ValueError('a racional, 0<a<1')
    if type(m) is not int or not 1<=m<=1000:
        raise ValueError('m inteiro entre 1 e 1000')
    a=Q(a);delta=(1-a)/m
    return [(Q(0) if k==0 else a+k*delta,a+(k+1)*delta) for k in range(m)]

def risk(a,m):
    return sum(((hi-lo)**3/12 for lo,hi in intervals(a,m)),Q(0))

def message(x,a,m):
    cells=intervals(a,m)
    if type(x) not in (int,Q) or not 0<=x<=1:
        raise ValueError('x racional em [0,1]')
    for k,(lo,hi) in enumerate(cells):
        if lo<=x<hi or (k==m-1 and x==hi): return k
    raise AssertionError('partição inválida')

if __name__=='__main__':
    a=Q(1,2)
    for m in (1,2,4,8):
        print('faixas:',m,'risco:',risk(a,m))
        for k,(lo,hi) in enumerate(intervals(a,m)):
            print(' mensagem',k,'pré-imagem',lo,hi,'média',(lo+hi)/2)
    assert risk(a,2)==Q(7,192)
    assert risk(a,4)==Q(1,48)
