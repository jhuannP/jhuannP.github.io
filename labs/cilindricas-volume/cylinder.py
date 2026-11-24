"""Own quarter-annular paraboloid worksheet; moments are coefficients of pi."""
from fractions import Fraction as F
import math


def integral(coefficients,a,b):
    """Exact polynomial integral; coefficients in ascending powers."""
    if type(a) not in (int,F) or type(b) not in (int,F) or b<a:
        raise ValueError('ordered rational endpoints')
    if not isinstance(coefficients,(list,tuple)) or any(type(c) not in (int,F) for c in coefficients):
        raise ValueError('rational coefficients')
    return sum((F(c)*(F(b)**(i+1)-F(a)**(i+1))/(i+1) for i,c in enumerate(coefficients)), F(0))


def midpoint(n,jacobian=True):
    """Radial midpoint only: angle and z integrated analytically, L=1."""
    if type(n) is not int or not 1<=n<=10000 or type(jacobian) is not bool:
        raise ValueError('integer 1..10000 and boolean flag')
    h=F(1,n)
    return sum((4-(1+(j+F(1,2))*h)**2)*((1+(j+F(1,2))*h) if jacobian else 1)*h/2 for j in range(n))


def moments():
    # Quarter turn contributes pi/2. Report coefficients, not numerical pi.
    volume=integral((0,4,0,-1),1,2)/2
    radial_second=integral((0,0,0,4,0,-1),1,2)/2
    vertical_first=integral((0,8,0,-4,0,F(1,2)),1,2)/2
    return volume,radial_second,vertical_first


def point(r,theta,z):
    if any(type(x) not in (int,float) for x in (r,theta,z)):
        raise ValueError('finite real coordinates')
    try:r,theta,z=map(float,(r,theta,z))
    except OverflowError as e:raise ValueError('representable coordinates') from e
    if not all(math.isfinite(x) for x in (r,theta,z)) or r<0 or abs(theta)>1e6:
        raise ValueError('r>=0, finite coordinates, |theta|<=1e6')
    return r*math.cos(theta),r*math.sin(theta),z


def inverse(x,y,z):
    # Reuse validation of Cartesian real scalars, then choose a half-open angle.
    for v in (x,y,z):
        if type(v) not in (int,float):raise ValueError('finite reals')
        try:valid=math.isfinite(v)
        except OverflowError:valid=False
        if not valid:raise ValueError('finite reals')
    r=math.hypot(x,y)
    if r==0 or not math.isfinite(r):raise ValueError('angle undefined on axis or radius overflow')
    return r,math.atan2(y,x)%(2*math.pi),z


if __name__=='__main__':
    print('Coefficients of pi: V/L³, radial moment/L⁵, vertical moment/L⁴:',moments())
    for n in (1,2,4,8,16):print(n,midpoint(n),midpoint(n,False))
    print('Exact V=9*pi*L³/8; omitting r converges to wrong 5*pi/6 at L=1.')
