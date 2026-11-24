"""Mistura ideal gelo/água: g, °C, J; valores arredondados fixos.
Balanço de entalpia a pressão constante, sem ambiente/recipiente/outro trabalho.
"""
from fractions import Fraction as Q
from dataclasses import dataclass
CI=Q(21,10) # J/(g K)
CW=Q(21,5)
LF=Q(334) # J/g

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(v)

@dataclass(frozen=True)
class Equilibrium:
    state:str
    temperature:Q
    ice:Q
    liquid:Q
    thermal_reference:Q

def equilibrium(mi,ti,mw,tw):
    mi,ti,mw,tw=map(rational,(mi,ti,mw,tw))
    if mi<0 or mw<0 or mi+mw<=0:raise ValueError("Massas não negativas e total positivo.")
    if not -40<=ti<=0 or not 0<=tw<=90:raise ValueError("Domínio ideal: gelo −40..0°C, água 0..90°C.")
    mass=mi+mw
    h=mi*CI*ti+mw*(LF+CW*tw)
    if h<=0:return Equilibrium('gelo',h/(mass*CI),mass,Q(0),h)
    if h<mass*LF:
        liquid=h/LF
        return Equilibrium('mistura',Q(0),mass-liquid,liquid,h)
    return Equilibrium('agua',(h-mass*LF)/(mass*CW),Q(0),mass,h)

if __name__=='__main__':
    print(equilibrium(100,-10,200,40))
    print(equilibrium(100,-10,200,60))
    print(equilibrium(100,-20,10,5))
