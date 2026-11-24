"""Bisseção independente da norma do elétron, usando cossenos exatos selecionados."""
from decimal import Decimal,localcontext
from pathlib import Path
import json


def reference(alpha,angle,cosine):
    with localcontext() as ctx:
        ctx.prec=80
        a=Decimal(str(alpha));c=Decimal(str(cosine));lo=Decimal(0);hi=a
        def residual(q):return (1+a-q)**2-(a*a+q*q-2*a*q*c)-1
        if residual(hi)==0:q=hi
        else:
            for _ in range(230):
                mid=(lo+hi)/2
                if residual(mid)>0:lo=mid
                else:hi=mid
            q=(lo+hi)/2
        return dict(alpha=alpha,angle=angle,scattered=str(q),kinetic=str(a-q))


if __name__=='__main__':
    rows=[reference(a,t,c) for a in (.1,.5,1,2) for t,c in ((0,1),(60,.5),(90,0),(120,-.5),(180,-1))]
    Path(__file__).with_name('decimal_reference.json').write_text(json.dumps(rows,indent=2)+'\n')
