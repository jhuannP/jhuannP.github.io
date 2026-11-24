"""Inserção instrumentada: comparações entre chaves e deslocamentos separados.
Chaves devem ter ordem coerente, sem NaN; comparabilidade não validada exaustivamente.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class Result:
    items:tuple
    comparisons:int
    shifts:int
    writes:int
    trace:tuple

def insertion(values,key=None,capture=False):
    if key is not None and not callable(key):raise TypeError("key precisa ser chamável.")
    if type(capture) is not bool:raise TypeError("capture precisa ser bool.")
    items=list(values)
    keys=[v if key is None else key(v) for v in items]
    comparisons=shifts=writes=0
    history=[tuple(items)] if capture else []
    for i in range(1,len(items)):
        value=items[i];rank=keys[i];j=i-1
        while j>=0:
            comparisons+=1
            if not keys[j]>rank:break
            items[j+1]=items[j];keys[j+1]=keys[j]
            j-=1;shifts+=1;writes+=1
        items[j+1]=value;keys[j+1]=rank;writes+=1
        if capture:history.append(tuple(items))
    return Result(tuple(items),comparisons,shifts,writes,tuple(history))

if __name__=='__main__':
    print(insertion([4,1,3,2],capture=True))
    records=[(2,'A'),(1,'B'),(2,'C'),(1,'D')]
    print(insertion(records,key=lambda r:r[0]))
