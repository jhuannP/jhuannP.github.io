"""Frenagem até parada versus aceleração continuada; parâmetros racionais sintéticos."""
from fractions import Fraction as F

def number(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):raise ValueError('Use int ou Fraction')
    return F(x)

def comparison(v0=10,b=2,t=5):
    v0,b,t=map(number,(v0,b,t))
    if v0<0 or b<=0 or t<0:raise ValueError('v0>=0, b>0 e t>=0')
    stop=v0/b;elapsed=min(t,stop)
    position=v0*elapsed-b*elapsed**2/2
    velocity=max(F(0),v0-b*t)
    phase='parado' if v0==0 or t>stop else ('junção' if t==stop else 'freando')
    acceleration=F(0) if phase=='parado' else (-b if phase=='freando' else None)
    continued_position=v0*t-b*t*t/2;continued_velocity=v0-b*t
    continued_distance=continued_position if t<=stop else v0*v0/(2*b)+b*(t-stop)**2/2
    return dict(stop=stop,distance=v0*v0/(2*b),position=position,velocity=velocity,
                phase=phase,acceleration=acceleration,average_acceleration=None if t==0 else (velocity-v0)/t,
                continued_position=continued_position,continued_velocity=continued_velocity,
                continued_distance=continued_distance)

if __name__=='__main__':
    for t in (0,5,10):
        print('t=',t,comparison(t=t))
    assert comparison(t=10)['position']==25
    assert comparison(t=10)['continued_position']==0
    assert comparison(t=10)['continued_distance']==50
    assert comparison(t=5)['acceleration'] is None
