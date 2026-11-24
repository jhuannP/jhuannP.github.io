import unittest
from .experiment import solve,exhaustive,allowed

class BacktrackingTests(unittest.TestCase):
    def test_solutions_against_independent_permutation_search(self):
        for n in range(1,9):
            solutions,stats=solve(n)
            self.assertEqual(solutions,exhaustive(n))
            self.assertEqual(len(solutions),len(set(solutions)))
        self.assertEqual(solve(4)[0],[(1,3,0,2),(2,0,3,1)])
        self.assertEqual(len(solve(8)[0]),92)

    def test_state_restoration_and_statistic_contract(self):
        for n in range(1,9):
            first,stats=solve(n)
            self.assertEqual((first,stats),solve(n))
            self.assertEqual(stats['attempts'],stats['nodes']-1+stats['pruned'])
            for solution in first:self.assertIsInstance(solution,tuple)
        self.assertEqual(solve(4)[1],dict(nodes=17,attempts=60,pruned=44))

    def test_partial_constraints_and_empty_results(self):
        self.assertFalse(allowed([1],1))  # Mesma coluna.
        self.assertFalse(allowed([1],0))  # Diagonal.
        self.assertTrue(allowed([1],3))
        prefix=[1,3]
        self.assertTrue(allowed(prefix,0))
        self.assertEqual(prefix,[1,3])
        self.assertEqual(solve(2)[0],[])
        self.assertEqual(solve(3)[0],[])

    def test_contracts(self):
        for n in (0,9,True,2.5):
            with self.assertRaises(ValueError):solve(n)
            with self.assertRaises(ValueError):exhaustive(n)

if __name__=='__main__':unittest.main()
