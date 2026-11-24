import unittest
from itertools import product
from fractions import Fraction as Q
from .solenoid import solenoid


class MagnetizationTests(unittest.TestCase):
    def test_original_examples(self):
        a=solenoid(1000,2,Q(1,1000));b=solenoid(1000,2,Q(-1,1000))
        self.assertEqual((a['H'],a['M'],a['B_over_mu0']),(2000,2,2002))
        self.assertEqual((b['H'],b['M'],b['B_over_mu0']),(2000,-2,1998))

    def test_free_and_total_ampere(self):
        for n,I,chi,L in product((100,1000),(-2,0,2),(Q(-1,1000),Q(0),Q(1,1000)),(Q(1,10),1,2)):
            a=solenoid(n,I,chi)
            free_current=n*L*I;bound_current=a['M']*L
            self.assertEqual(a['H']*L,free_current)
            self.assertEqual(a['B_over_mu0']*L,free_current+bound_current)
            self.assertEqual(a['B_over_mu0'],a['mu_relative']*a['H'])

    def test_sign_and_linearity(self):
        for chi in (Q(-1,1000),Q(0),Q(1,1000)):
            a=solenoid(1000,2,chi);b=solenoid(1000,-2,chi);c=solenoid(1000,4,chi)
            for k in ('H','M','B_over_mu0','free_sheet','bound_sheet'):
                self.assertEqual(b[k],-a[k]);self.assertEqual(c[k],2*a[k])
        v=solenoid(1000,2,0)
        self.assertEqual(v['M'],0);self.assertEqual(v['H'],v['B_over_mu0'])

    def test_contracts(self):
        for n,I,chi in ((-1,1,0),(1,1,-1),(True,1,0),(1,1.,0),(1,1,Q(-3,2))):
            with self.assertRaises(ValueError):solenoid(n,I,chi)


if __name__=='__main__':unittest.main()
