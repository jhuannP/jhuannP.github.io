"""Exact 2x2 rational checks for supplied eigenvalues; not an eigensolver."""
from fractions import Fraction as Q

def scalar(x):
    if type(x) not in (int,Q):
        raise TypeError("int or Fraction required, excluding bool/float")
    return Q(x)

def vector(v):
    if not isinstance(v,(tuple,list)) or len(v)!=2:
        raise ValueError("two-component vector required")
    return tuple(scalar(x) for x in v)

def matrix(a):
    if not isinstance(a,(tuple,list)) or len(a)!=2:
        raise ValueError("2x2 matrix required")
    return tuple(vector(row) for row in a)

def matvec(a,v):
    a,v=matrix(a),vector(v)
    return tuple(sum(x*y for x,y in zip(row,v)) for row in a)

def candidate(a,v):
    """Return exact eigenvalue if v is an eigenvector; None if not."""
    a,v=matrix(a),vector(v)
    if v==(0,0):raise ValueError("zero is not an eigenvector")
    w=matvec(a,v)
    i=next(i for i,x in enumerate(v) if x!=0)
    lam=w[i]/v[i]
    return lam if w==tuple(lam*x for x in v) else None

def characteristic(a):
    a=matrix(a)
    return (Q(1),-a[0][0]-a[1][1],a[0][0]*a[1][1]-a[0][1]*a[1][0])

def eigenspace(a,lam):
    """Basis of ker(A-lambda I), for a supplied rational lambda."""
    a,lam=matrix(a),scalar(lam)
    m=((a[0][0]-lam,a[0][1]),(a[1][0],a[1][1]-lam))
    if m[0][0]*m[1][1]-m[0][1]*m[1][0]!=0:return ()
    rows=[r for r in m if r!=(0,0)]
    if not rows:return ((Q(1),Q(0)),(Q(0),Q(1)))
    x,y=rows[0]
    return ((-y,x),)

if __name__ == "__main__":
    a=((2,1),(1,2))
    print("characteristic coefficients:",characteristic(a))
    for lam in (3,1,2):print(lam,eigenspace(a,lam))
    print("repeated eigenvalue, one direction:",eigenspace(((2,1),(0,2)),2))
