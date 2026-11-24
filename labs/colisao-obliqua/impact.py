"""Contato binário liso, normal prescrita, impulso externo desprezível. Não detecta contato."""
from fractions import Fraction as Q


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use inteiro ou Fraction, não float/bool.')
    return Q(x)


def vector(v):
    if not isinstance(v,(tuple,list)) or len(v)!=2:
        raise ValueError('Vetor de dois componentes.')
    return tuple(map(rational,v))


def dot(u,v):return sum(a*b for a,b in zip(u,v))
def add(u,v):return tuple(a+b for a,b in zip(u,v))
def scale(s,v):return tuple(s*a for a in v)


def impact(m1,m2,u1,u2,n,e):
    """n unitária do centro1 ao2 no contato. g=(u1-u2).n>0 é aproximação.

    m em kg,u em m/s,J em N*s,K em J. e normal prescrito em[0,1].
    Se g<=0,nenhum impulso repulsivo é aplicado. Sem atrito,adesão ou spin.
    """
    m1,m2,e=map(rational,(m1,m2,e));u1,u2,n=map(vector,(u1,u2,n))
    if m1<=0 or m2<=0 or not 0<=e<=1:raise ValueError('Massas positivas e e em[0,1].')
    if dot(n,n)!=1:raise ValueError('Normal racional exatamente unitária.')
    tangent=(-n[1],n[0]);g=dot(add(u1,scale(-1,u2)),n)
    mu=m1*m2/(m1+m2)
    J=mu*(1+e)*g if g>0 else Q(0)
    v1=add(u1,scale(-J/m1,n));v2=add(u2,scale(J/m2,n))
    momentum=lambda a,b:add(scale(m1,a),scale(m2,b))
    energy=lambda a,b:(m1*dot(a,a)+m2*dot(b,b))/2
    return dict(v1=v1,v2=v2,impulse=J,closing=g,
                relative_normal_after=dot(add(v1,scale(-1,v2)),n),
                tangent_before=(dot(u1,tangent),dot(u2,tangent)),
                tangent_after=(dot(v1,tangent),dot(v2,tangent)),
                P_before=momentum(u1,u2),P_after=momentum(v1,v2),
                K_before=energy(u1,u2),K_after=energy(v1,v2),
                loss=energy(u1,u2)-energy(v1,v2))


if __name__=='__main__':
    print('Dados prescritos em SI, não medição. Normal do1 ao2 no contato já fornecida.')
    print(impact(2,3,(3,1),(-1,0),(Q(3,5),Q(4,5)),Q(1,2)))
