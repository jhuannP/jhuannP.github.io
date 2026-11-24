"""Atrito seco1D: decisão instantânea; trajetória apenas com força externa zero."""
from fractions import Fraction as Q

def q(v):
    if type(v) not in (int,Q):raise ValueError('use int/Fraction')
    return Q(v)

def parameters(m,g,ms,mk):
    m,g,ms,mk=map(q,(m,g,ms,mk))
    if m<=0 or g<=0 or not 0<=mk<=ms:raise ValueError('m,g positivos e0<=mk<=ms')
    return m,g,ms,mk

def state(v,F,m=2,g=10,ms=Q(1,2),mk=Q(3,10)):
    m,g,ms,mk=parameters(m,g,ms,mk);v,F=map(q,(v,F));N=m*g
    if not v and abs(F)<=ms*N:
        return dict(normal=N,friction=-F,acceleration=Q(0),regime='estático')
    direction=(1 if v>0 else -1) if v else (1 if F>0 else -1)
    f=-mk*N*direction
    return dict(normal=N,friction=f,acceleration=(F+f)/m,
                regime='deslizante' if v else 'início')

def coast(v,dt,m=2,g=10,ms=Q(1,2),mk=Q(3,10)):
    """Sem força aplicada: freia até v=0 e permanece em repouso."""
    m,g,ms,mk=parameters(m,g,ms,mk);v,dt=map(q,(v,dt))
    if dt<0:raise ValueError('duração não negativa')
    decel=mk*g
    stop=abs(v)/decel if decel and v else (Q(0) if not v else None)
    moving=min(dt,stop) if stop is not None else dt
    direction=1 if v>0 else (-1 if v<0 else 0)
    a=-direction*decel
    displacement=v*moving+a*moving*moving/2
    final_v=v+a*moving
    return dict(stop_time=stop,displacement=displacement,distance=abs(displacement),velocity=final_v,
                work=-mk*m*g*abs(displacement),delta_k=m*(final_v**2-v**2)/2)

if __name__=='__main__':
    assert state(0,6)['friction']==-6
    assert state(-3,6)['acceleration']==6
    assert coast(3,2)['distance']==Q(3,2)
    print(coast(3,2))
