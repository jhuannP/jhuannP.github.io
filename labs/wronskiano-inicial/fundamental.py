"""Matriz fundamental com fator exponencial separado; não solver geral."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction')
    return Q(x)


def polynomial(p):
    if not isinstance(p,(tuple,list)) or not 1<=len(p)<=8:
        raise ValueError('De 1 a 8 coeficientes em ordem crescente')
    return tuple(map(rational,p))


def evaluate(p,t):
    p=polynomial(p);t=rational(t);value=Q(0)
    for c in reversed(p):value=value*t+c
    return value


def derivative(p):
    p=polynomial(p)
    return tuple(i*p[i] for i in range(1,len(p))) or (Q(0),)


def wronskian(f,g,t):
    f,g=polynomial(f),polynomial(g);t=rational(t)
    return evaluate(f,t)*evaluate(derivative(g),t)-evaluate(derivative(f),t)*evaluate(g,t)


def stripped_fundamental(t):
    t=rational(t)
    # Phi(t)=exp(-2t)*B(t); B abaixo NÃO é Phi.
    return ((Q(1),t),(-Q(2),1-2*t))


def coefficients_at_zero(y,v):
    y,v=map(rational,(y,v))
    return y,v+2*y


def stripped_state(t,c1,c2):
    c1,c2=map(rational,(c1,c2));b=stripped_fundamental(t)
    return tuple(row[0]*c1+row[1]*c2 for row in b)


if __name__=='__main__':
    c=coefficients_at_zero(3,-4)
    assert c==(3,2) and stripped_state(1,*c)==(5,-8)
    assert wronskian((0,0,1),(0,0,0,1),0)==0
    assert wronskian((0,0,1),(0,0,0,1),1)==1
    print("c=",c,"estado multiplicado por exp(2t), em t=1:",stripped_state(1,*c))
