"""Dois canais irreversíveis sintéticos; base mantida constante externamente.
kE,kS: L/(mol s), base/substrato/produtos: mol/L, tempo:s.
Não prediz reatividade, produtos ou seletividade de substâncias reais.
"""
from math import expm1,isfinite

def real(x):
    if isinstance(x,bool):raise ValueError("Real finito necessário.")
    try:x=float(x)
    except (TypeError,ValueError,OverflowError):raise ValueError("Real finito necessário.") from None
    if not isfinite(x):raise ValueError("Real finito necessário.")
    return x

def state(k_e,k_s,base,s0,t):
    k_e,k_s,base,s0,t=map(real,(k_e,k_s,base,s0,t))
    if min(k_e,k_s,base,s0,t)<0:raise ValueError("Parâmetros não negativos necessários.")
    total=real(k_e+k_s);rate=real(total*base)
    if total==0 or rate==0:
        return dict(substrate=s0,elimination=0.,substitution=0.,rate_e=0.,rate_s=0.,fraction_e=None,decay_rate=rate)
    fraction=k_e/total
    consumed=real(s0*(-expm1(-rate*t)))
    remaining=real(s0-consumed)
    return dict(substrate=remaining,elimination=real(fraction*consumed),
                substitution=real((1-fraction)*consumed),rate_e=real(k_e*base*remaining),
                rate_s=real(k_s*base*remaining),fraction_e=fraction,decay_rate=rate)

if __name__=='__main__':
    from math import log
    print(state(.2,.8,.5,.1,log(2)/.5))
