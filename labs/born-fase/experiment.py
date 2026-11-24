"""Estado contínuo normalizado em [0,L]; sem simular preparação ou evolução temporal."""
from math import sin,cos,pi,sqrt,isfinite
from cmath import exp

def phase(k):
    if type(k) is not int or k not in range(9): raise ValueError("k inteiro de 0 a 8")
    return k*pi/4

def wave(x,k=0,L=1.):
    phi=phase(k)
    if isinstance(L,bool) or not isinstance(L,(int,float)) or not isfinite(L) or L<=0:
        raise ValueError("L positivo finito")
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x):
        raise ValueError("x real finito")
    if not 0<=x<=L:return 0j
    u=x/L
    return (sin(pi*u)+exp(1j*phi)*sin(2*pi*u))/sqrt(L)

def probability(a,b,k=0,L=1.):
    wave(0,k,L)
    if any(isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) for x in (a,b)) or not 0<=a<=b<=L:
        raise ValueError("Use 0≤a≤b≤L")
    c=cos(phase(k))
    primitive=lambda u:u-sin(2*pi*u)/(4*pi)-sin(4*pi*u)/(8*pi)+c*(sin(pi*u)/pi-sin(3*pi*u)/(3*pi))
    return primitive(b/L)-primitive(a/L)

def model(k=0):
    c=cos(phase(k))
    return dict(k=k,left=.5+4*c/(3*pi),right=.5-4*c/(3*pi),mean_u=.5-16*c/(9*pi*pi),norm=1.)

if __name__=="__main__":
    r=model(0)
    assert abs(probability(0,.5)-r["left"])<1e-12
    print(r)
