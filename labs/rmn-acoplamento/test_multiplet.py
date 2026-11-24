import unittest
from fractions import Fraction as Q
from itertools import product
from collections import Counter
from math import comb
from .multiplet import sticks, positions_ppm, moments

class MultipletTests(unittest.TestCase):
    def test_named_fixtures(self):
        self.assertEqual(sticks([(2,6)]),((Q(-6),Q(1,4)),(Q(0),Q(1,2)),(Q(6),Q(1,4))))
        self.assertEqual(sticks([(1,6),(1,2)]),tuple((Q(x),Q(1,4)) for x in (-4,-2,2,4)))
        self.assertEqual(sticks([(1,6),(1,3)]),tuple((Q(x,2),Q(1,4)) for x in (-9,-3,3,9)))
        self.assertEqual(sticks([(1,6),(1,6)]),sticks([(2,6)]))
        self.assertEqual(sticks([]),((Q(0),Q(1)),))
        self.assertEqual(sticks([(4,0)]),((Q(0),Q(1)),))

    def test_independent_full_spin_enumeration(self):
        # 1+3+...+3**6=1093 coupling lists. No binomial/convolution oracle.
        for n in range(7):
            for js in product((Q(0),Q(2),Q(3)),repeat=n):
                counts=Counter(sum((j*sign/Q(2) for j,sign in zip(js,spins)),Q(0))
                               for spins in product((-1,1),repeat=n))
                expected=tuple(sorted((x,Q(count,2**n)) for x,count in counts.items()))
                self.assertEqual(sticks([(1,j) for j in js]),expected)

    def test_grouping_and_binomial(self):
        for n in range(1,13):
            grouped=sticks([(n,6)])
            self.assertEqual(grouped,sticks([(1,6)]*n))
            self.assertEqual(len(grouped),n+1)
            self.assertEqual([w for x,w in grouped],[Q(comb(n,k),2**n) for k in range(n+1)])

    def test_moments_symmetry_and_signs(self):
        for js in product((Q(1),Q(2),Q(5,2)),repeat=3):
            lines=sticks([(1,j) for j in js])
            total,center,var=moments(lines)
            self.assertEqual((total,center),(1,0))
            self.assertEqual(var,sum(j*j/Q(4) for j in js))
            self.assertEqual(lines,sticks([(1,-j) for j in reversed(js)]))
            self.assertEqual(lines,tuple(sorted((-x,w) for x,w in lines)))

    def test_field_scaling_and_integrated_area(self):
        groups=[(1,6),(1,2)]
        for ref in (100,400,800):
            lines=positions_ppm(groups,Q(2),ref)
            total,center,var=moments(lines)
            self.assertEqual((total,center),(1,2))
            self.assertEqual(var,Q(10,ref*ref))
            self.assertEqual(tuple((x-Q(2))*ref for x,w in lines),tuple(Q(x) for x in (-4,-2,2,4)))
        self.assertEqual(positions_ppm(groups,2,400),tuple((Q(x,200),Q(1,4)) for x in (398,399,401,402)))
        self.assertEqual(sum(3*w for x,w in sticks(groups)),3)

    def test_contracts(self):
        for groups in (None,'x',iter(())):
            with self.assertRaises(TypeError):sticks(groups)
        for groups in ([(True,6)],[(1,6.0)],[(1,'6')],[(1,)],[(1,True)]):
            with self.assertRaises(TypeError):sticks(groups)
        for groups in ([(0,6)],[(-1,6)],[(13,6)]):
            with self.assertRaises(ValueError):sticks(groups)
        with self.assertRaises(ValueError):positions_ppm([],2,0)
        with self.assertRaises(TypeError):positions_ppm([],2.0,400)

if __name__=='__main__':unittest.main()
