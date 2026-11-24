import unittest
from fractions import Fraction as Q
from .sequence import aitken, two_modes

class AitkenTests(unittest.TestCase):
    def test_geometric_and_translation(self):
        for q in [Q(-3,4),Q(-1,2),Q(1,4),Q(1,2),Q(99,100)]:
            for c in [Q(-2),Q(1,3),Q(5)]:
                for n in range(8):
                    v=[Q(2)+c*q**(n+i) for i in range(3)]
                    self.assertEqual(aitken(*v),2)
                    self.assertEqual(aitken(*(x+10**20 for x in v)),2+10**20)
    def test_two_modes_error_identity(self):
        for n in range(20):
            v=[two_modes(n+i) for i in range(3)]
            a,b=Q(1,2)**n,Q(1,4)**n
            residual=a*b*Q(1,4)**2/(a*Q(1,2)**2+b*Q(3,4)**2)
            self.assertEqual(aitken(*v)-2,residual)
        self.assertEqual(aitken(4,Q(11,4),Q(37,16)),Q(27,13))
    def test_harmonic_and_perturbation(self):
        for n in range(100):
            self.assertEqual(aitken(*(Q(1,n+i+1) for i in range(3))),Q(1,2*(n+2)))
        self.assertEqual(aitken(1,Q(101,100),Q(10199,10000)),2)
        self.assertEqual(aitken(1,Q(101,100),Q(20399,20000)),3)
    def test_contracts_and_information_loss(self):
        for v in [(2,2,2),(1,2,3)]:
            with self.assertRaises(ArithmeticError):aitken(*v)
        for bad in [True,1.5,'1',float('nan'),None]:
            with self.assertRaises(ValueError):aitken(bad,2,3)
        for n in [-1,101,True,1.5]:
            with self.assertRaises(ValueError):two_modes(n)
        self.assertEqual(len({float(Q(10**20)+x) for x in [Q(1),Q(3,2),Q(7,4)]}),1)

if __name__=='__main__':unittest.main()
