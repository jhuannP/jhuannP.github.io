"""Correlação real 1D válida: um canal, passo1, sem padding ou bias."""
from fractions import Fraction as F

def vector(seq):
    seq=tuple(seq)
    if not 1<=len(seq)<=30 or any(isinstance(v,bool) or not isinstance(v,(int,F)) for v in seq):
        raise ValueError('Vetor de1 a30 inteiros ou Fraction')
    return tuple(F(v) for v in seq)

def correlate(x,k):
    x,k=vector(x),vector(k)
    if len(k)>len(x):raise ValueError('Kernel maior que entrada')
    return tuple(sum((k[j]*x[i+j] for j in range(len(k))),F(0))
                 for i in range(len(x)-len(k)+1))

def pullback(x,k,g):
    x,k,g=vector(x),vector(k),vector(g)
    y=correlate(x,k)
    if len(g)!=len(y):raise ValueError('Gradiente de saída incompatível')
    dx=[F(0)]*len(x);dk=[F(0)]*len(k)
    for i,gi in enumerate(g):
        for j,kj in enumerate(k):
            dx[i+j]+=gi*kj
            dk[j]+=gi*x[i+j]
    return tuple(dx),tuple(dk)

def squared_loss(x,k,target):
    y=correlate(x,k);target=vector(target)
    if len(target)!=len(y):raise ValueError('Alvo incompatível')
    g=tuple(a-b for a,b in zip(y,target))
    return sum((v*v for v in g),F(0))/2,pullback(x,k,g)

if __name__=='__main__':
    x=(2,-1,3,0);k=(1,2)
    print('y=',correlate(x,k))
    print('perda linear g=(1,-2,1):',pullback(x,k,(1,-2,1)))
    print('perda quadrática alvo=(1,1,1):',squared_loss(x,k,(1,1,1)))
