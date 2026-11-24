"""Duas portas indutivas lineares, recíprocas e de geometria fixa."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use int/Fraction')
    return Q(x)

def coefficients(L1,L2,M):
    a,b,m=map(rational,(L1,L2,M))
    if not Q(1,1000)<=a<=1000 or not Q(1,1000)<=b<=1000 or m*m>a*b:
        raise ValueError('L1,L2 entre.001 e1000 H; M²<=L1*L2 necessário')
    return a,b,m

def pair(values,limit):
    values=list(values)
    if len(values)!=2:raise ValueError('Duas componentes necessárias')
    values=tuple(rational(x) for x in values)
    if any(abs(x)>limit for x in values):raise ValueError('Fora do limite didático')
    return values

def flux(L1,L2,M,currents):
    a,b,m=coefficients(L1,L2,M);i,j=pair(currents,100)
    return a*i+m*j,m*i+b*j

def energy(L1,L2,M,currents):
    a,b,m=coefficients(L1,L2,M);i,j=pair(currents,100)
    return a*i*i/2+b*j*j/2+m*i*j

def voltages(L1,L2,M,derivatives):
    a,b,m=coefficients(L1,L2,M);di,dj=pair(derivatives,1000)
    return a*di+m*dj,m*di+b*dj

if __name__=='__main__':
    print('U=',energy(4,9,3,[2,-1]),'J')
    print('Fluxos ligados=',flux(4,9,3,[2,-1]),'Wb')
    print('Tensões passivas=',voltages(4,9,3,[2,0]),'V')
    assert energy(4,9,3,[2,-1])==Q(13,2)
