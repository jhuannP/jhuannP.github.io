"""Momentos sobre D: 0<=x<=1, x**2<=y<=x. Coordenadas adimensionais."""
from fractions import Fraction as Q

def exponents(a,b):
    if any(type(v) is not int or not 0<=v<=20 for v in (a,b)):
        raise ValueError("Expoentes inteiros entre zero e vinte necessários")

def moment_dy_dx(a,b):
    exponents(a,b)
    return Q(1,b+1)*(Q(1,a+b+2)-Q(1,a+2*b+3))

def moment_dx_dy(a,b):
    exponents(a,b)
    return Q(1,a+1)*(Q(2,2*b+a+3)-Q(1,a+b+2))

def polynomial_integral(terms,order='dy_dx'):
    if not isinstance(terms,dict):raise ValueError("Mapa de monômios necessário")
    if order not in ('dy_dx','dx_dy'):raise ValueError("Ordem inválida")
    fn=moment_dy_dx if order=='dy_dx' else moment_dx_dy
    total=Q(0)
    for powers,coefficient in terms.items():
        if not isinstance(powers,tuple) or len(powers)!=2 or type(coefficient) not in (int,Q):
            raise ValueError("Use chave (a,b) e coeficiente racional")
        total+=coefficient*fn(*powers)
    return total

def midpoint_example(n):
    if type(n) is not int or not 1<=n<=256:raise ValueError("N entre um e 256 necessário")
    total=0.
    for i in range(n):
        x=(i+.5)/n;span=x-x*x
        for j in range(n):
            y=x*x+span*(j+.5)/n
            total+=(x+2*y)*span/(n*n)
    return total

if __name__=='__main__':
    terms={(1,0):1,(0,1):2}
    for order in ('dy_dx','dx_dy'):print(order,polynomial_integral(terms,order))
    for n in (10,20,40):print(n,midpoint_example(n))
