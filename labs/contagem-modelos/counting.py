"""Contagens exatas em quatro modelos finitos, sem restrições adicionais."""
from math import comb,perm

def count(n,k,*,ordered,repetition):
    if any(type(x) is not int or x<0 for x in (n,k)):
        raise ValueError('n,k devem ser int não negativos, sem bool')
    if type(ordered) is not bool or type(repetition) is not bool:
        raise ValueError('Declare ordered/repetition como bool')
    if k==0:return 1
    if n==0 or (not repetition and k>n):return 0
    if ordered:return n**k if repetition else perm(n,k)
    return comb(n+k-1,k) if repetition else comb(n,k)

if __name__=='__main__':
    for order in (True,False):
        for repeat in (False,True):
            print('Ordem:',order,'Repetição:',repeat,'Total:',count(5,3,ordered=order,repetition=repeat))
