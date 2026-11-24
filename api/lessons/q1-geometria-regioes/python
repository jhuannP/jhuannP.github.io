"""VSEPR restrito e vetores esquemáticos. Não calcula estrutura ou dipolo real."""
from fractions import Fraction as Q
from math import acos, degrees


def classify(bond_regions, lone_pairs):
    """Recorte: 2–4 regiões e apenas as seis combinações listadas."""
    if type(bond_regions) is not int or type(lone_pairs) is not int:
        raise ValueError('Contagens inteiras, sem booleanos.')
    shapes = {
        (2,0):('linear','linear'),
        (3,0):('trigonal plana','trigonal plana'),
        (2,1):('trigonal plana','angular'),
        (4,0):('tetraédrica','tetraédrica'),
        (3,1):('tetraédrica','piramidal trigonal'),
        (2,2):('tetraédrica','angular'),
    }
    if (bond_regions,lone_pairs) not in shapes:
        raise ValueError('Combinação fora deste recorte, não prova de impossibilidade química.')
    electron,molecular=shapes[bond_regions,lone_pairs]
    return dict(regions=bond_regions+lone_pairs,electron=electron,molecular=molecular)


def rational(value):
    if type(value) not in (int,Q):
        raise ValueError('Use int ou Fraction, sem float ou bool.')
    return Q(value)


def vector3(values):
    if not isinstance(values,(tuple,list)) or len(values)!=3:
        raise ValueError('Vetor com três componentes necessário.')
    return tuple(rational(value) for value in values)


def dot(u,v):
    return sum(a*b for a,b in zip(vector3(u),vector3(v)))


def weighted_sum(vectors,weights):
    if not vectors or len(vectors)!=len(weights):
        raise ValueError('Vetores e pesos devem ter o mesmo comprimento positivo.')
    vectors=[vector3(v) for v in vectors]
    weights=[rational(w) for w in weights]
    return tuple(sum(w*v[k] for w,v in zip(weights,vectors)) for k in range(3))


# Comprimentos iguais dentro de cada arranjo, sem afirmar que são unitários.
TETRA=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))
PLANAR=((1,-1,0),(0,1,-1),(-1,0,1))
LINEAR=((1,0,0),(-1,0,0))


if __name__=='__main__':
    for species,counts in [('CO2',(2,0)),('CH4',(4,0)),('NH3',(3,1)),('H2O',(2,2))]:
        print(species,classify(*counts))
    print('Soma tetraédrica com pesos iguais:',weighted_sum(TETRA,[1]*4))
    print('Um peso diferente:',weighted_sum(TETRA,[2,1,1,1]))
    cosine=dot(TETRA[0],TETRA[1])/dot(TETRA[0],TETRA[0])
    print('Ângulo do tetraedro regular (graus):',degrees(acos(float(cosine))))
    print('Sem otimização molecular, ângulo de água calculado ou dipolo físico.')
