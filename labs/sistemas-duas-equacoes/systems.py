"""Sistemas 2x2 racionais. Python é apoio opcional à resolução manual."""
from fractions import Fraction as Q

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(v)

def rows(values):
    values=tuple(tuple(rational(v) for v in row) for row in values)
    if len(values)!=2 or any(len(row)!=3 for row in values):
        raise ValueError("Duas linhas (coeficiente x, coeficiente y, termo independente).")
    return values

def solve(values):
    """Retorna (status, ponto). Ponto só existe em status unica."""
    (a,b,r),(c,d,s)=rows(values)
    determinant=a*d-b*c
    if determinant:
        return 'unica',((r*d-b*s)/determinant,(a*s-r*c)/determinant)
    if not any([a,b,c,d]):
        return ('infinitas',None) if r==s==0 else ('nenhuma',None)
    if a*s-c*r or b*s-d*r:return 'nenhuma',None
    return 'infinitas',None

def satisfies(values,point):
    rr=rows(values);point=tuple(rational(v) for v in point)
    if len(point)!=2:raise ValueError("Par ordenado com duas coordenadas.")
    x,y=point
    return all(a*x+b*y==r for a,b,r in rr)

def combine(values,multiplier):
    """Preserva a primeira; troca a segunda por segunda + multiplier*primeira."""
    first,second=rows(values);m=rational(multiplier)
    return first,tuple(v+m*u for u,v in zip(first,second))

def scale_row(values,index,factor):
    rr=list(rows(values));factor=rational(factor)
    if type(index) is not int or index not in (0,1) or not factor:
        raise ValueError("Índice 0/1 e fator não nulo necessários.")
    rr[index]=tuple(factor*v for v in rr[index])
    return tuple(rr)

if __name__=='__main__':
    model=[(3,2,94),(2,3,86)]
    print(solve(model))
    print('Conferência:',satisfies(model,[22,14]))
