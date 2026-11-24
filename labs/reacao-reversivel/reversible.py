"""A <=> B, primeira ordem nas duas direções, volume e T constantes.
Concentrações mol/L, tempo s, constantes s^-1; sistema fechado 1:1.
"""
from math import exp,log,isfinite

def number(x):
    if isinstance(x,bool):raise ValueError("Real finito necessário.")
    try:x=float(x)
    except (TypeError,ValueError,OverflowError):raise ValueError("Real finito necessário.") from None
    if not isfinite(x):raise ValueError("Real finito necessário.")
    return x

def model(kf,kb,a0,b0):
    kf,kb,a0,b0=map(number,(kf,kb,a0,b0))
    if kf<=0 or kb<=0 or min(a0,b0)<0:raise ValueError("kf,kb>0; concentrações>=0.")
    lam=number(kf+kb);total=number(a0+b0)
    if total<=0:raise ValueError("Inventário positivo necessário.")
    ae=number(total*(kb/lam));be=number(total*(kf/lam))
    if ae<=0 or be<=0:raise ValueError("Equilíbrio não resolvido em float.")
    return kf,kb,a0,b0,lam,total,ae,be

def state(kf,kb,a0,b0,t):
    kf,kb,a0,b0,lam,total,ae,be=model(kf,kb,a0,b0)
    t=number(t)
    if t<0:raise ValueError("Tempo não negativo necessário.")
    # Combinação convexa evita cancelamento em extremos de concentrações.
    weight=exp(-lam*t)
    a=number(weight*a0+(1-weight)*ae)
    b=number(weight*b0+(1-weight)*be)
    forward=number(kf*a);backward=number(kb*b)
    return dict(a=a,b=b,a_eq=ae,b_eq=be,forward=forward,backward=backward,
                da_dt=number(backward-forward),db_dt=number(forward-backward),
                relaxation_time=number(1/lam),equilibrium_ratio=number(kf/kb))

def relative_time(kf,kb,epsilon):
    kf,kb,_,_,lam,_,_,_=model(kf,kb,1,0)
    epsilon=number(epsilon)
    if not 0<epsilon<=1:raise ValueError("0<epsilon<=1 necessário.")
    return number(-log(epsilon)/lam)

if __name__=='__main__':
    print(state(.3,.1,1,0,log(2)/.4))
    print('Tempo até 1% do desvio inicial:',relative_time(.3,.1,.01))
