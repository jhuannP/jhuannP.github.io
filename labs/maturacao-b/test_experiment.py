import itertools,unittest
from fractions import Fraction
from .experiment import HEAVY,SELF,choose,model

class MaturationTests(unittest.TestCase):
    def test_exhaustive_prefix_sets_independent_oracle(self):
        # Conjunto de zeros no prefixo, em vez da máquina de busca sequencial.
        for bits in itertools.product((0,1),repeat=3):
            for budget in range(3):
                zeros={j for j in range(budget+1) if bits[j]==0}
                s=choose(bits,budget);expected=min(zeros) if zeros else budget
                self.assertEqual(s['passed'],bool(zeros))
                self.assertEqual(s['last'],expected)
                self.assertEqual(s['visited'],list(range(expected+1)))
                self.assertEqual(s['edits_used'],expected)
                self.assertTrue(all(bits[j] for j in s['visited'][:-1]))

    def test_six_cases_by_hand_and_denominators(self):
        expected=((1,2,3),(2,3,4))
        for panel in (0,1):
            for edits in range(3):
                s=model(edits,panel)
                self.assertEqual(s['passed'],expected[panel][edits])
                self.assertEqual(s['eligible'],4);self.assertEqual(s['excluded'],2)
                self.assertEqual(s['passed']+s['unresolved']+s['excluded'],6)
                self.assertEqual(Fraction(s['passed'],s['eligible']),Fraction(expected[panel][edits],4))
                self.assertAlmostEqual(s['fraction'],expected[panel][edits]/4)
                self.assertAlmostEqual(s['all_fraction'],expected[panel][edits]/6)
        self.assertEqual(model(1,0)['selected']['visited'],[0,1])
        self.assertTrue(model(1,0)['selected']['passed'])
        self.assertEqual(model(1,0)['edited_pass'],1)

    def test_prefix_stability_reactivity_rechecked_and_selection_only(self):
        for panel in (0,1):
            states=[model(b,panel) for b in range(3)]
            for i,heavy in enumerate(HEAVY):
                for a,b in zip(states,states[1:]):
                    old,new=a['rows'][i],b['rows'][i]
                    self.assertEqual(old['visited'],new['visited'][:len(old['visited'])])
                    if old['passed']:self.assertEqual(old,new)
                for s in states:
                    row=s['rows'][i]
                    if not heavy:self.assertEqual(row['visited'],[]);self.assertIsNone(row['last'])
                    elif row['passed']:self.assertEqual(row['reactivity'][row['last']],0)
                    else:self.assertTrue(all(row['reactivity'][j] for j in row['visited']))
            for cell in range(1,7):
                s=model(1,panel,cell)
                self.assertEqual(s['rows'],states[1]['rows'])
                self.assertEqual(s['selected'],s['rows'][cell-1])
        self.assertFalse(model(2,0,5)['selected']['passed'])
        self.assertEqual(model(2,0,5)['selected']['visited'],[0,1,2])
        self.assertNotEqual(model(0,0,2)['selected']['passed'],model(0,1,2)['selected']['passed'])

    def test_contract_no_input_mutation(self):
        a=[1,0,1];choose(a,2);self.assertEqual(a,[1,0,1])
        for a,b in [([1,0],1),([1,2,0],1),([False,0,1],1),([0,0,0],-1),([0,0,0],3),([0,0,0],1.5)]:
            with self.assertRaises(ValueError):choose(a,b)
        for args in ((1,2,3),(1,0,0),(1,0,7),(1,0,3.5)):
            with self.assertRaises(ValueError):model(*args)
        before=repr((HEAVY,SELF));model(2,1,5);self.assertEqual(repr((HEAVY,SELF)),before)
