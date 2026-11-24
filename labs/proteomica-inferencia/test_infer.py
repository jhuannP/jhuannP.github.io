import unittest
from itertools import combinations
from .infer import DATABASE,infer


class InferenceTests(unittest.TestCase):
    def test_shared_and_unique_examples(self):
        self.assertEqual(infer(DATABASE,{'GHIK'})['minimum'],[('A',),('B',)])
        s=infer(DATABASE,{'ACDF','GHIK'})
        self.assertEqual(s['minimum'],[('A',)])
        self.assertIn(('A','B'),s['covers'])
        self.assertEqual(s['unique_within_database'],{'ACDF':'A'})
        self.assertEqual(infer(DATABASE,{'GHIK','QRST'})['minimum'],[('A','C'),('B','C')])

    def test_all_observation_subsets_and_coverage(self):
        universe=sorted(set.union(*DATABASE.values()))
        for n in range(len(universe)+1):
            for obs in combinations(universe,n):
                s=infer(DATABASE,obs)
                for g in s['covers']:
                    self.assertTrue(all(any(p in DATABASE[k] for k in g) for p in obs))
                # Nenhum subconjunto menor que uma solução mínima pode cobrir.
                for g in s['minimum']:
                    for size in range(len(g)):
                        for shorter in combinations(DATABASE,size):
                            self.assertTrue(any(not any(p in DATABASE[k] for k in shorter) for p in obs))
        empty=infer(DATABASE,set())
        self.assertEqual(empty['minimum'],[()]);self.assertEqual(len(empty['covers']),8)

    def test_database_dependence_and_missing(self):
        db={**DATABASE,'D':{'ACDF'}}
        s=infer(db,{'ACDF'})
        self.assertEqual(s['minimum'],[('A',),('D',)])
        self.assertEqual(s['unique_within_database'],{})
        unknown=infer(DATABASE,{'VWYA'})
        self.assertEqual(unknown['unmatched'],['VWYA']);self.assertEqual(unknown['covers'],[])
        self.assertEqual(infer(DATABASE,['GHIK','GHIK']),infer(DATABASE,{'GHIK'}))

    def test_contracts(self):
        for db,obs in [({},set()),({'A':set()},set()),(DATABASE,{'bad'}),(DATABASE,'GHIK'),
                       ({str(i):{'ACDF'} for i in range(13)},{'ACDF'})]:
            with self.assertRaises(ValueError):infer(db,obs)


if __name__=='__main__':unittest.main()
