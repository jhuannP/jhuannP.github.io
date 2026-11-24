"""Referência independente: bisseção Decimal 70 dígitos do balanço polinomial."""
from decimal import Decimal,localcontext
import json
from pathlib import Path


def root(delta,ratio):
    with localcontext() as ctx:
        ctx.prec=70
        K=Decimal(10)**Decimal(str(delta));r=Decimal(str(ratio));lo=Decimal(0);hi=min(Decimal(1),r)
        for _ in range(200):
            x=(lo+hi)/2
            if x*x>K*(1-x)*(r-x):hi=x
            else:lo=x
        return str((lo+hi)/2)


if __name__=='__main__':
    rows=[dict(delta=d,ratio=r,ueq=root(d,r)) for d in (-6,-2,0,2,6) for r in (.25,1,4)]
    Path(__file__).with_name('decimal_reference.json').write_text(json.dumps(rows,indent=2)+'\n')
