"""Complexação ideal 1:1: intervalo racional para concentração de ML.
Totais em mmol/L; Kc em L/mmol. Não é modelo de metal específico.
"""
from fractions import Fraction as Q

def equilibrium(metal_total,ligand_total,kc,steps=80):
    vals=(metal_total,ligand_total,kc)
    if any(type(z) not in (int,Q) or z<0 for z in vals):
        raise ValueError("Totais e Kc devem ser inteiros ou Fraction não negativos.")
    if type(steps) is not int or not 1<=steps<=256:
        raise ValueError("Use de 1 a 256 passos.")
    a,b,k=map(Q,vals)
    lo,hi=Q(0),min(a,b)
    if k==0 or hi==0:hi=Q(0)
    def residual(x):return k*(a-x)*(b-x)-x
    for _ in range(steps):
        mid=(lo+hi)/2
        f=residual(mid)
        if f==0:
            lo=hi=mid
            break
        if f>0:lo=mid
        else:hi=mid
    x=(lo+hi)/2
    return dict(lower=lo,upper=hi,complex=x,metal_free=a-x,
                ligand_free=b-x,metal_total=a,ligand_total=b,kc=k,
                fraction=None if a==0 else x/a,residual=residual(x))

if __name__=="__main__":
    s=equilibrium(2,3,Q(1,2))
    print("ML, M livre, L livre em mmol/L:",float(s["complex"]),
          float(s["metal_free"]),float(s["ligand_free"]))
    print("Intervalo racional:",s["lower"],s["upper"])
