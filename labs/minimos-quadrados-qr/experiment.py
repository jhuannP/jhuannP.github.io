"""Mínimos quadrados didáticos, Householder sem pivotamento de colunas.
Matrizes pequenas m>=n, valores finitos e limiar relativo declarado.
"""
from math import sqrt,copysign,isfinite

def qr_fit(A,y,rtol=1e-12):
    m=len(A);n=len(A[0]) if m else 0
    if not n or m<n or len(y)!=m or any(len(row)!=n for row in A):raise ValueError('Matriz retangular m>=n e y compatível')
    if any(not isfinite(float(z)) for row in A for z in row) or any(not isfinite(float(z)) for z in y) or not isfinite(rtol) or rtol<=0:raise ValueError('Dados finitos e tolerância positiva')
    R=[list(map(float,row)) for row in A];z=list(map(float,y));qt=[[float(i==j) for j in range(m)] for i in range(m)]
    scale=max(sqrt(sum(row[j]**2 for row in R)) for j in range(n));threshold=rtol*scale
    for k in range(n):
        norm=sqrt(sum(R[i][k]**2 for i in range(k,m)))
        if norm<=threshold:return dict(status='rank',beta=None,R=R,qt=qt,threshold=threshold)
        v=[R[i][k] for i in range(k,m)];v[0]+=copysign(norm,v[0])
        vn=sqrt(sum(t*t for t in v));v=[t/vn for t in v]
        for j in range(k,n):
            d=2*sum(v[i-k]*R[i][j] for i in range(k,m))
            for i in range(k,m):R[i][j]-=d*v[i-k]
        d=2*sum(v[i-k]*z[i] for i in range(k,m))
        for i in range(k,m):z[i]-=d*v[i-k]
        for j in range(m):
            d=2*sum(v[i-k]*qt[i][j] for i in range(k,m))
            for i in range(k,m):qt[i][j]-=d*v[i-k]
        for i in range(k+1,m):R[i][k]=0.
    beta=[0.]*n
    for i in range(n-1,-1,-1):beta[i]=(z[i]-sum(R[i][j]*beta[j] for j in range(i+1,n)))/R[i][i]
    pred=[sum(a*b for a,b in zip(row,beta)) for row in A];res=[yi-pi for yi,pi in zip(y,pred)]
    return dict(status='ok',beta=beta,R=R,qt=qt,threshold=threshold,pred=pred,residual=res,sse=sum(r*r for r in res),gradient=[sum(A[i][j]*res[i] for i in range(m)) for j in range(n)])

def normal_fit(A,y,rtol=1e-12):
    n=len(A[0]);G=[[sum(row[i]*row[j] for row in A) for j in range(n)]+[sum(row[i]*b for row,b in zip(A,y))] for i in range(n)]
    threshold=rtol*max(abs(G[i][j]) for i in range(n) for j in range(n))
    for k in range(n):
        pivot=max(range(k,n),key=lambda i:abs(G[i][k]));G[k],G[pivot]=G[pivot],G[k]
        if abs(G[k][k])<=threshold:return dict(status='pivot',beta=None)
        for i in range(k+1,n):
            f=G[i][k]/G[k][k]
            for j in range(k+1,n+1):G[i][j]-=f*G[k][j]
    b=[0.]*n
    for i in range(n-1,-1,-1):b[i]=(G[i][n]-sum(G[i][j]*b[j] for j in range(i+1,n)))/G[i][i]
    return dict(status='ok',beta=b)

def dataset(mode,delta,level=1):
    if mode not in (0,1,2) or level not in (0,1,2,3) or not isfinite(delta):raise ValueError('Controles do roteiro')
    eps=[1.,1e-4,1e-8,0.][level];xs=[-2.,-1.,0.,1.,2.]
    y=[1+.5*x+.5*x*x+(delta if x==0 else 0) for x in xs]
    def basis(x):return [1.,x] if mode==0 else [1.,x,x*x] if mode==1 else [1.,x,x+eps*x*x]
    return dict(xs=xs,y=y,A=[basis(x) for x in xs],eps=eps)

if __name__=='__main__':
    for level in range(4):
        d=dataset(2,0,level);r=qr_fit(d['A'],d['y']);print(level,r['status'],r['beta'])
