"""Transformações racionais 2D; sistemas singulares não são classificados."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError('use int/Fraction, sem bool/float')
    return Q(x)

def vector(v):
    if len(v)!=2:raise ValueError('vetor de dimensão2')
    return tuple(map(rational,v))

def matrix(A):
    if len(A)!=2 or any(len(r)!=2 for r in A):raise ValueError('matriz2x2')
    return tuple(vector(r) for r in A)

def apply(A,v):
    A,v=matrix(A),vector(v)
    return tuple(sum(a*x for a,x in zip(row,v)) for row in A)

def det(A):
    ((a,b),(c,d))=matrix(A)
    return a*d-b*c

def area(vertices):
    vertices=tuple(vector(v) for v in vertices)
    if len(vertices)<3:raise ValueError('ao menos3 vértices')
    return sum(vertices[i][0]*vertices[(i+1)%len(vertices)][1]-vertices[(i+1)%len(vertices)][0]*vertices[i][1] for i in range(len(vertices)))/2

def preimage_invertible(A,w):
    ((a,b),(c,d))=matrix(A);u,v=vector(w);D=a*d-b*c
    if not D:raise ValueError('rotina limitada a determinante não nulo; não classifica o caso singular')
    return ((d*u-b*v)/D,(-c*u+a*v)/D)

if __name__=='__main__':
    A=[[2,1],[0,1]]
    assert apply(A,(1,2))==(4,2)
    assert preimage_invertible(A,(4,2))==(1,2)
    print('Imagem:',apply(A,(1,2)),'; determinante:',det(A))
