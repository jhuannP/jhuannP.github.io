"""Modelo passivo efetivo: g em nS, C em pF, V em mV, I em pA, t em ms."""
from fractions import Fraction as Q
from math import exp,isfinite

EK=Q(-90);ENA=Q(60)

def rational(v):
    if type(v) not in (int,Q):raise ValueError("Use int/Fraction, sem bool")
    return Q(v)

def stationary(gk,gna,C=100,I=0):
    gk,gna,C,I=map(rational,(gk,gna,C,I))
    G=gk+gna
    if gk<0 or gna<0 or G<=0 or C<=0:raise ValueError("Condutâncias não negativas, soma e C positivos")
    V=(gk*EK+gna*ENA+I)/G
    return dict(Vinf=V,tau=C/G,G=G,IK=gk*(V-EK),INa=gna*(V-ENA))

def transient(gk,gna,C=100,I=0,V0=-80,t=0):
    s=stationary(gk,gna,C,I);V0=rational(V0);t=rational(t)
    if t<0:raise ValueError("t não negativo")
    factor=exp(-float(t/s["tau"]))
    V=float(s["Vinf"])+float(V0-s["Vinf"])*factor
    dV=-float(V0-s["Vinf"])*factor/float(s["tau"])
    IK=float(gk)*(V-float(EK));INa=float(gna)*(V-float(ENA))
    if not all(map(isfinite,(V,dV,IK,INa))):raise ValueError("Escala fora do intervalo numérico")
    return dict(V=V,dV=dV,IK=IK,INa=INa,**{k:float(v) for k,v in s.items() if k not in ("IK","INa")})

if __name__=="__main__":
    s=stationary(4,1)
    assert s==dict(Vinf=-60,tau=20,G=5,IK=120,INa=-120)
    print("Estado estacionário:",s)
    print("Em t=20ms:",transient(4,1,t=20))
