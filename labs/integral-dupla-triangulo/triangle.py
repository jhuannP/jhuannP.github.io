"""Contas exatas específicas do triângulo unitário, sem quadratura geral."""
from fractions import Fraction as Q

def monomial(a,b):
    if any(type(k) is not int or k<0 for k in (a,b)):raise ValueError('expoentes inteiros não negativos necessários')
    return Q(1,(b+1)*(a+b+2))
def simpson(f,a,b):return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6

if __name__=='__main__':
    for a in range(6):
        for b in range(6):
            reverse=Q(1,a+1)*(Q(1,b+1)-Q(1,a+b+2))
            assert monomial(a,b)==reverse
            if a+b<=2:
                numerical=simpson(lambda x:simpson(lambda y:x**a*y**b,Q(0),x),Q(0),Q(1))
                assert numerical==monomial(a,b)
    for n in range(1,41):
        cells=[(i,j) for i in range(n) for j in range(i)]
        cover=[(i,j) for i in range(n) for j in range(i+1)]
        assert Q(len(cells),n*n)==Q(n-1,2*n)
        assert Q(len(cover),n*n)==Q(n+1,2*n)
        lower=sum((Q(i+j,n**3) for i,j in cells),Q(0))
        upper=sum((Q(i+j+2,n**3) for i,j in cover),Q(0))
        assert (lower,upper)==(Q((n-1)**2,2*n*n),Q((n+1)**2,2*n*n))
        assert lower<=Q(1,2)<=upper and upper-lower==Q(2,n)
    positive=simpson(lambda x:simpson(lambda y:x-2*y,Q(0),x/2),Q(0),Q(1))
    negative=simpson(lambda x:simpson(lambda y:2*y-x,x/2,x),Q(0),Q(1))
    assert positive==negative==Q(1,12)
    assert positive-negative==0 and positive+negative==Q(1,6)
    assert monomial(1,0)+monomial(0,1)==Q(1,2)
    assert 3*2**2*(monomial(1,0)+monomial(0,1))==6
    for args in [(True,0),(-1,0),(1.,0)]:
        try:monomial(*args)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('36 monômios em duas ordens; 6 por Simpson; 40 malhas; cancelamento, massa e contratos aprovados.')
