"""Mapas afins e construção ReLU exata; não executa treinamento."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int/Fraction')
    return Q(x)

def matrix(W,b):
    W=[list(row) for row in W]; b=list(b)
    if not 1<=len(W)<=4 or not 1<=len(W[0])<=4:
        raise ValueError('Matriz não vazia até4x4 necessária')
    d=len(W[0])
    if len(b)!=len(W) or any(len(row)!=d for row in W):
        raise ValueError('Matriz retangular e bias compatível necessários')
    return [[rational(v) for v in row] for row in W],[rational(v) for v in b]

def affine(W,b,x):
    W,b=matrix(W,b);x=[rational(v) for v in x]
    if len(x)!=len(W[0]):raise ValueError('Dimensões incompatíveis')
    return [sum(w*v for w,v in zip(row,x))+bias for row,bias in zip(W,b)]

def collapse(W1,b1,W2,b2):
    W1,b1=matrix(W1,b1);W2,b2=matrix(W2,b2)
    if len(W2[0])!=len(W1):raise ValueError('Camadas incompatíveis')
    W=[[sum(W2[i][h]*W1[h][j] for h in range(len(W1)))
        for j in range(len(W1[0]))] for i in range(len(W2))]
    b=affine(W2,b2,b1)
    return W,b

def relu(t):
    return max(Q(0),rational(t))

def xor_score(x):
    """Definido no quadrado; o rótulo XOR é alegado apenas nos4vértices."""
    x=list(x)
    if len(x)!=2:raise ValueError('Duas entradas necessárias')
    x=[rational(v) for v in x]
    if any(not 0<=v<=1 for v in x):raise ValueError('Entradas em[0,1] necessárias')
    h=affine([[1,-1],[-1,1]],[0,0],x)
    return affine([[2,2]],[-1],[relu(v) for v in h])[0]

if __name__=='__main__':
    W,b=collapse([[1,2],[-1,1]],[1,-2],[[3,-2]],[4])
    assert W==[[5,4]] and b==[11]
    print('Composição afim:',W,b)
    for x in ([0,0],[1,0],[0,1],[1,1]):print(x,xor_score(x))
