"""FTCS racional, Dirichlet zero, malha uniforme; sem solver geral."""
from fractions import Fraction as F

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):raise ValueError("int ou Fraction necessários")
    return F(x)

def grid(u):
    u=tuple(map(rational,u))
    if not 3<=len(u)<=33 or u[0]!=0 or u[-1]!=0:raise ValueError("3 a33 pontos,bordas zero")
    return u

def update(u,r):
    return (F(0),)+tuple((1-2*r)*u[i]+r*(u[i-1]+u[i+1]) for i in range(1,len(u)-1))+(F(0),)

def evolve(u,r,steps):
    u=grid(u);r=rational(r)
    if not 0<=r<=F(1,2):raise ValueError("evolução aceita requer 0<=r<=1/2")
    if type(steps) is not int or not 0<=steps<=200:raise ValueError("0 a200 passos")
    history=[u]
    for _ in range(steps):u=update(u,r);history.append(u)
    return tuple(history)

def diagnostic_step(u,r):
    """Só um passo para demonstrar perda de propriedades; não é evolução aceita."""
    u=grid(u);r=rational(r)
    if not F(1,2)<r<=1:raise ValueError("diagnóstico restrito a1/2<r<=1")
    return update(u,r)

if __name__=='__main__':
    u=(0,1,0,1,0)
    print('r=1/4:',evolve(u,F(1,4),1)[-1])
    print('diagnóstico r=3/5:',diagnostic_step(u,F(3,5)))
    print('modo j=2, quatro passos:',evolve((0,1,0,-1,0),F(1,4),4)[-1])
