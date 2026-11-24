"""Exact rational Lorentz force. Values use a consistent SI convention."""
from fractions import Fraction as Q

def scalar(x):
    if type(x) not in (int,Q):
        raise TypeError("exact int or Fraction required, excluding bool/float")
    return Q(x)

def vector(v):
    if not isinstance(v,(tuple,list)) or len(v)!=3:
        raise ValueError("three-component tuple or list required")
    return tuple(scalar(x) for x in v)

def cross(a,b):
    a,b=vector(a),vector(b)
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def dot(a,b):
    return sum(x*y for x,y in zip(vector(a),vector(b)))

def force(q,v,b,e=(0,0,0)):
    q=scalar(q);e=vector(e);mag=cross(v,b)
    return tuple(q*(x+y) for x,y in zip(e,mag))

if __name__ == "__main__":
    for q in (2,-2):print(q,force(q,(3,0,0),(0,0,4)))
