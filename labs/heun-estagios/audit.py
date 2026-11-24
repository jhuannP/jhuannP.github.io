"""Audit the explicit trapezoid already implemented as 'heun' in numerics4."""
from fractions import Fraction as Q
from math import exp
from numerics4 import integrate

def factor(q):
    if type(q) not in (int,Q):
        raise TypeError("q must be int or Fraction, excluding bool")
    if q <= 0:
        raise ValueError("q must be positive")
    q=Q(q)
    return 1-q+q*q/2

def experiment(n,method):
    calls=0
    def rhs(t,y):
        nonlocal calls
        calls+=1
        return [-y[0]]
    trace=integrate(rhs,0,1,[1],n,method)
    value=trace[-1][1][0]
    return {"n":n,"method":method,"evaluations":calls,"value":value,
            "error":abs(value-exp(-1))}

if __name__ == "__main__":
    for q in (Q(1,2),Q(3,2),2,Q(5,2)):
        print("q, amplification:",q,factor(q))
    for n,method in ((20,'euler'),(10,'heun'),(20,'heun'),(40,'heun')):
        print(experiment(n,method))
