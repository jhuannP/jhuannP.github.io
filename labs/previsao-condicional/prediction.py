"""Previsões populacionais no modelo fixo f(x,y)=3x, 0<=y<=x<=1.
Somente int/Fraction; nenhuma estimação a partir de amostras.
"""
from fractions import Fraction as Q

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):
        raise TypeError("Use int ou Fraction.")
    return Q(v)

def bounds(a,b):
    a,b=rational(a),rational(b)
    if not 0<=a<b<=1: raise ValueError("Faixa positiva dentro de [0,1].")
    return a,b

def joint_moment(k,a=0,b=1):
    """E[Y**k * 1{a<X<=b}], k inteiro não negativo."""
    a,b=bounds(a,b)
    if type(k) is not int or not 0<=k<=20:
        raise ValueError("Ordem inteira de 0 a 20.")
    return Q(3,(k+1)*(k+3))*(b**(k+3)-a**(k+3))

def bin_stats(a,b):
    mass=joint_moment(0,a,b)
    mean=joint_moment(1,a,b)/mass
    variance=joint_moment(2,a,b)/mass-mean*mean
    return mass,mean,variance

def partition(edges):
    edges=tuple(rational(v) for v in edges)
    if len(edges)<2 or edges[0]!=0 or edges[-1]!=1:
        raise ValueError("Partição completa de 0 até 1.")
    for a,b in zip(edges,edges[1:]): bounds(a,b)
    return tuple(bin_stats(a,b) for a,b in zip(edges,edges[1:]))

def partition_risk(edges):
    return sum((mass*var for mass,mean,var in partition(edges)),Q(0))

def affine_risk(a,b):
    """E[(Y-a-bX)**2], erro quadrático populacional adimensional."""
    a,b=rational(a),rational(b)
    return Q(1,5)-2*a*Q(3,8)-2*b*Q(3,10)+a*a+2*a*b*Q(3,4)+b*b*Q(3,5)

if __name__=='__main__':
    print("Sem X:",partition_risk([0,1]))
    print("Duas faixas:",partition_risk([0,Q(1,2),1]))
    print("X exato:",affine_risk(0,Q(1,2)))
