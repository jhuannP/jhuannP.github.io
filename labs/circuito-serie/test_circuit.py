import unittest
from fractions import Fraction as Q
from .circuit import series


class SeriesTests(unittest.TestCase):
    def test_original_and_energy(self):
        r=series(12,[2,4],60)
        self.assertEqual(r['equivalent'],6);self.assertEqual(r['current'],2)
        self.assertEqual(r['drops'],(4,8));self.assertEqual(r['potentials'],(12,8,0))
        self.assertEqual(r['powers'],(8,16));self.assertEqual(r['supplied_power'],24)
        self.assertEqual(r['energies'],(480,960));self.assertEqual(r['supplied_energy'],1440)
        self.assertEqual(r['charge'],120);self.assertEqual(r['source_absorbed_power'],-24)

    def test_independent_node_equations(self):
        # Solve midpoint by conductances: (V-mid)/R1 = mid/R2.
        for v in range(13):
            for r1 in range(1,7):
                for r2 in range(1,7):
                    mid=Q(v,r1)/(Q(1,r1)+Q(1,r2))
                    left=(v-mid)/r1;right=mid/r2
                    r=series(v,[r1,r2])
                    self.assertEqual(left,right);self.assertEqual(r['current'],left)
                    self.assertEqual(r['potentials'],(v,mid,0))
                    self.assertEqual(r['powers'],((v-mid)*left,mid*right))

    def test_balanes_many_resistors(self):
        for n in range(1,11):
            resistances=[Q(i,3) for i in range(1,n+1)]
            r=series(Q(17,5),resistances,Q(7,2))
            self.assertEqual(sum(r['drops']),Q(17,5))
            self.assertEqual(sum(r['powers'])+r['source_absorbed_power'],0)
            self.assertEqual(sum(r['energies']),r['supplied_energy'])
            self.assertEqual(r['potentials'][-1],0)
            self.assertEqual(r['charge']*Q(17,5),r['supplied_energy'])

    def test_scaling_and_order(self):
        original=series(12,[2,4],60)
        doubled=series(24,[2,4],60)
        self.assertEqual(doubled['current'],2*original['current'])
        self.assertEqual(doubled['supplied_power'],4*original['supplied_power'])
        scaled=series(12,[6,12],60)
        self.assertEqual(scaled['drops'],original['drops'])
        self.assertEqual(scaled['current'],original['current']/3)
        swapped=series(12,[4,2],60)
        self.assertEqual(swapped['current'],original['current'])
        self.assertEqual(swapped['drops'],tuple(reversed(original['drops'])))
        self.assertEqual(series(12,[2,4,6])['current'],1)

    def test_contracts_and_zero(self):
        z=series(0,[2,4],60)
        self.assertEqual(z['supplied_energy'],0);self.assertEqual(z['current'],0)
        self.assertEqual(series(12,[2,4])['energies'],(0,0))
        for args in [(-1,[2],1),(12,[0],1),(12,[],1),(12,[2],-1),(True,[2],1),(12,[2.0],1),(12,[2],True)]:
            with self.assertRaises(ValueError):series(*args)
