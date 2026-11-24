"""-Δu=2π² sin(πx)sin(πy) no quadrado unitário, bordas zero.
Variáveis adimensionais; n subintervalos por direção; início zero.
"""
from math import sin,pi


def solve(n,sweeps,method='jacobi'):
    if isinstance(n,bool) or not isinstance(n,int) or n<4 or n>32 or n%2:
        raise ValueError('n par entre 4 e 32.')
    if isinstance(sweeps,bool) or not isinstance(sweeps,int) or not 0<=sweeps<=5000:
        raise ValueError('De 0 a 5000 varreduras.')
    if method not in ('jacobi','gs'):raise ValueError('Método jacobi ou gs.')
    h=1/n
    exact=[[sin(pi*i/n)*sin(pi*j/n) if 0<i<n and 0<j<n else 0.
            for j in range(n+1)] for i in range(n+1)]
    rhs=[[2*pi*pi*v for v in row] for row in exact]
    eigenvalue=8*n*n*sin(pi/(2*n))**2
    factor=2*pi*pi/eigenvalue
    discrete=[[factor*v for v in row] for row in exact]
    u=[[0.]*(n+1) for _ in range(n+1)]
    for _ in range(sweeps):
        target=[row[:] for row in u] if method=='jacobi' else u
        for i in range(1,n):
            for j in range(1,n):
                target[i][j]=(u[i-1][j]+u[i+1][j]+u[i][j-1]+u[i][j+1]+h*h*rhs[i][j])/4
        u=target
    interior=[(i,j) for i in range(1,n) for j in range(1,n)]
    residual=max(abs(rhs[i][j]-n*n*(4*u[i][j]-u[i-1][j]-u[i+1][j]-u[i][j-1]-u[i][j+1])) for i,j in interior)
    algebraic=max(abs(u[i][j]-discrete[i][j]) for i,j in interior)
    grid_error=max(abs(discrete[i][j]-exact[i][j]) for i,j in interior)
    total=max(abs(u[i][j]-exact[i][j]) for i,j in interior)
    return dict(u=u,discrete=discrete,exact=exact,residual=residual,
                algebraic=algebraic,grid_error=grid_error,total=total,factor=factor)


if __name__=='__main__':
    for method in ('jacobi','gs'):
        for sweeps in (0,20,100,300):
            q=solve(8,sweeps,method)
            print(method,sweeps,{k:q[k] for k in ('residual','algebraic','grid_error','total')})
    print('A varredura não é passo de tempo; o orçamento não certifica convergência.')
