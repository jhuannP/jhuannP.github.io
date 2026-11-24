"""Quadrática e níveis reais; constantes/afins tratados separadamente."""
from fractions import Fraction as F
from math import sqrt

def _solve(a,b,c):
    if a==0:
        if b:return dict(kind='one',roots=(float(F(-c,b)),),discriminant=None)
        return dict(kind='all' if c==0 else 'none',roots=(),discriminant=None)
    d=b*b-4*a*c
    if d<0:return dict(kind='none',roots=(),discriminant=d)
    if d==0:return dict(kind='one',roots=(float(F(-b,2*a)),),discriminant=d)
    return dict(kind='two',roots=tuple(sorted(((-b-sqrt(d))/(2*a),(-b+sqrt(d))/(2*a)))),discriminant=d)

def model(a=1,b=-4,c=3,level=0):
    for value,lo,hi in ((a,-2,2),(b,-4,4),(c,-3,3),(level,-4,4)):
        if isinstance(value,bool) or not isinstance(value,int) or not lo<=value<=hi:raise ValueError('Coeficientes/nível inteiros nas faixas do painel')
    vertex=None if a==0 else (F(-b,2*a),F(4*a*c-b*b,4*a))
    image='all' if a==0 and b else 'constant' if a==0 else 'lower' if a>0 else 'upper'
    roots=_solve(a,b,c);intersections=_solve(a,b,c-level)
    h=float(vertex[0]) if vertex else 0.0
    return dict(vertex=vertex,image=image,bound=vertex[1] if vertex else F(c) if not b else None,
                zeros=roots,level=intersections,window=(h-3,h+3) if a else (-4.0,4.0))

if __name__=='__main__':
    r=model()
    assert r['vertex']==(2,-1) and r['zeros']['roots']==(1,3)
    assert model(1,-4,3,-1)['level']['kind']=='one'
    assert model(1,-4,3,-2)['level']['kind']=='none'
    print(r)
