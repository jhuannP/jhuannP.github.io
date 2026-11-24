"""Potencial de par LJ12-6 sem corte; variáveis reduzidas, não material real."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use int/Fraction')
    return Q(x)

def reduced(q):
    """q=(sigma/r)^6. Retorna U/epsilon e r*F_r/epsilon, NÃO F_r isolado."""
    q=rational(q)
    if not Q(1,4096)<=q<=64:raise ValueError('q entre1/4096 e64 necessário')
    return dict(energy=4*q*(q-1),rforce=24*q*(2*q-1))

def at_distance(x):
    """x=r/sigma. Retorna U/epsilon e F_r*sigma/epsilon."""
    x=rational(x)
    if not Q(1,2)<=x<=4:raise ValueError('.5<=r/sigma<=4 necessário')
    z=reduced(1/x**6)
    return dict(energy=z['energy'],force=z['rforce']/x)

if __name__=='__main__':
    for q in (Q(1),Q(1,2),Q(1,4)):
        print('q=',q,reduced(q))
    assert reduced(Q(1,2))==dict(energy=-1,rforce=0)
    assert at_distance(1)==dict(energy=0,force=24)
