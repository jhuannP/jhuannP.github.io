"""Partículas newtonianas em uma dimensão; referência racional, SI."""
from fractions import Fraction as Q


def rational(value):
    if type(value) not in (int,Q):
        raise ValueError('Use int ou Fraction, sem float ou bool.')
    return Q(value)


def analyze(masses,positions,velocities):
    if not all(isinstance(x,(list,tuple)) for x in (masses,positions,velocities)):
        raise ValueError('Forneça três listas ou tuplas.')
    if not masses or len(masses)!=len(positions) or len(masses)!=len(velocities):
        raise ValueError('Listas de mesmo comprimento positivo necessárias.')
    m=tuple(map(rational,masses)); x=tuple(map(rational,positions)); v=tuple(map(rational,velocities))
    if any(a<=0 for a in m):
        raise ValueError('Massas estritamente positivas necessárias.')
    M=sum(m); P=sum(a*b for a,b in zip(m,v)); R=sum(a*b for a,b in zip(m,x))/M
    V=P/M; rel_x=tuple(a-R for a in x); rel_v=tuple(a-V for a in v)
    K=sum(a*b*b/2 for a,b in zip(m,v))
    Kcm=M*V*V/2; Krel=sum(a*b*b/2 for a,b in zip(m,rel_v))
    return dict(M=M,R=R,V=V,P=P,relative_positions=rel_x,relative_velocities=rel_v,
                internal_momentum=sum(a*b for a,b in zip(m,rel_v)),K=K,Kcm=Kcm,Krel=Krel)


def internal_impulse(m1,m2,v1,v2,J):
    """Impulsos +J e -J; não fornece forças, duração ou trabalho por mecanismo."""
    m1,m2,v1,v2,J=map(rational,(m1,m2,v1,v2,J))
    if m1<=0 or m2<=0:
        raise ValueError('Massas positivas necessárias.')
    return (v1+J/m1,v2-J/m2)


if __name__=='__main__':
    before=analyze((1,3),(0,4),(4,0))
    after_v=internal_impulse(1,3,4,0,-3)
    after=analyze((1,3),(0,4),after_v)
    print('Antes:',before)
    print('Após impulsos internos especificados, velocidades:',after_v)
    print('P antes/depois:',before['P'],after['P'],'kg m/s')
    print('K antes/depois:',before['K'],after['K'],'J')
    print('As posições foram mantidas para comparar estados; não houve integração temporal.')
