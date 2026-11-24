"""Audit the existing numerics4 Euler integrator; this is not a second solver."""
from fractions import Fraction as Q
from math import exp
from numerics4 import integrate

def exact_recurrence(q, n):
    """Exact algebraic Euler value for y'=-a*y, y0=1, q=a*h."""
    if type(q) not in (int,Q):
        raise TypeError("q must be int or Fraction, excluding bool")
    if q <= 0:
        raise ValueError("q must be positive")
    if type(n) is not int:
        raise TypeError("n must be int, excluding bool")
    if n < 0:
        raise ValueError("n must be nonnegative")
    return (1-Q(q))**n

def regime(q):
    exact_recurrence(q,0)
    if q < 1: return "decaimento positivo"
    if q == 1: return "anulacao em um passo"
    if q < 2: return "alternancia com decaimento"
    if q == 2: return "alternancia sem decaimento"
    return "alternancia com crescimento"

def refinement():
    """Fixed IVP y'=-y, y(0)=1, same final time T=1."""
    rows=[]
    for n in (10,20,40,80):
        trace=integrate(lambda t,y:[-y[0]],0,1,[1],n,'euler')
        value=trace[-1][1][0]
        error=abs(value-exp(-1))
        rows.append((n,value,error))
    return rows

if __name__ == "__main__":
    for q in (Q(1,2),1,Q(3,2),2,Q(5,2)):
        print(q,regime(q),[exact_recurrence(q,n) for n in range(3)])
    print("refinement: n, value at T=1, absolute error")
    for row in refinement():print(row)
