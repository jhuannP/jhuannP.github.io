"""Matrizes racionais retangulares não vazias; vetores coluna."""
from fractions import Fraction as Q

def scalar(value):
    if isinstance(value,bool) or not isinstance(value,(int,Q)):
        raise TypeError('Use int ou Fraction, sem bool ou float')
    return Q(value)

def matrix(rows):
    if not isinstance(rows,(list,tuple)) or not rows or any(not isinstance(r,(list,tuple)) or not r for r in rows):
        raise ValueError('Matriz retangular não vazia')
    width=len(rows[0])
    if any(len(r)!=width for r in rows):raise ValueError('Linhas de tamanhos diferentes')
    return tuple(tuple(scalar(x) for x in r) for r in rows)

def product(left,right):
    left=matrix(left);right=matrix(right)
    if len(left[0])!=len(right):raise ValueError('Dimensões incompatíveis')
    return tuple(tuple(sum((left[i][k]*right[k][j] for k in range(len(right))),Q(0))
                       for j in range(len(right[0]))) for i in range(len(left)))

def apply(a,vector):
    a=matrix(a)
    if not isinstance(vector,(list,tuple)):raise TypeError('Vetor em lista ou tupla')
    if len(vector)!=len(a[0]):raise ValueError('Dimensão do vetor incompatível')
    vector=tuple(scalar(x) for x in vector)
    return tuple(sum((x*y for x,y in zip(row,vector)),Q(0)) for row in a)
