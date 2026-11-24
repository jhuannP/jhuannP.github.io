import unittest
from fractions import Fraction as Q
from itertools import combinations, product
from .pairs import population, kinds


class ChairPairs(unittest.TestCase):
    def test_fixtures(self):
        self.assertEqual(population(1,1,2,1)['probabilities'],(Q(5,8),Q(3,8)))
        self.assertEqual(population(1,1,2,-1)['probabilities'],(Q(1,16),Q(15,16)))
        self.assertEqual(population(1,1,4,1,3,3)['probabilities'],(Q(1,2),Q(1,2)))

    def test_six_classification_cases(self):
        # Tabela química deduzida por faces; existência de uma cadeira diequatorial.
        for distance, cis_has_ee in [(1,False),(2,True),(3,False)]:
            for face2 in (-1,1):
                r=population(1,1,1+distance,face2)
                has_ee=('equatorial','equatorial') in r['states']
                self.assertEqual(has_ee, cis_has_ee if face2==1 else not cis_has_ee)

    def test_all_pairs_and_inversion(self):
        axial_faces={1:1,2:-1,3:1,4:-1,5:1,6:-1}
        for i,j in combinations(range(1,7),2):
            for f,g in product((-1,1),repeat=2):
                r=population(i,f,j,g)
                oracle=tuple('axial' if axial_faces[s]==face else 'equatorial'
                             for s,face in [(i,f),(j,g)])
                self.assertEqual(r['states'][0],oracle)
                self.assertTrue(all(a!=b for a,b in zip(*r['states'])))
                reflected=population(i,-f,j,-g)
                self.assertEqual(r['relation'],reflected['relation'])
                self.assertEqual(r['probabilities'],tuple(reversed(reflected['probabilities'])))
                swapped=population(j,g,i,f,5,3)
                self.assertEqual(r['probabilities'],swapped['probabilities'])

    def test_normalized_independent_group_weights(self):
        # Produto de Bernoullis com P(axial)=1/(1+r), condicionado às duas cadeiras.
        for r1,r2 in product((1,2,Q(5,2),5),repeat=2):
            r=population(1,1,2,1,r1,r2)
            law={state:Q(1) for state in product(('axial','equatorial'),repeat=2)}
            for state in law:
                for kind,penalty in zip(state,(r1,r2)):
                    penalty=Q(penalty)
                    law[state] *= Q(1,1+penalty) if kind=='axial' else penalty/(1+penalty)
            total=sum(law[state] for state in r['states'])
            self.assertEqual(r['probabilities'],tuple(law[state]/total for state in r['states']))
            self.assertEqual(sum(r['probabilities']),1)
        # R2 tem custo axial maior: a cadeira com R2 equatorial é favorecida.
        self.assertGreater(population(1,1,2,1,3,5)['probabilities'][0],Q(1,2))

    def test_contracts(self):
        for args in [(0,1,2,1),(1,0,2,1),(1,1,1,-1),(True,1,2,1),(1,1,2.0,1)]:
            with self.assertRaises(ValueError): population(*args)
        for r in [0,Q(1,2),True,3.0,'3']:
            with self.assertRaises(ValueError): population(1,1,2,1,r,5)
        with self.assertRaises(ValueError):kinds(2,1,1,2,1)
