import unittest
from fractions import Fraction as Q
from itertools import product
from .exchange import stationary, derivative


class ExchangeTests(unittest.TestCase):
    def test_fixture(self):
        r=stationary(12,3,1,3,1)
        self.assertEqual((r['nuclear'],r['cytosolic'],r['cn'],r['cc']),(9,3,9,1))
        self.assertEqual(r['ratio'],9);self.assertEqual(r['inward'],9)
        self.assertEqual(r['outward'],9);self.assertEqual(r['tau'],Q(1,4))
        self.assertEqual(derivative(0,12,3,1),36)

    def test_conservation_fixed_point_and_relaxation(self):
        # 27 modelos e cinco estados; uma etapa de balanço independente preserva faixa.
        for total,a,b in product((1,3,12),(1,2,5),(1,3,4)):
            r=stationary(total,a,b);dt=Q(1,2*(a+b))
            self.assertEqual(r['nuclear']+r['cytosolic'],total)
            self.assertEqual(a*r['cytosolic'],b*r['nuclear'])
            self.assertEqual(derivative(r['nuclear'],total,a,b),0)
            for j in range(5):
                x=Q(total*j,4)
                # Transferências para dentro e fora calculadas separadamente.
                incoming=dt*a*(total-x);outgoing=dt*b*x
                new=x+incoming-outgoing
                self.assertTrue(0<=new<=total)
                self.assertEqual(new-r['nuclear'],(x-r['nuclear'])/2)

    def test_identifiability_scales_and_volumes(self):
        r=stationary(12,3,1,3,1)
        s=stationary(12,Q(3,10),Q(1,10),3,1)
        self.assertEqual(r['nuclear'],s['nuclear']);self.assertEqual(r['ratio'],s['ratio'])
        self.assertEqual(r['inward'],10*s['inward']);self.assertEqual(s['tau'],10*r['tau'])
        volumes=stationary(12,3,1,1,1)
        self.assertEqual(volumes['nuclear'],9);self.assertEqual(volumes['ratio'],3)
        swapped=stationary(12,1,3,1,3)
        self.assertEqual(swapped['cn'],r['cc']);self.assertEqual(swapped['cc'],r['cn'])
        self.assertEqual(swapped['ratio']*r['ratio'],1)
        scaled=stationary(24,3,1,3,1)
        self.assertEqual(scaled['ratio'],r['ratio']);self.assertEqual(scaled['inward'],2*r['inward'])

    def test_zero_and_contracts(self):
        r=stationary(0,3,1)
        self.assertIsNone(r['ratio']);self.assertEqual(r['inward'],0)
        for args in [(-1,3,1),(12,0,1),(12,3,0),(True,3,1),(12,3.0,1),(12,3,1,0,1)]:
            with self.assertRaises(ValueError):stationary(*args)
        with self.assertRaises(ValueError):derivative(13,12,3,1)
