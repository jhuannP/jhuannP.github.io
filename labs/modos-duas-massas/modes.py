"""Duas massas iguais, molas externas k0>0, acoplamento kc>=0; SI.
Solução modal analítica em float, sem dissipação e sem colisão entre massas.
"""
from math import sqrt,sin,cos,isfinite

def real(v):
    if isinstance(v,bool):raise ValueError("Real finito necessário.")
    try:v=float(v)
    except (TypeError,ValueError,OverflowError):raise ValueError("Real finito necessário.") from None
    if not isfinite(v):raise ValueError("Real finito necessário.")
    return v

def pair(values):
    values=tuple(real(v) for v in values)
    if len(values)!=2:raise ValueError("Duas componentes necessárias.")
    return values

def parameters(m,k0,kc):
    m,k0,kc=map(real,(m,k0,kc))
    if m<=0 or k0<=0 or kc<0:raise ValueError("m,k0 positivos; kc não negativo.")
    return m,k0,kc

def transform(values):
    a,b=pair(values);root=sqrt(2)
    return real((a+b)/root),real((a-b)/root)

def acceleration(m,k0,kc,position):
    m,k0,kc=parameters(m,k0,kc);x,y=pair(position)
    return real((-k0*x+kc*(y-x))/m),real((-k0*y-kc*(y-x))/m)

def energy(m,k0,kc,position,velocity):
    m,k0,kc=parameters(m,k0,kc);x,y=pair(position);u,v=pair(velocity)
    return real(.5*m*(u*u+v*v)+.5*k0*(x*x+y*y)+.5*kc*(y-x)*(y-x))

def state(m,k0,kc,position0,velocity0,t):
    m,k0,kc=parameters(m,k0,kc);t=real(t)
    qs=transform(position0);vs=transform(velocity0)
    omega=(real(sqrt(k0/m)),real(sqrt((k0+2*kc)/m)))
    if not all(w>0 for w in omega):raise ValueError("Frequências devem ser resolvidas em float.")
    q=[];v=[]
    for q0,v0,w in zip(qs,vs,omega):
        angle=real(w*t)
        q.append(real(q0*cos(angle)+(v0/w)*sin(angle)))
        v.append(real(-w*q0*sin(angle)+v0*cos(angle)))
    x=transform(q);speed=transform(v)
    modal_energy=tuple(real(.5*m*(u*u+w*w*a*a)) for a,u,w in zip(q,v,omega))
    return dict(position=x,velocity=speed,acceleration=acceleration(m,k0,kc,x),
                q=tuple(q),qdot=tuple(v),omega=omega,modal_energy=modal_energy,
                energy=energy(m,k0,kc,x,speed))

if __name__=='__main__':
    print(state(1,4,4,(.1,0),(0,0),0))
    print(state(1,4,4,(.1,0),(0,0),1))
