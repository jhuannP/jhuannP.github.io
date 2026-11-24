import itertools
import unittest
from collections import deque
from .experiment import LinkedQueue,_Node

class QueueContractTests(unittest.TestCase):
    def test_against_deque_for_all_small_traces(self):
        for trace in itertools.product(range(4),repeat=6):
            q=LinkedQueue();reference=deque()
            for op in trace:
                if op<2:q.enqueue(op);reference.append(op)
                elif reference:
                    expected=reference.popleft() if op==2 else reference[0]
                    actual=q.dequeue() if op==2 else q.peek()
                    self.assertEqual(actual,expected)
                else:
                    with self.assertRaises(IndexError):q.dequeue() if op==2 else q.peek()
                self.assertTrue(q.validate());self.assertEqual(q.values(),tuple(reference));self.assertEqual(len(q),len(reference))

    def test_drain_and_reuse(self):
        q=LinkedQueue()
        for _ in range(10):
            q.enqueue(None);self.assertIsNone(q.dequeue());self.assertEqual(q.values(),())
            self.assertIsNone(q._head);self.assertIsNone(q._tail)
        q.enqueue('A');q.enqueue('B');self.assertEqual((q.dequeue(),q.dequeue()),('A','B'))

    def test_diagnostic_catches_corruption(self):
        q=LinkedQueue();q.enqueue(1);q._head.next=q._head
        with self.assertRaises(ValueError):q.validate()
        q=LinkedQueue();q.enqueue(1);q._tail=_Node(2)
        with self.assertRaises(ValueError):q.validate()
        q=LinkedQueue();q._size=1
        with self.assertRaises(ValueError):q.validate()

    def test_shallow_payload_alias_is_explicit(self):
        q=LinkedQueue();value=[1];q.enqueue(value);snapshot=q.values();value.append(2)
        self.assertIs(snapshot[0],value);self.assertEqual(q.peek(),[1,2]);self.assertEqual(len(q),1)
