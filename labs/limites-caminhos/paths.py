"""Valores racionais para três funções; amostras não provam limite universal."""
from fractions import Fraction as Q

def values(x,y):
    if type(x) not in (int,Q) or type(y) not in (int,Q):raise ValueError('coordenadas racionais sem bool necessárias')
    x,y=Q(x),Q(y)
    if x==y==0:raise ValueError('origem excluída')
    return x*y/(x*x+y*y),x*x*y/(x**4+y*y),x*x*y/(x*x+y*y)

if __name__=='__main__':
    count=0
    for n in range(1,11):
        for sign in (-1,1):
            t=Q(sign,2**n)
            for k in range(-4,5):
                f,g,h=values(t,k*t)
                assert f==Q(k,1+k*k)
                assert g==(Q(k)*t/(t*t+k*k) if k else 0)
                _,curve,_=values(t,k*t*t)
                assert curve==Q(k,1+k*k)
                count+=1
    points=0
    for i in range(-10,11):
        for j in range(-10,11):
            if i==j==0:continue
            x,y=Q(i,20),Q(j,20);f,g,h=values(x,y)
            assert abs(h)<=abs(y)
            assert h*h<=x*x+y*y
            assert abs(f)<=Q(1,2) and abs(g)<=Q(1,2)
            points+=1
    assert values(Q(3,50),Q(2,25))[2]==Q(18,625)
    for x,y in [(0,0),(True,1),(.1,1)]:
        try:values(x,y)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print(count,'combinações de reta/parábola;',points,'pontos de cotas; exemplo e contratos aprovados. Não é prova por amostragem.')
