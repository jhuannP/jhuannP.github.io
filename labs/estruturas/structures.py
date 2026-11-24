"""Tipos próprios para estudar LIFO, FIFO e custo amortizado."""

class Node:
    def __init__(self,value,next_node=None):
        self.value=value
        self.next=next_node

class LinkedStack:
    def __init__(self):
        self._top=None
        self._size=0

    def __len__(self):return self._size

    def push(self,value):
        self._top=Node(value,self._top)
        self._size+=1

    def peek(self):
        if self._top is None:raise IndexError('Pilha vazia')
        return self._top.value

    def pop(self):
        value=self.peek()
        self._top=self._top.next
        self._size-=1
        return value

    def values(self):
        # Retrato para ensino: O(n), não parte do custo de push/pop.
        result=[];node=self._top
        while node is not None:
            result.append(node.value);node=node.next
        return result

class CircularQueue:
    def __init__(self,capacity=2):
        if isinstance(capacity,bool) or not isinstance(capacity,int) or capacity<2:
            raise ValueError('Capacidade inicial inteira >=2')
        self._data=[None]*capacity
        self._head=0
        self._size=0
        self.copied=0
        self.inserted=0

    def __len__(self):return self._size

    @property
    def capacity(self):return len(self._data)

    def values(self):
        return [self._data[(self._head+i)%self.capacity] for i in range(self._size)]

    def enqueue(self,value):
        if self._size==self.capacity:
            old=self._data
            size=len(old)
            new=[None]*(2*size)
            for i in range(self._size):new[i]=old[(self._head+i)%size]
            self.copied+=self._size
            self._data=new
            self._head=0
        tail=(self._head+self._size)%self.capacity
        self._data[tail]=value
        self._size+=1
        self.inserted+=1

    def peek(self):
        if not self._size:raise IndexError('Fila vazia')
        return self._data[self._head]

    def dequeue(self):
        value=self.peek()
        self._data[self._head]=None # Libera a referência retirada.
        self._head=(self._head+1)%self.capacity
        self._size-=1
        return value

    def snapshot(self):
        # Consulta O(capacidade+n), só para inspeção didática.
        return dict(slots=self._data[:],head=self._head,size=self._size,
                    capacity=self.capacity,logical=self.values(),copied=self.copied,
                    inserted=self.inserted)

    def invariant(self):
        occupied={(self._head+i)%self.capacity for i in range(self._size)}
        return (0<=self._head<self.capacity and 0<=self._size<=self.capacity
                and all(x is None for i,x in enumerate(self._data) if i not in occupied))

OPERATIONS=(('in','A'),('in','B'),('out',None),('in','C'),('in','D'),('in','E'),
            ('out',None),('out',None),('in','F'),('in','G'),('in','H'),
            ('out',None),('out',None),('out',None))

def queue_trace(capacity=2):
    q=CircularQueue(capacity)
    trace=[dict(action='Inicial',removed=None,**q.snapshot())]
    for operation,value in OPERATIONS:
        removed=None
        if operation=='in':q.enqueue(value);action='Entrar '+value
        else:removed=q.dequeue();action='Retirar '+removed
        trace.append(dict(action=action,removed=removed,**q.snapshot()))
    return trace

def insert_cost(n):
    if isinstance(n,bool) or not isinstance(n,int) or n<0:raise ValueError('n inteiro >=0')
    q=CircularQueue()
    for i in range(n):q.enqueue(i)
    return dict(inserted=q.inserted,copied=q.copied,capacity=q.capacity,
                item_writes=q.inserted+q.copied)

if __name__=='__main__':
    stack=LinkedStack()
    for item in ['A','B','C']:stack.push(item)
    assert [stack.pop() for _ in range(3)]==['C','B','A']
    for row in queue_trace():
        print(row['action'],'fila:',row['logical'],'cabeça:',row['head'],
              'capacidade:',row['capacity'],'copiados:',row['copied'])
    print('64 inserções:',insert_cost(64))
