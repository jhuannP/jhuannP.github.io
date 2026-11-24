"""Conjuntos finitos: laboratório, não substituto de provas gerais."""
from itertools import combinations


def decode(mask):
    if isinstance(mask,bool) or not isinstance(mask,int) or not 0<=mask<=15:
        raise ValueError('Código inteiro de 0 a 15.')
    return frozenset(i+1 for i in range(4) if mask & (1<<i))


def compare(a,b):
    A,B=decode(a),decode(b)
    U=frozenset(range(1,5))
    return dict(A=A,B=B,union=A|B,intersection=A&B,difference=A-B,
                complement=U-A,subset=A<=B)


def powerset(values):
    values=tuple(sorted(set(values)))
    return frozenset(frozenset(c) for n in range(len(values)+1) for c in combinations(values,n))


def image(mapping,subset):
    if not set(subset)<=mapping.keys():raise ValueError('Elemento fora do domínio.')
    return frozenset(mapping[x] for x in subset)


def preimage(mapping,target):
    return frozenset(x for x,y in mapping.items() if y in target)


if __name__=='__main__':
    r=compare(5,6)
    for name in ('A','B','union','intersection','difference','complement'):
        print(name,sorted(r[name]))
    print('Subconjuntos de {1,2}:',len(powerset({1,2})))
    mapping={-2:4,-1:1,0:0,1:1,2:4}
    print('Pré-imagem de {1}:',sorted(preimage(mapping,{1})))
    print('Imagem de {-1}:',sorted(image(mapping,{-1})))
    print('Pré-imagem da imagem de {-1}:',sorted(preimage(mapping,image(mapping,{-1}))))
