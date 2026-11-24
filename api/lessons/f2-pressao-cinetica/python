"""Segundos momentos de uma população sintética simétrica por inversão, em SI."""
from collections import Counter
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q):raise ValueError('Use int/Fraction, sem bool/float.')
    return Q(x)


def population(mass,volume,velocities):
    m,V=map(rational,(mass,volume))
    if m<=0 or V<=0:raise ValueError('Massa e volume positivos.')
    v=[tuple(map(rational,w)) for w in velocities]
    if not v or any(len(w)!=3 for w in v):raise ValueError('Vetores 3D e população não vazia.')
    counts=Counter(v)
    if any(counts[w]!=counts[tuple(-x for x in w)] for w in counts):
        raise ValueError('Exige simetria por inversão: pares v e -v com mesma multiplicidade.')
    N=len(v);second=tuple(tuple(sum(w[i]*w[j] for w in v)/N for j in range(3)) for i in range(3))
    tensor=tuple(tuple(N*m*second[i][j]/V for j in range(3)) for i in range(3))
    U=sum(m*sum(x*x for x in w)/2 for w in v)
    same_second=all(second[i][j]==(second[0][0] if i==j else 0) for i in range(3) for j in range(3))
    # Igualdade dos segundos momentos não demonstra isotropia da distribuição inteira.
    return dict(N=N,density=Q(N)/V,mean=tuple(sum(w[i] for w in v)/N for i in range(3)),
                second=second,tensor=tensor,normal=tuple(tensor[i][i] for i in range(3)),
                U=U,energy_density=U/V,mean_normal=sum(tensor[i][i] for i in range(3))/3,
                isotropic_second_moment=same_second)


def example():
    v=[]
    for i in range(3):
        for sign in (-1,1):v.append(tuple(sign*300 if j==i else 0 for j in range(3)))
    return population(Q(1,10**26),Q(6,10**25),v)


if __name__=='__main__':
    print(example())
    print('População discreta sintética; não é Maxwell, dinâmica molecular ou medição.')
