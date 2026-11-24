"""Grupo C2v de um triátomo AB2 angular ideal no plano xz; sem cálculo eletrônico."""
NAMES=('E','C2(z)','sigma(xz)','sigma(yz)')
SIGNS=((1,1,1),(-1,-1,1),(1,-1,1),(-1,1,1))
ATOMS=((0,0,0),(1,0,1),(-1,0,1))

def validate(k):
    if not isinstance(k,int) or not 0<=k<4:raise ValueError('Operação inteira de 0 a 3.')

def matrix(k):
    validate(k)
    return [[SIGNS[k][i] if i==j else 0 for j in range(3)] for i in range(3)]

def apply(k,v):
    validate(k)
    if len(v)!=3:raise ValueError('Vetor deve ter três componentes.')
    return tuple(a*b for a,b in zip(SIGNS[k],v))

def compose(a,b):
    """Aplicar b primeiro e a depois, na convenção de vetores coluna."""
    validate(a);validate(b)
    return SIGNS.index(tuple(x*y for x,y in zip(SIGNS[a],SIGNS[b])))

def snapshot(a,b):
    k=compose(a,b);v=apply(k,(1,2,3));s=SIGNS[k]
    return dict(op=k,permutation=[0,1,2] if s[0]==1 else [0,2,1],probe=list(v),determinant=s[0]*s[1]*s[2])

if __name__=='__main__':
    print('Linhas: A; colunas: B; entrada: A após B')
    for a in range(4):print(NAMES[a],[NAMES[compose(a,b)] for b in range(4)])
    print('C2 após sigma(xz):',snapshot(1,2))
