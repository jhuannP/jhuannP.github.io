"""Busca por ocorrência e limite inferior. Rotinas próprias, contratos distintos."""
DATASETS=((1,3,5,7,9,11,13,15),(1,3,3,3,5,7,7,9),(),(4,))

def busca_binaria(values,target):
    """Uma ocorrência ou -1. Pré-condição: ordem crescente não estrita."""
    low,high=0,len(values)-1
    while low<=high:
        mid=(low+high)//2
        if values[mid]==target:return mid
        if values[mid]<target:low=mid+1
        else:high=mid-1
    return -1

def lower_bound(values,target):
    """Primeira posição p com values[p]>=target, ou n. Não valida ordem."""
    low,high=0,len(values)
    while low<high:
        mid=(low+high)//2
        if values[mid]<target:low=mid+1
        else:high=mid
    return low

def trace(values,target):
    """Cliente didático validado O(n), mais busca/registro O(log(n+1))."""
    if not isinstance(values,(list,tuple)) or isinstance(target,bool) or not isinstance(target,int):
        raise ValueError('Lista/tupla de inteiros e alvo inteiro')
    if any(isinstance(x,bool) or not isinstance(x,int) for x in values):raise ValueError('Inteiros, sem bool')
    if any(a>b for a,b in zip(values,values[1:])):raise ValueError('Ordem crescente não estrita')
    rows=[];low,high=0,len(values)
    while low<high:
        mid=(low+high)//2;less=values[mid]<target
        nxt_low,nxt_high=(mid+1,high) if less else (low,mid)
        rows.append(dict(low=low,high=high,mid=mid,value=values[mid],less=less,
                         next_low=nxt_low,next_high=nxt_high))
        low,high=nxt_low,nxt_high
    position=low
    equality=1 if position<len(values) else 0
    found=position if equality and values[position]==target else -1
    rows.append(dict(low=low,high=high,mid=None,value=None,less=None,next_low=low,next_high=high))
    return dict(position=position,found=found,rows=rows,ordered_comparisons=len(rows)-1,
                equality_comparisons=equality,total_key_comparisons=len(rows)-1+equality)

if __name__=='__main__':
    assert busca_binaria(DATASETS[0],11)==5
    assert busca_binaria(DATASETS[1],3)==3  # não promete a primeira
    assert lower_bound(DATASETS[1],3)==1
    assert lower_bound(DATASETS[1],4)==4
    assert lower_bound([],7)==0
    print(trace(DATASETS[1],3))
