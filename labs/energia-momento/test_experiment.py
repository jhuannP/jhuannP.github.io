import json,math,unittest
from pathlib import Path
from .experiment import gamma,boost,kinetic,model


class EnergyMomentumTests(unittest.TestCase):
    def test_rapidity_reference_and_inverse(self):
        # Hyperbolic parametrization is independent of the gamma/boost arithmetic.
        for beta in (0,.1,.6,.95):
            for w in (-.8,-.4,0,.4,.8):
                for sign in (-1,1):
                    eta=math.atanh(sign*beta)-math.atanh(w)
                    e,p=boost(gamma(beta),sign*gamma(beta)*beta,w)
                    self.assertAlmostEqual(e,math.cosh(eta),delta=2e-14)
                    self.assertAlmostEqual(p,math.sinh(eta),delta=2e-14)
                    er,pr=boost(e,p,-w)
                    self.assertAlmostEqual(er,gamma(beta),delta=2e-14)
                    self.assertAlmostEqual(pr,sign*gamma(beta)*beta,delta=2e-14)

    def test_decimal_and_small_kinetic(self):
        rows=json.loads(Path(__file__).with_name('decimal_reference.json').read_text())
        for row in rows:
            b=row['beta'];s=model(0,b,0);p=s['particles'][0]
            self.assertAlmostEqual(p['energy'],float(row['energy']),delta=2e-15)
            self.assertAlmostEqual(p['momentum'],float(row['momentum']),delta=2e-15)
            ref=float(row['kinetic'])
            if ref:self.assertLessEqual(abs(p['kinetic']-ref)/ref,5e-15)
            else:self.assertEqual(p['kinetic'],0)
        self.assertEqual(gamma(1e-9)-1,0) # Subtraction loses the small result in binary64.
        self.assertGreater(model(0,1e-9,0)['sum_kinetic'],0)
        self.assertAlmostEqual(model(0,.6,0)['sum_kinetic'],.25,delta=1e-15)
        self.assertAlmostEqual(model(0,.6,0)['relative_error'],.28,delta=1e-15)

    def test_system_invariants_and_merger(self):
        for system in (0,1):
            for b in (0,.1,.6,.95):
                for w in (-.8,-.4,0,.4,.8):
                    s=model(system,b,w)
                    self.assertAlmostEqual(s['mass_squared'],s['mass']**2,delta=2e-13)
                    for p in s['particles']:
                        self.assertLess(abs(p['velocity']),1)
                        self.assertAlmostEqual((p['energy']-p['momentum'])*(p['energy']+p['momentum']),1,delta=2e-14)
                    self.assertAlmostEqual(s['sum_kinetic'],s['bulk_kinetic']+s['internal'],delta=1e-14)
                    # For the pair, complete sticking without escape preserves the total 4-vector.
                    if system==1:
                        e,p=boost(s['mass'],0,w)
                        self.assertAlmostEqual(s['energy'],e,delta=1e-14)
                        self.assertAlmostEqual(s['momentum'],p,delta=1e-14)
                        self.assertGreaterEqual(s['mass'],2)
        s=model(1,.6,0)
        self.assertAlmostEqual(s['mass'],2.5,delta=1e-15)
        self.assertEqual(s['bulk_kinetic'],0)
        self.assertAlmostEqual(s['sum_kinetic'],.5,delta=1e-15)

    def test_velocity_photons_and_domain(self):
        for b in (0,.6,.95):
            for w in (-.8,0,.6,.8):
                v=model(0,b,w)['particles'][0]['velocity']
                self.assertAlmostEqual(v,(b-w)/(1-b*w),delta=4e-16)
        # E=|p| branch, no gamma(1): two opposite unit photons give total M=2.
        for w in (-.8,0,.8):
            a,b=boost(1,1,w),boost(1,-1,w)
            e,p=a[0]+b[0],a[1]+b[1]
            self.assertAlmostEqual((e-p)*(e+p),4,delta=1e-14)
        for args in ((2,.6,0),(0,1,0),(0,.6,.9),(0,float('nan'),0)):
            with self.assertRaises(ValueError):model(*args)
        for beta in (-1,1,float('inf')):
            with self.assertRaises(ValueError):gamma(beta)
        with self.assertRaises(ValueError):boost(1,2,0)
