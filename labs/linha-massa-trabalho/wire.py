"""Quadratura didática de um fio semicircular e campo rotacional sintéticos."""
from math import sin,cos,pi,hypot,isfinite
from dataclasses import dataclass

def real(v):
    if isinstance(v,bool) or not isinstance(v,(int,float)):raise TypeError("Use int ou float finito.")
    try:v=float(v)
    except OverflowError:raise ValueError("Valor fora da escala float.") from None
    if not isfinite(v):raise ValueError("Valor finito necessário.")
    return v

def panels(n):
    if isinstance(n,bool) or not isinstance(n,int):raise TypeError("Número inteiro par necessário.")
    if not 2<=n<=100000 or n%2:raise ValueError("2<=n<=100000 e par; limite operacional.")
    return n

def simpson(f,a,b,n):
    n=panels(n);h=(b-a)/n
    vals=[real(f(a+i*h)) for i in range(n+1)]
    value=h/3*(vals[0]+vals[-1]+4*sum(vals[1:-1:2])+2*sum(vals[2:-1:2]))
    return real(value)

@dataclass(frozen=True)
class Result:
    length:float
    mass:float
    x_center:float
    y_center:float
    work:float

def integrate_wire(radius=2,density=3,field_scale=1,mode='forward',n=512):
    """λ=λ0(1+(x/R)^2), F=k(-y,x); R em m, λ0 em kg/m, k em N/m.
    out-and-back conta duas passagens: não é uma parametrização simples do fio físico.
    """
    R,lam,k=map(real,(radius,density,field_scale));panels(n)
    if R<=0 or lam<=0:raise ValueError("Raio e densidade de referência positivos.")
    if mode=='forward':segments=[(lambda u:pi*u,lambda u:pi)]
    elif mode=='reverse':segments=[(lambda u:pi*(1-u),lambda u:-pi)]
    elif mode=='nonlinear':segments=[(lambda u:pi*(u+u*u)/2,lambda u:pi*(1+2*u)/2)]
    elif mode=='out-and-back':
        # Dois segmentos separados usam derivadas laterais consistentes no retorno.
        segments=[(lambda u:pi*u,lambda u:pi),(lambda u:pi*(1-u),lambda u:-pi)]
    else:raise ValueError("Modo desconhecido.")
    total=[0.0]*5
    for angle,rate in segments:
        def values(u):
            t=angle(u);dt=rate(u);x,y=R*cos(t),R*sin(t)
            dx,dy=-R*sin(t)*dt,R*cos(t)*dt
            speed=hypot(dx,dy);linear=lam*(1+(x/R)**2)
            return speed,linear*speed,x*linear*speed,y*linear*speed,(-k*y)*dx+(k*x)*dy
        for j in range(5):total[j]+=simpson(lambda u:values(u)[j],0.0,1.0,n)
    length,mass,mx,my,work=total
    if mass<=0:raise ArithmeticError("Massa numérica não positiva; escala fora do domínio operacional.")
    return Result(real(length),real(mass),real(mx/mass),real(my/mass),real(work))

if __name__=='__main__':
    for mode in ('forward','reverse','nonlinear','out-and-back'):
        print(mode,integrate_wire(mode=mode))
