"""Ordenação estável por contagem; chaves inteiras em [0,K)."""
def prepare(records,K):
    if isinstance(K,bool) or not isinstance(K,int) or K<1:
        raise ValueError('K inteiro positivo')
    if not isinstance(records,(list,tuple)):
        raise ValueError('Sequência finita de pares(chave,valor)')
    for entry in records:
        if not isinstance(entry,tuple) or len(entry)!=2:
            raise ValueError('Cada registro é uma tupla(chave,valor)')
        key=entry[0]
        if isinstance(key,bool) or not isinstance(key,int) or not 0<=key<K:
            raise ValueError('Chave inteira em[0,K)')
    freq=[0]*K
    for key,_ in records:freq[key]+=1
    starts=[0]*K;total=0
    for key in range(K):
        starts[key]=total
        total+=freq[key]
    return freq,starts

def counting(records,K):
    freq,starts=prepare(records,K)
    cursor=starts.copy();out=[None]*len(records)
    for entry in records:
        key=entry[0]
        out[cursor[key]]=entry
        cursor[key]+=1
    return out

def distribution_trace(records,K):
    freq,starts=prepare(records,K)
    cursor=starts.copy();out=[None]*len(records)
    states=[dict(cursor=cursor.copy(),out=out.copy())]
    for entry in records:
        key=entry[0];out[cursor[key]]=entry;cursor[key]+=1
        states.append(dict(cursor=cursor.copy(),out=out.copy()))
    return dict(freq=freq,starts=starts,states=states)

if __name__=='__main__':
    records=[(2,'A'),(0,'B'),(2,'C'),(1,'D'),(0,'E'),(2,'F')]
    result=counting(records,3)
    assert [v for _,v in result]==['B','E','D','A','C','F']
    print(result)
