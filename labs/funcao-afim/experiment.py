"""Função afim com domínio explícito; exploração opcional para ensino médio."""
import math


def affine(a,b,x):
    return a*x+b


def coefficients(x1,y1,x2,y2):
    if not all(math.isfinite(x) for x in (x1,y1,x2,y2)) or x1==x2:
        raise ValueError('Pontos finitos com entradas diferentes')
    a=(y2-y1)/(x2-x1)
    return a,y1-a*x1


def preco(distancia_km):
    if not math.isfinite(distancia_km) or distancia_km<0:
        raise ValueError('Distância não negativa finita')
    return 6+2*distancia_km


def model(a=2.,b=1.,x1=0.,x2=2.,domain=0):
    if not all(math.isfinite(x) for x in (a,b,x1,x2)) or not -3<=a<=3 or not -3<=b<=6 or not -3<=x1<=3 or not -3<=x2<=3 or domain not in (0,1):
        raise ValueError('a ±3, b −3..6, entradas ±3, domínio 0/1')
    valid=lambda x:domain==0 or x>=0
    y1=affine(a,b,x1) if valid(x1) else None
    y2=affine(a,b,x2) if valid(x2) else None
    dx=x2-x1
    dy=y2-y1 if y1 is not None and y2 is not None else None
    slope=dy/dx if dy is not None and dx else None
    if a:
        root=-b/a
        if root==0:root=0
        zero_kind='unico' if valid(root) else 'fora'
    else:root=None;zero_kind='todos' if b==0 else 'nenhum'
    image='R' if domain==0 and a else ('{b}' if a==0 else '[b,+infinito)' if a>0 else '(-infinito,b]')
    return dict(a=a,b=b,x1=x1,x2=x2,domain=domain,y1=y1,y2=y2,dx=dx,dy=dy,
                slope=slope,root=root,zero_kind=zero_kind,image=image,
                monotonic='crescente' if a>0 else 'decrescente' if a<0 else 'constante')


if __name__=='__main__':
    assert preco(5)==16
    assert coefficients(0,6,5,16)==(2,6)
    print(model())
