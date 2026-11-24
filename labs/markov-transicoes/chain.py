"""Propagação exata de distribuições finitas e exemplo de dois estados."""
from fractions import Fraction as F

def probability(x):
    if isinstance(x,bool) or not isinstance(x,(int,F)):raise TypeError('Use int ou Fraction.')
    x=F(x)
    if not 0<=x<=1:raise ValueError('Probabilidade entre zero e um.')
    return x

def vector(values,n=None):
    if not isinstance(values,(list,tuple)) or not 1<=len(values)<=8:raise ValueError('Vetor de 1–8 estados.')
    if n is not None and len(values)!=n:raise ValueError('Dimensões incompatíveis.')
    values=tuple(map(probability,values))
    if sum(values)!=1:raise ValueError('A soma exata deve ser um.')
    return values

def kernel(P):
    if not isinstance(P,(list,tuple)) or not 1<=len(P)<=8:raise ValueError('Matriz de 1–8 estados.')
    return tuple(vector(row,len(P)) for row in P)

def step(p,P):
    P=kernel(P);p=vector(p,len(P))
    return tuple(sum(p[i]*P[i][j] for i in range(len(P))) for j in range(len(P)))

def steps(n):
    if isinstance(n,bool) or not isinstance(n,int):raise TypeError('Número inteiro de passos.')
    if not 0<=n<=100:raise ValueError('Use 0–100 passos.')
    return n

def orbit(p,P,n):
    n=steps(n);P=kernel(P);p=vector(p,len(P));result=[p]
    for _ in range(n):
        p=step(p,P);result.append(p)
    return tuple(result)

def two_state(alpha,beta):
    alpha,beta=map(probability,(alpha,beta))
    return ((1-alpha,alpha),(beta,1-beta))

def stationary_two(alpha,beta):
    alpha,beta=map(probability,(alpha,beta))
    if alpha+beta==0:raise ValueError('Identidade: estacionária não é única.')
    return (beta/(alpha+beta),alpha/(alpha+beta))

def first_hit_tail(alpha,n):
    """Partindo de A, probabilidade de a primeira chegada a B ocorrer depois de n."""
    alpha=probability(alpha);n=steps(n)
    return (1-alpha)**n

def first_hit_mean(alpha):
    alpha=probability(alpha)
    if alpha==0:raise ValueError('B não é atingido a partir de A nesse modelo.')
    return 1/alpha

P=two_state(F(1,5),F(2,5))
if __name__=='__main__':
    path=orbit((1,0),P,4)
    print('Distribuições:',path)
    pi=stationary_two(F(1,5),F(2,5))
    assert path[2]==(F(18,25),F(7,25))
    assert path[4][0]-pi[0]==F(16,1875)
    print('Erro após quatro passos:',path[4][0]-pi[0])
    print('Primeira chegada média em passos:',first_hit_mean(F(1,5)))
