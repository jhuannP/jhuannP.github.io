"""Contadores didáticos de operações; nenhum tempo de hardware é medido."""
from itertools import product,combinations
from fractions import Fraction as Q
import unittest


def size(n):
    if isinstance(n,bool) or not isinstance(n,int) or n<0:
        raise ValueError('Tamanho inteiro não negativo')
    return n


def pairs(n,store=False):
    n=size(n)
    total=0
    saved=[] if store else None
    for i in range(n):
        for j in range(i+1,n):
            total+=1
            if store:saved.append((i,j))
    return total,saved


def linear_search(values,target):
    if not isinstance(values,(list,tuple)) or any(isinstance(x,bool) or not isinstance(x,int) for x in values):
        raise ValueError('Lista/tupla de inteiros pequenos no modelo')
    if isinstance(target,bool) or not isinstance(target,int):
        raise ValueError('Alvo inteiro')
    comparisons=0
    for i,item in enumerate(values):
        comparisons+=1
        if item==target:
            return i,comparisons
    return -1,comparisons


def halves(n):
    q=size(n)
    count=0
    while q>0:
        count+=1
        q//=2
    return count


class Checks(unittest.TestCase):
    def test_pairs_formula_and_storage(self):
        for n in range(101):
            count,saved=pairs(n)
            self.assertEqual(count,n*(n-1)//2)
            self.assertIsNone(saved)
            if n<=30:
                stored_count,stored=pairs(n,True)
                reference=list(combinations(range(n),2))
                self.assertEqual(stored,reference)
                self.assertEqual(stored_count,len(reference))

    def test_growth_bounds_and_doubling(self):
        for n in range(2,101):
            count=pairs(n)[0]
            self.assertGreaterEqual(count,Q(n*n,4))
            self.assertLessEqual(count,Q(n*n,2))
            self.assertEqual(Q(pairs(2*n)[0],count),4+Q(2,n-1))
        self.assertEqual(100*201,201*200//2)
        self.assertGreater(100*200,200*199//2)
        self.assertLess(100*202,202*201//2)

    def test_search_exhaustive_small_arrays(self):
        cases=0
        for n in range(7):
            for values in product((-1,0,1),repeat=n):
                for target in (-1,0,1,2):
                    matches=[i for i,x in enumerate(values) if x==target]
                    expected=matches[0] if matches else -1
                    actual,cost=linear_search(values,target)
                    self.assertEqual(actual,expected)
                    self.assertEqual(cost,n if expected==-1 else expected+1)
                    cases+=1
        self.assertEqual(cases,4372)

    def test_uniform_position_mean_and_halving(self):
        for n in range(1,41):
            values=list(range(n))
            costs=[linear_search(values,t)[1] for t in values]
            self.assertEqual(Q(sum(costs),n),Q(n+1,2))
        for n in range(4097):
            self.assertEqual(halves(n),n.bit_length())
        self.assertEqual(halves(8),4)

    def test_contracts(self):
        for n in (-1,True,1.5):
            with self.assertRaises(ValueError):pairs(n)
            with self.assertRaises(ValueError):halves(n)
        for values,target in (([True],1),([1.],1),('abc',1),([1],True)):
            with self.assertRaises(ValueError):linear_search(values,target)


if __name__=='__main__':
    for n in (4,8,16,32):print(n,'visitas simples:',n,'visitas a pares:',pairs(n)[0])
    unittest.main()
