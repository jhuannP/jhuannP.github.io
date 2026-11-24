import math
import unittest
from .vapor import vapor_pressure,boiling_temperature,CURVES

# Entradas numéricas da fonte repetidas como referência independente do cadastro.
REFERENCE={"ethanol":(5.37229,1670.409,-40.191,273.,351.70),
           "dimethyl_ether":(4.11475,894.669,-30.604,194.93,248.24)}


def bisection(species,pressure):
    A,B,C,lo,hi=REFERENCE[species]
    for _ in range(65):
        mid=(lo+hi)/2
        if 10**(A-B/(mid+C))<pressure:lo=mid
        else:hi=mid
    return (lo+hi)/2


class VaporTests(unittest.TestCase):
    def test_inverse_against_independent_bisection(self):
        for species in REFERENCE:
            for pressure in (.05,.1,.2,.5,.9):
                t=boiling_temperature(species,pressure)
                self.assertAlmostEqual(t,bisection(species,pressure),places=10)
                self.assertAlmostEqual(vapor_pressure(species,t),pressure,places=12)

    def test_endpoints_and_monotonicity(self):
        for species,(_,_,_,lo,hi) in REFERENCE.items():
            temperatures=[lo+(hi-lo)*i/100 for i in range(101)]
            ps=[vapor_pressure(species,t) for t in temperatures]
            self.assertTrue(all(a<b for a,b in zip(ps,ps[1:])))
            for t in temperatures:
                self.assertAlmostEqual(boiling_temperature(species,vapor_pressure(species,t)),t,places=10)
            self.assertGreater(ps[0],0)

    def test_specific_example_and_pressure_change(self):
        ethanol=boiling_temperature("ethanol",.9)
        ether=boiling_temperature("dimethyl_ether",.9)
        self.assertAlmostEqual(ethanol,348.495607,places=6)
        self.assertAlmostEqual(ether,245.642430,places=6)
        self.assertAlmostEqual(ethanol-273.15,75.345607,places=6)
        self.assertAlmostEqual(ether-273.15,-27.507570,places=6)
        for species in REFERENCE:
            self.assertLess(boiling_temperature(species,.5),boiling_temperature(species,.9))
        self.assertLess(boiling_temperature("ethanol",1.01325),351.7)
        # O ajuste do éter termina ANTES da solução calculada para1atm.
        with self.assertRaises(ValueError):boiling_temperature("dimethyl_ether",1.01325)

    def test_outside_range_is_rejected_not_clamped(self):
        for species,(_,_,_,lo,hi) in REFERENCE.items():
            for t in (lo-1e-5,hi+1e-5,0,1000):
                with self.assertRaises(ValueError):vapor_pressure(species,t)
            for t in (lo-1e-5,hi+1e-5):
                A,B,C,_,_=REFERENCE[species]
                pressure=10**(A-B/(t+C))
                with self.assertRaises(ValueError):boiling_temperature(species,pressure)

    def test_units_contracts_and_source(self):
        for species in REFERENCE:
            self.assertTrue(CURVES[species].source.startswith("https://webbook.nist.gov/"))
            for bad in (True,"300",None):
                with self.assertRaises(TypeError):vapor_pressure(species,bad)
            for bad in (math.nan,math.inf,-math.inf):
                with self.assertRaises(ValueError):vapor_pressure(species,bad)
                with self.assertRaises(ValueError):boiling_temperature(species,bad)
            for bad in (0,-1,1e100):
                with self.assertRaises(ValueError):boiling_temperature(species,bad)
        for species in ("water",[],None):
            with self.assertRaises(ValueError):vapor_pressure(species,300)
        with self.assertRaises(ValueError):vapor_pressure("ethanol",10**10000)

if __name__=="__main__":unittest.main()
