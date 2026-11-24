import unittest
from math import inf, nan
from .experiment import pressure, R

class OsmoticPressureTests(unittest.TestCase):
    def test_independent_known_values_and_units(self):
        self.assertAlmostEqual(pressure(.01,300),24943.387854,places=7)
        self.assertAlmostEqual(pressure(.02,300)/1000,49.886775708,places=9)
        # 0.01 mol/L = 10 mol/m³; nRT/V calculado independentemente.
        self.assertAlmostEqual(pressure(.01,300),.02*R*300/.002,places=8)

    def test_homogeneity_and_zero(self):
        for c in (0,.001,.005,.01,.02):
            for T in (280,300,320):
                self.assertEqual(pressure(0,T),0)
                self.assertAlmostEqual(pressure(2*c,T),2*pressure(c,T),places=8)
                self.assertAlmostEqual(pressure(c,2*T),2*pressure(c,T),places=8)
                self.assertAlmostEqual(pressure(c,T)+pressure(c,T),pressure(2*c,T),places=8)

    def test_unit_conversion_regression(self):
        self.assertAlmostEqual(pressure(.001,300)/(R*300),1)
        self.assertAlmostEqual(pressure(.01,320)/pressure(.01,280),320/280)

    def test_invalid_inputs(self):
        for c,T in [(-.1,300),(0,0),(0,-1),(True,300),(.1,False),(nan,300),(.1,inf),('0.1',300)]:
            with self.assertRaises(ValueError):pressure(c,T)
