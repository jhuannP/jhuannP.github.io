"""Projeção polinomial em {1,x}, peso 1 e intervalo [0,1].
Coeficientes em ordem crescente; aritmética exata com Fraction.
"""
from fractions import Fraction as Q


def integral(coefficients):
    return sum((Q(c,k+1) for k,c in enumerate(coefficients)),Q(0))


def residual(coefficients,a,b):
    r=list(map(Q,coefficients))+[Q(0),Q(0)]
    r[0]-=a;r[1]-=b
    return r


def square_integral(coefficients):
    return sum((Q(a)*Q(b)/Q(i+j+1) for i,a in enumerate(coefficients)
                for j,b in enumerate(coefficients)),Q(0))


def project(coefficients):
    if not coefficients or any(isinstance(c,bool) or not isinstance(c,(int,Q)) for c in coefficients):
        raise ValueError('Lista não vazia de inteiros ou Fraction.')
    g0=integral(coefficients);g1=integral([0]+list(coefficients))
    b=12*(g1-g0/2);a=g0-b/2
    r=residual(coefficients,a,b)
    return a,b,square_integral(r)


def sampled_quadratic(n):
    if isinstance(n,bool) or not isinstance(n,int) or n<1:
        raise ValueError('n inteiro positivo: n+1 pontos uniformes.')
    xs=[Q(i,n) for i in range(n+1)];ys=[x*x for x in xs]
    xm=sum(xs)/len(xs);ym=sum(ys)/len(ys)
    b=sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs)
    return ym-b*xm,b


if __name__=='__main__':
    a,b,J=project([0,0,1]);print('Contínuo: a,b,J=',a,b,J)
    for n in (1,2,4,16):
        a,b=sampled_quadratic(n)
        print('Amostras:',n+1,'a,b=',a,b,'J contínuo=',square_integral(residual([0,0,1],a,b)))
