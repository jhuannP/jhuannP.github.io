"""Resposta inicial de partícula sobre chão liso; g=10 m/s² didático."""
import math


def acceleration(forces,m):
    forces=tuple(forces)
    if not math.isfinite(m) or m<=0 or not all(math.isfinite(x) for x in forces):
        raise ValueError('Massa positiva e forças finitas')
    return sum(forces)/m


def direction(angle):
    r=math.sqrt(3)/2
    special={-180:(-1.,0.),-150:(-r,-.5),-120:(-.5,-r),-90:(0.,-1.),
             -60:(.5,-r),-30:(r,-.5),0:(1.,0.),30:(r,.5),60:(.5,r),
             90:(0.,1.),120:(-.5,r),150:(-r,.5),180:(-1.,0.)}
    return special.get(angle,(math.cos(math.radians(angle)),math.sin(math.radians(angle))))


def response(mass,fx,fy,vx=0):
    if not all(math.isfinite(v) for v in (mass,fx,fy,vx)) or mass<=0:
        raise ValueError('Massa positiva e entradas finitas')
    weight=10*mass;trial=weight-fy
    normal=max(trial,0)
    net_y=0 if trial>=0 else fy-weight
    state='contato' if trial>0 else 'limite' if trial==0 else 'separacao'
    return dict(mass=mass,fx=fx,fy=fy,vx=vx,weight=weight,normal=normal,
                ax=fx/mass,ay=net_y/mass,net_y=net_y,state=state,
                power=fx*vx if fx and vx else 0,kinetic=mass*vx*vx/2)


def model(mass=2.,force=6.,angle=0.,vx=2.):
    if not all(math.isfinite(v) for v in (mass,force,angle,vx)) or not 1<=mass<=4 or not 0<=force<=40 or not -180<=angle<=180 or not -4<=vx<=4:
        raise ValueError('m 1..4 kg, F 0..40 N, ângulo ±180°, vx ±4 m/s')
    c,s=direction(angle)
    clean=lambda v:0. if v==0 else v
    return dict(response(mass,clean(force*c),clean(force*s),vx),force=force,angle=angle)


if __name__=='__main__':
    assert acceleration((10,-4),2)==3
    assert model()['ax']==3
    for F in (10,20,30):print(model(2,F,90,0))
