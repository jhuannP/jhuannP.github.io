"""Inventário idealizado de uma cadeia saturada par, sem inferência fisiológica."""
from fractions import Fraction as F

def inventory(n):
    if type(n) is not int or not 4<=n<=40 or n%2:
        raise ValueError("n par entre 4 e 40")
    remaining,acetyl,cycles,trace=n,0,0,[]
    while remaining:
        released=2 if remaining==4 else 1
        remaining-=2*released;acetyl+=released;cycles+=1
        trace.append(dict(cycle=cycles,remaining=remaining,acetyl=acetyl,released=released))
    return dict(carbons=n,cycles=cycles,acetyl=acetyl,beta_nadh=cycles,
                beta_etf_pairs=cycles,total_nadh=cycles+3*acetyl,
                total_q_pairs=cycles+acetyl,gtp=acetyl,trace=trace)

def atp_equivalents(n,p_nadh=F(5,2),p_q=F(3,2),free_acid=True):
    if type(free_acid) is not bool:raise ValueError("free_acid booleano")
    if any(not isinstance(x,F) or x<0 for x in (p_nadh,p_q)):
        raise ValueError("rendimentos racionais não negativos")
    v=inventory(n)
    gross=v['total_nadh']*p_nadh+v['total_q_pairs']*p_q+v['gtp']
    cost=2 if free_acid else 0
    return dict(gross=gross,activation=cost,net=gross-cost)

if __name__=='__main__':
    v=inventory(14)
    print({k:x for k,x in v.items() if k!='trace'})
    for row in v['trace']:print(row)
    print('ácido livre:',atp_equivalents(14))
    print('acil-CoA já ativado:',atp_equivalents(14,free_acid=False))
