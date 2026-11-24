import itertools,math,unittest
from fractions import Fraction as Q
from .gibbs import distribution,entropy,relative_entropy,grouping

class GibbsTests(unittest.TestCase):
    def test_reference_and_zeros(self):
        self.assertEqual(entropy([1,0,0,0]),0)
        self.assertAlmostEqual(entropy([Q(1,4)]*4),math.log(4),places=14)
        self.assertAlmostEqual(entropy([Q(1,2),Q(1,4),Q(1,8),Q(1,8)]),Q(7,4)*math.log(2),places=14)
        for n in range(1,21):self.assertAlmostEqual(entropy([Q(1,n)]*n),math.log(n),places=13)

    def test_chain_rule_many_distributions(self):
        groups_list=[[[0,1],[2,3]],[[0,2,3],[1]],[[0],[1],[2],[3]],[[0,1,2,3]]]
        count=0
        for weights in itertools.product(range(3),repeat=4):
            total=sum(weights)
            if not total:continue
            p=[Q(w,total) for w in weights]
            for groups in groups_list:
                r=grouping(p,groups)
                self.assertEqual(sum(r['masses']),1)
                self.assertAlmostEqual(r['micro'],r['macro']+r['within'],places=13)
                self.assertGreaterEqual(r['within'],-1e-14)
                self.assertLessEqual(r['macro'],r['micro']+1e-13)
                self.assertLessEqual(r['micro'],math.log(4)+1e-13)
                count+=1
        self.assertEqual(count,320)

    def test_original_example_and_maximum(self):
        p=[Q(1,2),Q(1,4),Q(1,8),Q(1,8)];r=grouping(p,[[0,1],[2,3]])
        self.assertEqual(r['masses'],(Q(3,4),Q(1,4)))
        self.assertEqual(r['conditional'],((Q(2,3),Q(1,3)),(Q(1,2),Q(1,2))))
        self.assertEqual(r['uniform_within'],(Q(3,8),Q(3,8),Q(1,8),Q(1,8)))
        self.assertAlmostEqual(r['macro'],2*math.log(2)-Q(3,4)*math.log(3),places=14)
        gap=r['max_given_groups']-r['micro']
        self.assertAlmostEqual(gap,relative_entropy(p,r['uniform_within']),places=14)
        # Outras distribuições com as mesmas massas de grupo não ultrapassam o máximo.
        for a in range(13):
            for b in range(5):
                candidate=[Q(a,16),Q(12-a,16),Q(b,16),Q(4-b,16)]
                self.assertLessEqual(entropy(candidate),r['max_given_groups']+1e-14)

    def test_zero_groups_permutations_and_support(self):
        r=grouping([1,0,0,0],[[0,1],[2,3]])
        self.assertEqual(r['masses'],(1,0));self.assertIsNone(r['conditional'][1])
        self.assertEqual(r['within'],0)
        self.assertEqual(relative_entropy([1,0],[0,1]),math.inf)
        self.assertEqual(relative_entropy([1,0],[1,0]),0)
        p=[Q(1,2),Q(1,4),Q(1,8),Q(1,8)]
        for perm in itertools.permutations(p):self.assertAlmostEqual(entropy(perm),entropy(p),places=14)
        self.assertAlmostEqual(math.log(4)-entropy(p),relative_entropy(p,[Q(1,4)]*4),places=14)

    def test_contracts(self):
        for p in [[],[True,0],[.5,.5]]:
            with self.assertRaises(TypeError):entropy(p)
        for p in [[1,1],[-1,2],[Q(1,3),Q(1,3)]]:
            with self.assertRaises(ValueError):entropy(p)
        for groups in [[],[[0,1],[1,2,3]],[[0,1],[2]],[[0,1,2,3],[]],[[False,1],[2,3]],[[0,1],[2,4]]]:
            with self.assertRaises(ValueError):grouping([Q(1,4)]*4,groups)
        with self.assertRaises(ValueError):relative_entropy([1,0],[1])

if __name__=='__main__':unittest.main()
