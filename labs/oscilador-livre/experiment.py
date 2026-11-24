"""Oscilador linear livre: solução analítica em unidades SI."""
from math import sqrt, sin, cos, hypot, atan2, pi, isfinite

def state(m,k,x0,v0,t):
    values=(m,k,x0,v0,t)
    if any(type(z) not in (int,float) or not isfinite(z) for z in values):
        raise ValueError("Use números reais finitos; bool não é parâmetro.")
    if m<=0 or k<=0:
        raise ValueError("m e k devem ser positivos.")
    try:
        omega=sqrt(k/m)
        if not isfinite(omega) or omega==0: raise ValueError("Escala não representável.")
        c,s=cos(omega*t),sin(omega*t)
        x=x0*c+(v0/omega)*s
        v=-omega*x0*s+v0*c
        amplitude=hypot(x0,v0/omega)
        phase=None if amplitude==0 else atan2(-v0/omega,x0)
        kinetic=m*v*v/2
        potential=k*x*x/2
        out=dict(x=x,v=v,a=-(k/m)*x,omega=omega,period=2*pi/omega,
                 amplitude=amplitude,phase=phase,kinetic=kinetic,
                 potential=potential,energy=kinetic+potential)
    except (OverflowError,ZeroDivisionError) as exc:
        raise ValueError("Escala numérica não representável.") from exc
    if any(z is not None and not isfinite(z) for z in out.values()):
        raise ValueError("Resultado fora da escala numérica.")
    return out

if __name__=="__main__":
    a=state(2,8,.6,1.6,pi/4)
    print("t=T/4: x, v, energia =",a["x"],a["v"],a["energy"])
    print("Amplitude e fase =",a["amplitude"],a["phase"])
