"""Planar prescribed forces and ideal support candidates, exact rational arithmetic."""
from fractions import Fraction as Q


def scalar(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise TypeError('Use int or Fraction without bool/float')
    return Q(x)


def vector(v):
    if not isinstance(v,(tuple,list)) or len(v)!=2:
        raise ValueError('Two components required')
    return tuple(map(scalar,v))


def cross(a,b):
    a,b=vector(a),vector(b)
    return a[0]*b[1]-a[1]*b[0]


def resultant(loads, origin=(0,0)):
    """Loads are (point,force) pairs; all points use the same frame."""
    ox,oy=vector(origin)
    if not isinstance(loads,(list,tuple)) or len(loads)>100:
        raise ValueError('At most 100 prescribed loads')
    fx=fy=tau=Q(0)
    for point,force in loads:
        x,y=vector(point);a,b=vector(force)
        fx+=a;fy+=b;tau+=(x-ox)*b-(y-oy)*a
    return dict(force=(fx,fy),torque=tau)


def beam(length,weight,point_load,x):
    """Horizontal uniform beam, two upward-only endpoint supports; x may overhang."""
    length,weight,point_load,x=map(scalar,(length,weight,point_load,x))
    if length<=0 or min(weight,point_load,x)<0:
        raise ValueError('L positive; weights and load position nonnegative')
    rb=weight/2+point_load*x/length
    ra=weight+point_load-rb
    return dict(RA=ra,RB=rb,unilateral_ok=ra>=0 and rb>=0)


if __name__=='__main__':
    s=beam(6,12,6,5)
    loads=[((0,0),(0,s['RA'])),((6,0),(0,s['RB'])),((3,0),(0,-12)),((5,0),(0,-6))]
    print('candidate',s)
    print('origin A',resultant(loads))
    print('origin B',resultant(loads,(6,0)))
    print('overhang x15',beam(6,12,6,15))
