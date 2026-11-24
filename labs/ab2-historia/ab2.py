"""AB2 escalar racional, passo uniforme, t0=0, y1 fornecido.
RHS deve ser função pura de (t,y), retornando int/Fraction.
O histórico retornado usa O(N) memória; avanço guarda uma derivada anterior.
"""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q): raise ValueError("use int ou Fraction, sem bool/float")
    return Q(x)

def settings(h,n):
    h=rational(h)
    if h<=0 or type(n) is not int or not 1<=n<=1000: raise ValueError("h>0, N inteiro de1 a1000")
    return h,n

def heun_start(f,y0,h):
    h,_=settings(h,1);y0=rational(y0)
    k0=rational(f(Q(0),y0));k1=rational(f(h,y0+h*k0))
    return y0+h*(k0+k1)/2

def integrate(f,y0,y1,h,n):
    h,n=settings(h,n);y0,y1=map(rational,(y0,y1))
    if not callable(f): raise ValueError("RHS chamável")
    trace=[(Q(0),y0),(h,y1)]
    if n==1: return trace
    old=rational(f(Q(0),y0))
    for i in range(1,n):
        now=rational(f(i*h,trace[-1][1]))
        trace.append(((i+1)*h,trace[-1][1]+h*(3*now-old)/2))
        old=now
    return trace

def test_sequence(z,y0,y1,n):
    z=rational(z)
    return [y for _,y in integrate(lambda t,y:z*y,y0,y1,1,n)]

def characteristic(r,z):
    r,z=map(rational,(r,z))
    return r*r-(1+3*z/2)*r+z/2
