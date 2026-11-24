"""Diferenças centrais para função escalar real determinística; sem framework."""
from math import isfinite

def real(v):
    if isinstance(v,bool):raise ValueError("Real finito necessário.")
    try:out=float(v)
    except (TypeError,ValueError,OverflowError):raise ValueError("Real finito necessário.") from None
    if not isfinite(out):raise ValueError("Real finito necessário.")
    return out

def vector(theta):
    theta=tuple(real(v) for v in theta)
    if not theta:raise ValueError("Vetor não vazio necessário.")
    return theta

def stencil(loss,theta,direction,h):
    h=real(h)
    if h<=0:raise ValueError("Passo positivo necessário.")
    plus=tuple(real(t+h*v) for t,v in zip(theta,direction))
    minus=tuple(real(t-h*v) for t,v in zip(theta,direction))
    if all(v==0 for v in direction):raise ValueError("Direção não nula necessária.")
    if any(v!=0 and (p==t or m==t) for t,v,p,m in zip(theta,direction,plus,minus)):
        raise ArithmeticError("Perturbação não representável nesta escala.")
    return real((real(loss(plus))-real(loss(minus)))/real(2*h))

def central(loss,theta,h):
    theta=vector(theta);n=len(theta)
    return tuple(stencil(loss,theta,tuple(float(i==j) for j in range(n)),h) for i in range(n))

def directional(loss,theta,direction,h):
    theta=vector(theta);direction=vector(direction)
    if len(theta)!=len(direction):raise ValueError("Dimensões incompatíveis.")
    return stencil(loss,theta,direction,h)

def compare(loss,theta,gradient,h=1e-5,atol=1e-8,rtol=1e-5):
    theta=vector(theta);gradient=vector(gradient);atol,rtol=real(atol),real(rtol)
    if len(theta)!=len(gradient) or min(atol,rtol)<0:raise ValueError("Contrato de comparação inválido.")
    numeric=central(loss,theta,h);out=[]
    for i,(a,n) in enumerate(zip(gradient,numeric)):
        error=real(abs(a-n));bound=real(atol+rtol*max(abs(a),abs(n)))
        out.append(dict(index=i,analytic=a,numeric=n,error=error,bound=bound,passed=error<=bound))
    return out
