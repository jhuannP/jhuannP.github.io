from itertools import product
import unittest
from .experiment import counting,distribution_trace

class StableCounting(unittest.TestCase):
    def test_exhaustive_against_stable_comparison_sort(self):
        for K in range(1,5):
            for n in range(7):
                for keys in product(range(K),repeat=n):
                    records=[(k,{'id':i}) for i,k in enumerate(keys)]
                    expected=sorted(records,key=lambda r:r[0])
                    actual=counting(records,K)
                    self.assertEqual(actual,expected)
                    self.assertEqual([id(x) for x in actual],[id(x) for x in expected])

    def test_distribution_prefix_invariant(self):
        for n in range(6):
            for keys in product(range(3),repeat=n):
                records=[(k,i) for i,k in enumerate(keys)];z=distribution_trace(records,3)
                for key in range(3):self.assertEqual(z['starts'][key],sum(k<key for k in keys))
                for step,state in enumerate(z['states']):
                    filled=[x for x in state['out'] if x is not None]
                    self.assertEqual(sorted(v for _,v in filled),list(range(step)))
                    for key in range(3):
                        start=z['starts'][key];seen=sum(k==key for k in keys[:step])
                        self.assertEqual(state['cursor'][key],start+seen)
                        self.assertEqual(state['out'][start:start+seen],[rec for rec in records[:step] if rec[0]==key])
                        self.assertLessEqual(state['cursor'][key],start+z['freq'][key])
                self.assertEqual(z['states'][-1]['out'],counting(records,3))

    def test_empty_sparse_shallow_and_immutable_input(self):
        self.assertEqual(counting([],100),[])
        a,b=object(),object();records=[(7,a),(0,None),(7,b)];before=records.copy()
        actual=counting(records,10)
        self.assertEqual(records,before);self.assertIs(actual[1][1],a);self.assertIs(actual[2][1],b)
        trace=distribution_trace(records,10)
        self.assertTrue(all(x is None for x in trace['states'][0]['out']))
        self.assertEqual(trace['starts'][9],3) # fim exclusivo de região vazia,não uma escrita

    def test_contracts(self):
        for K in [0,-1,True,3.0,'3']:
            with self.assertRaises(ValueError):counting([],K)
        for records in [None,[(3,'x')],[(-1,'x')],[(True,'x')],[(1.0,'x')],[[1,'x']],[(1,)]]:
            with self.assertRaises(ValueError):counting(records,3)
