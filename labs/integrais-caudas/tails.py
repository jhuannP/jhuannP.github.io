"""Exact truncation and finite-interval brackets for x**(-p), integer p >= 2."""
from fractions import Fraction as Q

def _power(p):
    if type(p) is not int:
        raise TypeError("p must be an integer, excluding bool")
    if p < 2:
        raise ValueError("this exact laboratory implements only p >= 2")

def _rational(value, name):
    if type(value) not in (int, Q):
        raise TypeError(name + " must be int or Fraction")
    return Q(value)

def tail(p, boundary):
    _power(p)
    boundary = _rational(boundary, "boundary")
    if boundary < 1:
        raise ValueError("boundary must be >= 1")
    return Q(1, p-1) / boundary**(p-1)

def partial(p, boundary):
    remaining = tail(p, boundary)
    return Q(1, p-1) - remaining

def cutoff(p, tolerance):
    """Smallest integer B >= 1 with tail(p,B) STRICTLY below tolerance."""
    _power(p)
    tolerance = _rational(tolerance, "tolerance")
    if tolerance <= 0:
        raise ValueError("tolerance must be positive")
    if tail(p, 1) < tolerance:
        return 1
    lo, hi = 1, 2
    while tail(p, hi) >= tolerance:
        lo, hi = hi, 2*hi
    while hi-lo > 1:
        mid = (lo+hi)//2
        if tail(p, mid) < tolerance:
            hi = mid
        else:
            lo = mid
    return hi

def finite_bracket(p, boundary, n):
    """Right/left rectangle bounds for integral on [1,B]; no tail included."""
    _power(p)
    boundary = _rational(boundary, "boundary")
    if boundary < 1:
        raise ValueError("boundary must be >= 1")
    if type(n) is not int:
        raise TypeError("n must be int, excluding bool")
    if n <= 0:
        raise ValueError("n must be positive")
    step = (boundary-1)/n
    lower = step*sum(1/(1+i*step)**p for i in range(1,n+1))
    upper = step*sum(1/(1+i*step)**p for i in range(n))
    return lower, upper

if __name__ == "__main__":
    print("p=2, B=10:", partial(2,10), tail(2,10))
    print("strict tail < 1/100:", cutoff(2,Q(1,100)))
    lo, hi = finite_bracket(2,10,100)
    print("finite quadrature bracket:", float(lo), float(hi))
    print("full bracket with exact tail:", float(lo+tail(2,10)), float(hi+tail(2,10)))
