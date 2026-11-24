"""Famílias fixas da aula, aritmética exata, sem algoritmo de autovalores."""
from fractions import Fraction as Q

def exponent(n):
    if type(n) is not int or not 0<=n<=100:raise ValueError('inteiro 0..100 necessário')
def pair(v):
    if not isinstance(v,(tuple,list)) or len(v)!=2 or any(type(x) not in (int,Q) for x in v):raise ValueError('vetor racional de duas componentes necessário')
    return tuple(Q(x) for x in v)
def diagonal_action(v,n):
    exponent(n);x,y=pair(v);alpha=(x+y)/2;beta=(x-y)/2
    return (3**n*alpha+beta,3**n*alpha-beta)
def repeated(v,n,jordan=False):
    exponent(n);x,y=pair(v)
    for _ in range(n):
        x,y=(x+y,y) if jordan else (2*x+y,x+2*y)
    return x,y

if __name__=='__main__':
    cases=0
    for x in range(-3,4):
        for y in range(-3,4):
            for n in range(13):
                v=(Q(x,2),Q(y,3))
                assert diagonal_action(v,n)==repeated(v,n)
                assert repeated(v,n,True)==(v[0]+n*v[1],v[1])
                cases+=1
    # P inverse and AP=PD, checked by direct products on each column.
    P=((Q(1),Q(1)),(Q(1),Q(-1)));Pinv=tuple(tuple(v/2 for v in row) for row in P)
    mul=lambda A,B:tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
    I=((1,0),(0,1));A=((2,1),(1,2));D=((3,0),(0,1))
    assert mul(P,Pinv)==mul(Pinv,P)==I
    assert mul(A,P)==mul(P,D)
    for n in range(13):
        result=tuple(x/Q(3)**n for x in diagonal_action((1,0),n))
        assert result==(Q(1,2)+Q(1,2*3**n),Q(1,2)-Q(1,2*3**n))
    for v,n in [((True,1),1),((1.,0),1),((1,0),True),((1,0),-1),((1,0),101)]:
        try:diagonal_action(v,n)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print(cases,'pares vetor/expoente: A e J conferidos; identidade/similaridade, normalização e contratos aprovados.')
