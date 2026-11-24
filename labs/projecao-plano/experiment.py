"""Projeção euclidiana em span((1,0,1),(0,1,1)); frações exatas."""
from fractions import Fraction as F
from math import sqrt
U=(1,0,1);V=(0,1,1);N=(-1,-1,1)
P=tuple(tuple(F(x,3) for x in row) for row in ((2,-1,1),(-1,2,1),(1,1,2)))

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def apply(matrix,b):return tuple(dot(row,b) for row in matrix)

def project(b):
    return apply(P,b)

def model(x=1,y=1,z=1,s=1):
    if any(isinstance(v,bool) or not isinstance(v,int) or not -2<=v<=2 for v in (x,y,z,s)):
        raise ValueError('Quatro controles inteiros entre-2 e2')
    b=(F(x),F(y),F(z));p=project(b);residual=tuple(a-c for a,c in zip(b,p))
    candidate=tuple(a+s*u for a,u in zip(p,U))
    error=tuple(a-c for a,c in zip(b,candidate))
    naive=tuple(dot(b,U)*u/F(2)+dot(b,V)*v/F(2) for u,v in zip(U,V))
    naive_residual=tuple(a-c for a,c in zip(b,naive))
    coefficients=(F(2*x-y+z,3),F(-x+2*y+z,3))
    # Plot is an affine orthonormal slice, not a drawing of the full plane.
    horizontal=dot(b,U)/sqrt(2);vertical=dot(b,N)/sqrt(3)
    return dict(b=b,p=p,residual=residual,candidate=candidate,coefficients=coefficients,
                residual_squared=dot(residual,residual),candidate_error_squared=dot(error,error),
                increment=F(2*s*s),p_squared=dot(p,p),b_squared=dot(b,b),
                naive=naive,naive_dot_u=dot(naive_residual,U),naive_dot_v=dot(naive_residual,V),
                omitted=(-x+2*y+z)/sqrt(6),
                points=((float(horizontal),float(vertical)),(float(horizontal),0.0),(float(horizontal+s*sqrt(2)),0.0)))

if __name__=='__main__':
    old_v=(3,1);old_u=(1,1)
    old_c=F(dot(old_v,old_u),dot(old_u,old_u))
    assert old_c==2 and tuple(old_c*a for a in old_u)==(2,2)
    r=model()
    print('p=',r['p'],'r=',r['residual'],'erro mínimo²=',r['residual_squared'])
    print('q=p+u; erro²=',r['candidate_error_squared'])
    assert r['residual_squared']==F(1,3)
    assert r['candidate_error_squared']==F(7,3)
