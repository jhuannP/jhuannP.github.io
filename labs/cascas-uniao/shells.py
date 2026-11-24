"""Polinômios de exemplos de cascas; não calcula união geométrica geral."""
from fractions import Fraction as Q

def integral_poly(coefficients,a,b):
    if not isinstance(coefficients,(list,tuple)) or not coefficients or any(type(c) not in (int,Q) for c in coefficients):raise ValueError('coeficientes racionais sem bool')
    if type(a) not in (int,Q) or type(b) not in (int,Q) or a>b:raise ValueError('limites racionais ordenados')
    a,b=Q(a),Q(b)
    return sum((Q(c)*(b**(j+1)-a**(j+1))/(j+1) for j,c in enumerate(coefficients)),Q(0))

def simpson_poly(coefficients,a,b):
    a,b=Q(a),Q(b);m=(a+b)/2
    value=lambda x:sum(Q(c)*x**j for j,c in enumerate(coefficients))
    return (b-a)*(value(a)+4*value(m)+value(b))/6

if __name__=='__main__':
    # All values below are V/pi in dimensionless coordinates.
    base=2*integral_poly([0,0,0,1],0,1)
    left=2*integral_poly([0,0,1,1],0,1)
    right=2*integral_poly([0,0,2,-1],0,1)
    inside=2*integral_poly([0,0,Q(-1,2),1],Q(1,2),1)
    duplicate=2*integral_poly([0,0,Q(1,2),-1],0,Q(1,2))
    assert (base,left,right,inside,inside+duplicate)==(Q(1,2),Q(7,6),Q(5,6),Q(17,96),Q(3,16))
    assert duplicate==Q(1,96)
    cases=0
    for coefficients in ([0,0,0,1],[0,0,1,1],[0,0,2,-1],[0,0,Q(-1,2),1],[0,0,Q(1,2),-1]):
        for a,b in [(Q(0),Q(1,2)),(Q(1,2),Q(1)),(Q(0),Q(1))]:
            assert integral_poly(coefficients,a,b)==simpson_poly(coefficients,a,b)
            cases+=1
    # Independent y-slices: disk then washer, using sqrt quadrature.
    from math import sqrt,isclose
    n=1000;a=.25;b=1;h=(b-a)/n
    f=lambda y:sqrt(y)-y
    washer=h/3*(f(a)+f(b)+sum((4 if k%2 else 2)*f(a+k*h) for k in range(1,n)))
    assert isclose(1/16+washer,float(inside),abs_tol=1e-11)
    # Same radius: the left interval is contained in the right interval at every r.
    for k in range(101):
        r=Q(k,200)
        assert (Q(1,2)-r)**2<=(Q(1,2)+r)**2
    for args in [([True],0,1),([1],1,0),([1],0.,1)]:
        try:integral_poly(*args)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('V/pi: eixo0=',base,'eixo-1=',left,'eixo2=',right,'eixo1/2=',inside)
    print('Soma ingênua=',inside+duplicate,'excesso=',duplicate,'; quadraturas polinomiais:',cases)
