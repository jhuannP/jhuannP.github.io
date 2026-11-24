"""van't Hoff com DeltaCp constante; dados sintéticos, unidades SI."""
from math import isfinite,log1p,exp
R=8.314462618

def real(x,low,high):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or not low<=x<=high:
        raise ValueError("parâmetro real finito fora da faixa didática")
    return float(x)

def parameters(T,T0,H0,Cp):
    return real(T,200,1000),real(T0,200,1000),real(H0,-200000,200000),real(Cp,-500,500)

def log_ratio(T,T0,H0,Cp=0.):
    T,T0,H0,Cp=parameters(T,T0,H0,Cp)
    h=(T-T0)/T0
    return H0/R*(1/T0-1/T)+Cp/R*(log1p(h)+T0/T-1)

def equilibrium(T,T0,H0,Cp=0.,logK0=0.):
    logK0=real(logK0,-100,100)
    value=logK0+log_ratio(T,T0,H0,Cp)
    return dict(logK=value,K=exp(value))

def integrand(T,T0,H0,Cp=0.):
    T,T0,H0,Cp=parameters(T,T0,H0,Cp)
    return (H0+Cp*(T-T0))/(R*T*T)

if __name__=='__main__':
    from math import log
    for Cp in (0.,4*R):
        print('DeltaCp/R=',Cp/R,equilibrium(400,300,1200*R,Cp,log(2)))
