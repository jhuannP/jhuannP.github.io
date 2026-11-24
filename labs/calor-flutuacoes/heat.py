"""Ensemble canônico finito,Theta=kB*T na mesma unidade de energia dos níveis."""
from math import fsum,log,exp,isfinite

def real(x):
    if isinstance(x,bool):raise ValueError('Real finito necessário')
    try:x=float(x)
    except (TypeError,ValueError,OverflowError):raise ValueError('Real finito necessário') from None
    if not isfinite(x) or abs(x)>1e4:raise ValueError('Módulo limitado a 1e4')
    return x

def canonical(energies,theta,degeneracies=None):
    E=tuple(map(real,energies));theta=real(theta)
    if not 1<=len(E)<=30 or theta<1e-4:raise ValueError('De 1 a 30 níveis e Theta entre 1e-4 e 1e4')
    g=(1,)*len(E) if degeneracies is None else tuple(degeneracies)
    if len(g)!=len(E) or any(type(v) is not int or not 1<=v<=1000 for v in g):raise ValueError('Degenerescências de 1 a 1000')
    base=min(E);gap=tuple(e-base for e in E)
    logw=tuple(log(d)-e/theta for d,e in zip(g,gap));top=max(logw)
    weights=tuple(exp(v-top) for v in logw);total=fsum(weights);p=tuple(v/total for v in weights)
    u=fsum(v*e for v,e in zip(p,gap));variance=fsum(v*(e-u)**2 for v,e in zip(p,gap))
    return dict(probabilities=p,U=base+u,variance=variance,C_over_kB=variance/theta**2)

if __name__=='__main__':
    print(canonical([0,1],1/log(3),[1,3]))
