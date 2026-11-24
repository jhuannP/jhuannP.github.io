"""Oscilador normalizado,aritimética racional; não é solver geral."""
from fractions import Fraction as Q

def _q(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use inteiro ou Fraction.')
    return Q(x)

def trace(q=Q(1),p=Q(0),eta=Q(1),n=6):
    q,p,eta=map(_q,(q,p,eta))
    if not 0<eta<=3:raise ValueError('Passo normalizado em(0,3].')
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=200:raise ValueError('Passos0–200.')
    out=[(q,p)]
    for _ in range(n):
        p=p-eta*q;q=q+eta*p;out.append((q,p))
    return out

def energy(q,p):
    q,p=map(_q,(q,p));return (q*q+p*p)/2

def invariant(q,p,eta):
    q,p,eta=map(_q,(q,p,eta));return (q*q+p*p-eta*q*p)/2

if __name__=='__main__':
    for eta in [Q(1),Q(2)]:
        print('eta:',eta)
        for i,(q,p) in enumerate(trace(eta=eta,n=6)):
            print(i,q,p,'E:',energy(q,p),'I:',invariant(q,p,eta))
