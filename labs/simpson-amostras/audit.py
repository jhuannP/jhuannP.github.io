"""Auditoria racional de um painel Simpson para polinômios, não integrador genérico."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction.')
    return Q(x)


def polynomial(coeff):
    c=tuple(map(rational,coeff))
    if not 1<=len(c)<=21:raise ValueError('1..21 coeficientes, ordem crescente.')
    return c


def value(coeff,x):
    x=rational(x);out=Q(0)
    for a in reversed(coeff):out=out*x+a
    return out


def product(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return tuple(out)


def hidden():
    q=(Q(1),)
    for r in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
        q=product(q,(-r,Q(1)))
    # Exact integral of q² is 5/1419264; normalization gives integral1.
    return tuple(c*Q(1419264,5) for c in product(q,q))


def compare(coeff,a=0,b=1):
    coeff=polynomial(coeff);a,b=map(rational,(a,b))
    if not a<b:raise ValueError('Intervalo crescente.')
    cache={}
    def f(x):
        if x not in cache:cache[x]=value(coeff,x)
        return cache[x]
    def simpson(lo,hi):
        return (hi-lo)*(f(lo)+4*f((lo+hi)/2)+f(hi))/6
    coarse=simpson(a,b);m=(a+b)/2
    fine=simpson(a,m)+simpson(m,b);delta=fine-coarse
    corrected=fine+delta/15
    exact=sum(c*(b**(i+1)-a**(i+1))/(i+1) for i,c in enumerate(coeff))
    return dict(coarse=coarse,fine=fine,indicator=abs(delta)/15,
                corrected=corrected,exact=exact,true_error=abs(corrected-exact),
                evaluations=len(cache))


if __name__=='__main__':
    for name,coeff in (('x4',(0,0,0,0,1)),('oculto',hidden())):
        print(name,compare(coeff))
    print('Integral exata só disponível porque o laboratório conhece o polinômio.')
