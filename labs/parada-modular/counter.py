"""Decisão apenas para x <- (x+d) mod m, com parada em zero."""
from dataclasses import dataclass
from math import gcd

@dataclass(frozen=True)
class Result:
    status: str
    steps: int | None
    cycle_length: int | None
    divisor: int

def classify(initial,increment,modulus):
    if any(type(v) is not int for v in (initial,increment,modulus)):
        raise TypeError('Entradas inteiras, sem bool')
    if modulus<1 or not (0<=initial<modulus and 0<=increment<modulus):
        raise ValueError('m>=1; x,d em range(m)')
    g=gcd(increment,modulus)
    if initial==0:return Result('parada',0,None,g)
    if initial%g:return Result('ciclo',None,modulus//g,g)
    reduced=modulus//g
    # initial!=0 e divisível por g garante reduced>1.
    steps=(-(initial//g)*pow(increment//g,-1,reduced))%reduced
    return Result('parada',steps,None,g)
