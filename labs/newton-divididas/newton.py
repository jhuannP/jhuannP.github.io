"""Interpolação racional em nós distintos; laboratório pequeno."""
from fractions import Fraction as F

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):
        raise ValueError("Use int ou Fraction")
    return F(x)

def data(xs,ys):
    xs,ys=tuple(map(rational,xs)),tuple(map(rational,ys))
    if not 1<=len(xs)<=12 or len(xs)!=len(ys) or len(set(xs))!=len(xs):
        raise ValueError("1 a 12 nós distintos e valores correspondentes")
    return xs,ys

def coefficients(xs,ys):
    xs,ys=data(xs,ys);c=list(ys)
    for order in range(1,len(xs)):
        for i in range(len(xs)-1,order-1,-1):
            c[i]=(c[i]-c[i-1])/(xs[i]-xs[i-order])
    return tuple(c)

def evaluate(xs,c,x):
    xs,c=data(xs,c);x=rational(x);total=c[-1]
    for i in range(len(c)-2,-1,-1):
        total=c[i]+(x-xs[i])*total
    return total

def append_node(xs,c,x,y):
    xs,c=data(xs,c);x,y=rational(x),rational(y)
    if len(xs)==12 or x in xs:raise ValueError("nó novo distinto; máximo 12")
    product=F(1)
    for old in xs:product*=x-old
    correction=(y-evaluate(xs,c,x))/product
    return xs+(x,), c+(correction,)

if __name__=='__main__':
    xs=(-1,1,2);ys=(2,0,2);c=coefficients(xs,ys)
    print("coeficientes:",c,"p(3/2):",evaluate(xs,c,F(3,2)))
    xx,cc=append_node(xs,c,3,8)
    print("novo coeficiente:",cc[-1],"novo p(0):",evaluate(xx,cc,0))
