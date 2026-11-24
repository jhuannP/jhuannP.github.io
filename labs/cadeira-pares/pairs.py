"""Dois grupos em carbonos distintos; duas cadeiras ideais, pesos prescritos."""
from fractions import Fraction as Q


def integer(value, allowed):
    if isinstance(value,bool) or not isinstance(value,int) or value not in allowed:
        raise ValueError('Inteiro fora do domínio')
    return value


def configuration(site1, face1, site2, face2):
    sites = integer(site1, range(1,7)), integer(site2, range(1,7))
    faces = integer(face1, (-1,1)), integer(face2, (-1,1))
    if sites[0] == sites[1]:
        raise ValueError('Dois carbonos distintos; sem caso geminal')
    return sites, faces


def kinds(chair, site1, face1, site2, face2):
    chair = integer(chair,(0,1))
    sites,faces=configuration(site1,face1,site2,face2)
    return tuple('axial' if face == (-1)**(site-1+chair) else 'equatorial'
                 for site,face in zip(sites,faces))


def population(site1, face1, site2, face2, r1=3, r2=5):
    sites,faces=configuration(site1,face1,site2,face2)
    penalties=[]
    for value in (r1,r2):
        if isinstance(value,bool) or not isinstance(value,(int,Q)) or value < 1:
            raise ValueError('Penalidades racionais >=1')
        penalties.append(Q(value))
    states=tuple(kinds(c,site1,face1,site2,face2) for c in (0,1))
    weights=[]
    for state in states:
        w=Q(1)
        for kind,r in zip(state,penalties):
            if kind == 'axial': w /= r
        weights.append(w)
    z=sum(weights,Q(0))
    return dict(relation='cis' if faces[0]==faces[1] else 'trans',
                states=states, weights=tuple(weights),
                probabilities=tuple(w/z for w in weights))


if __name__ == '__main__':
    cis=population(1,1,2,1)
    trans=population(1,1,2,-1)
    assert cis['probabilities']==(Q(5,8),Q(3,8))
    assert trans['probabilities']==(Q(1,16),Q(15,16))
    print('cis C1/C2:',cis)
    print('trans C1/C2:',trans)
