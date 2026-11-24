"""Exact local curvature squared from prescribed 3D derivatives, not data."""
from fractions import Fraction as Q

def scalar(x):
    if type(x) not in (int,Q):raise TypeError("use int or Fraction")
    return Q(x)

def vector(x):
    if type(x) not in (tuple,list) or len(x)!=3:
        raise TypeError("expected 3 components")
    return tuple(scalar(a) for a in x)

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def curvature_squared(velocity,acceleration):
    v=vector(velocity);a=vector(acceleration)
    speed2=dot(v,v)
    if not speed2:raise ValueError("regular parametrization required: nonzero derivative")
    c=cross(v,a)
    return dot(c,c)/speed2**3

def normal_acceleration_squared(velocity,acceleration):
    v=vector(velocity);a=vector(acceleration)
    speed2=dot(v,v)
    if not speed2:raise ValueError("nonzero derivative required")
    # Orthogonal projection, independent of the cross-product implementation.
    return dot(a,a)-dot(v,a)**2/speed2

def reparameterize(velocity,acceleration,first,second):
    v=vector(velocity);a=vector(acceleration)
    p=scalar(first);q=scalar(second)
    return (tuple(x*p for x in v),tuple(y*p*p+x*q for x,y in zip(v,a)))

def parabola(u):
    """gamma(u)=(2u,u**2,0), returns position, first, second derivative."""
    u=scalar(u)
    return (2*u,u*u,Q(0)),(Q(2),2*u,Q(0)),(Q(0),Q(2),Q(0))

if __name__=='__main__':
    for u in (Q(0),Q(1,2),Q(1)):
        point,v,a=parabola(u)
        vnew,anew=reparameterize(v,a,2,2)
        print("point",point,"kappa squared",curvature_squared(v,a),
              "after change",curvature_squared(vnew,anew))
    print("helix jet at t=0:",curvature_squared((0,2,3),(-2,0,0)))
