import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import evaluate

def direct(c,x):
    return sum((Q(a)*x**j for j,a in enumerate(c)),Q(0))
def derivative(c,x):
    return sum((j*Q(c[j])*x**(j-1) for j in range(1,len(c))),Q(0))

class HornerTraceTests(unittest.TestCase):
    def test_exact_enumeration_value_derivative_and_division(self):
        for length in range(1,5):
            for c in product((-1,0,1),repeat=length):
                for x in (Q(-2),Q(-1,2),Q(0),Q(1,3),Q(2)):
                    r=evaluate(c,x)
                    self.assertEqual(r["value"],direct(c,x))
                    self.assertEqual(r["derivative"],derivative(c,x))
                    self.assertEqual(direct(r["quotient"],x),r["derivative"])
                    for z in (Q(-3,2),Q(0),Q(5,2)):
                        self.assertEqual(direct(c,z),(z-x)*direct(r["quotient"],z)+r["remainder"])
                    self.assertEqual(r["value_multiplications"],length-1)

    def test_trace_and_old_value_for_derivative(self):
        r=evaluate([1,-3,2],2)
        self.assertEqual([(s["index"],s["value"],s["derivative"]) for s in r["trace"]],
                         [(2,2,0),(1,1,2),(0,3,5)])
        self.assertEqual(r["quotient"],[1,2])
        self.assertEqual(evaluate([0],2)["derivative"],0)
        self.assertEqual(evaluate([7],2)["quotient"],[])

    def test_each_partial_polynomial_invariant(self):
        c=[Q(2),Q(0),Q(-1,2),Q(3)]
        for x in (Q(-1),Q(1,2),Q(2)):
            r=evaluate(c,x)
            for row in r["trace"]:
                partial=c[row["index"]:]
                self.assertEqual(row["value"],direct(partial,x))
                self.assertEqual(row["derivative"],derivative(partial,x))

    def test_coefficient_sensitivity_is_not_root_error(self):
        x=Q(10001,10000);c=[1,-2,1];eps=Q(1,10**12)
        base=evaluate(c,x)["value"]
        perturbed=evaluate([Q(a)+eps*abs(a) for a in c],x)["value"]
        self.assertEqual(base,Q(1,10**8))
        scale=sum(abs(Q(a)*x**j) for j,a in enumerate(c))
        self.assertEqual(scale/abs(base),400040001)
        self.assertEqual(abs(perturbed-base),eps*scale)

    def test_contracts_and_no_input_mutation(self):
        c=[1,-3,2];evaluate(c,2);self.assertEqual(c,[1,-3,2])
        for coeff,x in (([],1),([True],1),([1.],1),([1],True),([1],.5),("123",1)):
            with self.assertRaises(ValueError):evaluate(coeff,x)
