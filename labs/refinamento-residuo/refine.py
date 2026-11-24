"""Modelo racional 2×2 de correção; não simula um solver IEEE/LAPACK."""
from fractions import Fraction as Q

def scalar(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)) or abs(x)>1000:
        raise ValueError('Use int/Fraction de módulo até 1000')
    return Q(x)

def vector(v):
    if not isinstance(v,(list,tuple)) or len(v)!=2: raise ValueError('Vetor 2D necessário')
    return tuple(scalar(x) for x in v)

def matrix(a):
    if not isinstance(a,(list,tuple)) or len(a)!=2: raise ValueError('Matriz 2×2 necessária')
    return tuple(vector(row) for row in a)

def mv(a,x):
    a=matrix(a);x=vector(x)
    return tuple(sum((v*w for v,w in zip(row,x)),Q(0)) for row in a)

def residual(a,b,x):
    b=vector(b)
    return tuple(v-w for v,w in zip(b,mv(a,x)))

def norm(v): return max(map(abs,vector(v)))

def inverse(a):
    a=matrix(a);u,v=a[0];w,z=a[1];det=u*z-v*w
    if not det: raise ValueError('Matriz singular')
    result=((z/det,-v/det),(-w/det,u/det))
    return matrix(result)

def step(a,b,x,B,noise=(0,0)):
    """x+B(r+noise); B é uma aplicação inversa aproximada fixa."""
    x=vector(x);r=residual(a,b,x);noise=vector(noise)
    delta=mv(B,tuple(v+w for v,w in zip(r,noise)))
    return vector(tuple(v+w for v,w in zip(x,delta)))

def quantize(v,quantum):
    """Grade racional, empate para par; modelo artificial, não float IEEE."""
    v=scalar(v);quantum=scalar(quantum)
    if quantum<=0: raise ValueError('Passo positivo necessário')
    return Q(round(v/quantum))*quantum

if __name__=='__main__':
    A=((4,1),(1,3));b=(1,2);x=(Q(1,10),Q(3,5))
    exact=step(A,b,x,inverse(A));assert exact==(Q(1,11),Q(7,11))
    B=((Q(1,4),0),(0,Q(1,4)))
    for k in range(5):
        print(k,x,'resíduo',residual(A,b,x),'erro',norm(tuple(u-v for u,v in zip(exact,x))))
        x=step(A,b,x,B)
