"""Contagem de termos LS numa única subcamada equivalente s,p,d; sem energias."""
from collections import Counter
from itertools import combinations

def histogram(l,n):
    if isinstance(l,bool) or not isinstance(l,int) or not 0<=l<=2:
        raise ValueError('l inteiro entre0 e2')
    if isinstance(n,bool) or not isinstance(n,int) or not 0<=n<=2*(2*l+1):
        raise ValueError('Número de elétrons incompatível')
    orbitals=tuple((m,s2) for m in range(-l,l+1) for s2 in (-1,1))
    return Counter((sum(m for m,s in selected),sum(s for m,s in selected))
                   for selected in combinations(orbitals,n))

def terms(l,n):
    remaining=histogram(l,n);out=[]
    while any(remaining.values()):
        # Maior projeção de spin ainda disponível, depois maior ML nessa linha.
        S2=max(s for (m,s),count in remaining.items() if count)
        L=max(m for (m,s),count in remaining.items() if count and s==S2)
        if S2<0 or L<0:raise RuntimeError('Histograma residual inválido')
        for m in range(-L,L+1):
            for s2 in range(-S2,S2+1,2):
                remaining[m,s2]-=1
                if remaining[m,s2]<0:raise RuntimeError('Decomposição inconsistente')
        out.append((L,S2))
    return tuple(out)

def j_values2(L,S2):
    if any(isinstance(v,bool) or not isinstance(v,int) or v<0 for v in (L,S2)):
        raise ValueError('L e2S inteiros não negativos')
    return tuple(range(abs(2*L-S2),2*L+S2+1,2))

if __name__=='__main__':
    for L,S2 in terms(2,2):
        print('L=',L,'2S=',S2,'dimensão=',(2*L+1)*(S2+1),'2J=',j_values2(L,S2))
    print('microestados=',sum(histogram(2,2).values()))
