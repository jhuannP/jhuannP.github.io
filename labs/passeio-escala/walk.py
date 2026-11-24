"""Enumeração exata de passeios simétricos pequenos; não simula W contínuo."""
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import comb

def paths(n,step):
    if type(n) is not int or not 0<=n<=10:raise ValueError('n inteiro0..10')
    if type(step) not in (int,Q) or step<=0:raise ValueError('passo racional positivo')
    step=Q(step);result=[]
    for signs in product((-1,1),repeat=n):
        row=[Q(0)]
        for s in signs:row.append(row[-1]+s*step)
        result.append(tuple(row))
    return result

if __name__=='__main__':
    for n in range(9):
        sample=paths(n,Q(1,2));counts=Counter(row[-1] for row in sample);size=2**n
        expected={Q(2*k-n,2):comb(n,k) for k in range(n+1)}
        assert counts==expected
        for j in range(n+1):
            assert sum(row[j] for row in sample)/size==0
            for k in range(n+1):
                covariance=sum(row[j]*row[k] for row in sample)/size
                assert covariance==Q(min(j,k),4)
    sample=paths(4,Q(1,2));counts=Counter(row[-1] for row in sample)
    assert Q(counts[0],len(sample))==Q(3,8)
    assert sum(row[-1]**2 for row in sample)/len(sample)==1
    wrong=paths(4,Q(1,4));assert sum(row[-1]**2 for row in wrong)/len(wrong)==Q(1,4)
    for args in [(True,Q(1,2)),(11,1),(2,0),(2,0.5)]:
        try:paths(*args)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('Lei final reescalada:',{str(k):str(Q(v,len(sample))) for k,v in sorted(counts.items())})
    print('Distribuições binomiais e covariâncias conferidas para n=0..8.')
