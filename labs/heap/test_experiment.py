import itertools
import unittest
from .experiment import PriorityQueue,trace

class HeapTests(unittest.TestCase):
    def test_all_small_traces_against_sorted_reference(self):
        for actions in itertools.product(range(4),repeat=6):
            q=PriorityQueue();reference=[];ticket=0
            for op in actions:
                if op<2:
                    value={'id':ticket};q.push(op,value);reference.append((op,ticket,value));ticket+=1
                elif reference:
                    best=min(reference,key=lambda e:e[:2]);actual=q.pop() if op==2 else q.peek()
                    self.assertEqual(actual,(best[0],best[2]))
                    if op==2:reference.remove(best)
                else:
                    with self.assertRaises(IndexError):q.pop() if op==2 else q.peek()
                self.assertEqual(len(q),len(reference));self.assertTrue(q.validate())
                self.assertEqual(sorted((p,t,v['id']) for p,t,v in q.entries()),sorted((p,t,v['id']) for p,t,v in reference))

    def test_stable_ties_and_incomparable_payloads(self):
        q=PriorityQueue();values=[{},[],None,object()]
        for value in values:q.push(-1,value)
        for value in values:self.assertIs(q.pop()[1],value)
        with self.assertRaises(IndexError):q.pop()
        q.push(5,'novo');self.assertEqual(q.pop(),(5,'novo'))

    def test_trace_and_heap_is_not_sorted(self):
        states=trace();self.assertEqual(states[4]['heap'],[[1,1,'B'],[2,3,'D'],[1,2,'C'],[3,0,'A']])
        self.assertEqual(states[-1]['removed'],['B','C','E','D','A']);self.assertEqual(states[-1]['heap'],[])
        self.assertNotEqual(states[4]['heap'],sorted(states[4]['heap']))

    def test_contract_and_corruption(self):
        q=PriorityQueue()
        for value in (True,1.5,float('nan'),'1',None):
            with self.assertRaises(ValueError):q.push(value,'x')
        self.assertEqual(len(q),0)
        q.push(1,'a');q.push(2,'b');q._heap[0],q._heap[1]=q._heap[1],q._heap[0]
        with self.assertRaises(ValueError):q.validate()
