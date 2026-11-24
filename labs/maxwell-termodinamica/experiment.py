"""Gás ideal ilustrativo: F em J; S em J/K; p em Pa. Não são dados medidos."""
from math import isfinite, log
R = 8.314  # J/(mol K), valor arredondado
T0, V0 = 300.0, 0.01  # K e volume molar de referência em m³/mol

def state(T, V, n=1.0, cv=20.0):
    for x in (T,V,n,cv):
        if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or x<=0:
            raise ValueError("T,V,n e capacidade molar cv devem ser positivos e finitos")
    lt, lv = log(T/T0), log(V/(n*V0))
    F = n*cv*T*(1-lt)-n*R*T*lv
    S = n*cv*lt+n*R*lv
    return dict(F=F,S=S,U=n*cv*T,p=n*R*T/V,dS_dV=n*R/V,dp_dT=n*R/V)

def entropy_isotherm(V1,V2,n=1.0):
    state(T0,V1,n); state(T0,V2,n)
    return n*R*log(V2/V1)

if __name__ == "__main__":
    a,b=state(300,.01),state(300,.02)
    ds=entropy_isotherm(.01,.02)
    assert abs(ds-(b["S"]-a["S"]))<1e-12
    assert abs(a["F"]+300*a["S"]-a["U"])<1e-9
    print("ΔS =",ds,"J/K; ΔU =",b["U"]-a["U"],"J")
