"""Exact fixtures for F=(-y,x,z) and G=(x,y,z), not a general integrator."""
from fractions import Fraction as Q


def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise TypeError('Use int/Fraction without bool/float')
    return Q(x)


def point(v):
    if not isinstance(v,(tuple,list)) or len(v)!=3:raise ValueError('Three coordinates required')
    return tuple(map(number,v))


def edge_integral(start,end):
    """Integral of (-y,x,z).dr along the straight segment start->end."""
    x,y,z=point(start);u,v,w=point(end)
    return x*v-y*u+(w*w-z*z)/2


def stokes_rectangle(a,b,c,p,q,orientation=1):
    """Graph z=c+p*x+q*y over [0,a]x[0,b], up if orientation=+1."""
    a,b,c,p,q=map(number,(a,b,c,p,q))
    if min(a,b)<=0:raise ValueError('Positive base lengths')
    if type(orientation) is not int or orientation not in (-1,1):raise ValueError('Orientation is -1 or +1')
    vertices=[(Q(0),Q(0),c),(a,Q(0),c+p*a),(a,b,c+p*a+q*b),(Q(0),b,c+q*b)]
    if orientation==-1:vertices=[vertices[i] for i in (0,3,2,1)]
    edges=tuple(edge_integral(vertices[i],vertices[(i+1)%4]) for i in range(4))
    return dict(vertices=tuple(vertices),edges=edges,circulation=sum(edges,Q(0)),curl_flux=orientation*2*a*b)


def gauss_box(lower,lengths):
    """Outward flux of G=(x,y,z) on all SIX faces of a translated box."""
    x,y,z=point(lower);a,b,c=point(lengths)
    if min(a,b,c)<=0:raise ValueError('Positive lengths')
    faces=dict(x_low=-x*b*c,x_high=(x+a)*b*c,
               y_low=-y*a*c,y_high=(y+b)*a*c,
               z_low=-z*a*b,z_high=(z+c)*a*b)
    return dict(faces=faces,flux=sum(faces.values(),Q(0)),divergence_integral=3*a*b*c)


if __name__=='__main__':
    print('Stokes',stokes_rectangle(2,3,1,1,2))
    print('Gauss',gauss_box((1,2,3),(2,3,4)))
