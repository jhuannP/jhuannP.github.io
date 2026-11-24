"""q''+2*zeta*q'+q=cos(r*tau); unidades adimensionais."""
import math

def response(zeta,r):
    a=1-r*r;b=2*zeta*r;D=a*a+b*b
    if D==0:return dict(amplitude=None,phase=None,power=None,peak=None)
    return dict(amplitude=1/math.sqrt(D),phase=math.atan2(b,a),power=zeta*r*r/D,
                peak=math.sqrt(1-2*zeta*zeta) if 0<zeta<1/math.sqrt(2) else None)

def state(zeta=.5,r=1.,initial=0,tau=6.):
    if not math.isfinite(zeta) or not 0<=zeta<=.9 or not math.isfinite(r) or not 0<=r<=2.5 or type(initial) is not int or initial not in (0,1,2) or not math.isfinite(tau) or not 0<=tau<=40:
        raise ValueError('zeta 0..0.9, r 0..2.5, preparação 0..2 e tau 0..40.')
    a=1-r*r;b=2*zeta*r;D=a*a+b*b;w=math.sqrt(1-zeta*zeta)
    if D:
        qp=(a*math.cos(r*tau)+b*math.sin(r*tau))/D
        vp=r*(-a*math.sin(r*tau)+b*math.cos(r*tau))/D
        ap=-r*r*qp;p0=a/D;v0=r*b/D
    else:
        qp=tau*math.sin(tau)/2;vp=(math.sin(tau)+tau*math.cos(tau))/2
        ap=math.cos(tau)-tau*math.sin(tau)/2;p0=v0=0.
    q0,vinit=((0.,0.),(p0,v0),(1.,0.))[initial]
    C=q0-p0;S=(vinit-v0+zeta*C)/w
    c=math.cos(w*tau);s=math.sin(w*tau);e=math.exp(-zeta*tau)
    qt=e*(C*c+S*s);vt=e*((-zeta*C+w*S)*c+(-zeta*S-w*C)*s)
    at=-2*zeta*vt-qt
    q=qp+qt;v=vp+vt;acc=ap+at
    power_in=math.cos(r*tau)*v;loss=2*zeta*v*v
    return dict(zeta=zeta,r=r,initial=initial,tau=tau,q=q,v=v,acc=acc,particular=qp,homogeneous=qt,
                envelope=math.hypot(C,S)*e,energy=(q*q+v*v)/2,power_in=power_in,loss=loss,
                energy_rate=power_in-loss,**response(zeta,r))

if __name__=='__main__':
    print(state())
    assert state(0,1,0,0)['q']==0
    assert response(.5,1)['amplitude']==1
