import unittest
from .experiment import formula,formula_text,cleave

class PeptideTests(unittest.TestCase):
    def test_independent_known_formulas(self):
        for seq,text in [('G','C2H5NO2'),('A','C3H7NO2'),('S','C3H7NO3'),('GA','C5H10N2O3'),('GAS','C8H15N3O5'),('GASGAS','C16H28N6O9')]:
            self.assertEqual(formula_text(formula(seq)),text)
        self.assertEqual(formula('GASGAS'),formula('SAGSAG'))
        self.assertNotEqual('GASGAS','SAGSAG')

    def test_all_subsets_against_graph_components(self):
        for seq in ('G','GA','GAS','GASGAS'):
            n=len(seq)
            for mask in range(1<<(n-1)):
                cuts=[i+1 for i in range(n-1) if mask&(1<<i)]
                r=cleave(seq,cuts);adj={i:set() for i in range(n)}
                for i in range(n-1):
                    if i+1 not in cuts:adj[i].add(i+1);adj[i+1].add(i)
                unseen=set(range(n));components=[]
                while unseen:
                    stack=[min(unseen)];component=set()
                    while stack:
                        i=stack.pop()
                        if i in component:continue
                        component.add(i);stack.extend(adj[i]-component)
                    unseen-=component;components.append(sorted(component))
                fragments=[''.join(seq[i] for i in c) for c in components]
                self.assertEqual(r['fragments'],fragments)
                self.assertEqual(r['bonds'],sum(map(len,adj.values()))//2)
                self.assertEqual(r['n_termini'],len(components));self.assertEqual(r['c_termini'],len(components))
                self.assertEqual(r['waters'],len(cuts))

    def test_atom_closure_and_complete_hydrolysis(self):
        for seq in ('GA','GAS','GASGAS','GGGGGG','SSSSSS'):
            for mask in range(1<<(len(seq)-1)):
                cuts=[i+1 for i in range(len(seq)-1) if mask&(1<<i)]
                r=cleave(seq,cuts);expected=formula(seq).copy()
                expected['H']+=2*len(cuts);expected['O']+=len(cuts)
                self.assertEqual(r['aggregate'],expected)
                self.assertEqual(sum(len(f)-1 for f in r['fragments']),r['bonds'])
            full=cleave(seq,range(1,len(seq)))
            self.assertEqual(full['fragments'],list(seq));self.assertEqual(full['bonds'],0)
            self.assertEqual(full['waters'],len(seq)-1)

    def test_idempotent_cuts_and_invalid_domain(self):
        self.assertEqual(cleave('GAS',[2,2]),cleave('GAS',[2]))
        self.assertEqual(cleave('G')['waters'],0)
        for seq,cuts in [('',[]),('GAX',[]),('ga',[]),('GA',[0]),('GA',[2]),('GA',[True])]:
            with self.assertRaises(ValueError):cleave(seq,cuts)

if __name__=='__main__':unittest.main()
