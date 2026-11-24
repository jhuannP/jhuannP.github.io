"""A(g) <-> 2 B(g), gás ideal a T e P controladas; x é fração dissociada."""
from fractions import Fraction as Q

def scalar(x):
    if type(x) not in (int,Q):raise ValueError("Use int/Fraction, sem bool")
    return Q(x)

def state(x,r):
    x,r=map(scalar,(x,r))
    if not 0<=x<1 or r<=0:raise ValueError("0<=x<1 e r=P/p_padrao positivo")
    nA=1-x;nB=2*x;total=nA+nB
    yA=nA/total;yB=nB/total
    aA=yA*r;aB=yB*r
    return dict(nA=nA,nB=nB,total=total,yA=yA,yB=yB,aA=aA,aB=aB,Q=aB*aB/aA)

def equilibrium_square(K,r):
    K,r=map(scalar,(K,r))
    if K<=0 or r<=0:raise ValueError("K e r positivos")
    return K/(K+4*r)

if __name__=="__main__":
    s=state(Q(1,2),1)
    assert s["Q"]==Q(4,3)
    assert equilibrium_square(Q(4,3),1)==Q(1,4)
    assert equilibrium_square(Q(4,3),4)==Q(1,13)
    print("x=1/2, P=p°:",s)
    print("Equilíbrio em P=4p°: x² =",equilibrium_square(Q(4,3),4))
