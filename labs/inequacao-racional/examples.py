"""Três expressões didáticas exatas; não é resolvedor simbólico geral."""
from fractions import Fraction as Q

def exact(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(x)

def value(x,example='linear'):
    x=exact(x)
    if example=='linear':return None if x==-2 else (x-1)/(x+2)
    if example=='hole':return None if x==2 else ((x-2)*(x+1))/(x-2)
    if example=='double':return None if x==-2 else (x-1)**2/(x+2)
    raise ValueError("Exemplo desconhecido.")

def satisfies(v,strict=False):
    if not isinstance(strict,bool):raise TypeError("strict deve ser bool.")
    if v is None:return False
    v=exact(v)
    return v>0 if strict else v>=0
