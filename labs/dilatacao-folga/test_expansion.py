import unittest
from fractions import Fraction as Q
from .expansion import length,square,gap


class ExpansionTests(unittest.TestCase):
    def test_examples_and_units(self):
        a=Q(1,10000)
        r=length(1,a,50)
        self.assertEqual(r['change'],Q(5,1000));self.assertEqual(r['final'],Q(201,200))
        self.assertEqual(1000*r['change'],5)
        ar=square(1,a,50)
        self.assertEqual(ar['area'],Q(40401,40000))
        self.assertEqual(ar['first_order'],Q(101,100))
        self.assertEqual(ar['difference'],Q(1,40000))
        self.assertEqual(ar['difference']*10**6,25)

    def test_scaling_sign_and_area_remainder(self):
        for L in (Q(1,2),1,2):
            for a in (Q(0),Q(1,10000),Q(1,20000)):
                for t in (-50,0,50):
                    r=length(L,a,t)
                    self.assertEqual(length(2*L,a,t)['change'],2*r['change'])
                    self.assertEqual(length(L,a,-t)['change'],-r['change'])
                    self.assertEqual(square(L,a,t)['difference'],L**2*(a*t)**2)

    def test_gap_boundary_and_zero_coefficient(self):
        a=Q(1,10000);params=(1,a,Q(1,2),a,Q(6,1000))
        for t in (-20,0,20,40,50):
            r=gap(*params,t)
            self.assertEqual(r['free_gap'],Q(6,1000)-Q(3,20000)*t)
            self.assertEqual(r['first_contact_deltaT'],40)
            self.assertEqual(r['status']=='livre',t<40)
        self.assertEqual(gap(*params,50)['free_gap'],Q(-15,10000))
        self.assertIsNone(gap(1,0,1,0,Q(1,1000),50)['first_contact_deltaT'])
        self.assertNotEqual(gap(1,0,1,0,0,0)['status'],'livre')
        self.assertEqual(gap(1,0,1,0,0,0)['first_contact_deltaT'],0)

    def test_contracts(self):
        for args in ((0,0,1),(1,-1,0),(True,0,1),(1,.001,1),(1,1,1)):
            with self.assertRaises(ValueError):length(*args)
        with self.assertRaises(ValueError):gap(1,0,1,0,-1,0)


if __name__=='__main__':unittest.main()
