"""LayerNorm vetorial original; forward e produto vetor-Jacobiano."""
from math import sqrt,fsum,isfinite

def real(v):
    if isinstance(v,bool):raise ValueError('Real finito necessário')
    try:v=float(v)
    except (ValueError,TypeError,OverflowError):raise ValueError('Real finito necessário') from None
    if not isfinite(v) or abs(v)>1e6:raise ValueError('Módulo limitado a 1e6')
    return v

def vector(v,n=None):
    v=tuple(map(real,v))
    if not 1<=len(v)<=100 or (n is not None and len(v)!=n):raise ValueError('Forma vetorial incompatível')
    return v

def forward(x,eps=1e-5,gamma=None,beta=None):
    x=vector(x);n=len(x);eps=real(eps)
    if eps<1e-12:raise ValueError('Epsilon pelo menos 1e-12')
    gamma=(1.0,)*n if gamma is None else vector(gamma,n)
    beta=(0.0,)*n if beta is None else vector(beta,n)
    mean=fsum(x)/n;c=tuple(v-mean for v in x);var=fsum(v*v for v in c)/n;s=sqrt(var+eps)
    z=tuple(v/s for v in c);y=tuple(g*v+b for g,v,b in zip(gamma,z,beta))
    return dict(mean=mean,var=var,s=s,c=c,z=z,y=y,gamma=gamma)

def backward(x,upstream,eps=1e-5,gamma=None):
    state=forward(x,eps,gamma);n=len(state['z']);u=vector(upstream,n)
    q=tuple(a*g for a,g in zip(u,state['gamma']));avg=fsum(q)/n
    cross=fsum(a*c for a,c in zip(q,state['c']))/n;s=state['s']
    dx=tuple((a-avg)/s-c*cross/s**3 for a,c in zip(q,state['c']))
    return dict(dx=dx,dgamma=tuple(a*z for a,z in zip(u,state['z'])),dbeta=u)

if __name__=='__main__':
    print(forward([1,3],3,gamma=[2,4],beta=[1,0]))
    print(backward([1,3],[1,0],3))
