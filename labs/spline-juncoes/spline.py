"""Spline natural racional; nós/valores sem unidade física implícita."""
from fractions import Fraction as Q
from bisect import bisect_right


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiros ou Fraction.')
    return Q(x)


def natural(xs,ys):
    xs,ys=tuple(map(rational,xs)),tuple(map(rational,ys))
    if len(xs)!=len(ys) or len(xs)<2 or any(a>=b for a,b in zip(xs,xs[1:])):
        raise ValueError('Ao menos dois nós crescentes, tamanhos iguais.')
    h=[b-a for a,b in zip(xs,xs[1:])]
    slopes=[(b-a)/step for a,b,step in zip(ys,ys[1:],h)]
    m=len(xs)-2
    diagonal=[2*(h[i]+h[i+1]) for i in range(m)]
    rhs=[6*(slopes[i+1]-slopes[i]) for i in range(m)]
    # Symmetric tridiagonal interior, positive definite for h>0.
    for i in range(1,m):
        factor=h[i]/diagonal[i-1]
        diagonal[i]-=factor*h[i]
        rhs[i]-=factor*rhs[i-1]
    inside=[Q(0)]*m
    for i in range(m-1,-1,-1):
        inside[i]=(rhs[i]-(h[i+1]*inside[i+1] if i+1<m else 0))/diagonal[i]
    M=(Q(0),*inside,Q(0))
    coeff=tuple((ys[i],slopes[i]-h[i]*(2*M[i]+M[i+1])/6,
                 M[i]/2,(M[i+1]-M[i])/(6*h[i])) for i in range(len(h)))
    return xs,M,coeff


def local(coeff,t,order=0):
    t=rational(t)
    if isinstance(order,bool) or not isinstance(order,int) or not 0<=order<=3:
        raise ValueError('Derivada de ordem0..3.')
    c=list(coeff)
    for _ in range(order): c=[i*c[i] for i in range(1,len(c))]
    value=Q(0)
    for a in reversed(c): value=value*t+a
    return value


def evaluate(model,x,order=0):
    xs,M,coeff=model; x=rational(x)
    if not xs[0]<=x<=xs[-1]: raise ValueError('Sem extrapolação.')
    i=min(bisect_right(xs,x)-1,len(coeff)-1)
    # At an internal node order3 is the right-hand third derivative, not a C3 claim.
    return local(coeff[i],x-xs[i],order)


if __name__=='__main__':
    s=natural([0,1,3],[0,1,1])
    print('M:',s[1],'coeficientes locais:',s[2])
    print('S(2)=',evaluate(s,2),'; S´(3)=',evaluate(s,3,1))
    print('Interpolação C2 não garante monotonicidade ou C3.')
