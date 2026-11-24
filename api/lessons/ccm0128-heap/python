"""Fila de prioridade mínima com desempate por ordem de inserção."""
class PriorityQueue:
    def __init__(self):self._heap=[];self._ticket=0
    def __len__(self):return len(self._heap)
    @staticmethod
    def _key(entry):return entry[:2]
    def push(self,priority,value):
        if isinstance(priority,bool) or not isinstance(priority,int):
            raise ValueError('Prioridade inteira; menor valor sai primeiro.')
        entry=(priority,self._ticket,value);self._ticket+=1
        self._heap.append(entry);i=len(self._heap)-1
        while i>0:
            parent=(i-1)//2
            if self._key(self._heap[parent])<=self._key(self._heap[i]):break
            self._heap[parent],self._heap[i]=self._heap[i],self._heap[parent];i=parent
    def peek(self):
        if not self._heap:raise IndexError('Fila de prioridade vazia')
        priority,_,value=self._heap[0];return priority,value
    def pop(self):
        result=self.peek();last=self._heap.pop()
        if self._heap:
            self._heap[0]=last;i=0;n=len(self._heap)
            while 2*i+1<n:
                child=2*i+1
                if child+1<n and self._key(self._heap[child+1])<self._key(self._heap[child]):child+=1
                if self._key(self._heap[i])<=self._key(self._heap[child]):break
                self._heap[i],self._heap[child]=self._heap[child],self._heap[i];i=child
        return result
    def validate(self):
        for i in range(1,len(self._heap)):
            if self._key(self._heap[(i-1)//2])>self._key(self._heap[i]):raise ValueError('Ordem do heap quebrada')
        return True
    def entries(self):return tuple(self._heap)  # Retrato raso O(n), sem ordenar.


def trace():
    q=PriorityQueue();removed=[];out=[dict(heap=[],removed=[],action='Estado vazio')]
    actions=[(3,'A'),(1,'B'),(1,'C'),(2,'D'),None,None,(0,'E'),None,None,None]
    for action in actions:
        if action is None:
            priority,value=q.pop();removed.append(value);label='Retirar '+value
        else:
            priority,value=action;q.push(priority,value);label='Inserir '+value+' com prioridade '+str(priority)
        q.validate();out.append(dict(heap=[list(e) for e in q.entries()],removed=list(removed),action=label))
    return out


if __name__=='__main__':
    for i,state in enumerate(trace()):print(i,state)
    print('O vetor é um heap, não uma lista totalmente ordenada.')
