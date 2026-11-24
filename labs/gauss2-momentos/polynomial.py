"""Gauss2 racional para polinômios; elimina a raiz pela soma simétrica."""
from fractions import Fraction as Q
from math import comb

def rational(v):
    if type(v) not in (int,Q):raise ValueError('Inteiro ou Fraction necessário')
    return Q(v)

def inputs(coeff,a,b):
    coeff=tuple(map(rational,coeff));a=rational(a);b=rational(b)
    if not 1<=len(coeff)<=9 or a>=b:raise ValueError('Grau até8 e intervalo crescente')
    return coeff,a,b

def integral(coeff,a,b):
    coeff,a,b=inputs(coeff,a,b)
    return sum((c*(b**(k+1)-a**(k+1))/(k+1) for k,c in enumerate(coeff)),Q(0))

def gauss2(coeff,a,b,panels=1):
    coeff,a,b=inputs(coeff,a,b)
    if type(panels) is not int or not 1<=panels<=32:raise ValueError('De 1 a 32 painéis')
    width=(b-a)/panels;half=width/2;total=Q(0)
    for i in range(panels):
        mid=a+(i+Q(1,2))*width
        for k,c in enumerate(coeff):
            # f(mid+half/sqrt3)+f(mid-half/sqrt3): potências ímpares cancelam.
            for j in range(0,k+1,2):
                total+=half*2*c*comb(k,j)*mid**(k-j)*half**j/Q(3)**(j//2)
    return total

if __name__=='__main__':
    f=[Q(1,9),0,Q(-2,3),0,1]
    print('Integral:',integral(f,-1,1))
    for n in (1,2,4):print('painéis',n,'Q=',gauss2(f,-1,1,n))
