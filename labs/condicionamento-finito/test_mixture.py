import itertools
import unittest
from fractions import Fraction as F
from .mixture import independent_mixture

class MixtureTests(unittest.TestCase):
    def test_independent_label_enumeration(self):
        # G, A e B são definidos por três índices uniformes em {0,1,2,3}.
        # Enumera os 64 resultados sem usar a fórmula de mistura da implementação.
        for k,p0,q0,p1,q1 in itertools.product(range(5),repeat=5):
            counts=[0]*4
            for ig,ia,ib in itertools.product(range(4),repeat=3):
                g=ig<k
                a=int(ia<(p1 if g else p0));b=int(ib<(q1 if g else q0))
                counts[2*a+b]+=1
            r=independent_mixture(*map(lambda x:F(x,4),(k,p0,q0,p1,q1)))
            cells=tuple(F(n,64) for n in counts)
            self.assertEqual(r['cells'],cells)
            self.assertEqual(sum(cells),1)
            self.assertEqual(r['a'],cells[2]+cells[3]);self.assertEqual(r['b'],cells[1]+cells[3])
            self.assertEqual(r['gap'],F(k,4)*(1-F(k,4))*F(p1-p0,4)*F(q1-q0,4))
            self.assertEqual(r['independent'],r['gap']==0)
    def test_original_example_and_opposite_association(self):
        r=independent_mixture(F(1,2),F(1,4),F(1,4),F(3,4),F(3,4))
        self.assertEqual((r['joint'],r['gap'],r['a_given_b']),(F(5,16),F(1,16),F(5,8)))
        negative=independent_mixture(F(1,2),F(1,4),F(3,4),F(3,4),F(1,4))
        self.assertEqual(negative['gap'],-F(1,16))
    def test_group_exchange_and_equal_margin(self):
        for w in (F(1,5),F(1,2),F(4,5)):
            r=independent_mixture(w,F(1,3),F(1,4),F(2,3),F(3,4))
            exchanged=independent_mixture(1-w,F(2,3),F(3,4),F(1,3),F(1,4))
            self.assertEqual(r['cells'],exchanged['cells'])
            self.assertTrue(independent_mixture(w,F(1,3),F(1,4),F(1,3),F(3,4))['independent'])
    def test_contract_and_empty_groups(self):
        r=independent_mixture(0,F(1,4),0,F(3,4),1)
        self.assertEqual(r['a_given_group'],(F(1,4),None));self.assertIsNone(r['a_given_b'])
        self.assertEqual(independent_mixture(1,0,0,1,1)['a_given_group'],(None,F(1)))
        for bad in (-1,2,.5,True,'1/2',None):
            for position in range(5):
                args=[F(1,2)]*5;args[position]=bad
                with self.assertRaises(ValueError): independent_mixture(*args)
