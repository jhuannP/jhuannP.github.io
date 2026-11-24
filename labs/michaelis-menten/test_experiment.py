import importlib.util
import itertools
import math
import unittest
from decimal import Decimal as D,localcontext
from pathlib import Path
spec=importlib.util.spec_from_file_location('enzyme',Path(__file__).with_name('experiment.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class EnzymeTests(unittest.TestCase):
    def test_mass_balance_and_stationary_flux(self):
        for s,e,k,tau in itertools.product([0,.1,2,10],[.01,.02,.1],[.25,1,4],[0,1,3,5]):
            r=m.model(s,e,k,tau)
            self.assertAlmostEqual(r['free_now']+r['complex_now'],e)
            self.assertAlmostEqual(r['steady_free']+r['steady_complex'],e)
            binding=m.K_ON*r['steady_free']*s
            release=(m.K_OFF+k)*r['steady_complex']
            self.assertAlmostEqual(binding,release)
            self.assertTrue(0<=r['complex_now']<=r['steady_complex']<=e)
            self.assertTrue(0<=r['rate_now']<=r['steady_rate']<=r['vmax'])
            self.assertGreaterEqual(r['product'],0)
        self.assertEqual(m.model(2,.02,1)['fraction'],.5)
        self.assertEqual(m.model(substrate=0)['steady_rate'],0)

    def test_transient_ode_and_product_derivative(self):
        for s,e,k,tau in itertools.product([.1,2,10],[.02,.1],[.25,1,4],[.25,1,3]):
            r=m.model(s,e,k,tau);dt=1e-6
            before=m.model(s,e,k,tau-dt*r['relaxation'])
            after=m.model(s,e,k,tau+dt*r['relaxation'])
            derivative=(after['complex_now']-before['complex_now'])/(2*dt)
            rhs=m.K_ON*r['free_now']*s-(m.K_OFF+k)*r['complex_now']
            self.assertAlmostEqual(derivative,rhs,delta=1e-10)
            dp=(after['product']-before['product'])/(2*dt)
            self.assertAlmostEqual(dp,r['rate_now'],delta=1e-10)

    def test_decimal_and_small_time(self):
        with localcontext() as ctx:
            ctx.prec=70
            for s,k,t in itertools.product(['0.1','2','10'],['0.25','1','4'],['1e-8','1','3']):
                r=m.model(float(s),.02,float(k),float(t));sd,kd,tau=map(D,[s,k,t])
                km=1+kd;rate=kd*D('.02')*sd/(km+sd);lam=sd+1+kd
                exp=(-tau).exp();ref=rate/lam*(tau-1+exp)
                self.assertAlmostEqual(r['product'],float(ref),delta=max(abs(float(ref))*2e-14,1e-35))

    def test_parameters_are_distinct_and_domain(self):
        a=m.model();b=m.model(enzyme=.04)
        self.assertEqual(a['km'],b['km']);self.assertEqual(b['steady_rate'],2*a['steady_rate'])
        faster=m.model(kcat=4)
        self.assertEqual(faster['km'],5);self.assertEqual(faster['kd'],1)
        self.assertNotEqual(faster['km'],faster['kd'])
        self.assertEqual(m.model(tau=0)['rate_now'],0)
        for args in [(-1,.02,1,3),(1,0,1,3),(1,.02,0,3),(1,.02,1,-1),(float('nan'),.02,1,3)]:
            with self.assertRaises(ValueError):m.model(*args)

if __name__=='__main__':unittest.main()
