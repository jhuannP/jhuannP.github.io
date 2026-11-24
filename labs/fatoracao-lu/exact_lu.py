"""Doolittle exato sem pivotamento; referência didática, não solver geral."""
from fractions import Fraction as Q

class ZeroPivot(ArithmeticError):
    pass

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):
        raise TypeError("Use int ou Fraction.")
    return Q(v)

def matrix(A):
    rows=tuple(tuple(rational(v) for v in row) for row in A)
    n=len(rows)
    if not n or any(len(row)!=n for row in rows):
        raise ValueError("Matriz quadrada não vazia necessária.")
    return rows

def factor(A):
    A=matrix(A);n=len(A)
    L=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    U=[[Q(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            U[i][j]=A[i][j]-sum(L[i][k]*U[k][j] for k in range(i))
        if U[i][i]==0:
            raise ZeroPivot("Pivô zero na ordem atual; não conclui singularidade em geral.")
        for j in range(i+1,n):
            L[j][i]=(A[j][i]-sum(L[j][k]*U[k][i] for k in range(i)))/U[i][i]
    return tuple(map(tuple,L)),tuple(map(tuple,U))

def solve(L,U,b):
    L,U=matrix(L),matrix(U);n=len(L);b=tuple(rational(v) for v in b)
    if len(U)!=n or len(b)!=n:raise ValueError("Dimensões incompatíveis.")
    if any(L[i][i]!=1 or U[i][i]==0 for i in range(n)):
        raise ValueError("Exigidos diag(L)=1 e pivôs U não nulos.")
    if any(L[i][j]!=0 for i in range(n) for j in range(i+1,n)):
        raise ValueError("L deve ser triangular inferior.")
    if any(U[i][j]!=0 for i in range(n) for j in range(i)):
        raise ValueError("U deve ser triangular superior.")
    y=[]
    for i in range(n):y.append(b[i]-sum(L[i][k]*y[k] for k in range(i)))
    x=[Q(0)]*n
    for i in range(n-1,-1,-1):
        x[i]=(y[i]-sum(U[i][k]*x[k] for k in range(i+1,n)))/U[i][i]
    return tuple(x)
