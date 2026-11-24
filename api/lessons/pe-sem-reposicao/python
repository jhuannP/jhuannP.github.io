"""Urna de dois tipos, sorteio uniforme de objetos identificáveis; sem dependências."""
from fractions import Fraction as Q
from math import comb

def validate(N, K, n, replacement=False):
    if type(replacement) is not bool:
        raise ValueError("replacement deve ser bool")
    if any(type(v) is not int for v in (N,K,n)):
        raise ValueError("N, K e n devem ser inteiros; bool não é contagem")
    if N < 1 or not 0 <= K <= N or n < 0 or (not replacement and n > N):
        raise ValueError("Exija N>=1, 0<=K<=N e tamanho amostral permitido")

def distribution(N, K, n, replacement=False):
    """Tupla P(X=k), k=0,...,n, incluindo zeros fora do suporte."""
    validate(N,K,n,replacement)
    if replacement:
        p=Q(K,N)
        return tuple(comb(n,k)*p**k*(1-p)**(n-k) for k in range(n+1))
    lo,hi=max(0,n-(N-K)),min(n,K)
    return tuple(Q(comb(K,k)*comb(N-K,n-k),comb(N,n))
                 if lo<=k<=hi else Q(0) for k in range(n+1))

def path_probability(N, K, colors):
    """Probabilidade de uma sequência de cores V/A, sem reposição."""
    colors=tuple(colors)
    validate(N,K,len(colors))
    if any(c not in ("V","A") for c in colors):
        raise ValueError("Use V para vermelha e A para azul")
    red,blue=K,N-K
    result=Q(1)
    for c in colors:
        available=red if c=="V" else blue
        if not available:
            return Q(0)
        result *= Q(available,red+blue)
        if c=="V":red-=1
        else:blue-=1
    return result

if __name__ == "__main__":
    exact=distribution(5,3,2)
    independent=distribution(5,3,2,replacement=True)
    assert exact==(Q(1,10),Q(3,5),Q(3,10))
    assert path_probability(5,3,"VA")==Q(3,10)
    print("Sem reposição, k=0,1,2:",exact)
    print("Com reposição, k=0,1,2:",independent)
    for label,d in [("sem",exact),("com",independent)]:
        mean=sum(k*p for k,p in enumerate(d))
        variance=sum((k-mean)**2*p for k,p in enumerate(d))
        print(label,"média",mean,"variância",variance)
