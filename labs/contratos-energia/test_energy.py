import unittest
from math import isfinite
from fractions import Fraction as Q
from .energy import energy_si,finite_real

class ContractTests(unittest.TestCase):
    def test_known_values_zero_and_units(self):
        self.assertEqual(energy_si(3,-4),24)
        self.assertEqual(energy_si(2,72/3.6),400)
        self.assertEqual(energy_si(2,72),5184)
        self.assertEqual(energy_si(0,1e308),0)
        self.assertEqual(energy_si(4,0),0)
        self.assertIs(type(energy_si(3,4)),float)

    def test_invalid_inputs_in_both_positions(self):
        for bad in (True,False,'3',None,1j,Q(1,2),float('nan'),float('inf'),-float('inf'),10**400):
            for args in ((bad,2),(2,bad)):
                with self.assertRaises(ValueError):energy_si(*args)
        with self.assertRaises(ValueError):energy_si(-1,2)
        self.assertEqual(finite_real(2**53+1,'valor'),float(2**53))

    def test_output_overflow_and_underflow(self):
        with self.assertRaises(OverflowError):energy_si(1e308,1e308)
        with self.assertRaises(ArithmeticError):energy_si(1e-300,1e-300)
        # Positive mass below float rounding range may already convert to zero;
        # input contract explicitly uses the converted float value.
        smallest=float.fromhex('0x0.0000000000001p-1022')
        self.assertGreater(energy_si(smallest,1e100),0)
        self.assertTrue(isfinite(energy_si(1e-300,1e200)))

    def test_physical_scalings_on_exactly_representable_inputs(self):
        for m in range(9):
            for v in range(-8,9):
                E=energy_si(m,v)
                self.assertEqual(E,energy_si(m,-v))
                self.assertEqual(energy_si(2*m,v),2*E)
                self.assertEqual(energy_si(m,2*v),4*E)
                self.assertGreaterEqual(E,0)
                self.assertEqual(E,float(Q(m*v*v,2)))

    def test_same_declared_inputs_repeat_without_state(self):
        inputs=(3,-4)
        first=energy_si(*inputs)
        energy_si(5,7)
        self.assertEqual(energy_si(*inputs),first)
        self.assertEqual(inputs,(3,-4))
