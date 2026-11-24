"""Limites racionais por somas de Riemann para ln(x), x racional positivo."""
from fractions import Fraction as Q

def log_bounds(x,n=16):
    if type(x) not in (int,Q) or x<=0:
        raise ValueError('x deve ser int/Fraction positivo, sem bool/float/texto')
    if type(n) is not int or n<1:raise ValueError('n deve ser int positivo, sem bool')
    x=Q(x)
    a,b=min(Q(1),x),max(Q(1),x)
    h=(b-a)/n
    lower=h*sum((1/(a+i*h) for i in range(1,n+1)),Q(0))
    upper=h*sum((1/(a+i*h) for i in range(n)),Q(0))
    if x<1:lower,upper=-upper,-lower
    return dict(lower=lower,upper=upper,midpoint=(lower+upper)/2,
                max_midpoint_error=(upper-lower)/2)

if __name__=='__main__':
    print('ln(2), n=4:',log_bounds(2,4))
    assert log_bounds(2,4)['lower']==Q(533,840)
    assert log_bounds(2,4)['upper']==Q(319,420)
