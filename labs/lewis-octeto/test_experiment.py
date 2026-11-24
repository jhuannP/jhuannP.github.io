from itertools import product,permutations
from fractions import Fraction as F
import unittest
from .experiment import inspect,contributors

class LewisOctet(unittest.TestCase):
    def test_electron_tokens_independent(self):
        # Elétrons com identidade: cada ligação recebe um par e cada átomo recebe
        # metade dos compartilhados para CF. Não usa a fórmula de CF do modelo.
        for species in (0,1):
            for orders in product(range(1,4),repeat=3):
                assigned=[set() for _ in range(4)];shells=[set() for _ in range(4)];idx=0
                for j,order in enumerate(orders,1):
                    for _ in range(order):
                        pair={idx,idx+1};shells[0]|=pair;shells[j]|=pair
                        assigned[0].add(idx);assigned[j].add(idx+1);idx+=2
                    for _ in range(8-2*order):
                        assigned[j].add(idx);shells[j].add(idx);idx+=1
                z=inspect(species,orders)
                self.assertEqual(idx,24)
                self.assertEqual(len(set.union(*assigned)),24)
                self.assertEqual(sum(map(len,assigned)),24)
                self.assertEqual([len(x) for x in shells],z['shells'])
                self.assertEqual([v-len(a) for v,a in zip([5 if species==0 else 4,6,6,6],assigned)],z['formal'])
                self.assertEqual(sum(z['formal']),z['charge'])

    def test_exhaustive_octet_and_averages(self):
        expected=set(permutations((2,1,1)))
        for species in (0,1):
            actual=set(contributors(species));self.assertEqual(actual,expected)
            for j in range(3):
                self.assertEqual(sum(F(b[j],3) for b in actual),F(4,3))
                self.assertEqual(sum(F(inspect(species,b)['formal'][j+1],3) for b in actual),F(-2,3))
            self.assertEqual(inspect(species,(1,1,1))['shells'][0],6)
            self.assertFalse(inspect(species,(2,2,1))['octets'])

    def test_relabeling_oxygen_sites(self):
        for species in (0,1):
            for orders in product(range(1,4),repeat=3):
                z=inspect(species,orders)
                for perm in permutations(range(3)):
                    w=inspect(species,[orders[j] for j in perm])
                    self.assertEqual(w['formal'][0],z['formal'][0])
                    self.assertEqual(w['formal'][1:],[z['formal'][j+1] for j in perm])
                    self.assertEqual(w['octets'],z['octets'])

    def test_contracts(self):
        for species in [True,-1,2,0.0,'0']:
            with self.assertRaises(ValueError):inspect(species)
        for orders in [(1,1),(0,1,1),(4,1,1),(True,1,1),(1.0,1,1),None,'211']:
            with self.assertRaises(ValueError):inspect(0,orders)
