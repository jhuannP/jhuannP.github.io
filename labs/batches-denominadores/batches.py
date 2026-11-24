"""Partições e gradientes escalares com frações exatas, sem framework."""
from fractions import Fraction as Q

def partition(values,B,drop=False):
    if isinstance(B,bool) or not isinstance(B,int) or B<=0:raise ValueError("B inteiro positivo")
    if not isinstance(drop,bool):raise ValueError("drop booleano")
    a=list(values);groups=[a[i:i+B] for i in range(0,len(a),B)]
    if drop and groups and len(groups[-1])<B:groups.pop()
    return groups

def mean(values):
    a=list(values)
    if not a or any(isinstance(v,bool) or not isinstance(v,(int,Q)) for v in a):
        raise ValueError("Lista não vazia de racionais")
    return sum(map(Q,a))/len(a)

def combine(rows):
    # Cada par é (denominador efetivo, média nesse denominador).
    a=list(rows)
    if not a:raise ValueError("Nenhuma contribuição")
    for n,m in a:
        if isinstance(n,bool) or not isinstance(n,int) or n<=0:raise ValueError("Contagem positiva")
        if isinstance(m,bool) or not isinstance(m,(int,Q)):raise ValueError("Média racional")
    return sum(n*Q(m) for n,m in a)/sum(n for n,m in a)

def grad(w,targets):return 2*mean([w-t for t in targets])

def compositions(n):
    # Todas as partições contíguas não vazias da lista de n itens.
    for mask in range(1<<(n-1)):
        out=[];start=0
        for i in range(n-1):
            if mask&(1<<i):out.append((start,i+1));start=i+1
        out.append((start,n));yield out

def verify():
    profiles=0;gradients=0
    for n in range(1,9):
        recipes=([Q(i%3+1) for i in range(n)],[Q(0)]*(n-1)+[Q(5)],[Q(i,2) for i in range(n)])
        for values in recipes:
            for slices in compositions(n):
                groups=[values[a:b] for a,b in slices]
                assert combine([(len(g),mean(g)) for g in groups])==mean(values)
                for w in map(Q,(-1,0,2)):
                    assert combine([(len(g),grad(w,g)) for g in groups])==grad(w,values)
                    gradients+=1
                profiles+=1
    values=[Q(1)]*4+[Q(2)]*4+[Q(3)]*2
    groups=partition(values,4)
    assert [len(g) for g in groups]==[4,4,2]
    assert combine([(len(g),mean(g)) for g in groups])==Q(9,5)
    assert mean([mean(g) for g in groups])==2
    kept=partition(values,4,drop=True)
    assert mean([v for g in kept for v in g])==Q(3,2)
    assert partition([],4)==[]
    # Mesmo estado w=0: acumular equivale ao batch inteiro, sem atualizar no meio.
    targets=[Q(1),Q(1),Q(3)];micro=[targets[:2],targets[2:]];eta=Q(1,10)
    full=grad(Q(0),targets)
    accumulated=combine([(len(g),grad(Q(0),g)) for g in micro])
    assert full==accumulated==-Q(10,3)
    assert -eta*full==Q(1,3)
    assert mean([grad(Q(0),g) for g in micro])==-4
    def sequential(groups):
        w=Q(0)
        for g in groups:w-=eta*grad(w,g)
        return w
    assert sequential(micro)==Q(19,25)
    assert sequential(list(reversed(micro)))==Q(17,25)
    # Mesmo ponderando cada passo, mudar w entre gradientes altera o procedimento.
    w=Q(0)
    for g in micro:w-=eta*Q(len(g),3)*grad(w,g)
    assert w==Q(73,225)!=Q(1,3)
    assert mean([1,1,1,1,5])==Q(9,5)
    assert mean([mean([1,1,1,1]),mean([5])])==3
    for bad in (0,True,1.5):
        try:partition(values,bad)
        except ValueError:pass
        else:raise AssertionError("batch")
    for call in (lambda:mean([]),lambda:combine([]),lambda:combine([(0,Q(1))])):
        try:call()
        except ValueError:pass
        else:raise AssertionError("denominador")
    print(f"{profiles} agregações de perda e {gradients} agregações de gradiente conferidas")
    print("Acumulado: w=1/3; passos sequenciais:19/25 e17/25; não são equivalentes")

if __name__=='__main__':verify()
