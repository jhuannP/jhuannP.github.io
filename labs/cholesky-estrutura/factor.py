"""Cholesky didática da aula preservada, mais substituições triangulares."""
from math import isfinite, sqrt, pi, cos, sin, exp, e, fsum

def _real(value):
    try:
        if isinstance(value,bool): raise ValueError
        result=float(value)
    except (TypeError,ValueError,OverflowError):
        raise ValueError('Valor real finito necessário') from None
    if not isfinite(result): raise ValueError('Valor real finito necessário')
    return result

def _system(A,b):
    n=len(A)
    if n==0 or len(b)!=n or any(len(row)!=n for row in A):raise ValueError('Sistema quadrado não vazio necessário')
    return [[_real(x) for x in row] for row in A],[_real(x) for x in b]

def cholesky(A):
    A,_=_system(A,[0]*len(A));n=len(A)
    if any(A[i][j]!=A[j][i] for i in range(n) for j in range(n)):raise ValueError('Matriz simétrica necessária')
    L=[[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            valor=_real(A[i][j]-sum(L[i][k]*L[j][k] for k in range(j)))
            if i==j:
                if valor<=0:raise ArithmeticError('Pivô não positivo no cálculo de Cholesky')
                L[i][j]=sqrt(valor)
            else:L[i][j]=_real(valor/L[j][j])
    return L


def solve_factor(L,b):
    """Resolver LLᵀx=b; fator pode ser reutilizado. Entradas não são alteradas."""
    L,b=_system(L,b);n=len(L)
    if any(L[i][j]!=0 for i in range(n) for j in range(i+1,n)):
        raise ValueError("Fator precisa ser triangular inferior.")
    if any(L[i][i]<=0 for i in range(n)):
        raise ArithmeticError("Diagonal positiva necessária.")
    y=[0.0]*n
    for i in range(n):
        y[i]=_real((b[i]-fsum(L[i][j]*y[j] for j in range(i)))/L[i][i])
    x=[0.0]*n
    for i in range(n-1,-1,-1):
        x[i]=_real((y[i]-fsum(L[j][i]*x[j] for j in range(i+1,n)))/L[i][i])
    return x

def relative_factor_residual(A,L):
    A,_=_system(A,[0]*len(A));L,_=_system(L,[0]*len(L))
    if len(A)!=len(L):raise ValueError("Dimensões precisam coincidir.")
    n=len(A);scale=max(fsum(abs(v) for v in row) for row in A)
    if scale==0:raise ValueError("Norma de A precisa ser positiva.")
    error=max(fsum(abs(A[i][j]-fsum(L[i][k]*L[j][k] for k in range(n)))
                   for j in range(n)) for i in range(n))
    return _real(error/scale)

if __name__=='__main__':
    A=[[4,2,-2],[2,5,1],[-2,1,3]]
    L=cholesky(A)
    print('L=',L)
    print('x=',solve_factor(L,[-2,-1,3]))
    print('resíduo relativo da fatoração=',relative_factor_residual(A,L))
