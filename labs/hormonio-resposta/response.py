"""Original receptor/response reduction; no hormone-specific fitted parameters."""
from fractions import Fraction as F
import math


def rational(x):
    if type(x) not in (int,F):raise ValueError('int or Fraction required, no bool/float')
    return F(x)


def equilibrium(h,kd,alpha,beta):
    h,kd,alpha,beta=map(rational,(h,kd,alpha,beta))
    if h<0 or kd<=0 or alpha<0 or beta<=0:raise ValueError('h>=0,Kd>0,alpha>=0,beta>0')
    u=h/(kd+h)
    rate=alpha*u+beta
    return {'u':u,'x':alpha*u/rate,'rate':rate,'maximum':alpha/(alpha+beta),
            'half_concentration':beta*kd/(alpha+beta) if alpha else None}


def drift(x,h,kd,alpha,beta):
    x=rational(x)
    if not 0<=x<=1:raise ValueError('0<=x<=1')
    state=equilibrium(h,kd,alpha,beta)
    return rational(alpha)*state['u']*(1-x)-rational(beta)*x


def transient(h,kd,alpha,beta,x0,t):
    x0,t=rational(x0),rational(t)
    if not 0<=x0<=1 or t<0:raise ValueError('initial fraction in[0,1],time>=0')
    s=equilibrium(h,kd,alpha,beta)
    try:r,tf=float(s['rate']),float(t)
    except OverflowError as e:raise ValueError('rates/time must be float-representable') from e
    if not math.isfinite(r) or not math.isfinite(tf) or r<=0:raise ValueError('positive representable rate, finite time')
    target=float(s['x']);initial=float(x0)
    return initial+(target-initial)*(-math.expm1(-r*tf))


if __name__=='__main__':
    print('Prescribed shared Kd=2,h=2:')
    for a,b in [(4,1),(1,4)]:print(a,b,equilibrium(2,2,a,b))
    print('A at h=2/5:',equilibrium(F(2,5),2,4,1))
    print('This is a reduction with arbitrary rates, not hormone dosage or measured biology.')
