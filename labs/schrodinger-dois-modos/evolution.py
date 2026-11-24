"""Solução espectral de dois modos do poço infinito; não é integrador de EDP."""
import cmath
import math

def finite(value,name):
    if isinstance(value,bool) or not isinstance(value,(int,float)):
        raise TypeError(name+': use int ou float')
    try:value=float(value)
    except OverflowError:raise ValueError(name+': fora de float') from None
    if not math.isfinite(value):raise ValueError(name+': deve ser finito')
    return value

def amplitudes(tau,shift=0):
    tau=finite(tau,'tau');shift=finite(shift,'shift')
    phases=[-(n*n+shift)*tau for n in (1,2)]
    if not all(math.isfinite(x) for x in phases):raise ValueError('Fase fora de float')
    return tuple(cmath.exp(1j*x)/math.sqrt(2) for x in phases)

def wave(s,tau,shift=0):
    s=finite(s,'s')
    if not 0<=s<=1:raise ValueError('s entre 0 e 1')
    c1,c2=amplitudes(tau,shift)
    return math.sqrt(2)*(c1*math.sin(math.pi*s)+c2*math.sin(2*math.pi*s))

def derivative_s(s,tau):
    s=finite(s,'s')
    if not 0<=s<=1:raise ValueError('s entre 0 e 1')
    c1,c2=amplitudes(tau)
    return math.sqrt(2)*math.pi*(c1*math.cos(math.pi*s)+2*c2*math.cos(2*math.pi*s))

def left_probability(tau):
    tau=finite(tau,'tau')
    angle=3*tau
    if not math.isfinite(angle):raise ValueError('Fase fora de float')
    return .5+4/(3*math.pi)*math.cos(angle)

def current_tau(s,tau):
    # J = j_phys*hbar/E1, para dP/dtau = J(esquerda)-J(direita).
    return 2/(math.pi**2)*(wave(s,tau).conjugate()*derivative_s(s,tau)).imag
