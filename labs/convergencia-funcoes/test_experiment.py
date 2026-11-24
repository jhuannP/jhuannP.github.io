import unittest
from fractions import Fraction as Q
from .experiment import power_witness,restricted_error,uniform_linear_index,spike

class FunctionConvergenceTests(unittest.TestCase):
    def test_moving_witness_prevents_uniform_convergence(self):
        for n in range(1,101):
            r=power_witness(n)
            self.assertLess(r['x'],1)
            self.assertGreaterEqual(r['value'],Q(1,2))
            self.assertEqual(r['value'],r['x']**n)
        self.assertGreater(power_witness(100)['x'],power_witness(1)['x'])

    def test_restricted_bounds_and_epsilon_index(self):
        for b in (Q(0),Q(1,2),Q(3,4)):
            for n in (1,2,5,20):
                bound=restricted_error(n,b)
                for k in range(21):self.assertLessEqual((b*Q(k,20))**n,bound)
        for eps in (Q(1,2),Q(1,10),Q(1,100),Q(2)):
            N=uniform_linear_index(eps)
            self.assertLess(Q(1,N),eps)
        self.assertEqual(uniform_linear_index(Q(1,10)),11)
        self.assertEqual(restricted_error(4,Q(1,2)),Q(1,16))

    def test_spike_integral_does_not_follow_pointwise_limit(self):
        for n in range(2,31):
            a,b,c=Q(0),Q(1,n),Q(2,n)
            self.assertEqual(spike(n,a),0)
            self.assertEqual(spike(n,b),n)
            self.assertEqual(spike(n,c),0)
            area=(b-a)*(spike(n,a)+spike(n,b))/2+(c-b)*(spike(n,b)+spike(n,c))/2
            self.assertEqual(area,1)
        for x in (Q(1,10),Q(1,2),Q(1)):
            n=int(2/x)+1
            self.assertEqual(spike(n,x),0)
        self.assertEqual(spike(20,0),0)

    def test_contracts(self):
        for n in (0,101,True,1.5):
            with self.assertRaises(ValueError):power_witness(n)
        for b in (-1,1,True):
            with self.assertRaises(ValueError):restricted_error(2,b)
        with self.assertRaises(ValueError):uniform_linear_index(0)
        with self.assertRaises(ValueError):spike(1,0)

if __name__=='__main__':unittest.main()
