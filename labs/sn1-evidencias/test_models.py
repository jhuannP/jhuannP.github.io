import unittest
from decimal import Decimal,localcontext
from fractions import Fraction as Q
from math import log
from .models import decay,stereo

class SN1Tests(unittest.TestCase):
    def test_decimal_decay(self):
        with localcontext() as ctx:
            ctx.prec=70
            for s in (0,0.1,0.2):
                for k in (0,0.01,0.2):
                    for t in (0,1,4,10):
                        expected=Decimal(str(s))*(-Decimal(str(k))*Decimal(str(t))).exp()
                        self.assertAlmostEqual(decay(s,k,t),float(expected),places=14)
    def test_half_life_and_conservation(self):
        k=log(2)/8
        for halves in range(5):
            s=decay(0.16,k,8*halves)
            self.assertAlmostEqual(s,0.16/2**halves,places=14)
            product=0.16-s
            self.assertAlmostEqual(s+product,0.16,places=14)
            self.assertGreaterEqual(product,0)
        self.assertEqual(decay(0.2,0,100),0.2)
    def test_stereo_event_enumeration(self):
        # Enumerate 20 equally weighted prescribed events; free count even.
        for count in range(0,21,2):
            events=['inv','ret']*(count//2)+['inv']*(20-count)
            inv,ret=stereo(Q(count,20))
            self.assertEqual(inv,Q(events.count('inv'),20))
            self.assertEqual(ret,Q(events.count('ret'),20))
            self.assertEqual(inv+ret,1)
        self.assertEqual(stereo(Q(3,5)),(Q(7,10),Q(3,10)))
    def test_pseudo_first_order_indistinguishability(self):
        # One curve cannot distinguish k1 from a fixed k2*Nu.
        k1=0.1;k2=0.5;nu=0.2
        for t in (0,1,4,8):
            self.assertAlmostEqual(decay(0.2,k1,t),decay(0.2,k2*nu,t),places=14)
        # Changing Nu under the fixed-constant assumption changes only model 2.
        self.assertLess(decay(0.2,k2*2*nu,4),decay(0.2,k1,4))
    def test_contracts(self):
        for args in [(-1,1,1),(1,-1,1),(1,1,-1),(1,float('nan'),1),(True,1,1)]:
            with self.assertRaises(ValueError): decay(*args)
        for x in (Q(-1,2),Q(3,2),0.5,True):
            with self.assertRaises(ValueError): stereo(x)

if __name__=='__main__':unittest.main()
