"""Rainhas em tabuleiro pequeno: busca com poda e restauração de estado."""
from itertools import permutations


def size(n):
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=8:
        raise ValueError('n inteiro entre 1 e 8 para este laboratório.')
    return n


def allowed(prefix,column):
    row=len(prefix)
    return all(column!=c and abs(column-c)!=row-r for r,c in enumerate(prefix))


def solve(n):
    n=size(n)
    chosen=[]
    solutions=[]
    stats=dict(nodes=0,attempts=0,pruned=0)
    def visit():
        stats['nodes']+=1
        if len(chosen)==n:
            solutions.append(tuple(chosen))  # Cópia: não guardar a lista mutável.
            return
        for column in range(n):
            stats['attempts']+=1
            if not allowed(chosen,column):
                stats['pruned']+=1
                continue
            chosen.append(column)
            try:
                visit()
            finally:
                chosen.pop()  # Restaurar o prefixo antes de testar outra escolha.
    visit()
    assert chosen==[]
    return solutions,stats


def exhaustive(n):
    n=size(n)
    # Referência independente: todas as permutações e unicidade das diagonais.
    return [p for p in permutations(range(n))
            if len({r+c for r,c in enumerate(p)})==n
            and len({r-c for r,c in enumerate(p)})==n]


if __name__=='__main__':
    for n in (1,2,3,4,5):
        solutions,stats=solve(n)
        print('n=',n,'soluções=',len(solutions),'estatísticas=',stats)
        if n==4:print('Colunas por linha, índices desde zero:',solutions)
    print('Nó conta uma chamada com prefixo válido; tentativa conta testar uma coluna.')
    print('Poda rejeita conflito já presente; não elimina solução possível.')
