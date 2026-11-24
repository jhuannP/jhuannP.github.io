"""Ordens aparentes0,1,2;concentrações normalizadas com mesma velocidade inicial."""
from math import exp,log,isfinite

def inspect(u=1):
    if isinstance(u,bool) or not isinstance(u,(int,float)) or not isfinite(u) or not 0<=u<=3:
        raise ValueError('u finito em[0,3]')
    concentrations=[max(1-u,0),exp(-u),1/(1+u)]
    rates=[1 if u<1 else None if u==1 else 0,concentrations[1],concentrations[2]**2]
    return dict(concentrations=concentrations,products=[1-a for a in concentrations],rates=rates,
                half_times=[.5,log(2),1])

def half_life(order,A0,k):
    if isinstance(order,bool) or not isinstance(order,int) or order not in (0,1,2):
        raise ValueError('Ordem0,1 ou2')
    if any(isinstance(v,bool) or not isinstance(v,(int,float)) or not isfinite(v) or v<=0 for v in (A0,k)):
        raise ValueError('A0 e k positivos e finitos')
    return A0/(2*k) if order==0 else log(2)/k if order==1 else 1/(k*A0)

if __name__=='__main__':
    z=inspect(1)
    assert z['concentrations'][0]==0 and z['concentrations'][2]==.5
    assert z['rates'][0] is None # quina do modelo por partes na exaustão
    print(z)
