"""Modelo sintético a T,P fixos: n em mol,V em cm³ e volumes molares em cm³/mol."""
from fractions import Fraction as Q


def amount(v):
    if type(v) not in (int,Q) or v<0:raise ValueError('Use int/Fraction não negativo.')
    return Q(v)


def state(nA,nB):
    a,b=map(amount,(nA,nB));N=a+b
    if not N:raise ValueError('Quantidade total positiva.')
    xA,xB=a/N,b/N
    ideal=100*a+60*b;excess=-4*a*b/N
    partialA=100-4*xB*xB;partialB=60-4*xA*xA
    return dict(nA=a,nB=b,total=N,xA=xA,xB=xB,V=ideal+excess,ideal=ideal,excess=excess,
                molar=(ideal+excess)/N,partialA=partialA,partialB=partialB,
                dpartialA_dxB=-8*xB,dpartialB_dxB=8*xA)


def add_B(nA,nB,delta):
    delta=amount(delta);a=state(nA,nB);b=state(a['nA'],a['nB']+delta)
    actual=b['V']-a['V'];linear=a['partialB']*delta
    return dict(actual=actual,linear=linear,remainder=actual-linear,final=b)


if __name__=='__main__':
    print('Mistura inicial:',state(3,1))
    print('Adicionar 1/2 mol de B:',add_B(3,1,Q(1,2)))
    print('Modelo original prescrito; não é medição de uma mistura real ou regra de fases.')
