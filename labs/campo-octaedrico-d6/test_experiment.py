from fractions import Fraction as Q
from itertools import product
from collections import Counter
import unittest
from .experiment import state,d6_states,minima

class OctahedralOccupancyTests(unittest.TestCase):
    def test_three_candidate_energies(self):
        h=(2,1,1,1,1);i=(2,2,1,1,0);l=(2,2,2,0,0)
        self.assertEqual([state(o,10,12)["total"] for o in (h,i,l)],[8,10,12])
        self.assertEqual([state(o,20,12)["total"] for o in (h,i,l)],[4,-4,-12])
        self.assertEqual([state(o,12,12)["total"] for o in (h,i,l)],[Q(36,5)]*3)
        self.assertEqual([state(o,10,12)["singles"] for o in (h,i,l)],[4,2,0])
    def test_binary_spin_orbital_reference(self):
        # Independente: ocupações de dez spin-orbitais agrupadas em cinco orbitais espaciais.
        patterns=Counter(tuple(bits[2*j]+bits[2*j+1] for j in range(5))
                         for bits in product((0,1),repeat=10) if sum(bits)==6)
        self.assertEqual(sum(patterns.values()),210)
        self.assertEqual(len(patterns),45)
        for delta,p in product((Q(1,2),1,2,5), (0,Q(1,2),1,3)):
            rows=d6_states(delta,p)
            self.assertEqual({r["occupancy"] for r in rows},set(patterns))
            energies=[Q(-2,5)*delta]*3+[Q(3,5)*delta]*2
            for r in rows:
                ref=sum(n*e for n,e in zip(r["occupancy"],energies))+p*sum(n//2 for n in r["occupancy"])
                self.assertEqual(r["total"],ref)
                self.assertEqual(r["electrons"],2*r["pairs"]+r["singles"])
    def test_grid_minima_and_crossing(self):
        for delta in range(1,13):
            for p in range(13):
                r=minima(delta,p)
                classes={(x["upper"],x["pairs"],x["singles"]) for x in r}
                expected={(2,1,4)} if delta<p else {(0,3,0)} if delta>p else {(0,3,0),(1,2,2),(2,1,4)}
                self.assertEqual(classes,expected)
                self.assertEqual(len(r),3 if delta<p else 1 if delta>p else 10)
                # Comparação explícita do par usual baixo/alto, não resolve multiplicidades de spin.
                low=state((2,2,2,0,0),delta,p)["total"]
                high=state((2,1,1,1,1),delta,p)["total"]
                self.assertEqual(low-high,2*(p-delta))
    def test_barycenter_scaling_and_within_group_permutations(self):
        self.assertEqual(3*Q(-2,5)+2*Q(3,5),0)
        for row in d6_states(3,2):
            o=row["occupancy"]
            permuted=(o[2],o[0],o[1],o[4],o[3])
            self.assertEqual(state(permuted,3,2)["total"],row["total"])
            scaled=state(o,Q(9,2),3)
            self.assertEqual(scaled["total"],Q(3,2)*row["total"])
    def test_contracts_and_empty_or_full_shell(self):
        for o in ((0,0),(3,1,1,1,0),(True,1,1,1,1),(1.0,1,1,1,1)):
            with self.assertRaises(ValueError):state(o,1,1)
        for delta,p in ((0,1),(-1,1),(1,-1),(True,1),(1,.5)):
            with self.assertRaises(ValueError):minima(delta,p)
        self.assertEqual(state((0,0,0,0,0),2,3)["field"],0)
        full=state((2,2,2,2,2),2,3)
        self.assertEqual(full["field"],0);self.assertEqual(full["pairs"],5)
