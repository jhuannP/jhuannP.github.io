"""Movimento vertical ideal com eixo para baixo e fluido em repouso.
F_d=-b*v, m>0, b>=0, g>=0, t>=0; SI, sem empuxo.
Solução analítica em float; kernels estáveis para tempos pequenos.
Não estima b nem valida um regime físico.
"""
import math

def finite(x):
    if isinstance(x,bool): raise ValueError("número real finito")
    try: x=float(x)
    except (ValueError,TypeError,OverflowError): raise ValueError("número real finito") from None
    if not math.isfinite(x): raise ValueError("número real finito")
    return x

def kernels(r):
    # phi1=(1-exp(-r))/r; phi2=(r-1+exp(-r))/r².
    if r<1e-4:
        phi1=1+r*(-.5+r*(1/6+r*(-1/24+r*(1/120-r/720))))
        phi2=.5+r*(-1/6+r*(1/24+r*(-1/120+r*(1/720-r/5040))))
    else:
        phi1=-math.expm1(-r)/r
        phi2=(1-phi1)/r
    return phi1,phi2

def state(m,b,g,t,v0=0,y0=0):
    m,b,g,t,v0,y0=map(finite,(m,b,g,t,v0,y0))
    if m<=0 or b<0 or g<0 or t<0: raise ValueError("m>0, b,g,t>=0")
    if b==0:
        return dict(velocity=finite(v0+g*t),position=finite(y0+v0*t+g*t*t/2),
                    acceleration=g,tau=None,terminal=None)
    tau=finite(m/b)
    if tau<=0: raise ValueError("escala de tempo não resolvida em float")
    r=finite(t/tau);phi1,phi2=kernels(r)
    v=finite(v0*math.exp(-r)+g*t*phi1)
    y=finite(y0+v0*t*phi1+g*t*t*phi2)
    acceleration=finite(g-v/tau)
    return dict(velocity=v,position=y,acceleration=acceleration,tau=tau,terminal=finite(g*tau))
