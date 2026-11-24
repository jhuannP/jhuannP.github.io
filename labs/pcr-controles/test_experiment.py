import itertools
import unittest
from .experiment import model,signals

class PCRControlsTests(unittest.TestCase):
    def test_six_conceptual_cases(self):
        cases=[((1,0,0,1,0),(1,0,1,1)),((0,0,0,1,0),(0,0,1,1)),
               ((1,1,0,1,0),(0,0,1,0)),((0,0,1,1,0),(1,1,1,1)),
               ((1,0,0,0,0),(0,0,0,0)),((0,0,0,1,1),(1,0,1,1))]
        for state,observed in cases:self.assertEqual(signals(*state),observed)
    def test_observational_equivalence_and_partition(self):
        a=model(1,0,0,1,0);b=model(0,0,0,1,1)
        self.assertEqual(a,b);self.assertEqual(a['compatible_count'],3)
        self.assertEqual(a['target_values'],[0,1])
        # Falha global oculta todas as 16 combinações das outras condições.
        self.assertEqual(model(0,0,0,0,0)['compatible_count'],16)
        groups={}
        for state in itertools.product((0,1),repeat=5):
            groups.setdefault(signals(*state),set()).add(state)
        self.assertEqual(sum(map(len,groups.values())),32)
        for observed,states in groups.items():
            candidate=model(*next(iter(states)))
            self.assertEqual({tuple(row[k] for k in ('target','inhibited','contamination','working','nonspecific')) for row in candidate['compatible']},states)
    def test_controls_and_contracts(self):
        for target,inhibited,contamination,nonspecific in itertools.product((0,1),repeat=4):
            self.assertEqual(signals(target,inhibited,contamination,0,nonspecific),(0,0,0,0))
            obs=signals(target,inhibited,contamination,1,nonspecific)
            self.assertEqual(obs[1],contamination)
            self.assertEqual(obs[2],1)
            self.assertEqual(obs[3],1-inhibited)
            if inhibited:self.assertEqual(obs[0],0)
        for bad in (-1,2,True,.5,None,'1'):
            for i in range(5):
                args=[1,0,0,1,0];args[i]=bad
                with self.assertRaises(ValueError):model(*args)
