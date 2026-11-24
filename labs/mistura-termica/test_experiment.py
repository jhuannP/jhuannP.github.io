from fractions import Fraction as Q
from itertools import product
import unittest
from .experiment import mix

class ThermalMixTests(unittest.TestCase):
    def test_reference_and_zero_capacity(self):
        self.assertEqual(mix(1,2,80,20,1,20),dict(Tf=35,Q1=-45,Q2=30,Qcal=15))
        self.assertEqual(mix(1,2,80,20)["Tf"],40)
        a=mix(1,2,80,20,0,10);b=mix(1,2,80,20,0,80)
        self.assertEqual(a,b)
    def test_grid_conservation_bounds_and_signs(self):
        for C1,C2,T1,T2,Ccal,Tcal in product((1,2,4),(1,2,4),(10,40,80),(10,40,80),(0,1,2),(10,40,80)):
            r=mix(C1,C2,T1,T2,Ccal,Tcal)
            self.assertEqual(r["Q1"]+r["Q2"]+r["Qcal"],0)
            temps=[T1,T2]+([Tcal] if Ccal else [])
            self.assertLessEqual(min(temps),r["Tf"]);self.assertLessEqual(r["Tf"],max(temps))
            # Reconstruct temperature from energy relative to 20°C, independently of implementation.
            energy=C1*(T1-20)+C2*(T2-20)+Ccal*(Tcal-20)
            self.assertEqual(r["Tf"],20+Q(energy,C1+C2+Ccal))
    def test_offset_and_capacity_scaling(self):
        a=mix(1,2,80,20,1,20);shift=Q(27315,100)
        b=mix(1,2,80+shift,20+shift,1,20+shift)
        self.assertEqual(b["Tf"],a["Tf"]+shift)
        for k in ("Q1","Q2","Qcal"):self.assertEqual(b[k],a[k])
        c=mix(3,6,80,20,3,20)
        self.assertEqual(c["Tf"],a["Tf"])
        for k in ("Q1","Q2","Qcal"):self.assertEqual(c[k],3*a[k])
    def test_exchange_symmetry_and_equal_temperatures(self):
        a=mix(1,2,80,20,1,40);b=mix(2,1,20,80,1,40)
        self.assertEqual(a["Tf"],b["Tf"])
        self.assertEqual(a["Q1"],b["Q2"]);self.assertEqual(a["Q2"],b["Q1"])
        self.assertEqual(mix(2,3,30,30,4,30),dict(Tf=30,Q1=0,Q2=0,Qcal=0))
    def test_contracts(self):
        for args in [(0,1,20,30),(-1,1,20,30),(1,1,20,30,-1),(True,1,20,30),(1.,1,20,30),(1,1,-274,30)]:
            with self.assertRaises(ValueError):mix(*args)
        self.assertEqual(mix(1,1,-10,10)["Tf"],0) # generic phase-preserving model, not liquid water
