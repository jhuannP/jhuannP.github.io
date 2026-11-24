"""Volumes/pi para raios lineares, coordenadas em uma mesma unidade de comprimento."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):
        raise ValueError('Use int/Fraction, sem float/bool.')
    return Q(x)


def polynomial_integral(c,a,b):
    a,b=map(rational,(a,b));c=tuple(map(rational,c))
    if b<=a:raise ValueError('Intervalo positivo necessário.')
    return sum(v*(b**(i+1)-a**(i+1))/(i+1) for i,v in enumerate(c))


def annulus(a,b,outer,inner=(0,0)):
    """R(x)=outer[0]+outer[1]*x; r análogo. Retorna coeficiente V/pi."""
    a,b=map(rational,(a,b))
    if b<=a or len(outer)!=2 or len(inner)!=2:
        raise ValueError('Intervalo positivo e dois coeficientes por raio.')
    R0,R1=map(rational,outer);r0,r1=map(rational,inner)
    for x in (a,b):
        R=R0+R1*x;r=r0+r1*x
        if not 0<=r<=R:raise ValueError('Exige 0<=r<=R em todo intervalo.')
    # Para raios lineares, as desigualdades nos extremos bastam.
    return polynomial_integral((R0*R0-r0*r0,2*(R0*R1-r0*r1),R1*R1-r1*r1),a,b)


def cone_sums(n):
    """Somas para A/pi=x², 0<=x<=1: esquerda, meio e direita."""
    if type(n) is not int or n<1:raise ValueError('n inteiro positivo.')
    return tuple(sum(Q(2*k+j,2*n)**2 for k in range(n))/n for j in (0,1,2))


if __name__=='__main__':
    print('Cone, V/pi:',annulus(0,1,(0,1)))
    print('R=1+x,r=x, V/pi:',annulus(0,1,(1,1),(0,1)))
    print('Mesma região 0<=y<=x, eixo y=2, V/pi:',annulus(0,1,(2,0),(2,-1)))
    print('Somas esquerda/meio/direita, n=4:',cone_sums(4))
    print('Coeficientes em unidades cúbicas; multiplicar por pi. Não modela superfícies.')
