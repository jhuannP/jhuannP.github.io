import unittest,itertools
from collections import deque
from random import Random
try:
    from .structures import LinkedStack,CircularQueue,insert_cost,queue_trace
except ImportError:
    from structures import LinkedStack,CircularQueue,insert_cost,queue_trace

class StructuresTests(unittest.TestCase):
    def test_stack_against_list(self):
        rng=Random(42);stack=LinkedStack();reference=[]
        for n in range(1000):
            if not reference or rng.random()<.55:
                value=None if n%10==0 else n
                stack.push(value);reference.append(value)
            else:self.assertEqual(stack.pop(),reference.pop())
            self.assertEqual(len(stack),len(reference))
            self.assertEqual(stack.values(),reference[::-1])
            if reference:self.assertEqual(stack.peek(),reference[-1])
        while reference:self.assertEqual(stack.pop(),reference.pop())
        for method in [stack.pop,stack.peek]:
            with self.assertRaises(IndexError):method()

    def test_all_small_operation_sequences(self):
        for length in range(9):
            for ops in itertools.product([0,1],repeat=length):
                for capacity in [2,3,4]:
                    q=CircularQueue(capacity);reference=deque()
                    for i,op in enumerate(ops):
                        if op:q.enqueue(i);reference.append(i)
                        elif reference:self.assertEqual(q.dequeue(),reference.popleft())
                        else:
                            before=q.snapshot()
                            with self.assertRaises(IndexError):q.dequeue()
                            self.assertEqual(q.snapshot(),before)
                        self.assertTrue(q.invariant())
                        self.assertEqual(q.values(),list(reference))
                        self.assertEqual(len(q),len(reference))

    def test_wrap_growth_none_and_independence(self):
        q=CircularQueue();other=CircularQueue()
        q.enqueue(None);q.enqueue('B');self.assertIsNone(q.dequeue())
        q.enqueue('C');q.enqueue('D') # Cresce com cabeça !=0.
        self.assertEqual(q.values(),['B','C','D']);self.assertEqual(q.capacity,4)
        self.assertEqual(q.copied,2);self.assertEqual(q.snapshot()['head'],0)
        while len(q):q.dequeue()
        self.assertEqual(q.snapshot()['slots'],[None]*4)
        q.enqueue('X');self.assertEqual(q.dequeue(),'X');self.assertEqual(len(other),0)
        self.assertEqual(queue_trace()[-1]['logical'],['G','H'])

    def test_amortized_bound(self):
        for n in range(1,513):
            cost=insert_cost(n)
            self.assertEqual(cost['inserted'],n)
            self.assertLess(cost['copied'],2*n)
            self.assertLess(cost['item_writes'],3*n)
            if n>=2:self.assertLess(cost['capacity'],2*n)
        self.assertEqual(insert_cost(64)['copied'],62)
        self.assertEqual(insert_cost(64)['item_writes'],126)

    def test_contracts_and_peek(self):
        for bad in [0,1,-2,True,2.5,'2']:
            with self.assertRaises(ValueError):CircularQueue(bad)
        q=CircularQueue()
        with self.assertRaises(IndexError):q.peek()
        q.enqueue('A');before=q.snapshot();self.assertEqual(q.peek(),'A')
        self.assertEqual(q.snapshot(),before)
        for bad in [-1,True,1.5]:
            with self.assertRaises(ValueError):insert_cost(bad)

if __name__=='__main__':unittest.main()
