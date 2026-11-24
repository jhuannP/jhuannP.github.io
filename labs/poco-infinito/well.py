"""Modos do poço infinito 0<x<L. s=x/L, Phi=sqrt(L)*phi.
Avalia fórmulas analíticas, não resolve potencial geral ou equação por malha.
"""
import math
MAX_MODE=1000


def mode(n):
    if type(n) is not int or not 1<=n<=MAX_MODE:
        raise ValueError("Use inteiro n entre1 e1000; limite operacional do módulo.")
    return n


def number(v):
    if isinstance(v,bool) or not isinstance(v,(int,float)):
        raise TypeError("Use int/float finito, sem bool.")
    try:v=float(v)
    except OverflowError as exc:raise ValueError("Valor não representável.") from exc
    if not math.isfinite(v):raise ValueError("Valor deve ser finito.")
    return v


def phi(n,s):
    n=mode(n);s=number(s)
    return math.sqrt(2)*math.sin(n*math.pi*s) if 0<s<1 else 0.


def density(n,s):
    return phi(n,s)**2


def probability(n,a,b):
    n=mode(n);a,b=number(a),number(b)
    if not 0<=a<=b<=1:raise ValueError("Intervalo deve estar ordenado em0<=a<=b<=1.")
    d=b-a
    if d==0:return 0.
    k=n*math.pi;z=k*d;theta=k*(a+b)
    # P=d*(1-cos(theta)*sinc(z)); perto de z=0 evita subtração de quase iguais.
    if abs(z)<1e-3:
        z2=z*z
        one_minus_sinc=z2*(1/6-z2/120+z2*z2/5040-z2*z2*z2/362880)
    else:
        one_minus_sinc=1-math.sin(z)/z
    value=d*(2*math.sin(theta/2)**2+math.cos(theta)*one_minus_sinc)
    if not -1e-12<=value<=1+1e-12:
        raise ArithmeticError("Resultado numérico fora da faixa de probabilidade.")
    return min(1.,max(0.,value))


def energy(n,m=1,L=1,hbar=1):
    n=mode(n);m,L,hbar=number(m),number(L),number(hbar)
    if min(m,L,hbar)<=0:raise ValueError("m,L,hbar devem ser positivos.")
    try:value=((hbar/L)*n*math.pi)**2/(2*m)
    except (OverflowError,ZeroDivisionError) as exc:
        raise ArithmeticError("Energia fora da faixa numérica.") from exc
    if not math.isfinite(value) or value<=0:raise ArithmeticError("Energia fora da faixa numérica.")
    return value


def midpoint_norm(n,cells):
    n=mode(n)
    if type(cells) is not int or not 1<=cells<=100000:
        raise ValueError("Malha de1 a100000 células, sem bool.")
    return math.fsum(density(n,(i+.5)/cells) for i in range(cells))/cells


if __name__=="__main__":
    for n in (1,2,3):
        print("n",n,"E/E1",n*n,"P central",probability(n,.25,.75))
    print("Malha aliased",midpoint_norm(3,3),"malha refinada",midpoint_norm(3,1000))
