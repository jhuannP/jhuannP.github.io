"""PVI adimensional y'=-y,y(0)=1,T=1; Euler racional e referência Decimal."""
from fractions import Fraction as Q
from decimal import Decimal,localcontext
from math import log2


def count(n):
    if type(n) is not int or not 1<=n<=4096:raise ValueError('n inteiro entre1 e4096.')
    return n


def euler(n):
    n=count(n);return (1-Q(1,n))**n


def decimal(x):return Decimal(x.numerator)/Decimal(x.denominator)


def differences(coarse,fine,finer):
    if any(type(x) not in (int,Q) for x in (coarse,fine,finer)):
        raise ValueError('Use int/Fraction, sem bool/float.')
    c,f,g=map(Q,(coarse,fine,finer));d0=f-c;d1=g-f
    # Ordem não interpretada quando as diferenças são zero ou mudam de sinal.
    p=log2(float(abs(d0/d1))) if d0*d1>0 else None
    return dict(coarse_change=d0,fine_change=d1,observed_order=p,
                fine_error_estimate_order1=abs(d0),richardson_order1=2*f-c)


def table(ns=(8,16,32,64),precision=50):
    if type(precision) is not int or not 28<=precision<=100:raise ValueError('Precisão28..100.')
    with localcontext() as ctx:
        ctx.prec=precision;target=(-Decimal(1)).exp();rows=[]
        for n in ns:
            n=count(n)
            if 4*n>4096:raise ValueError('Tripla exige4n<=4096.')
            c,f,g=euler(n),euler(2*n),euler(4*n);d=differences(c,f,g)
            error=abs(decimal(f)-target);rich_error=abs(decimal(d['richardson_order1'])-target)
            rows.append(dict(n=n,h=Q(1,n),coarse=c,fine=f,finer=g,cost_three_runs=7*n,
                             true_fine_error=error,true_richardson_error=rich_error,**d))
        return rows


if __name__=='__main__':
    for row in table():
        print('n=',row['n'],'p_obs=',row['observed_order'],
              'erro fino=',row['true_fine_error'],'estimativa=',float(row['fine_error_estimate_order1']),
              'erro extrapolado=',row['true_richardson_error'],'avaliações=',row['cost_three_runs'])
    print('Diferenças coincidentes:',differences(1,1,1))
