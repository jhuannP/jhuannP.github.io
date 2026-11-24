import unittest
from fractions import Fraction as Q
from .audit import CASES,BUGS,passes,detected,minimal_suites,implementation

class CaseTests(unittest.TestCase):
    def test_literal_reference_cases(self):
        for name in CASES:
            with self.subTest(case=name):self.assertTrue(passes('correct',name))
        with self.assertRaises(ValueError):implementation('correct',-1,3)
    def test_counterexample_matrix(self):
        expected={'rest':set(),'general':{'no_half','no_square','mass_squared'},'zero_mass':{'zero_rejected'},'negative_velocity':{'no_half','no_square','mass_squared'},'invalid_mass':{'negative_accepted'}}
        for case,bugs in expected.items():
            self.assertEqual(detected(case),bugs)
        self.assertEqual(set().union(*(detected(c) for c in CASES)),set(BUGS))
    def test_smallest_sets_for_fixed_candidates(self):
        groups={frozenset(g) for g in minimal_suites()}
        self.assertEqual(groups,{frozenset(('general','zero_mass','invalid_mass')),frozenset(('negative_velocity','zero_mass','invalid_mass'))})
    def test_equivalent_and_domain(self):
        for m in range(4):
            for v in range(-3,4):
                self.assertEqual(implementation('correct',m,v),implementation('equivalent_abs',m,v))
        for case in CASES:self.assertTrue(passes('equivalent_abs',case))
        for args in [(True,2),(1,0.5),(Q(-1,2),2)]:
            with self.assertRaises(ValueError):implementation('correct',*args)

if __name__=='__main__':unittest.main()
