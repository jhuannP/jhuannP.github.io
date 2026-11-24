"""Duas cargas fixas: +1 nC em -1 m, s*1 nC em +1 m; k=9e9 SI."""
from fractions import Fraction as F

def axial(x=0,s=-1):
    if type(x) not in (int,F) or type(s) is not int or s not in (-1,1):
        raise ValueError("Use x int/Fraction e sinal s=-1 ou +1")
    x=F(x);fields=[];potentials=[]
    for position,sign in ((-1,1),(1,s)):
        displacement=x-position;distance=abs(displacement)
        if not distance:fields.append(None);potentials.append(None)
        else:
            fields.append(9*sign*displacement/distance**3)
            potentials.append(9*sign/distance)
    singular=any(v is None for v in fields)
    return dict(x=x,s=s,fields=fields,potentials=potentials,
                field=None if singular else sum(fields,F(0)),
                potential=None if singular else sum(potentials,F(0)),singular=singular)

if __name__=='__main__':
    for s in (-1,1):
        for x in (0,1,2):print(axial(x,s))
