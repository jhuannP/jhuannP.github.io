import collections,itertools,unittest
from .insertion import insertion

class InsertionTests(unittest.TestCase):
    def test_exhaustive_order_permutation_and_inversions(self):
        count=0
        for n in range(7):
            for values in itertools.product(range(3),repeat=n):
                result=insertion(values)
                self.assertEqual(result.items,tuple(sorted(values)))
                self.assertEqual(collections.Counter(result.items),collections.Counter(values))
                inversions=sum(values[i]>values[j] for i in range(n) for j in range(i+1,n))
                self.assertEqual(result.shifts,inversions)
                self.assertEqual(result.writes,inversions+max(n-1,0))
                self.assertTrue(inversions<=result.comparisons<=inversions+max(n-1,0))
                self.assertFalse(result.trace)
                count+=1
        self.assertEqual(count,1093)

    def test_trace_prefix_and_saved_key(self):
        r=insertion([4,1,3,2],capture=True)
        self.assertEqual(r.trace,((4,1,3,2),(1,4,3,2),(1,3,4,2),(1,2,3,4)))
        self.assertEqual((r.shifts,r.comparisons,r.writes),(4,6,7))
        original=[3,1,3,0]
        r=insertion(original,capture=True)
        self.assertEqual(original,[3,1,3,0])
        for i,state in enumerate(r.trace):
            self.assertEqual(list(state[:i+1]),sorted(original[:i+1]))
            self.assertEqual(state[i+1:],tuple(original[i+1:]))

    def test_stability_and_single_key_evaluation(self):
        values=[(2,'A'),(1,'B'),(2,'C'),(1,'D')];called=[]
        def key(item):called.append(item);return item[0]
        result=insertion(values,key=key)
        self.assertEqual(result.items,((1,'B'),(1,'D'),(2,'A'),(2,'C')))
        self.assertEqual(called,values)
        # Ordenar tuplas inteiras usa também o segundo campo, outro contrato.
        other=[(2,'Z'),(2,'A')]
        self.assertEqual(insertion(other,key=lambda r:r[0]).items,tuple(other))
        self.assertEqual(insertion(other).items,((2,'A'),(2,'Z')))

    def test_best_worst_and_duplicate_cases(self):
        for n in range(1,21):
            best=insertion(range(n));worst=insertion(range(n,0,-1))
            self.assertEqual(best.comparisons,n-1);self.assertEqual(best.shifts,0)
            self.assertEqual(worst.comparisons,n*(n-1)//2)
            self.assertEqual(worst.shifts,n*(n-1)//2)
            equal=insertion([7]*n)
            self.assertEqual(equal.shifts,0);self.assertEqual(equal.comparisons,n-1)
        self.assertEqual(insertion([]).items,())

    def test_shallow_copy_and_contracts(self):
        record={'key':1};values=[record]
        result=insertion(values,key=lambda r:r['key'],capture=True)
        self.assertIs(result.items[0],record)
        record['key']=2
        self.assertEqual(result.trace[0][0]['key'],2) # Snapshot das posições, não cópia profunda.
        with self.assertRaises(TypeError):insertion([1],key=1)
        with self.assertRaises(TypeError):insertion([1],capture=1)
        with self.assertRaises(TypeError):insertion([1,'a'])

if __name__=='__main__':unittest.main()
