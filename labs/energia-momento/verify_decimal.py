"""Cinética de partícula por gamma-1 em Decimal 70 dígitos, sem racionalização."""
from decimal import Decimal,localcontext
from pathlib import Path
import json


def reference(beta):
    with localcontext() as ctx:
        ctx.prec=70
        b=Decimal(str(beta));g=1/(1-b*b).sqrt()
        return dict(beta=beta,energy=str(g),momentum=str(g*b),kinetic=str(g-1))


if __name__=='__main__':
    Path(__file__).with_name('decimal_reference.json').write_text(json.dumps([reference(b) for b in (0,1e-9,1e-6,.01,.1,.6,.95)],indent=2)+'\n')
