"""Potências radiais exatas; não integra EDP ou fontes singulares."""
from fractions import Fraction as Q

def integer(x):
    if type(x) is not int or abs(x)>100: raise ValueError('Inteiro de módulo até 100')
    return x

def radius(r):
    if type(r) not in (int,Q): raise ValueError('Raio inteiro ou Fraction')
    r=Q(r)
    if r<=0: raise ValueError('Raio positivo')
    return r

def lap_power(k,r,d):
    k=integer(k);d=integer(d);r=radius(r)
    if not 2<=d<=10: raise ValueError('Dimensão de 2 a 10')
    return k*(k+d-2)*r**(k-2)

def shell3(r):
    r=radius(r)
    if not 1<=r<=2: raise ValueError('Casca entre 1 e 2')
    return 2-2/r

if __name__=='__main__':
    print('f(3/2)=',shell3(Q(3,2)))
    print('Laplaciano de r² em 3D=',lap_power(2,2,3))
