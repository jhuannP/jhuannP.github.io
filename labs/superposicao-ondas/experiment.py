"""Superposição linear: deslocamento em m, x em m, t em s.
A=0.01 m, lambda=1 m e frequência base 8 Hz.
"""
from math import cos,sin,pi,isfinite
A=.01
F=8.
K=2*pi
OMEGA=2*pi*F
C=F

def evaluate(mode,x,t,phase_pi=0.,df=1.):
    if mode not in (0,1,2) or not all(isfinite(v) for v in (x,t,phase_pi,df)) or df<0:
        raise ValueError('Modo 0/1/2, valores finitos e df não negativo')
    if mode==0:
        u=K*x-OMEGA*t;v=u+pi*phase_pi
        envelope=2*A*abs(cos(pi*phase_pi/2))
    elif mode==1:
        u=K*x-OMEGA*t;v=K*x+OMEGA*t
        envelope=2*A*abs(cos(K*x))
    else:
        # Série temporal num ponto fixo; x não é usado neste modo.
        u=2*pi*F*t;v=2*pi*(F+df)*t
        envelope=2*A*abs(cos(pi*df*t))
    y1=A*cos(u);y2=A*cos(v)
    return dict(y1=y1,y2=y2,total=y1+y2,envelope=envelope)

def beat_metrics(df):
    if not isfinite(df) or df<0:raise ValueError('df finito e não negativo')
    return dict(mean_frequency=F+df/2,beat_frequency=df,beat_period=1/df if df else None)

def standing_energy(x,t,mu=1.):
    if not all(isfinite(v) for v in (x,t,mu)) or mu<=0:raise ValueError('Valores finitos e mu positivo')
    tension=mu*C*C
    yt=-2*A*OMEGA*cos(K*x)*sin(OMEGA*t)
    yx=-2*A*K*sin(K*x)*cos(OMEGA*t)
    return dict(density=.5*mu*yt*yt+.5*tension*yx*yx,power=-tension*yx*yt)

if __name__=='__main__':
    for mode in (0,1,2):print(mode,evaluate(mode,.25,.5))
