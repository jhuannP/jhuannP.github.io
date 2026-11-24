"""Exact small-slope string model; prescribed tension, impedances and pulse."""
from fractions import Fraction as F


def real(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):
        raise ValueError('int/Fraction required')
    return F(x)


def coefficients(z1,z2):
    z1,z2=map(real,(z1,z2))
    if min(z1,z2)<=0:raise ValueError('positive impedances required')
    r=(z1-z2)/(z1+z2);tau=2*z1/(z1+z2)
    return dict(r=r,tau=tau,R=r*r,transmission=z2*tau*tau/z1)


def mean_power(z,omega,amplitude):
    z,omega,amplitude=map(real,(z,omega,amplitude))
    if z<=0 or omega<=0 or amplitude<0:raise ValueError('z,omega>0 and amplitude>=0 required')
    return z*omega*omega*amplitude*amplitude/2


def pulse(s,width):
    s,width=map(real,(s,width))
    if width<=0:raise ValueError('positive duration required')
    u=s/width
    if abs(u)>=1:return F(0),F(0)
    return (1-u*u)**3,-6*u*(1-u*u)**2/width


def field(side,x,t,z1=2,z2=6,tension=18,amplitude=F(1,100),width=F(1,20),arrival=F(1,3)):
    x,t,z1,z2,tension,amplitude,width,arrival=map(real,(x,t,z1,z2,tension,amplitude,width,arrival))
    c=coefficients(z1,z2)
    if tension<=0 or amplitude<0 or width<=0:raise ValueError('positive tension/duration, amplitude>=0 required')
    if side not in ('left','right') or (side=='left' and x>0) or (side=='right' and x<0):
        raise ValueError('side and half-line must agree')
    if side=='left':
        speed=tension/z1;mu=z1*z1/tension
        qi,di=pulse(t-x/speed-arrival,width);qr,dr=pulse(t+x/speed-arrival,width)
        y=amplitude*(qi+c['r']*qr)
        yt=amplitude*(di+c['r']*dr);yx=amplitude*(-di+c['r']*dr)/speed
    else:
        speed=tension/z2;mu=z2*z2/tension
        q,d=pulse(t-x/speed-arrival,width)
        y=c['tau']*amplitude*q;yt=c['tau']*amplitude*d;yx=-yt/speed
    return dict(y=y,yt=yt,yx=yx,flux=-tension*yx*yt,density=(mu*yt*yt+tension*yx*yx)/2)


def wall(kind,t,c=9,amplitude=F(1,100),width=F(1,20),arrival=F(1,3)):
    """Only boundary values x=0, for string on x<=0."""
    t,c,amplitude,width,arrival=map(real,(t,c,amplitude,width,arrival))
    if kind not in ('fixed','free') or c<=0 or amplitude<0:raise ValueError('valid end and positive speed required')
    q,d=pulse(t-arrival,width);r=-1 if kind=='fixed' else 1
    return dict(y=amplitude*(1+r)*q,yt=amplitude*(1+r)*d,yx=amplitude*(r-1)*d/c)


if __name__=='__main__':
    print('z1=2,z2=6:',coefficients(2,6))
    print('Reversed incidence:',coefficients(6,2))
    print('Powers (W), omega=4, incident amplitude=.01m:',
          mean_power(2,4,F(1,100)),mean_power(2,4,F(1,200)),mean_power(6,4,F(1,200)))
    print('Interface displacement at pulse center:',field('left',0,F(1,3))['y'],field('right',0,F(1,3))['y'])
    print('Free boundary at pulse center:',wall('free',F(1,3))['y'])
    print('Ideal linear strings only; no measured material or apparatus.')
