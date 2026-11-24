"""Modelo didático de MRU; metros e segundos, sem dados medidos."""
from fractions import Fraction as Q
import math

def rational(value):
    if not math.isfinite(float(value)): raise ValueError('Valor deve ser finito')
    return Q(str(value))

def kmh_to_ms(value): return rational(value)*Q(5,18)

def motion(x0, velocity, t, t0=0):
    x0,velocity,t,t0=map(rational,(x0,velocity,t,t0))
    dt=t-t0
    if dt<0: raise ValueError('Este roteiro exige t >= t0')
    displacement=velocity*dt
    return {'position':x0+displacement,'displacement':displacement,'distance':abs(velocity)*dt,'elapsed':dt}

if __name__=='__main__':
    print(motion(30,kmh_to_ms('-7.2'),9,4))
