"""Círculo de raio fixo e alpha constante; SI, ângulo em radianos.
Modelo cinemático e teste separado de contato horizontal, sem integração dinâmica.
"""
from math import sin,cos,isfinite,hypot

def real(v):
    if isinstance(v,bool):raise ValueError("Real finito necessário.")
    try:v=float(v)
    except (TypeError,ValueError,OverflowError):raise ValueError("Real finito necessário.") from None
    if not isfinite(v):raise ValueError("Real finito necessário.")
    return v

def state(radius,omega0,time,alpha=0,theta0=0):
    r,w0,t,alpha,theta0=map(real,(radius,omega0,time,alpha,theta0))
    if r<=0:raise ValueError("Raio positivo.")
    theta=real(theta0+w0*t+0.5*alpha*t*t);w=real(w0+alpha*t)
    er=(cos(theta),sin(theta));et=(-er[1],er[0])
    radial=real(-r*w*w);tangent=real(r*alpha)
    position=tuple(real(r*v) for v in er)
    velocity=tuple(real(r*w*v) for v in et)
    acceleration=tuple(real(radial*a+tangent*b) for a,b in zip(er,et))
    return dict(theta=theta,omega=w,position=position,velocity=velocity,
                acceleration=acceleration,radial=radial,tangent=tangent,speed=real(r*abs(w)))

def friction(mass,radius,speed,at,mu,g=10):
    m,r,v,at,mu,g=map(real,(mass,radius,speed,at,mu,g))
    if m<=0 or r<=0 or v<0 or mu<0 or g<=0:raise ValueError("m,R,g positivos; rapidez e mu não negativos.")
    radial=real(m*v*v/r);tangent=real(m*at)
    required=real(hypot(radial,tangent));limit=real(mu*m*g)
    return dict(radial=radial,tangent=tangent,required=required,limit=limit,
                feasible=required<=limit)

if __name__=='__main__':
    print(state(2,2,0))
    print(friction(.5,2,2,0,.5))
    print(friction(.5,2,4,0,.5))
