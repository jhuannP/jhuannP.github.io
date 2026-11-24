import unittest
from fractions import Fraction as F
from .occupancy import distribution,moments,enumerate_assignments,tail

class OccupancyTests(unittest.TestCase):
    def test_enumeration_independent_of_combinations(self):
        for n in range(1,13):
            counts=enumerate_assignments(n)
            self.assertEqual(sum(counts),2**n)
            self.assertEqual(tuple(F(k,2**n) for k in counts),distribution(n))
        self.assertEqual(enumerate_assignments(8),(1,8,28,56,70,56,28,8,1))

    def test_exact_moments_from_distribution(self):
        for n in range(1,65):
            p=distribution(n);m=moments(n)
            self.assertEqual(sum(p),1)
            self.assertEqual(p,tuple(reversed(p)))
            mean=sum(k*q for k,q in enumerate(p))
            var=sum((k-mean)**2*q for k,q in enumerate(p))
            self.assertEqual(mean,m['mean']);self.assertEqual(var,m['variance'])
            self.assertEqual(var/n**2,m['fraction_variance'])
            self.assertEqual(var/mean**2,m['relative_variance'])

    def test_original_events_and_concentration(self):
        p=distribution(8)
        self.assertEqual(p[4],F(35,128))
        self.assertEqual(p[0]+p[8],F(1,128))
        self.assertEqual(sum(p[2:7]),F(119,128))
        self.assertEqual(tail(8,3),F(9,128))
        self.assertLessEqual(tail(8,3),F(2,9))
        for n in range(2,64,2):
            p=distribution(n);next_p=distribution(n+2)
            self.assertEqual(next_p[(n+2)//2]/p[n//2],F(n+1,n+2))
            self.assertLess(next_p[(n+2)//2],p[n//2])
        self.assertEqual(tail(8,0),1)
        self.assertEqual(tail(8,5),0)
        # Perfectly correlated occupancy, same mean and different variance.
        correlated={0:F(1,2),8:F(1,2)}
        self.assertEqual(sum(k*q for k,q in correlated.items()),4)
        self.assertEqual(sum((k-4)**2*q for k,q in correlated.items()),16)

    def test_contract(self):
        for x in (True,2.0,'8',None):
            with self.assertRaises(TypeError):distribution(x)
        for x in (0,-1,513):
            with self.assertRaises(ValueError):distribution(x)
        with self.assertRaises(ValueError):enumerate_assignments(17)
        with self.assertRaises(ValueError):tail(8,-1)
        with self.assertRaises(TypeError):tail(8,1.0)
