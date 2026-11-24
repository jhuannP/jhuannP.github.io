"""Ajuste afim racional com intercepto, pesos iguais e um parâmetro livre no caso degenerado."""
from fractions import Fraction as Q

def scalar(v):
    if type(v) not in (int,Q):raise ValueError("Use int ou Fraction, sem bool")
    return Q(v)

def fit(xs,ys):
    if not isinstance(xs,(list,tuple)) or not isinstance(ys,(list,tuple)) or not xs or len(xs)!=len(ys):
        raise ValueError("Listas/tuplas não vazias de mesmo comprimento")
    x=tuple(map(scalar,xs));y=tuple(map(scalar,ys));n=len(x)
    xb=sum(x)/n;yb=sum(y)/n
    xx=sum((v-xb)**2 for v in x)
    if xx:
        slope=sum((u-xb)*(v-yb) for u,v in zip(x,y))/xx
        intercept=yb-slope*xb;rank=2;null_direction=None
    else:
        slope=Q(0);intercept=yb;rank=1;null_direction=(-xb,Q(1))
    fitted=tuple(intercept+slope*u for u in x)
    residual=tuple(p-v for p,v in zip(fitted,y))
    return dict(intercept=intercept,slope=slope,rank=rank,null_direction=null_direction,
                fitted=fitted,residual=residual,sse=sum(r*r for r in residual),
                normal_residual=(sum(residual),sum(u*r for u,r in zip(x,residual))))

if __name__=="__main__":
    r=fit((0,1,2),(1,2,2))
    assert r["intercept"]==Q(7,6) and r["slope"]==Q(1,2)
    assert r["sse"]==Q(1,6) and r["normal_residual"]==(0,0)
    print(r)
    print("Posto deficiente:",fit((1,1,1),(1,2,2)))
