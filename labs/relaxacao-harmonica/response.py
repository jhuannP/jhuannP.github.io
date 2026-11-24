"""y'+k y=B cos(omega t), y(0)=y0; solução analítica, não solver geral."""
from math import exp,cos,sin,hypot,atan2,isfinite

def real(v):
    if type(v) not in (int,float) or not isfinite(v):raise ValueError('Use int/float finito sem bool')
    return float(v)

def state(k=2,omega=3,B=13,y0=-1,t=0):
    k,omega,B,y0,t=map(real,(k,omega,B,y0,t))
    if not 1e-3<=k<=1000 or not 0<=omega<=1000 or abs(B)>1000 or abs(y0)>1000 or not 0<=t<=100:
        raise ValueError('k1e-3..1000, omega0..1000, |B|/|y0|<=1000, t0..100')
    den=k*k+omega*omega;a=B*k/den;b=B*omega/den
    c=y0-a;co=cos(omega*t);si=sin(omega*t);decay=exp(-k*t)
    particular=a*co+b*si;homogeneous=c*decay
    derivative=omega*(-a*si+b*co)-k*c*decay
    return dict(y=particular+homogeneous,dy=derivative,particular=particular,homogeneous=homogeneous,
                envelope=abs(c)*decay,a=a,b=b,c=c,amplitude=abs(B)/hypot(k,omega),phase=atan2(omega,k),
                gain=k/hypot(k,omega),tau=1/k,forcing=B*co)

if __name__=='__main__':
    from math import log,pi
    for t in (0,pi/6,2*pi/3,log(10)):
        s=state(t=t);print(t,s['y'],s['envelope'])
