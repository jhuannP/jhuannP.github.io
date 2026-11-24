"""Distribuição exata do ciclo já existente; não Monte Carlo ou inferência."""
from fractions import Fraction as Q
from importlib import import_module
_old=import_module('labs.mutacao-selecao.cycle')

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('int/Fraction requeridos')
    return Q(x)

def matrix(m,s,mu):
    if type(m) is not int or not 1<=m<=8:raise ValueError('M inteiro1..8')
    s,mu=map(rational,(s,mu))
    if not 0<=s<=10 or not 0<=mu<=1:raise ValueError('s em[0,10],mu em[0,1]')
    return tuple(tuple(_old.offspring(m,Q(i,m),s,mu)) for i in range(m+1))

def history(m,s,mu,initial,steps):
    T=matrix(m,s,mu)
    if type(steps) is not int or not 0<=steps<=20:raise ValueError('passos inteiros0..20')
    if not isinstance(initial,(tuple,list)) or len(initial)!=m+1:raise ValueError('lei comM+1 estados')
    law=tuple(map(rational,initial))
    if min(law)<0 or sum(law)!=1:raise ValueError('lei não negativa normalizada')
    out=[law]
    for _ in range(steps):
        law=tuple(sum((law[i]*T[i][j] for i in range(m+1)),Q(0)) for j in range(m+1))
        out.append(law)
    return tuple(out)

def summary(law):
    if not isinstance(law,(tuple,list)) or not 2<=len(law)<=9:raise ValueError('lei finita2..9 estados')
    law=tuple(map(rational,law));m=len(law)-1
    if min(law)<0 or sum(law)!=1:raise ValueError('lei não negativa normalizada')
    mean=sum((Q(i,m)*v for i,v in enumerate(law)),Q(0))
    variance=sum(((Q(i,m)-mean)**2*v for i,v in enumerate(law)),Q(0))
    survival=1-law[0]
    return {'mean':mean,'variance':variance,'loss_cdf':law[0],
            'survival':survival,'survivor_mean':mean/survival if survival else None}

if __name__=='__main__':
    for t,law in enumerate(history(4,1,Q(1,4),(0,1,0,0,0),8)):
        z=summary(law)
        print(t, 'mean',float(z['mean']),'P(loss by t)',float(z['loss_cdf']))
