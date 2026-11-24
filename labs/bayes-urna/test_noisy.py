import unittest
from fractions import Fraction as Q
from .noisy import infer_report
from .urn import infer


class NoisyTests(unittest.TestCase):
    def test_example_and_inventory(self):
        r = infer_report(3, {1:1,2:1}, Q(4,5), Q(1,5))
        self.assertEqual(r['evidence'], Q(1,2))
        self.assertEqual(r['joint_posterior'], {(1,0):Q(2,15),(1,1):Q(4,15),(2,0):Q(1,15),(2,1):Q(8,15)})
        self.assertEqual(r['posterior'], {1:Q(2,5),2:Q(3,5)})
        self.assertEqual(r['removed_red'], Q(4,5))
        self.assertEqual(r['next_red'], Q(2,5))
        self.assertNotEqual(r['next_red'], Q(3,10))  # relato não é cor observada

    def test_independent_atom_enumeration(self):
        # Oráculo: objetos identificados, cinco saídas equiprováveis do sensor,
        # e todas as próximas bolas. Não reaproveita a fórmula de inventário.
        for n in range(1,8):
            weights = {k:k+1 for k in range(n+1)}
            total = sum(weights.values())
            for s in (0,1,4,5):
                for f in (0,1,4,5):
                    for report in (0,1):
                        mass = Q(0); by_k = {k:Q(0) for k in weights}
                        red = Q(0); next_red = Q(0)
                        for k, w in weights.items():
                            for first in range(n):
                                actual = int(first < k)
                                for u in range(5):
                                    sensor = int(u < (s if actual else f))
                                    if sensor != report: continue
                                    atom = Q(w, total*n*5)
                                    mass += atom; by_k[k] += atom; red += atom*actual
                                    if n > 1:
                                        for second in range(n):
                                            if second != first and second < k: next_red += atom/Q(n-1)
                        r = infer_report(n,weights,Q(s,5),Q(f,5),report)
                        self.assertEqual(r['evidence'],mass)
                        if not mass:
                            self.assertIsNone(r['posterior']); continue
                        self.assertEqual(r['posterior'],{k:v/mass for k,v in by_k.items()})
                        self.assertEqual(r['removed_red'],red/mass)
                        self.assertEqual(r['next_red'],None if n==1 else next_red/mass)

    def test_limits_and_contracts(self):
        for report in (0,1):
            r=infer_report(3,{1:1,2:1},1,0,report)
            exact=infer(3,{1:1,2:1},(report,))
            self.assertEqual(r['posterior'],exact['posterior'])
            self.assertEqual(r['next_red'],exact['next_red'])
        r=infer_report(3,{1:1,2:1},Q(2,5),Q(2,5))
        self.assertEqual(r['posterior'],{1:Q(1,2),2:Q(1,2)})
        self.assertEqual(r['next_red'],Q(1,2))
        self.assertIsNone(infer_report(3,{1:1},0,0)['posterior'])
        self.assertIsNone(infer_report(1,{1:1},1,0)['next_red'])
        for s,f,report in [(True,0,1),(0.8,0,1),(1,-1,1),(1,2,1),(1,0,True),(1,0,2)]:
            with self.assertRaises(ValueError): infer_report(3,{1:1},s,f,report)
