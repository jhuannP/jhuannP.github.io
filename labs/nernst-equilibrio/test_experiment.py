import unittest
from math import exp,log,nan,inf
from .experiment import energy,model,R,F

class NernstTests(unittest.TestCase):
    def test_equilibrium_and_displacements(self):
        for ratio in (.1,.25,.5,1,2,4,10):
            for z in (-2,-1,1,2):
                for T in (280.,310.):
                    E=energy(ratio,1,0,z,T)['E_mV']
                    self.assertAlmostEqual(energy(ratio,1,E,z,T)['total'],0,delta=1e-10)
                    for dV in (-1.,1.):
                        self.assertAlmostEqual(energy(ratio,1,E+dV,z,T)['total'],z*F*dV/1000,delta=1e-9)
    def test_reversal_scale_temperature_and_valence(self):
        for ci,co in ((10,1),(1,4),(2,2)):
            E=energy(ci,co,0)['E_mV']
            self.assertAlmostEqual(energy(co,ci,0)['E_mV'],-E)
            self.assertAlmostEqual(energy(7*ci,7*co,0)['E_mV'],E)
            self.assertAlmostEqual(energy(ci,co,0,-1)['E_mV'],-E)
            self.assertAlmostEqual(energy(ci,co,0,2)['E_mV'],E/2)
            self.assertAlmostEqual(energy(ci,co,0,1,620)['E_mV'],2*E)
    def test_boltzmann_ratio_and_synthetic_model(self):
        for kind in (0,1):
            for q in range(-2,3):
                s=model(kind,q,0)
                recovered=exp(-s['z']*F*s['E_mV']/1000/(R*310))
                self.assertAlmostEqual(recovered,10.**q,delta=1e-10)
                self.assertAlmostEqual(s['total'],R*310*log(10.**q),delta=1e-10)
        self.assertLess(model(0,1)['E_mV'],0)
        self.assertGreater(model(1,1)['E_mV'],0)
        self.assertEqual(model(0,0,0)['total'],0)
    def test_affine_voltage_response_and_ion_sign(self):
        for kind in (0,1):
            for q in range(-2,3):
                a,b,c=model(kind,q,-100),model(kind,q,0),model(kind,q,100)
                self.assertAlmostEqual((a['total']+c['total'])/2,b['total'],delta=1e-10)
                self.assertAlmostEqual(c['total']-b['total'],b['z']*F*.1,delta=1e-10)
        self.assertLess(model(1,0,100)['total'],0) # ânion: entrada favorecida, não saída
    def test_contracts(self):
        for args in [(0,1,0),(1,-1,0),(1,1,False),(1,1,nan),(1,1,0,0),(1,1,0,True),(1,1,0,1,0)]:
            with self.assertRaises(ValueError):energy(*args)
        for args in [(True,1,0),(2,1,0),(0,3,0),(0,1,151),(0,1,inf)]:
            with self.assertRaises(ValueError):model(*args)
