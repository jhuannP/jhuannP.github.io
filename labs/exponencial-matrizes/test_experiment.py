import math
import unittest
from fractions import Fraction as Q
from .experiment import evolution,state

def multiply(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))

class MatrixExponentialTests(unittest.TestCase):
    def test_against_rational_matrix_power_series(self):
        identity=((Q(1),Q(0)),(Q(0),Q(1)))
        for a in (-1,0,1):
            for b in (0,1,3):
                for t in (Q(-1),Q(0),Q(1,2),Q(2)):
                    A=((Q(a),Q(b)),(Q(0),Q(a)));power=identity;series=identity;factor=Q(1)
                    for k in range(1,41):
                        power=multiply(power,A);factor*=t/k
                        series=tuple(tuple(series[i][j]+factor*power[i][j] for j in range(2)) for i in range(2))
                    actual=evolution(a,b,float(t))
                    for i in range(2):
                        for j in range(2):self.assertAlmostEqual(actual[i][j],float(series[i][j]),places=11)

    def test_group_law_initial_and_nilpotent(self):
        for a in (-1,0,1):
            for b in (0,1,3):
                self.assertEqual(evolution(a,b,0),((1,0),(0,1)))
                product=multiply(evolution(a,b,.5),evolution(a,b,1.5));direct=evolution(a,b,2)
                inverse=multiply(evolution(a,b,1),evolution(a,b,-1))
                for i in range(2):
                    for j in range(2):
                        self.assertAlmostEqual(product[i][j],direct[i][j]);self.assertAlmostEqual(inverse[i][j],int(i==j))
        self.assertEqual(evolution(0,2,2),((1,4),(0,1)))
        self.assertEqual(state(0,2,2,1,3)['x'],13)

    def test_independent_derivatives_and_repeated_eigenvalue(self):
        h=1e-5
        for a in (-1,0,1):
            for b in (0,1,3):
                for t in (0,1,2):
                    q=state(a,b,t,1,2);left=state(a,b,t-h,1,2);right=state(a,b,t+h,1,2)
                    for value,derivative in [('x','dx'),('y','dy')]:self.assertAlmostEqual((right[value]-left[value])/(2*h),q[derivative],places=6)
                    self.assertEqual(q['eigenspace_dimension'],2 if b==0 else 1)
        # Mesmo autovalor zero não impede crescimento por acoplamento.
        self.assertEqual(state(0,3,4)['x'],12);self.assertEqual(state(0,0,4)['x'],0)

    def test_contract_and_noncommuting_matrices(self):
        for value in (True,float('nan'),float('inf'),'0',3):
            with self.assertRaises(ValueError):evolution(value,1,1)
        with self.assertRaises(ValueError):evolution(1,5,0)
        with self.assertRaises(ValueError):state(0,1,0,5,0)
        A=((0,1),(0,0));B=((0,0),(1,0))
        self.assertNotEqual(multiply(A,B),multiply(B,A))
