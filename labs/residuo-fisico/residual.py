"""Baseline polinomial e contraexemplo analítico. Não implementa uma rede neural."""
from fractions import Fraction as F
import math

def frac(x):
    if type(x) is int:return F(x)
    if isinstance(x,F):return x
    raise ValueError("use int ou Fraction")

def point(x):
    x=frac(x)
    if not 0<=x<=1:raise ValueError("domínio [0,1]")
    return x

def trial(a,b,x):
    a,b=map(frac,(a,b));x=point(x)
    return x*(1-x)*(a+b*x)

def residual(a,b,x):
    a,b=map(frac,(a,b));x=point(x)
    return 2*(a-1)+(6*x-2)*b

def loss_gradient(a,b,xs):
    a,b=map(frac,(a,b));xs=tuple(map(point,xs))
    if not 1<=len(xs)<=1000:raise ValueError("de 1 a 1000 pontos")
    rs=[residual(a,b,x) for x in xs];n=len(xs)
    loss=sum((z*z for z in rs),F(0))/n
    ga=sum((4*z for z in rs),F(0))/n
    gb=sum((2*z*(6*x-2) for x,z in zip(xs,rs)),F(0))/n
    return loss,(ga,gb)

def step(a,b,xs,eta):
    eta=frac(eta)
    if eta<=0:raise ValueError("passo positivo")
    _,g=loss_gradient(a,b,xs)
    return frac(a)-eta*g[0],frac(b)-eta*g[1]

def alias(x,A=F(1,8),k=4):
    x=point(x);A=frac(A)
    if type(k) is not int or not 1<=k<=32:raise ValueError("k inteiro de1 a32")
    s=math.sin(k*math.pi*float(x))
    return {"error":float(A)*s,"residual":float(A)*(k*math.pi)**2*s}

if __name__=="__main__":
    xs=(F(1,4),F(3,4));print("Antes:",loss_gradient(0,0,xs))
    a,b=step(0,0,xs,F(1,16));print("Um passo:",a,b,loss_gradient(a,b,xs))
    for x in (F(0),F(1,4),F(1,8)):print("Contraexemplo:",x,alias(x))
