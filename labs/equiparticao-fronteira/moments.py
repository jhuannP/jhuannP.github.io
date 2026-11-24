"""Quadraturas em cortes declarados, sem simulação de partículas reais."""
from math import exp,sqrt,pi,erf,isfinite,isclose

def simpson(f,a,b,n=2000):
    if type(n) is not int or n<=0 or n%2 or not a<b:raise ValueError('intervalo crescente e n positivo par necessários')
    h=(b-a)/n
    return h/3*(f(a)+f(b)+sum((4 if j%2 else 2)*f(a+j*h) for j in range(1,n)))
def moment2(k,theta):
    if any(isinstance(v,bool) or not isinstance(v,(int,float)) or not isfinite(v) or v<=0 for v in (k,theta)):raise ValueError('k e theta finitos positivos necessários')
    scale=sqrt(theta/k);a=-10*scale;b=10*scale
    w=lambda q:exp(-k*q*q/(2*theta))
    return simpson(lambda q:q*q*w(q),a,b)/simpson(w,a,b)

if __name__=='__main__':
    cases=0
    for k in (.5,4,10):
        for theta in (.5,2,5):
            assert isclose(moment2(k,theta),theta/k,rel_tol=1e-10,abs_tol=1e-12)
            cases+=1
    w=lambda x:exp(-x**4)
    quartic=simpson(lambda x:x**4*w(x),-4,4,4000)/simpson(w,-4,4,4000)
    assert isclose(quartic,.25,rel_tol=1e-10,abs_tol=1e-12)
    for a in (.25,.5,1,2,4):
        w=lambda x:exp(-x*x/2)
        direct=simpson(lambda x:x*x*w(x),-a,a)/simpson(w,-a,a)
        normalization=sqrt(2*pi)*erf(a/sqrt(2))
        boundary=1-2*a*exp(-a*a/2)/normalization
        assert isclose(direct,boundary,rel_tol=1e-9,abs_tol=1e-11)
        assert 0<direct<1
    assert isclose(moment2(4,2),.5,rel_tol=1e-10)
    for args in [(0,2),(4,0),(True,2),(4,float('nan'))]:
        try:moment2(*args)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    # Domínio q em[-1,1],k=4: não usar o momento irrestrito nesta conta.
    high=[]
    for theta in (10,100,1000):
        weight=lambda q:exp(-2*q*q/theta)
        energy=simpson(lambda q:2*q*q*weight(q),-1,1)/simpson(weight,-1,1)
        h=2/theta;limit=2/3
        assert limit*exp(-h)<=energy<=limit*exp(h)
        assert abs(energy-limit)<=limit*(exp(h)-1)
        high.append((theta,energy))
    assert high[0][1]<high[1][1]<high[2][1]<2/3
    print(cases,'quadráticas;1 quártica;5 paredes;3 temperaturas finitas versus cotas;referência e contratos aprovados.')
    print('k=4,a=1: Theta e energia potencial média:',high,';limite:',2/3)
