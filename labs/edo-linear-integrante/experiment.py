"""Família racional y'+(m/t)y=q(t), em uma semirreta sem zero."""
from dataclasses import dataclass
from fractions import Fraction as Q

def scalar(x):
    if type(x) not in (int,Q):raise ValueError("Use int ou Fraction, sem bool")
    return Q(x)

@dataclass(frozen=True)
class Solution:
    m: int
    q: tuple
    t0: Q
    y0: Q
    constant: Q
    particular: tuple

    def argument(self,t):
        t=scalar(t)
        if t*self.t0<=0:raise ValueError("Use a mesma semirreta do ponto inicial, sem zero")
        return t

    def value(self,t):
        t=self.argument(t)
        return sum((a*t**(j+1) for j,a in enumerate(self.particular)),Q(0))+self.constant*t**(-self.m)

    def derivative(self,t):
        t=self.argument(t)
        return sum(((j+1)*a*t**j for j,a in enumerate(self.particular)),Q(0))-self.m*self.constant*t**(-self.m-1)

    def forcing(self,t):
        t=self.argument(t)
        return sum((a*t**j for j,a in enumerate(self.q)),Q(0))

def solve(m,q,t0,y0):
    if type(m) is not int or m<1:raise ValueError("m deve ser inteiro positivo")
    if not isinstance(q,(list,tuple)) or not q:raise ValueError("Polinômio não vazio")
    q=tuple(scalar(a) for a in q);t0=scalar(t0);y0=scalar(y0)
    if t0==0:raise ValueError("A equação não está definida em zero")
    particular=tuple(a/Q(m+j+1) for j,a in enumerate(q))
    yp0=sum((a*t0**(j+1) for j,a in enumerate(particular)),Q(0))
    constant=(y0-yp0)*t0**m
    return Solution(m,q,t0,y0,constant,particular)

if __name__=="__main__":
    s=solve(2,[3],1,2)
    assert s.constant==1 and s.value(2)==Q(9,4)
    for t in (Q(1,2),1,2,3):
        assert s.derivative(t)+Q(2,t)*s.value(t)==3
        print(t,s.value(t),s.derivative(t))
