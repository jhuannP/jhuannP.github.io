from collections import Counter
from itertools import product,permutations
from math import factorial
import unittest
from .counting import count

class CountingTests(unittest.TestCase):
    def test_four_examples(self):
        self.assertEqual(count(5,3,ordered=True,repetition=False),60)
        self.assertEqual(count(5,3,ordered=True,repetition=True),125)
        self.assertEqual(count(5,3,ordered=False,repetition=False),10)
        self.assertEqual(count(5,3,ordered=False,repetition=True),35)

    def test_enumeration_oracle(self):
        for n,k,ordered,repetition in product(range(6),range(5),(False,True),(False,True)):
            outcomes=product(range(n),repeat=k) if repetition else permutations(range(n),k)
            actual=set(outcomes) if ordered else {tuple(sorted(x)) for x in outcomes}
            self.assertEqual(count(n,k,ordered=ordered,repetition=repetition),len(actual),
                             (n,k,ordered,repetition))

    def test_dividing_by_factorial_requires_equal_multiplicity(self):
        distinct=Counter(tuple(sorted(p)) for p in permutations(range(5),3))
        self.assertEqual(len(distinct),10)
        self.assertEqual(set(distinct.values()),{factorial(3)})
        repeated=Counter(tuple(sorted(p)) for p in product('AB',repeat=3))
        self.assertEqual(repeated[('A','A','A')],1)
        self.assertEqual(repeated[('A','A','B')],3)
        self.assertEqual(len(repeated),4)
        self.assertEqual(sum(repeated.values()),8)

    def test_repetition_bijection(self):
        # Sorted choices x_i -> strictly increasing y_i=x_i+i.
        for n,k in product(range(1,5),range(5)):
            xs={tuple(sorted(p)) for p in product(range(n),repeat=k)}
            ys={tuple(x+i for i,x in enumerate(p)) for p in xs}
            targets={p for p in permutations(range(n+k-1),k) if list(p)==sorted(p)}
            self.assertEqual(ys,targets)

    def test_contracts_and_empty_selection(self):
        for o,r in product((False,True),repeat=2):
            self.assertEqual(count(0,0,ordered=o,repetition=r),1)
            self.assertEqual(count(0,3,ordered=o,repetition=r),0)
        self.assertEqual(count(2,3,ordered=True,repetition=False),0)
        for bad in (-1,True,2.,'2',None):
            with self.assertRaises(ValueError):count(bad,2,ordered=True,repetition=False)
            with self.assertRaises(ValueError):count(2,bad,ordered=True,repetition=False)
        with self.assertRaises(ValueError):count(2,1,ordered=1,repetition=False)

if __name__=='__main__':unittest.main()
