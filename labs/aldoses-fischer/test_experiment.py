from itertools import product
from math import comb
import unittest
from .experiment import inspect,relation,pattern,REFERENCE

def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def handedness(bit):
    # Quatro ligantes identificados OH,H,cadeia superior,inferior; sem atribuir CIP.
    right=(1,0,1);left=(-1,0,1);up=(0,1,-1);down=(0,-1,-1)
    oh,h=(right,left) if bit else (left,right)
    vectors=[tuple(v[i]-down[i] for i in range(3)) for v in (oh,h,up)]
    return det(*vectors)

class Fischer(unittest.TestCase):
    def test_oriented_tetrahedra_all_pairs(self):
        states=list(product((0,1),repeat=4))
        for a in states:
            for b in states:
                differences=[i+2 for i,(u,v) in enumerate(zip(a,b)) if handedness(u)*handedness(v)<0]
                z=relation(a,b);self.assertEqual(z['changed'],differences)
                n=len(differences)
                expected={0:'identical',1:'epimer',4:'enantiomer'}.get(n,'diastereomer')
                self.assertEqual(z['relation'],expected)
                self.assertEqual(relation(b,a)['relation'],expected)

    def test_counts_mirrors_and_involution(self):
        states=list(product((0,1),repeat=4));self.assertEqual(len({pattern(b) for b in states}),16)
        self.assertEqual(sum(inspect(b)['series']=='D' for b in states),8)
        for k in range(5):
            self.assertEqual(sum(len(relation(REFERENCE,b)['changed'])==k for b in states),comb(4,k))
        for b in states:
            mirror=tuple(1-x for x in b)
            self.assertEqual(tuple(1-x for x in mirror),b)
            self.assertEqual(relation(b,mirror)['relation'],'enantiomer')
            self.assertNotEqual(inspect(b)['series'],inspect(mirror)['series'])

    def test_examples_and_dl_not_sufficient(self):
        self.assertEqual(inspect((0,0,1,1))['name'],'D-manose')
        self.assertEqual(inspect((1,0,0,1))['changed'],[4])
        z=inspect((1,0,1,0));self.assertEqual(z['series'],'L')
        self.assertEqual(z['relation'],'epimer') # L não implica L-glicose
        self.assertEqual(inspect((0,1,0,0))['name'],'L-glicose')

    def test_contracts(self):
        for bits in [None,'1011',(1,0,1),(1,0,1,2),(True,0,1,1),(1.0,0,1,1)]:
            with self.assertRaises(ValueError):inspect(bits)
