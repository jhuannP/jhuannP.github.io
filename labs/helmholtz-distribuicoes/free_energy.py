"""Modelo finito de microestados; theta=kB*T_fisica em unidades de energia."""
from math import exp, log, isfinite

def number(x):
    if isinstance(x, (bool, str, bytes)):
        raise ValueError('Número real finito necessário')
    try:
        y=float(x)
    except (TypeError, ValueError, OverflowError):
        raise ValueError('Número real finito necessário') from None
    if not isfinite(y):
        raise ValueError('Número real finito necessário')
    return y

def compare(energies, theta, distribution):
    """Uma entrada por microestado. Não inclui multiplicidades implícitas."""
    E=[number(x) for x in energies]; t=number(theta)
    q=[number(x) for x in distribution]
    if not 2<=len(E)<=12 or any(abs(e)>10 for e in E) or not .1<=t<=10:
        raise ValueError('Limites didáticos: 2..12 estados, |E|<=10, .1<=theta<=10')
    if len(q)!=len(E) or any(x<0 or x>1 for x in q) or abs(sum(q)-1)>1e-12:
        raise ValueError('Distribuição normalizada sobre os mesmos estados necessária')
    base=min(E); logits=[-(e-base)/t for e in E]
    z=sum(exp(x) for x in logits); logz=log(z)
    logp=[x-logz for x in logits]; p=[exp(x) for x in logp]
    H=-sum(x*log(x) for x in q if x>0)
    U=sum(x*e for x,e in zip(q,E)); trial=U-t*H
    equilibrium=base-t*logz
    kl=sum(x*(log(x)-lp) for x,lp in zip(q,logp) if x>0)
    return dict(p=p,U=U,H=H,trial=trial,equilibrium=equilibrium,
                gap=trial-equilibrium,kl=kl)

if __name__=='__main__':
    t=1/log(2)
    for q in ([.5,.25,.25],[.5,.5,0],[1/3]*3):
        r=compare([0,1,1],t,q)
        print('q=',q,'U=',r['U'],'beta*F=',r['trial']/t,'KL=',r['kl'])
        assert abs(r['gap']-t*r['kl'])<1e-12
