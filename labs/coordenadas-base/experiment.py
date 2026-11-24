"""Mudanças de coordenadas 2D racionais; colunas de B são vetores da base."""
from fractions import Fraction as Q

def matrix(M):
    if not isinstance(M,(list,tuple)) or len(M)!=2 or any(not isinstance(r,(list,tuple)) or len(r)!=2 for r in M):
        raise ValueError("Matriz 2 por 2 necessária.")
    if any(type(v) not in (int,Q) for r in M for v in r):
        raise ValueError("Use int/Fraction, sem bool ou float.")
    return tuple(tuple(Q(v) for v in row) for row in M)

def vector(v):
    if not isinstance(v,(list,tuple)) or len(v)!=2 or any(type(x) not in (int,Q) for x in v):
        raise ValueError("Vetor de dois int/Fraction necessário.")
    return tuple(map(Q,v))

def apply(M,v):
    M,v=matrix(M),vector(v)
    return tuple(sum((a*b for a,b in zip(row,v)),Q(0)) for row in M)

def multiply(A,B):
    A,B=matrix(A),matrix(B)
    return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(2)),Q(0)) for j in range(2)) for i in range(2))

def inverse(B):
    B=matrix(B);a,b=B[0];c,d=B[1];det=a*d-b*c
    if det==0:raise ValueError("As colunas não formam uma base.")
    return ((d/det,-b/det),(-c/det,a/det))

def coordinates(B,v):return apply(inverse(B),v)
def transition(B,C):return multiply(inverse(C),B)
def representation(A,B):return multiply(multiply(inverse(B),A),B)
def gram(B):
    B=matrix(B);inverse(B)
    return multiply(tuple(zip(*B)),B)

if __name__=="__main__":
    B=((1,1),(0,1));C=((2,0),(0,1));v=(3,2);A=((2,0),(0,3))
    print("Coordenadas B:",coordinates(B,v),"coordenadas C:",coordinates(C,v))
    print("B para C:",transition(B,C),"operador em B:",representation(A,B))
    print("Métrica nas coordenadas B:",gram(B))
