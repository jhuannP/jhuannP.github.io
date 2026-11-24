"""Maclaurin de exp: cota analítica distinta de avaliação em ponto flutuante."""
import math

def polynomial(x,n):
    term=1.;terms=[term]
    for k in range(1,n+1):term*=x/k;terms.append(term)
    return math.fsum(terms)

def tail(x,n):
    # Soma 81 termos da cauda, sem subtrair exp(x)-P_n(x).
    if x==0:return 0.
    term=x**(n+1)/math.factorial(n+1);terms=[term]
    for k in range(n+2,n+82):term*=x/k;terms.append(term)
    return math.fsum(terms)

def uniform_bound(n,rho):
    return math.exp(rho)*rho**(n+1)/math.factorial(n+1)

def required_degree(rho,epsilon):
    for n in range(41):
        if uniform_bound(n,rho)<=epsilon:return n
    raise ValueError('Busca limitada a grau 40.')

def model(n=2,rho=1.,u=.1,p=4):
    if type(n) is not int or not 0<=n<=12 or type(p) is not int or not 2<=p<=6 or not math.isfinite(rho) or not .25<=rho<=1 or not math.isfinite(u) or not -1<=u<=1:
        raise ValueError('Grau 0..12, raio .25..1, posição relativa -1..1, expoente 2..6.')
    x=rho*u;P=polynomial(x,n);R=tail(x,n)
    local=math.exp(max(0.,x))*abs(x)**(n+1)/math.factorial(n+1)
    uniform=uniform_bound(n,rho);epsilon=10.**(-p)
    return dict(n=n,rho=rho,u=u,p=p,x=x,polynomial=P,remainder=R,local_bound=local,
                uniform_bound=uniform,epsilon=epsilon,required=required_degree(rho,epsilon),
                certified=uniform<=epsilon,normalized=R/uniform)

if __name__=='__main__':
    s=model();assert abs(s['polynomial']-1.105)<1e-14
    assert s['required']==7
    print('P, resto numérico, cota local/uniforme:',s['polynomial'],s['remainder'],s['local_bound'],s['uniform_bound'])
