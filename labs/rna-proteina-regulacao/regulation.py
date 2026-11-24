"""Balanço médio sintético de RNA e proteína, não modelo molecular de RISC.
M: uR; P: uP; alfa:uR/h, delta,gamma:h^-1, beta:uP/(uR h).
"""
from fractions import Fraction as Q
from math import exp,isfinite

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError("Use int/Fraction.")
    return Q(x)

def stationary(alpha,delta,beta,gamma):
    alpha,delta,beta,gamma=map(rational,(alpha,delta,beta,gamma))
    if min(alpha,beta)<0 or min(delta,gamma)<=0:raise ValueError("Produções>=0; perdas>0.")
    m=alpha/delta;p=beta*m/gamma
    return dict(rna=m,protein=p,protein_per_rna=beta/gamma)

def compare(reference,condition):
    def checked(r):
        if not isinstance(r,dict) or set(r)!={'rna','protein','protein_per_rna'}:raise ValueError("Registro estacionário necessário.")
        out={k:rational(v) for k,v in r.items()}
        if min(out.values())<0:raise ValueError("Valores não negativos necessários.")
        if out['protein']!=out['rna']*out['protein_per_rna']:raise ValueError("Registro inconsistente.")
        return out
    ref=checked(reference);cond=checked(condition)
    if min(ref.values())<=0:raise ValueError("Referência positiva necessária para razões.")
    if cond['rna']<=0:raise ValueError("RNA da condição deve ser positivo para comparar P/M.")
    return {key:cond[key]/ref[key] for key in ref}

def protein_clamp(m,beta,gamma,p0,t):
    # M mantido constante externamente: não resolve o sistema acoplado geral.
    values=(m,beta,gamma,p0,t)
    if any(isinstance(x,bool) for x in values):raise ValueError("Reais finitos necessários.")
    try:m,beta,gamma,p0,t=map(float,values)
    except (TypeError,ValueError,OverflowError):raise ValueError("Reais finitos necessários.") from None
    if not all(isfinite(x) for x in (m,beta,gamma,p0,t)) or min(m,beta,p0,t)<0 or gamma<=0:raise ValueError("Contrato fora do domínio.")
    target=beta*m/gamma
    if not isfinite(target):raise ValueError("Estado não resolvido em float.")
    w=exp(-gamma*t);p=w*p0+(1-w)*target
    if not isfinite(p):raise ValueError("Estado não resolvido em float.")
    return p

if __name__=='__main__':
    base=stationary(10,1,2,Q(1,2))
    translation=stationary(10,2,1,Q(1,2))
    protein_loss=stationary(10,2,2,1)
    print(base,translation,protein_loss)
    print(compare(base,translation));print(compare(base,protein_loss))
