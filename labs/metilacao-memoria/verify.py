"""Enumeração de descendentes de um sítio abstrato; não simula metiltransferases."""
from fractions import Fraction as Q

def descendants(population,maintain=False):
    children=[]
    for left,right in population:
        for old in (left,right):
            child=(old,0)
            if maintain and old:child=(1,1)
            children.append(child)
    return children

if __name__=='__main__':
    for maintain in (False,True):
        population=[(1,1)]
        for n in range(11):
            assert len(population)==2**n
            marks=sum(sum(x) for x in population)
            assert marks==(2**(n+1) if maintain else 2)
            assert Q(marks,2*len(population))==(1 if maintain else Q(1,2**n))
            if n and not maintain:
                assert sum(sum(x)==1 for x in population)==2
                assert sum(sum(x)==0 for x in population)==2**n-2
            population=descendants(population,maintain)
    print('22 estados de população: rodadas 0–10 com e sem manutenção ideal; contagens e frações conferidas.')
