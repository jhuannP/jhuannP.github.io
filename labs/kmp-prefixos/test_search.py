import unittest
from itertools import product
from .search import prefix,search

def strings(length):return tuple(''.join(chars)for chars in product('ab',repeat=length))

class Tests(unittest.TestCase):
    def test_prefix_independent_oracle(self):
        self.assertEqual(prefix('ababa'),(0,0,1,2,3))
        for m in range(1,6):
            for pat in strings(m):
                oracle=[]
                for end in range(1,m+1):
                    part=pat[:end]
                    oracle.append(max(k for k in range(end)if part[:k]==part[end-k:]))
                self.assertEqual(prefix(pat),tuple(oracle))
    def test_all_occurrences_and_linear_count(self):
        # Oráculo quadrático só nos testes; não reaproveita lógica de bordas.
        for n in range(8):
            for text in strings(n):
                for m in range(1,6):
                    for pat in strings(m):
                        r=search(text,pat)
                        expected=tuple(i for i in range(n-m+1)if text[i:i+m]==pat)
                        self.assertEqual(r['matches'],expected)
                        self.assertLessEqual(r['text_compares'],2*n)
                        self.assertLessEqual(r['pattern_compares'],2*(m-1))
        self.assertEqual(search('ababababa','ababa')['matches'],(0,2,4))
    def test_repetition_and_unicode(self):
        r=search('a'*512,'a'*63+'b')
        self.assertEqual(r['matches'],())
        self.assertLessEqual(r['text_compares'],1024)
        self.assertEqual(search('λ🙂λ🙂λ','λ🙂λ')['matches'],(0,2))
        self.assertEqual(search('é e\u0301','é')['matches'],(0,))
        self.assertEqual(search('ABC','abc')['matches'],())
        self.assertEqual(search('aaaa','a')['matches'],(0,1,2,3))
    def test_contracts(self):
        for bad in ('',None,True,[], 'a'*65):
            with self.assertRaises(ValueError):prefix(bad)
        for bad in (None,True,[], 'a'*513):
            with self.assertRaises(ValueError):search(bad,'a')
        self.assertEqual(search('','abc')['matches'],())
