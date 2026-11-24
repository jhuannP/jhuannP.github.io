import itertools
import unittest
from fractions import Fraction as F
from .events import probability,COUNTS,CIRCLE,BLUE
class ConditionalTests(unittest.TestCase):
    def test_table_and_reversed_condition(self):
        self.assertEqual(probability(COUNTS,CIRCLE,BLUE),F(12,19))
        self.assertEqual(probability(COUNTS,BLUE,CIRCLE),F(4,5))
        self.assertEqual(probability(COUNTS,BLUE),F(19,50))
        self.assertEqual(probability(COUNTS,CIRCLE,{'circle_red','square_red'}),F(3,31))
        changed={'circle_blue':8,'circle_red':2,'square_blue':18,'square_red':72}
        self.assertEqual(probability(changed,CIRCLE,BLUE),F(4,13))
        self.assertEqual(probability(changed,BLUE,CIRCLE),F(4,5))

    def test_product_partition_and_expanded_oracle(self):
        keys=list(COUNTS);samples=[k for k,n in COUNTS.items() for _ in range(n)]
        events=[set(k for i,k in enumerate(keys) if mask>>i&1) for mask in range(16)]
        for a,b in itertools.product(events,repeat=2):
            denom=sum(k in b for k in samples)
            if not denom:continue
            q=probability(COUNTS,a,b)
            expected=F(sum(k in a and k in b for k in samples),denom)
            self.assertEqual(q,expected)
            self.assertEqual(q*probability(COUNTS,b),probability(COUNTS,a&b))
            self.assertEqual(q+probability(COUNTS,set(keys)-a,b),1)
        self.assertEqual(sum(probability(COUNTS,BLUE,g)*probability(COUNTS,g)
                             for g in [CIRCLE,set(keys)-CIRCLE]),probability(COUNTS,BLUE))
        for factor in range(1,21):
            scaled={k:n*factor for k,n in COUNTS.items()}
            self.assertEqual(probability(scaled,CIRCLE,BLUE),F(12,19))

    def test_ordered_draws_without_replacement(self):
        # Enumerate physical IDs, not equiprobable category labels.
        blue=set(range(38));pairs=[(i,j) for i in range(100) for j in range(100) if i!=j]
        conditional=[j in blue for i,j in pairs if i in blue]
        self.assertEqual(F(sum(conditional),len(conditional)),F(37,99))
        self.assertEqual(F(sum(j in blue for _,j in pairs),len(pairs)),F(19,50))

    def test_contracts(self):
        for counts in [{},{'a':True},{'a':-1},{'a':.5}]:
            with self.assertRaises((TypeError,ValueError)):probability(counts,{'a'})
        for event,given in [('a',None),({'a'},'a'),({'z'},None),({'a'},set())]:
            with self.assertRaises((TypeError,ValueError)):probability({'a':1},event,given)
        with self.assertRaises(ValueError):probability({'a':0},{'a'})
if __name__=='__main__':unittest.main()
