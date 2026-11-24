from itertools import combinations,product
import unittest
from .subsets import verify,search,dp_decide,BudgetExceeded


def independent_sums(values):
    return {sum(values[i] for i in indices)
            for k in range(len(values)+1)
            for indices in combinations(range(len(values)),k)}


class SubsetTests(unittest.TestCase):
    def test_exhaustive_signed_instances_against_combinations(self):
        for n in range(6):
            for values in product((-1,0,2),repeat=n):
                reference=independent_sums(values)
                for target in range(-n-1,2*n+2):
                    cert=search(values,target)
                    self.assertEqual(cert is not None,target in reference)
                    if cert is not None:
                        self.assertEqual(len(cert),len(set(cert)))
                        self.assertEqual(sum(values[i] for i in cert),target)
                        self.assertTrue(verify(values,target,cert))

    def test_dp_against_independent_finite_sets(self):
        for n in range(6):
            for values in product((0,1,3),repeat=n):
                reference=independent_sums(values)
                for target in range(sum(values)+2):
                    self.assertEqual(dp_decide(values,target),target in reference)
        self.assertFalse(dp_decide([2],4))  # ascending updates would reuse one item
        self.assertTrue(dp_decide([2,2],4))
        self.assertTrue(dp_decide([],0));self.assertFalse(dp_decide([],1))

    def test_certificate_validation_and_equal_values(self):
        self.assertTrue(verify([2,5,9],11,[0,2]))
        self.assertFalse(verify([2,5,9],11,[0]))
        self.assertTrue(verify([5,5],10,[0,1]))
        for cert in ([0,0],[1],[-1],[True],[0.0],[[]],None,{0},[0,0,0]):
            self.assertFalse(verify([2],4,cert))
        self.assertTrue(verify([],0,[]));self.assertTrue(verify([0,0],0,[]))
        self.assertTrue(verify([-3,8],5,[0,1]))

    def test_budget_is_not_negative_answer_and_big_integers(self):
        with self.assertRaises(BudgetExceeded):search([2]*5,1,max_candidates=8)
        self.assertIsNone(search([2]*3,1,max_candidates=8))
        self.assertEqual(search([2]*100,0,max_candidates=1),[])
        huge=1<<1000
        self.assertTrue(verify([huge],huge,[0]))
        self.assertEqual(search([huge],huge),[0])
        with self.assertRaises(BudgetExceeded):dp_decide([huge],huge)
        with self.assertRaises(BudgetExceeded):dp_decide([],huge)
        self.assertTrue(dp_decide([2,5,9],11,max_work=36))
        with self.assertRaises(BudgetExceeded):dp_decide([2,5,9],11,max_work=35)

    def test_instance_domain_and_mutation(self):
        for values,target in [([True],1),([1.0],1),([1],True),([1],1.0),("12",3)]:
            with self.assertRaises(TypeError):verify(values,target,[])
        for values,target in [([-1,2],1),([1],-1)]:
            with self.assertRaises(ValueError):dp_decide(values,target)
        for bad in (0,-1,True,1.5):
            with self.assertRaises(ValueError):search([],0,max_candidates=bad)
            with self.assertRaises(ValueError):dp_decide([],0,max_work=bad)
        values=[2,5,9];cert=[0,2]
        verify(values,11,cert);search(values,11);dp_decide(values,11)
        self.assertEqual(values,[2,5,9]);self.assertEqual(cert,[0,2])

if __name__=="__main__":unittest.main()
