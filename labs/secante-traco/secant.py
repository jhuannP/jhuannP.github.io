"""Traço racional com orçamento finito, sem critério universal de convergência."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError('use int/Fraction sem bool')
    return Q(x)

def secant(f,a,b,steps):
    a,b=map(rational,(a,b))
    if a==b or type(steps) is not int or not 1<=steps<=8:raise ValueError('pontos distintos e orçamento1..8')
    fa,fb=rational(f(a)),rational(f(b));evaluations=2;trace=[]
    if fa==0:return dict(point=a,status='raiz exata',trace=trace,evaluations=evaluations)
    if fb==0:return dict(point=b,status='raiz exata',trace=trace,evaluations=evaluations)
    for _ in range(steps):
        if fa==fb:raise ArithmeticError('valores iguais: passo indefinido')
        c=b-fb*(b-a)/(fb-fa);fc=rational(f(c));evaluations+=1
        trace.append(dict(a=a,b=b,fa=fa,fb=fb,c=c,fc=fc))
        if fc==0:return dict(point=c,status='raiz exata',trace=trace,evaluations=evaluations)
        a,fa,b,fb=b,fb,c,fc
    return dict(point=b,status='orçamento',trace=trace,evaluations=evaluations)

if __name__=='__main__':
    from decimal import Decimal,localcontext
    calls=[]
    def f(x):calls.append(x);return x*x-2
    result=secant(f,1,2,4);points=[row['c'] for row in result['trace']]
    assert points==[Q(4,3),Q(7,5),Q(58,41),Q(816,577)]
    assert result['evaluations']==len(calls)==6
    assert result['status']=='orçamento' # irrational root cannot be reached as a rational value.
    for scale in (Q(1,10**8),Q(-3),Q(5)):
        assert [row['c'] for row in secant(lambda x:scale*(x*x-2),1,2,4)['trace']]==points
    for slope in (Q(-2),Q(1,3),Q(7)):
        linear=secant(lambda x:slope*(x-Q(5,4)),0,2,4)
        assert linear['point']==Q(5,4) and linear['evaluations']==3
    # High-precision reference supplements the analytical bound, not a general certificate.
    with localcontext() as ctx:
        ctx.prec=70;r=Decimal(2).sqrt()
        for row in result['trace']:
            x=row['c'];res=abs(x*x-2)
            err=abs(Decimal(x.numerator)/Decimal(x.denominator)-r)
            bound=Decimal(res.numerator)/Decimal(res.denominator)/2
            assert 1<=x<=2 and err<=bound
    try:secant(lambda x:x*x-2,-1,1,4)
    except ArithmeticError:pass
    else:raise AssertionError('deveria diagnosticar secante horizontal')
    for args in [(1,1,4),(1,2,0),(1,2,True),(1.0,2,4)]:
        try:secant(lambda x:x*x-2,*args)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    for row in result['trace']:print('novo=',row['c'],'resíduo=',row['fc'])
    print('Avaliações:',result['evaluations'],'status:',result['status'])
