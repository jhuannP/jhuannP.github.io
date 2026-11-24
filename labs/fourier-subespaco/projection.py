"""Projeção finita em sen(2πnx); quadraturas de exemplos, não FFT geral."""
from math import sin,pi,isclose

def mode(n,x):return sin(2*pi*n*x)
def target(x):return 1+mode(1,x)+mode(2,x)/2+mode(3,x)/4
def approx(x,a):return sum(c*mode(n,x) for n,c in enumerate(a,1))
def integral(f,m=1024):
    if type(m) is not int or not 1<=m<=8192:raise ValueError('malha inteira1..8192')
    return sum(f((j+.5)/m) for j in range(m))/m

def sampled_coefficient(f,n,m):
    if type(n) is not int or n<1 or type(m) is not int or not 1<=m<=8192:raise ValueError('modo positivo e malha1..8192')
    return 2*sum(f(j/m)*mode(n,j/m) for j in range(m))/m

if __name__=='__main__':
    for n in range(1,7):
        for k in range(1,7):
            assert isclose(integral(lambda x:mode(n,x)*mode(k,x)),.5 if n==k else 0,abs_tol=1e-12)
    coefficients=[2*integral(lambda x,n=n:target(x)*mode(n,x)) for n in range(1,7)]
    assert all(isclose(a,b,abs_tol=1e-12) for a,b in zip(coefficients,[1,.5,.25,0,0,0]))
    residual=integral(lambda x:(target(x)-approx(x,[1,.5]))**2)
    projected=integral(lambda x:approx(x,[1,.5])**2)
    assert isclose(residual,33/32,abs_tol=1e-12)
    assert isclose(projected,5/8,abs_tol=1e-12)
    assert isclose(integral(lambda x:target(x)**2),residual+projected,abs_tol=1e-12)
    for da in (-1,0,1):
        for db in (-1,0,1):
            loss=integral(lambda x:(target(x)-approx(x,[1+da,.5+db]))**2)
            assert isclose(loss,residual+(da*da+db*db)/2,abs_tol=1e-12)
    for n in range(1,7):assert abs(integral(lambda x:mode(n,x)))<1e-12
    assert isclose(sampled_coefficient(target,1,4),.75,abs_tol=1e-12)
    assert isclose(sampled_coefficient(target,1,16),1,abs_tol=1e-12)
    for j in range(4):assert isclose(mode(3,j/4),-mode(1,j/4),abs_tol=1e-12)
    print('Coeficientes contínuos conferidos por quadratura:',coefficients)
    print('Erro²=',residual,'norma projetada²=',projected)
    print('Quatro amostras:',sampled_coefficient(target,1,4),'dezesseis:',sampled_coefficient(target,1,16))
