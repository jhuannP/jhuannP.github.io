"""Rede resistiva fixa com duas fontes ideais referidas ao nó zero. Unidades SI."""
from fractions import Fraction as Q

def solve(e1,e2,r1,r2,r3):
    values=(e1,e2,r1,r2,r3)
    if any(type(x) not in (int,Q) for x in values):
        raise ValueError("Use inteiros ou Fraction")
    e1,e2,r1,r2,r3=map(Q,values)
    if min(r1,r2,r3)<=0:
        raise ValueError("As três resistências devem ser positivas")
    u=(e1/r1+e2/r2)/(1/r1+1/r2+1/r3)
    i1=(e1-u)/r1; i2=(e2-u)/r2; i3=u/r3
    dissipated=(r1*i1*i1,r2*i2*i2,r3*i3*i3)
    delivered=(e1*i1,e2*i2)
    return dict(u=u,i1=i1,i2=i2,i3=i3,dissipated=dissipated,delivered=delivered)

if __name__ == "__main__":
    result=solve(12,6,2,3,6)
    for key,value in result.items():print(key,value)
    assert result['i1']+result['i2']==result['i3']
    assert sum(result['delivered'])==sum(result['dissipated'])==20
