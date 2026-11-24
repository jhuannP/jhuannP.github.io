from fractions import Fraction as Q
from itertools import product
import unittest
from .experiment import protocol

class CapacitorProtocolTests(unittest.TestCase):
    def test_reference_and_energy_budget(self):
        a=protocol(2,3,3,"charge");b=protocol(2,3,3,"voltage")
        self.assertEqual((a["Q"],a["V"],a["U"],a["externalWork"]),(6,1,3,-6))
        self.assertEqual((b["Q"],b["V"],b["U"],b["batteryEnergy"],b["externalWork"]),(18,3,27,-36,-18))
        self.assertEqual(a["U0"],9);self.assertEqual(b["deltaU"],18)
    def test_grid_physical_relations_and_protocols(self):
        for C0,V0,k in product((Q(1,2),1,2,4),(-3,-1,0,1,3),(1,2,3,4)):
            for mode in ("charge","voltage"):
                r=protocol(C0,V0,k,mode)
                self.assertEqual(r["Q"],r["C"]*r["V"])
                self.assertEqual(r["U"],r["Q"]**2/(2*r["C"]))
                self.assertEqual(r["U"],r["C"]*r["V"]**2/2)
                self.assertEqual(r["externalWork"],r["deltaU"]+r["batteryEnergy"])
                self.assertLessEqual(r["externalWork"],0)
                if mode=="charge":
                    self.assertEqual(r["Q"],r["Q0"]);self.assertEqual(r["U"]*k,r["U0"])
                    self.assertEqual(r["batteryEnergy"],0)
                else:
                    self.assertEqual(r["V"],V0);self.assertEqual(r["U"],k*r["U0"])
                    self.assertEqual(r["batteryEnergy"],-V0*(r["Q"]-r["Q0"]))
    def test_capacitance_and_voltage_scaling(self):
        for mode in ("charge","voltage"):
            r=protocol(2,3,3,mode);c=protocol(6,3,3,mode);v=protocol(2,6,3,mode)
            for key in ("Q","Q0","U","U0","deltaU","batteryEnergy","externalWork"):
                self.assertEqual(c[key],3*r[key])
            self.assertEqual(v["Q"],2*r["Q"])
            for key in ("U","U0","deltaU","batteryEnergy","externalWork"):
                self.assertEqual(v[key],4*r[key])
    def test_identity_zero_voltage_and_polarity(self):
        for mode in ("charge","voltage"):
            same=protocol(2,3,1,mode)
            self.assertEqual((same["deltaU"],same["batteryEnergy"],same["externalWork"]),(0,0,0))
            zero=protocol(2,0,4,mode)
            self.assertEqual((zero["Q"],zero["U"],zero["externalWork"]),(0,0,0))
            a=protocol(2,3,3,mode);b=protocol(2,-3,3,mode)
            self.assertEqual(a["Q"],-b["Q"]);self.assertEqual(a["V"],-b["V"])
            for key in ("U","deltaU","batteryEnergy","externalWork"):self.assertEqual(a[key],b[key])
    def test_contracts(self):
        for args in [(0,3,2,"charge"),(1,3,Q(1,2),"charge"),(True,3,2,"charge"),
                     (1.,3,2,"charge"),(1,3,2,"other")]:
            with self.assertRaises(ValueError):protocol(*args)
