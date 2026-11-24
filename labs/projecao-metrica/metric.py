"""Projeção racional sobre uma reta em R2, com matriz G SPD."""
from fractions import Fraction as F

def values(xs,n):
    xs=tuple(xs)
    if len(xs)!=n or any(isinstance(x,bool) or not isinstance(x,(int,F)) for x in xs):
        raise ValueError("dimensão correta e int/Fraction necessários")
    return tuple(map(F,xs))

def metric(g):
    a,b,c,d=values(g,4)
    if b!=c or a<=0 or a*d-b*b<=0:raise ValueError("G deve ser simétrica definida positiva")
    return a,b,c,d

def inner(x,y,g):
    x,y=values(x,2),values(y,2);a,b,c,d=metric(g)
    return x[0]*(a*y[0]+b*y[1])+x[1]*(c*y[0]+d*y[1])

def project(b,u,g):
    b,u=values(b,2),values(u,2);g=metric(g)
    if u==(0,0):raise ValueError("gerador não nulo")
    alpha=inner(u,b,g)/inner(u,u,g)
    p=tuple(alpha*x for x in u);r=tuple(x-y for x,y in zip(b,p))
    return dict(alpha=alpha,p=p,r=r,error_squared=inner(r,r,g))

def matrix(u,g):
    u=values(u,2);g=metric(g)
    cols=[project(b,u,g)['p'] for b in ((1,0),(0,1))]
    return (cols[0][0],cols[1][0],cols[0][1],cols[1][1])

if __name__=='__main__':
    for g in ((1,0,0,1),(1,0,0,4)):
        print('G=',g,project((2,0),(1,1),g),'P=',matrix((1,1),g))
