"""Fila FIFO ligada: contrato público e diagnóstico de representação."""
class _Node:
    def __init__(self,value):self.value=value;self.next=None


class LinkedQueue:
    def __init__(self):self._head=None;self._tail=None;self._size=0
    def __len__(self):return self._size
    def enqueue(self,value):
        node=_Node(value)
        if self._tail is None:self._head=node
        else:self._tail.next=node
        self._tail=node;self._size+=1
    def peek(self):
        if self._head is None:raise IndexError('Fila vazia')
        return self._head.value
    def dequeue(self):
        value=self.peek();self._head=self._head.next;self._size-=1
        if self._head is None:self._tail=None
        return value
    def validate(self):
        # Diagnóstico O(n); não chamado em cada operação pública O(1).
        seen=set();node=self._head;last=None
        while node is not None:
            if id(node) in seen:raise ValueError('Ciclo na cadeia')
            seen.add(id(node));last=node;node=node.next
        if len(seen)!=self._size or last is not self._tail:
            raise ValueError('Contagem ou cauda inconsistente')
        if self._size<0 or (self._head is None)!=(self._tail is None):
            raise ValueError('Estado vazio inconsistente')
        return True
    def values(self):
        self.validate();out=[];node=self._head
        while node is not None:out.append(node.value);node=node.next
        return tuple(out)  # Retrato raso O(n), não cópia profunda dos valores.


if __name__=='__main__':
    q=LinkedQueue()
    for value in ('A','B','C'):q.enqueue(value)
    print(q.values());print('Retirada:',q.dequeue());print(q.values())
    while len(q):q.dequeue()
    q.enqueue('D');print('Após esvaziar e reutilizar:',q.values())
    q.validate()
