import unittest
from itertools import permutations
from .experiment import MOLECULES,analyze,isomorphic

class OrganicGraphsTests(unittest.TestCase):
    def test_independent_formulas_and_valence_balance(self):
        expected=[('C2H6O',[3,2,1],0),('C2H6O',[3,0,3],0),('C3H6O',[3,2,1,0],1),('C3H6O',[3,0,3,0],1),('C2H4O2',[3,0,0,1],1),('C2H4O2',[1,0,0,3],1)]
        for m,(f,H,dbe) in zip(MOLECULES,expected):
            q=analyze(m['atoms'],m['bonds']);self.assertEqual(q['formula'],f);self.assertEqual(q['hydrogens'],H);self.assertEqual(q['dbe'],dbe)
            self.assertEqual(sum(H),4*q['C']+2*q['O']-2*sum(o for i,j,o in m['bonds']))

    def test_all_108_relabelings_preserve_graph_and_formula(self):
        count=0
        for m in MOLECULES:
            for p in permutations(range(len(m['atoms']))):
                atoms=['']*len(p)
                for i,j in enumerate(p):atoms[j]=m['atoms'][i]
                alt=dict(atoms=atoms,bonds=[[p[i],p[j],o] for i,j,o in m['bonds']])
                self.assertTrue(isomorphic(m,alt))
                self.assertEqual(analyze(atoms,alt['bonds'])['formula'],analyze(m['atoms'],m['bonds'])['formula']);count+=1
        self.assertEqual(count,108)

    def test_constitution_pairs_and_local_motifs(self):
        for i in (0,2,4):
            a,b=MOLECULES[i:i+2]
            self.assertFalse(isomorphic(a,b));self.assertEqual(analyze(a['atoms'],a['bonds'])['formula'],analyze(b['atoms'],b['bonds'])['formula'])
        def carbonyl_neighbors(m):
            carbon=next(i if m['atoms'][i]=='C' else j for i,j,o in m['bonds'] if o==2)
            return sorted(m['atoms'][j if i==carbon else i] for i,j,o in m['bonds'] if o==1 and carbon in (i,j))
        self.assertEqual(carbonyl_neighbors(MOLECULES[2]),['C'])
        self.assertEqual(carbonyl_neighbors(MOLECULES[3]),['C','C'])
        self.assertEqual(analyze(MOLECULES[4]['atoms'],MOLECULES[4]['bonds'])['hydrogens'][-1],1)
        self.assertEqual(analyze(MOLECULES[5]['atoms'],MOLECULES[5]['bonds'])['hydrogens'][2],0)

    def test_invalid_graphs(self):
        for atoms,bonds in [(['N'],[]),(['C','C'],[]),(['C','O'],[[0,1,3]]),(['C','O'],[[0,1,1],[1,0,1]]),(['C'],[[0,1,1]]),(['C'],[[0,0,1]])]:
            with self.assertRaises(ValueError):analyze(atoms,bonds)

if __name__=='__main__':unittest.main()
