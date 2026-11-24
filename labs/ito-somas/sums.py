"""Auditoria exata de somas; não constrói um Browniano contínuo."""
from fractions import Fraction as Q
from itertools import product

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction, sem floats')
    return Q(x)

def quadrature(increments,w0=0):
    if not isinstance(increments,(list,tuple)) or not 1<=len(increments)<=256:
        raise ValueError('De 1 a 256 incrementos')
    w=rational(w0);left=right=trap=qv=Q(0)
    for value in increments:
        z=rational(value);following=w+z
        left+=w*z;right+=following*z;trap+=(w+following)*z/2;qv+=z*z
        w=following
    return dict(end=w,left=left,right=right,trapezoidal=trap,qv=qv)

def brownian_mse(steps):
    if not isinstance(steps,(list,tuple)) or not 1<=len(steps)<=256:
        raise ValueError('De 1 a 256 passos determinísticos')
    h=[rational(v) for v in steps]
    if any(v<=0 for v in h):raise ValueError('Passos positivos')
    return sum((v*v for v in h),Q(0))/2

def predictable_example(a,b,c):
    # Dois incrementos Rademacher independentes, variância 1; não gaussianos.
    a,b,c=map(rational,(a,b,c));rows=[]
    for first,second in product((-1,1),repeat=2):
        h0=a;h1=b+c*first
        value=h0*first+h1*second
        rows.append((value,h0*h0+h1*h1))
    mean=sum((v for v,e in rows),Q(0))/4
    second_moment=sum((v*v for v,e in rows),Q(0))/4
    energy=sum((e for v,e in rows),Q(0))/4
    return mean,second_moment,energy

if __name__=='__main__':
    result=quadrature([Q(1,2),Q(-1,4),Q(3,4)])
    assert result['left']==Q(1,16)
    print(result)
    print('MSE browniano, três passos de 1/2:',brownian_mse([Q(1,2)]*3))
    print('Modelo discreto previsível:',predictable_example(1,0,1))
