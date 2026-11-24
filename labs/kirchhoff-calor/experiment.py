"""Duas formas isoméricas hipotéticas, fase fixa e pressão padrão 1 bar."""
from math import isfinite
T0=300.

def number(x,lo,hi):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or not lo<=x<=hi:
        raise ValueError('Número finito fora do intervalo autorizado.')
    return x

def cp_integral(c0,slope,t1,t2):
    """Integral em J/mol; c0 em J/(mol K), slope em J/(mol K²)."""
    number(c0,1,100);number(slope,-.1,.1);number(t1,250,650);number(t2,250,650)
    if min(c0+slope*(t1-T0),c0+slope*(t2-T0))<=0:raise ValueError('Cp não positivo no intervalo.')
    # Fatoração mantém exato o zero e evita diferença de quadrados próximos.
    return (t2-t1)*(c0+slope*((t1-T0)+(t2-T0))/2)

def model(t=500,cpb=30):
    number(t,250,650);number(cpb,20,60);u=t-T0
    cpa=40+.02*u;dcp=cpb-cpa
    ha=cp_integral(40,.02,T0,t)/1000
    hb=2+cp_integral(cpb,0,T0,t)/1000
    # Entalpia de reação, por mol da reação A→B escrita 1:1.
    dh=hb-ha
    constant=2+(cpb-40)*u/1000
    return dict(t=t,cpb=cpb,cpa=cpa,dcp=dcp,ha=ha,hb=hb,dh=dh,constant=constant,error=dh-constant,
                heat_a=ha,heat_b=hb-2,cycle=-(ha)+2+(hb-2))

if __name__=='__main__':
    s=model();assert abs(s['dh']+.4)<1e-12
    print(s)
