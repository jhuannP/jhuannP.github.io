"""Encadeamento separado para strings; algoritmo didático, não o dict do Python."""
from math import isfinite

def raw_hash(key,mode='sum'):
    if not isinstance(key,str):raise TypeError('Chave deve ser string')
    if mode=='constant':return 0
    if mode=='sum':return sum(ord(c) for c in key)
    if mode=='poly':
        value=0
        for c in key:value=(31*value+ord(c))%(2**32)
        return value
    raise ValueError('Hash sum, poly ou constant')

class HashTable:
    def __init__(self,capacity=4,max_load=.75,mode='sum'):
        if isinstance(capacity,bool) or not isinstance(capacity,int) or capacity<2:
            raise ValueError('Capacidade inteira >=2')
        if isinstance(max_load,bool) or not isinstance(max_load,(int,float)) or not isfinite(max_load) or not .5<=max_load<=2:
            raise ValueError('Fator máximo finito entre 0.5 e 2')
        raw_hash('',mode)
        self._buckets=[[] for _ in range(capacity)]
        self._size=0;self.max_load=max_load;self.mode=mode;self.migrated=0

    def __len__(self):return self._size

    @property
    def capacity(self):return len(self._buckets)

    def index(self,key):return raw_hash(key,self.mode)%self.capacity

    def _grow(self):
        new=[[] for _ in range(2*self.capacity)]
        for bucket in self._buckets:
            for key,value in bucket:
                new[raw_hash(key,self.mode)%len(new)].append((key,value))
                self.migrated+=1
        self._buckets=new

    def put(self,key,value):
        bucket=self._buckets[self.index(key)]
        for i,(stored,_) in enumerate(bucket):
            if stored==key:
                bucket[i]=(key,value);return # Atualizar não cresce nem cria par.
        if self._size+1>self.max_load*self.capacity:self._grow()
        self._buckets[self.index(key)].append((key,value))
        self._size+=1

    def get(self,key):
        for stored,value in self._buckets[self.index(key)]:
            if stored==key:return value
        raise KeyError(key)

    def delete(self,key):
        bucket=self._buckets[self.index(key)]
        for i,(stored,value) in enumerate(bucket):
            if stored==key:
                bucket.pop(i);self._size-=1;return value
        raise KeyError(key)

    def snapshot(self):
        return dict(capacity=self.capacity,size=self._size,load=self._size/self.capacity,
                    buckets=[bucket[:] for bucket in self._buckets],migrated=self.migrated,
                    longest=max(map(len,self._buckets)))

    def invariant(self):
        keys=[k for bucket in self._buckets for k,_ in bucket]
        return (len(keys)==self._size and len(set(keys))==len(keys)
                and self._size<=self.max_load*self.capacity
                and all(self.index(k)==i for i,bucket in enumerate(self._buckets) for k,_ in bucket))

OPERATIONS=(('put','ab',1),('put','ba',2),('put','ad',3),('put','x',4),
            ('put','ab',9),('delete','ba',None),('put','y',5),('put','z',6))

def trace(max_load=.75,mode='sum'):
    table=HashTable(max_load=max_load,mode=mode)
    states=[dict(action='Inicial',**table.snapshot())]
    for operation,key,value in OPERATIONS:
        if operation=='put':table.put(key,value);action='Guardar '+key+'='+str(value)
        else:table.delete(key);action='Apagar '+key
        states.append(dict(action=action,**table.snapshot()))
    return states

if __name__=='__main__':
    for row in trace():
        print(row['action'],'n:',row['size'],'C:',row['capacity'],
              'carga:',row['load'],'maior balde:',row['longest'],'migrados:',row['migrated'])
    table=HashTable();table.put('ab',1);table.put('ba',2);table.put('ab',3)
    assert table.get('ab')==3 and table.get('ba')==2
