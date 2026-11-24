"""Oscilador livre sintético: m=1 kg, k=4 N/m, x0=1 m, v0=0."""
from math import sqrt, exp, expm1, sin, cos, isfinite

def model(b=2, t=2):
    if any(type(z) not in (int,float) or not isfinite(z) for z in (b,t)) or not 0<=b<=8 or not 0<=t<=10:
        raise ValueError("b em [0,8] kg/s e t em [0,10] s, finitos")
    gamma=b/2
    if b<4:
        w=sqrt(4-gamma*gamma)
        factor=sin(w*t)/w
        decay=exp(-gamma*t)
        x=decay*(cos(w*t)+gamma*factor)
        v=-4*decay*factor
        regime='sem amortecimento' if b==0 else 'subamortecido'
    elif b==4:
        x=exp(-2*t)*(1+2*t);v=-4*t*exp(-2*t)
        regime='crítico'
    else:
        beta=sqrt(gamma*gamma-4)
        slow=-4/(gamma+beta)
        decay=exp(slow*t)
        factor=expm1(-2*beta*t)/(2*beta)
        x=decay*(1+slow*factor);v=4*decay*factor
        regime='superamortecido'
    energy=v*v/2+2*x*x
    return dict(b=b,t=t,gamma=gamma,x=x,v=v,energy=energy,power=-b*v*v,
                regime=regime)

if __name__=='__main__':
    for b in (2,4,8):print(model(b,2))
