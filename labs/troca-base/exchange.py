"""Troca exata em R²; prova de dimensão geral está nas notas."""
from fractions import Fraction as Q

def vec(v):
    if not isinstance(v,(list,tuple)) or len(v)!=2: raise ValueError('Vetor2D necessário')
    if any(isinstance(x,bool) or not isinstance(x,(int,Q)) or abs(x)>100 for x in v):
        raise ValueError('Componentes int/Fraction de módulo até100')
    return tuple(Q(x) for x in v)

def det(columns):
    if not isinstance(columns,(list,tuple)) or len(columns)!=2:raise ValueError('Duas colunas necessárias')
    a,b=map(vec,columns)
    return a[0]*b[1]-a[1]*b[0]

def coordinates(columns,v):
    v=vec(v);a,b=map(vec,columns);delta=det((a,b))
    if delta==0:raise ValueError('Família original não é base de R²')
    return ((v[0]*b[1]-v[1]*b[0])/delta,(a[0]*v[1]-a[1]*v[0])/delta)

def exchange(columns,v,j):
    if isinstance(j,bool) or not isinstance(j,int) or j not in (0,1):raise ValueError('Índice0 ou1')
    v=vec(v);a,b=map(vec,columns);alpha=coordinates((a,b),v)
    if alpha[j]==0:raise ValueError('Coeficiente nulo: esta troca perde a base')
    result=[a,b];result[j]=v
    assert det(result)==alpha[j]*det((a,b))
    return tuple(result),alpha

if __name__=='__main__':
    old=((1,1),(1,-1));v=(3,1)
    new,alpha=exchange(old,v,0)
    assert alpha==(2,1) and det(new)==-4
    print('base nova',new,'coordenadas antigas',alpha)
    print('coordenadas de b1 na nova base',coordinates(new,old[0]))
