"""Dois centros equivalentes: H=[[a,b],[b,a]], S=[[1,s],[s,1]].
Parâmetros sintéticos em uma unidade de energia escolhida; |s|<1.
Vetores retornados sem normalizar e quadrado do coeficiente de normalização.
Não calcula integrais, densidade espacial ou energia molecular total.
"""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q): raise ValueError("use int ou Fraction")
    return Q(x)

def parameters(alpha,beta,s):
    alpha,beta,s=map(rational,(alpha,beta,s))
    if not -1<s<1: raise ValueError("base independente: |s|<1")
    return alpha,beta,s

def vector(v):
    if not isinstance(v,(list,tuple)) or len(v)!=2: raise ValueError("vetor de dois componentes")
    x,y=map(rational,v)
    if x==0 and y==0: raise ValueError("vetor não nulo")
    return x,y

def metric_inner(v,w,s):
    s=rational(s)
    if not -1<s<1: raise ValueError("|s|<1")
    x,y=vector(v);u,t=vector(w)
    return x*u+y*t+s*(x*t+y*u)

def rayleigh(alpha,beta,s,v):
    alpha,beta,s=parameters(alpha,beta,s);x,y=vector(v)
    return (alpha*(x*x+y*y)+2*beta*x*y)/metric_inner(v,v,s)

def modes(alpha,beta,s):
    alpha,beta,s=parameters(alpha,beta,s)
    return {name:dict(vector=(Q(1),Q(sign)),energy=(alpha+sign*beta)/(1+sign*s),
                      norm_squared=2*(1+sign*s),coefficient_squared=1/(2*(1+sign*s)))
            for name,sign in (('plus',1),('minus',-1))}

def shifted(alpha,beta,s,offset):
    alpha,beta,s=parameters(alpha,beta,s);offset=rational(offset)
    # Adicionar C*identidade do operador produz C*S na base não ortogonal.
    return alpha+offset,beta+offset*s,s
