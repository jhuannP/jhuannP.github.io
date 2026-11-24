"""Referência racional para sistemas pequenos; sem tolerância de singularidade."""
from fractions import Fraction as Q

def rational(x):
    if type(x) not in (int,Q):raise ValueError('use int ou Fraction')
    return Q(x)

def solve(A,b):
    n=len(A)
    if n==0 or len(b)!=n or any(len(row)!=n for row in A):raise ValueError('quadrado não vazio')
    U=[[rational(v) for v in row] for row in A];rhs=[rational(v) for v in b]
    steps=[]
    for k in range(n):
        p=max(range(k,n),key=lambda i:abs(U[i][k]))
        if U[p][k]==0:raise ArithmeticError('pivô exato zero; não classifica a família de soluções')
        U[k],U[p]=U[p],U[k];rhs[k],rhs[p]=rhs[p],rhs[k]
        multipliers=[]
        for i in range(k+1,n):
            factor=U[i][k]/U[k][k];multipliers.append((i,factor));U[i][k]=Q(0)
            for j in range(k+1,n):U[i][j]-=factor*U[k][j]
            rhs[i]-=factor*rhs[k]
        steps.append({'column':k,'pivot_row':p,'multipliers':tuple(multipliers)})
    x=[Q(0)]*n
    for i in range(n-1,-1,-1):x[i]=(rhs[i]-sum(U[i][j]*x[j] for j in range(i+1,n)))/U[i][i]
    return {'x':x,'U':U,'rhs':rhs,'steps':steps}

def residual(A,x,b):
    n=len(A)
    if not n or len(b)!=n or len(x)!=n or any(len(r)!=n for r in A):raise ValueError('dimensões incompatíveis')
    return [rational(v)-sum(rational(a)*rational(z) for a,z in zip(row,x)) for row,v in zip(A,b)]

def small_pivot_demo():
    # Mesmos dados binários no cálculo float e na referência racional.
    eps=Q(1,2**60);A=[[eps,1],[1,1]];b=[1,2]
    a=float(eps);factor=1/a
    y=(2-factor)/(1-factor);x=(1-y)/a
    return {'A':A,'b':b,'naive':[x,y],'exact':solve(A,b)['x']}

if __name__=='__main__':
    r=solve([[1,2],[3,5]],[5,13])
    assert r['x']==[1,2]
    assert r['U']==[[3,5],[0,Q(1,3)]]
    print('Solução:',r['x'],'; pequeno pivô sem troca:',small_pivot_demo()['naive'])
