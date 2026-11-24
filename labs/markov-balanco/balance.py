"""Evolução e fluxos racionais; recebe P e candidata pi, não resolve pi."""
from fractions import Fraction as Q

def exact(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(v)

def matrix(P):
    P=tuple(tuple(exact(v) for v in row) for row in P);n=len(P)
    if not n or any(len(r)!=n or min(r)<0 or sum(r)!=1 for r in P):
        raise ValueError("Matriz estocástica quadrada não vazia necessária.")
    return P

def distribution(p,n):
    p=tuple(exact(v) for v in p)
    if len(p)!=n or min(p,default=Q(-1))<0 or sum(p)!=1:raise ValueError("Distribuição inválida.")
    return p

def step(p,P):
    P=matrix(P);p=distribution(p,len(P))
    return tuple(sum(p[i]*P[i][j] for i in range(len(P))) for j in range(len(P)))

def diagnose(P,pi):
    P=matrix(P);pi=distribution(pi,len(P));n=len(P)
    flux=tuple(tuple(pi[i]*P[i][j] for j in range(n)) for i in range(n))
    current=tuple(tuple(flux[i][j]-flux[j][i] for j in range(n)) for i in range(n))
    next_pi=step(pi,P)
    return dict(next=next_pi,stationary=next_pi==pi,
                detailed_balance=all(v==0 for row in current for v in row),flux=flux,current=current)

def evolve(p,P,steps):
    if isinstance(steps,bool) or not isinstance(steps,int) or not 0<=steps<=1000:raise ValueError("0 a1000passos necessários.")
    P=matrix(P);p=distribution(p,len(P));history=[p]
    for _ in range(steps):p=step(p,P);history.append(p)
    return tuple(history)
