"""Mergesort didático instrumentado. Comparações de chaves, não tempo real."""
from itertools import permutations,product
from collections import Counter

def sort_count(values,key=lambda v:v):
    stats={"comparisons":0,"calls":0}
    def rec(a):
        stats["calls"]+=1
        if len(a)<=1:return list(a)
        middle=len(a)//2;left=rec(a[:middle]);right=rec(a[middle:])
        out=[];i=j=0
        while i<len(left) and j<len(right):
            stats["comparisons"]+=1
            if key(left[i])<=key(right[j]):out.append(left[i]);i+=1
            else:out.append(right[j]);j+=1
        out.extend(left[i:]);out.extend(right[j:])
        return out
    return rec(list(values)),stats

def bound(n):
    if isinstance(n,bool) or not isinstance(n,int) or n<0:raise ValueError("n inteiro não negativo")
    if n<=1:return 0
    h=(n-1).bit_length()
    return n*h-(1<<h)+1

def verify():
    permutations_checked=0
    for n in range(9):
        observed=0
        for values in permutations(range(n)):
            before=list(values);out,stats=sort_count(before)
            assert out==list(range(n)) and before==list(values)
            assert stats["calls"]==(2*n-1 if n else 1)
            assert stats["comparisons"]<=bound(n)
            observed=max(observed,stats["comparisons"]);permutations_checked+=1
        assert observed==bound(n)
    stable_cases=0
    for n in range(8):
        for keys in product(range(3),repeat=n):
            tagged=list(zip(keys,range(n)));original=tagged[:]
            out,stats=sort_count(tagged,key=lambda pair:pair[0])
            assert tagged==original and Counter(out)==Counter(tagged)
            assert out==sorted(tagged,key=lambda pair:pair[0])
            assert all(out[i][0]<=out[i+1][0] for i in range(len(out)-1))
            for k in range(3):
                assert [label for value,label in out if value==k]==[label for value,label in tagged if value==k]
            stable_cases+=1
    _,stats=sort_count(list(range(8)));assert stats["comparisons"]==12
    assert bound(8)==17 and bound(5)==8
    records=[(2,'A'),(1,'B'),(2,'C'),(1,'D')]
    out,_=sort_count(records,key=lambda pair:pair[0])
    assert out==[(1,'B'),(1,'D'),(2,'A'),(2,'C')]
    # Um único empate já basta para refutar a escolha da direita como regra estável.
    left=(1,'A');right=(1,'B')
    unstable=[left,right] if left[0]<right[0] else [right,left]
    assert unstable==[(1,'B'),(1,'A')]
    for n in (-1,True,1.5):
        try:bound(n)
        except ValueError:pass
        else:raise AssertionError("n inválido")
    print(f"{permutations_checked} permutações e {stable_cases} listas com chaves repetidas conferidas")
    print("n=8: máximo17 comparações; entrada ordenada12. Exemplo estável:",out)

if __name__=='__main__':verify()
