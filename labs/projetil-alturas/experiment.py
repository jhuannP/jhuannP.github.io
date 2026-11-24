"""Trajetória sem arrasto, g constante, unidades SI; estado racional exato."""
from fractions import Fraction as Q
import math

def rational(x):
    if type(x) not in (int,Q):raise ValueError("Use int ou Fraction")
    return Q(x)

def parameters(x0,y0,vx,vy,g):
    x0,y0,vx,vy,g=map(rational,(x0,y0,vx,vy,g))
    if y0<0 or g<=0:raise ValueError("Altura inicial não negativa e g positiva necessárias")
    return x0,y0,vx,vy,g

def state(t,x0=0,y0=15,vx=8,vy=10,g=10):
    t=rational(t)
    if t<0:raise ValueError("Tempo não negativo necessário")
    x0,y0,vx,vy,g=parameters(x0,y0,vx,vy,g)
    x=x0+vx*t;y=y0+vy*t-g*t*t/2;vyt=vy-g*t
    specific_energy=(vx*vx+vyt*vyt)/2+g*y
    return dict(x=x,y=y,vx=vx,vy=vyt,specific_energy=specific_energy)

def landing_time(y0=15,vy=10,g=10):
    _,y0,_,vy,g=parameters(0,y0,0,vy,g)
    if y0==0:return float(2*vy/g) if vy>0 else 0.0
    root=math.sqrt(float(vy*vy+2*g*y0))
    # Forma racionalizada evita subtrair números próximos quando vy<0.
    return float(2*y0)/(root-float(vy)) if vy<0 else (float(vy)+root)/float(g)

if __name__=="__main__":
    for t in (0,1,2,3):print(t,state(t))
    print("Tempo de chegada ao solo, s:",landing_time())
