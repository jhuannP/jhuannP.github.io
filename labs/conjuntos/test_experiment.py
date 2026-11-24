import unittest
from .experiment import decode,compare,powerset,image,preimage

class SetTests(unittest.TestCase):
    def test_operations_by_membership_and_de_morgan(self):
        U=frozenset(range(1,5))
        for a in range(16):
            for b in range(16):
                r=compare(a,b);A,B=r['A'],r['B']
                for x in U:
                    self.assertEqual(x in r['union'],x in A or x in B)
                    self.assertEqual(x in r['intersection'],x in A and x in B)
                    self.assertEqual(x in r['difference'],x in A and x not in B)
                self.assertEqual(U-(A|B),(U-A)&(U-B))
                self.assertEqual(U-(A&B),(U-A)|(U-B))
                self.assertEqual(len(A|B),len(A)+len(B)-len(A&B))

    def test_powerset_and_empty_distinctions(self):
        for mask in range(16):
            A=decode(mask);P=powerset(A)
            self.assertEqual(len(P),2**len(A))
            self.assertIn(frozenset(),P)
            self.assertTrue(all(s<=A for s in P))
        self.assertNotEqual(frozenset(),frozenset({frozenset()}))
        self.assertEqual(len(powerset([])),1)

    def test_image_and_preimage_without_invertibility(self):
        f={-2:4,-1:1,0:0,1:1,2:4}
        self.assertEqual(preimage(f,{1}),frozenset({-1,1}))
        self.assertNotEqual(preimage(f,image(f,{-1})),frozenset({-1}))
        for A in powerset(f.keys()):
            self.assertTrue(A<=preimage(f,image(f,A)))
        for S in powerset({0,1,4,9}):
            for T in powerset({0,1,4,9}):
                self.assertEqual(preimage(f,S&T),preimage(f,S)&preimage(f,T))
                self.assertEqual(preimage(f,S|T),preimage(f,S)|preimage(f,T))

    def test_contracts(self):
        for mask in (-1,16,True,.5):
            with self.assertRaises(ValueError):decode(mask)
        with self.assertRaises(ValueError):image({1:2},{3})

if __name__=='__main__':unittest.main()
