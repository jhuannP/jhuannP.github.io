"""Coeficientes crescentes de polinômios; aritmética racional exata."""
from fractions import Fraction as Q

def scalar(x):
    if isinstance(x, bool) or not isinstance(x, (int,Q)):
        raise ValueError('Use inteiros ou Fraction; sem floats ou bools')
    return Q(x)

def coefficients(p):
    if not isinstance(p, (list,tuple)) or not 1 <= len(p) <= 9:
        raise ValueError('De 1 a 9 coeficientes, em ordem crescente')
    return tuple(scalar(x) for x in p)

def derivative(p):
    p=coefficients(p)
    return tuple(i*p[i] for i in range(1,len(p))) or (Q(0),)

def primitive(q):
    q=coefficients(q)
    if len(q)>8: raise ValueError('Primitiva limitada ao grau 8')
    return (Q(0),)+tuple(a/Q(i+1) for i,a in enumerate(q))

def evaluate(p,t):
    p=coefficients(p);t=scalar(t);value=Q(0)
    for a in reversed(p):value=value*t+a
    return value

def reconstruct(q,t0,y0):
    p=primitive(q);c=scalar(y0)-evaluate(p,t0)
    return (c,)+p[1:]

if __name__=='__main__':
    p=reconstruct((2,-2,3),1,5)
    assert p==(3,2,-1,1)
    print('p:',p,'Dp:',derivative(p),'p(1):',evaluate(p,1))
