"""Cauda de sum(1/n²): certificado racional com cotas integrais."""
from fractions import Fraction as Q
import unittest

def bounds(n, m):
    if type(n) is not int or type(m) is not int or not 1 <= n <= m:
        raise ValueError('Inteiros 1 <= N <= M')
    block = sum((Q(1,k*k) for k in range(n+1,m+1)),Q(0))
    return block+Q(1,m+1), block+Q(1,m)

class Checks(unittest.TestCase):
    def test_width_and_nesting(self):
        for n in range(1,11):
            for m in range(n,40):
                lo,hi=bounds(n,m); nextlo,nexthi=bounds(n,m+1)
                self.assertEqual(hi-lo,Q(1,m*(m+1)))
                self.assertLess(lo,nextlo);self.assertLess(nexthi,hi)
    def test_finite_block_is_not_tail(self):
        for n in range(1,40):
            self.assertLess(Q(1,(n+1)**2),Q(1,n+1))
            self.assertEqual(bounds(n,n),(Q(1,n+1),Q(1,n)))
    def test_independent_telescoping_bounds(self):
        # Exact closed forms are independent of the computed p-series block.
        for n in range(1,16):
            for m in range(n+1,50):
                low_sum=sum((Q(1,k*(k+1)) for k in range(n+1,m+1)),Q(0))
                high_sum=sum((Q(1,k*(k-1)) for k in range(n+1,m+1)),Q(0))
                block=sum((Q(1,k*k) for k in range(n+1,m+1)),Q(0))
                self.assertEqual(low_sum,Q(1,n+1)-Q(1,m+1))
                self.assertEqual(high_sum,Q(1,n)-Q(1,m))
                self.assertLessEqual(low_sum,block)
                self.assertLessEqual(block,high_sum)

    def test_contract(self):
        for n,m in [(0,1),(2,1),(True,3),(1,2.0)]:
            with self.assertRaises(ValueError):bounds(n,m)

if __name__=='__main__':
    print('N=10, M=100:',bounds(10,100))
    unittest.main()
