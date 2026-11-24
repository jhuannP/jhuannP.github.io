"""Deterministic exact Euler model, not a complete scientific validation."""
from fractions import Fraction


def solve(config):
    if not isinstance(config,dict) or set(config)!={'rate_s_inv','duration_s','initial','steps'}:
        raise ValueError('four named configuration fields required')
    n=config['steps']
    if type(n) is not int or not 1<=n<=128:raise ValueError('integer steps in 1..128 required')
    values=[]
    for key in ['rate_s_inv','duration_s','initial']:
        s=config[key]
        if not isinstance(s,str) or len(s)>32:raise ValueError('short rational strings required')
        try:q=Fraction(s)
        except (ValueError,ZeroDivisionError):raise ValueError('valid rational strings required') from None
        if q<0 or max(abs(q.numerator),q.denominator)>10000:
            raise ValueError('nonnegative rational components <=10000 required')
        values.append(q)
    rate,duration,initial=values
    if duration<=0:raise ValueError('positive duration required')
    h=duration/n
    if rate*h>1:raise ValueError('monotone Euler profile requires rate*h<=1')
    y=initial
    for _ in range(n):y-=h*rate*y
    return y
