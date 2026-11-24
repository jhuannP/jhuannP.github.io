"""Original exact geometry lab. Rational coordinates, no physical time/dynamics."""
from fractions import Fraction as F


def real(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):
        raise ValueError('int/Fraction required')
    return F(x)


def controls(points):
    if not isinstance(points,(tuple,list)) or not 1<=len(points)<=17:
        raise ValueError('1..17 controls required')
    if not isinstance(points[0],(tuple,list)) or not 1<=len(points[0])<=3:
        raise ValueError('dimension 1..3 required')
    d=len(points[0])
    if any(not isinstance(p,(tuple,list)) or len(p)!=d for p in points):
        raise ValueError('matching dimensions required')
    return tuple(tuple(real(x) for x in p) for p in points)


def triangle(points,t):
    p=controls(points);t=real(t)
    if not 0<=t<=1:raise ValueError('parameter in [0,1] required')
    rows=[p]
    while len(p)>1:
        p=tuple(tuple((1-t)*a+t*b for a,b in zip(p[i],p[i+1])) for i in range(len(p)-1))
        rows.append(p)
    return tuple(rows)


def evaluate(points,t):
    return triangle(points,t)[-1][0]


def split(points,t):
    rows=triangle(points,t)
    return tuple(row[0] for row in rows),tuple(row[-1] for row in reversed(rows))


def derivative(points,t):
    p=controls(points);t=real(t)
    if not 0<=t<=1:raise ValueError('parameter in [0,1] required')
    n=len(p)-1
    if not n:return tuple(F(0) for _ in p[0])
    q=tuple(tuple(n*(b-a) for a,b in zip(p[i],p[i+1])) for i in range(n))
    return evaluate(q,t)


if __name__=='__main__':
    p=((0,0),(1,2),(2,2),(3,0))
    print('Original controls:',p)
    print('Triangle at 1/2:',triangle(p,F(1,2)))
    print('Two exact pieces:',split(p,F(1,2)))
    print('Endpoint derivatives:',derivative(p,0),derivative(p,1))
    print('Geometric parameter only; no physical trajectory or personal experiment is inferred.')
