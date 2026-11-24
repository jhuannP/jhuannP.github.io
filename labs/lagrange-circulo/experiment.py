"""Extremos de p*x+q*y no círculo de raio R: família analítica restrita."""
from math import hypot,isfinite

def extrema(p,q,radius,scale=1):
    if any(type(z) not in (int,float) or not isfinite(z) for z in (p,q,radius,scale)):
        raise ValueError("Use números reais finitos, sem bool.")
    if radius<0 or scale==0:
        raise ValueError("Raio não negativo; escala da restrição não nula.")
    s=hypot(p,q)
    if radius==0:
        point=dict(x=0.,y=0.,value=0.,multiplier=None)
        return dict(regular=False,all_points=True,minimum=point.copy(),maximum=point.copy())
    if s==0:
        return dict(regular=True,all_points=True,minimum=None,maximum=None)
    x,y=radius*(p/s),radius*(q/s)
    value=radius*s
    lam=(s/radius/2)/scale
    if lam==0 or not all(isfinite(z) for z in (x,y,value,lam)):
        raise ValueError("Escala numérica não representável.")
    maximum=dict(x=x,y=y,value=value,multiplier=lam)
    minimum={key:-v for key,v in maximum.items()}
    return dict(regular=True,all_points=False,minimum=minimum,maximum=maximum)

if __name__=="__main__":
    print(extrema(3,4,2))
