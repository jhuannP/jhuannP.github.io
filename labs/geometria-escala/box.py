"""Caixa retangular ideal: unidades comuns, dimensões racionais positivas."""
from fractions import Fraction as Q

def positive(x):
    if type(x) not in (int,Q) or x<=0:
        raise ValueError('Use int/Fraction positivo, sem bool/float/texto')
    return Q(x)

def box(a,b,c):
    a,b,c=map(positive,(a,b,c))
    return dict(base_area=a*b,surface_area=2*(a*b+a*c+b*c),volume=a*b*c)

def scale(a,b,c,kx,ky,kz):
    a,b,c,kx,ky,kz=map(positive,(a,b,c,kx,ky,kz))
    return box(a*kx,b*ky,c*kz)

if __name__=='__main__':
    print('Original:',box(2,3,4))
    print('Todas as dimensões dobradas:',scale(2,3,4,2,2,2))
    print('Só a primeira dobrada:',scale(2,3,4,2,1,1))
