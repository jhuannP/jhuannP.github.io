"""Bloco já deslizando à direita; forças constantes, até a primeira parada."""
from fractions import Fraction as Q
from math import sqrt

def inspect(m=2,v0=3,force=2,friction=5,distance=2):
    values=(m,v0,force,friction,distance)
    limits=((1,4),(1,6),(0,8),(0,8),(0,12))
    if any(isinstance(x,bool) or not isinstance(x,int) or not lo<=x<=hi for x,(lo,hi) in zip(values,limits)):
        raise ValueError('Use inteiros nos limites: massa1..4, v0 1..6, forças0..8, distância0..12')
    k0=Q(m*v0*v0,2);net=force-friction
    stop=k0/(-net) if net<0 else None
    reachable=k0+net*distance>=0
    end=min(Q(distance),stop) if stop is not None else Q(distance)
    k=k0+net*end
    return dict(k0=k0,net=net,stop=stop,reachable=reachable,
                query_k=k0+net*distance if reachable else None,
                end=end,k=k,speed=sqrt(2*k/m),
                applied=force*end,friction_work=-friction*end,net_work=net*end,
                internal=friction*end)

if __name__=='__main__':
    r=inspect()
    assert r['k0']==9 and r['k']==3 and r['net_work']==-6
    assert r['applied']==4 and r['friction_work']==-10
    print(r)
