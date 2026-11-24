"""Oráculo independente: séries de Taylor das EDOs polinomiais, Decimal 60."""
from decimal import Decimal as D,localcontext,ROUND_CEILING
import json


def reference(s0,enzyme,end,order=18):
    with localcontext() as ctx:
        ctx.prec=60;s0,enzyme,end=map(lambda x:D(str(x)),[s0,enzyme,end])
        n=max(1,int((end*(s0+enzyme+2)/D('.05')).to_integral_value(rounding=ROUND_CEILING)))
        h=end/n;y=[s0,D(0),D(0)]
        for _ in range(n):
            s=[y[0]];c=[y[1]];p=[y[2]]
            for j in range(order):
                association=enzyme*s[j]-sum(c[k]*s[j-k] for k in range(j+1))
                denominator=D(j+1)
                s.append((-association+c[j])/denominator)
                c.append((association-2*c[j])/denominator)
                p.append(c[j]/denominator)
            values=[]
            for coeff in [s,c,p]:
                value=coeff[-1]
                for term in reversed(coeff[:-1]):value=value*h+term
                values.append(value)
            y=values
        return [str(v) for v in y]


if __name__=='__main__':
    rows=[]
    for s,e in [(2,.02),(2,2),(.2,2)]:
        for t in [.5,1,2]:
            a=reference(s,e,t,18);b=reference(s,e,t,20)
            assert max(abs(D(x)-D(y)) for x,y in zip(a,b))<D('1e-30')
            rows.append(dict(s0=s,enzyme=e,time=t,state=a))
    print(json.dumps(rows,indent=2))
