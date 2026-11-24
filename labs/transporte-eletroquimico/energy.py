"""Thermodynamic differences for prescribed ideal reservoirs; no rate model."""
from math import isfinite, log

def _finite(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x):
        raise ValueError('use finite real numbers')
    return float(x)

def affinity(inside, outside, z=0, psi=0):
    """Delta mu/(RT), outside -> inside; psi=F*(V_in-V_out)/(RT)."""
    inside, outside, psi = map(_finite, (inside, outside, psi))
    if inside <= 0 or outside <= 0 or isinstance(z, bool) or not isinstance(z, int) or abs(z)>8:
        raise ValueError('positive concentrations and integer charge |z|<=8')
    # Difference of logs avoids overflow/underflow of a concentration ratio.
    return log(inside)-log(outside)+z*psi

def coupled(target, driver, copies):
    """Energy per target cycle divided by RT; copies positive integer."""
    target, driver = map(_finite,(target,driver))
    if isinstance(copies,bool) or not isinstance(copies,int) or not 1<=copies<=100:
        raise ValueError('copies must be an integer in 1..100')
    result=target+copies*driver
    if not isfinite(result): raise ValueError('energy overflow')
    return result

if __name__=='__main__':
    ln2=log(2)
    for z,psi in [(1,-log(16)),(-1,-log(16)),(1,-log(8))]:
        print('z, energia/(RT ln2):',z,round(affinity(8,1,z,psi)/ln2,12))
    for n in (2,3):
        print('ions/ciclo, energia/(RT ln2):',n,round(coupled(2*ln2,-ln2,n)/ln2,12))
