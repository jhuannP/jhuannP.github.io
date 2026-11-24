"""Modelo orbital reduzido: -2Δ/5, +3Δ/5 e custo P por par. Não resolve spin."""
from fractions import Fraction as Q
from itertools import product

def scalar(x):
    if type(x) not in (int,Q):raise ValueError("Use int ou Fraction, sem bool")
    return Q(x)

def state(occupancy,delta,pair_cost):
    delta=scalar(delta);pair_cost=scalar(pair_cost)
    if delta<=0 or pair_cost<0:raise ValueError("Exija Δ>0 e P>=0")
    if type(occupancy) not in (list,tuple) or len(occupancy)!=5:
        raise ValueError("Forneça cinco ocupações na ordem t2g,t2g,t2g,eg,eg")
    if any(type(n) is not int or not 0<=n<=2 for n in occupancy):
        raise ValueError("Cada orbital admite 0,1 ou 2 elétrons")
    lower=sum(occupancy[:3]);upper=sum(occupancy[3:])
    pairs=sum(n==2 for n in occupancy);singles=sum(n==1 for n in occupancy)
    field=delta*Q(-2*lower+3*upper,5)
    return dict(occupancy=tuple(occupancy),electrons=lower+upper,lower=lower,upper=upper,
                pairs=pairs,singles=singles,field=field,total=field+pair_cost*pairs)

def d6_states(delta,pair_cost):
    # Validar mesmo antes da enumeração.
    state((2,2,2,0,0),delta,pair_cost)
    return [state(o,delta,pair_cost) for o in product(range(3),repeat=5) if sum(o)==6]

def minima(delta,pair_cost):
    rows=d6_states(delta,pair_cost)
    energy=min(r["total"] for r in rows)
    return [r for r in rows if r["total"]==energy]

if __name__=="__main__":
    for delta in (10,12,20):
        rows=minima(delta,12)
        print("Δ=",delta,"P=12; padrões mínimos:",len(rows),
              "classes (eg,pares,simples):",sorted({(r["upper"],r["pairs"],r["singles"]) for r in rows}),
              "energia:",rows[0]["total"])
    assert len(d6_states(10,12))==45
