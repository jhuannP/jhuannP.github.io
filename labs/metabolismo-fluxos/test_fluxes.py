import unittest
from fractions import Fraction as F
from .fluxes import parameters,fluxes,steady,step


class FluxTests(unittest.TestCase):
    def test_literal_reference(self):
        s=steady();self.assertEqual((s['a'],s['y']),(4,4));f=s['fluxes']
        for k,v in dict(glycolysis=8,pentose=4,storage=4,mobilization=4,da=0,dy=0,
                        pyruvate=16,pentose_product=4,co2=4,nadph=8,
                        carbon_input=72,carbon_output=72).items():self.assertEqual(f[k],v)
        self.assertEqual(step(2,4,F(1,4)),(4,F(7,2)))
        modified=steady((12,5,1,1,1));self.assertEqual(modified['a'],2)
        self.assertEqual(modified['fluxes']['glycolysis'],10)
        self.assertEqual(modified['fluxes']['pentose'],2)

    def test_stationary_balances(self):
        for J in [0,3,12]:
            for kg,kp in [(2,1),(0,3),(3,0),(1,1)]:
                for ks in [0,1,3]:
                    for km in [1,2]:
                        p=(J,kg,kp,ks,km);s=steady(p);f=s['fluxes']
                        self.assertEqual((f['da'],f['dy']),(0,0))
                        self.assertEqual(f['glycolysis']+f['pentose'],J)
                        self.assertEqual(f['carbon_output'],6*J)
                        # Independent 2x2 determinant/Cramer reference for the linear balance.
                        a11,a12,a21,a22=-(kg+kp+ks),km,ks,-km
                        determinant=a11*a22-a12*a21
                        self.assertGreater(determinant,0);self.assertLess(a11+a22,0)
                        self.assertEqual(s['a'],F(J*km,determinant))
                        self.assertEqual(s['y'],F(J*ks,determinant))

    def test_carbon_ledger_off_stationary(self):
        # Count carbon atoms of products independently from model's grouped six-carbon output.
        for a in [0,1,4,7]:
            for y in [0,2,9]:
                f=fluxes(a,y)
                output=3*f['pyruvate']+5*f['pentose_product']+f['co2']
                accumulation=6*(f['da']+f['dy'])
                self.assertEqual(accumulation,72-output)
                self.assertEqual(output,f['carbon_output'])

    def test_nonidentifiability_scalings(self):
        base=steady();p=(12,2,1,1,1)
        for scale in [F(1,2),2,3]:
            both=steady(tuple(scale*x for x in p))
            self.assertEqual((both['a'],both['y']),(base['a'],base['y']))
            rates=steady((p[0],*(scale*x for x in p[1:])))
            self.assertEqual((rates['a'],rates['y']),(base['a']/scale,base['y']/scale))
            for key in ['glycolysis','pentose','storage','mobilization']:
                self.assertEqual(both['fluxes'][key],scale*base['fluxes'][key])
                self.assertEqual(rates['fluxes'][key],base['fluxes'][key])

    def test_euler_balance_and_nonnegativity(self):
        for a in [0,1,4,7]:
            for y in [0,2,9]:
                for h in [F(1,16),F(1,8),F(1,4)]:
                    an,yn=step(a,y,h);f=fluxes(a,y)
                    self.assertGreaterEqual(min(an,yn),0)
                    self.assertEqual(6*((an+yn)-(a+y)),h*(72-3*f['pyruvate']-5*f['pentose_product']-f['co2']))
        with self.assertRaises(ValueError):step(10,0,1)

    def test_contracts(self):
        for p in [(12,0,0,1,1),(12,2,1,1,0),(-1,2,1,1,1),(12,2,1,-1,1),(True,2,1,1,1)]:
            with self.assertRaises(ValueError):parameters(*p)
        for a,y in [(-1,0),(0,-1),(1.0,1),(True,0)]:
            with self.assertRaises(ValueError):fluxes(a,y)
        with self.assertRaises(ValueError):step(1,1,-1)

if __name__=='__main__':unittest.main()
