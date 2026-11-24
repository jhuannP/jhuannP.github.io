import unittest
from itertools import combinations
from .ancestry import AFTER, BEFORE, index_tree, relation


def flips(tree):
    if tree[0]=='gene':return [tree]
    left,right=tree[2]
    return [(tree[0],tree[1],children)
            for a in flips(left) for b in flips(right)
            for children in ((a,b),(b,a))]


class AncestryTests(unittest.TestCase):
    def test_nontransitivity_and_one_to_many(self):
        self.assertEqual(relation(AFTER,'A1','B1')['relation'],'ortólogos')
        self.assertEqual(relation(AFTER,'A2','B1')['relation'],'ortólogos')
        self.assertEqual(relation(AFTER,'A1','A2'),
                         {'ancestor':'dA','event':'D','relation':'parálogos'})
        self.assertEqual(len(index_tree(AFTER)[1]),3)

    def test_cross_species_paralogy(self):
        expected={('Ax','Bx'):'S',('Ay','By'):'S',('Ax','Ay'):'D',
                  ('Ax','By'):'D',('Bx','Ay'):'D',('Bx','By'):'D'}
        for pair,event in expected.items():
            self.assertEqual(relation(BEFORE,*pair)['event'],event)
        self.assertEqual(len(index_tree(BEFORE)[1]),4)

    def test_child_order_and_pair_symmetry(self):
        for tree in (AFTER,BEFORE):
            pairs=list(combinations(index_tree(tree)[1],2))
            for variant in flips(tree):
                for a,b in pairs:
                    self.assertEqual(relation(variant,a,b),relation(tree,a,b))
                    self.assertEqual(relation(variant,b,a),relation(tree,a,b))

    def test_contracts(self):
        bad=[(),('bad','r',()),('gene','','A'),('gene','g',''),
             ('S','r',(('gene','g','A'),)),
             ('D','r',(('gene','g','A'),('gene','g','B'))),
             ('D','r',(('gene','r','A'),('gene','b','B'))),
             ('gene','g',False)]
        for tree in bad:
            with self.subTest(tree=tree),self.assertRaises(ValueError):index_tree(tree)
        for a,b in [('A1','A1'),('absent','A1'),(True,'A1')]:
            with self.assertRaises(ValueError):relation(AFTER,a,b)
        big=('gene','g0','A')
        for i in range(32):big=('D',f'd{i}',(big,('gene',f'g{i+1}','A')))
        with self.assertRaises(ValueError):index_tree(big)


if __name__=='__main__':unittest.main()
