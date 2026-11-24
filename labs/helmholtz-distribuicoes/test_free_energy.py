import unittest
from math import exp,log
from itertools import product
from .free_energy import compare

class Tests(unittest.TestCase):
    def test_original_fixture_and_hidden_entropy(self):
        t=1/log(2); p=[.5,.25,.25]
        a=compare([0,1,1],t,p);b=compare([0,1,1],t,[.5,.5,0])
        for actual,expected in zip(a['p'],p):self.assertAlmostEqual(actual,expected)
        self.assertAlmostEqual(a['U'],.5);self.assertAlmostEqual(b['U'],.5)
        self.assertAlmostEqual(a['H'],1.5*log(2));self.assertAlmostEqual(b['H'],log(2))
        self.assertAlmostEqual(a['trial']/t,-log(2))
        self.assertAlmostEqual(b['kl'],.5*log(2));self.assertAlmostEqual(b['gap'],.5)
        # Níveis: P=(1/2,1/2),g=(1,2). Informação interna deve ser somada.
        group_H=log(2);micro_H=group_H+.5*log(2)
        self.assertAlmostEqual(micro_H,a['H']);self.assertNotAlmostEqual(group_H,a['H'])
    def test_simplex_vs_independent_direct_weights(self):
        count=0
        for E in ([0,1,1],[-2,0,3],[1,1,1]):
            for t in (.2,1,3):
                Z=sum(exp(-e/t) for e in E); f=-t*log(Z)
                for i in range(13):
                    for j in range(13-i):
                        q=[i/12,j/12,(12-i-j)/12];r=compare(E,t,q)
                        self.assertGreaterEqual(r['gap'],-1e-12)
                        self.assertAlmostEqual(r['equilibrium'],f,places=11)
                        self.assertAlmostEqual(r['gap'],t*r['kl'],places=11)
                        count+=1
        self.assertEqual(count,819)
    def test_shift_permutation_and_temperature_derivative(self):
        E=[-1,0,2];q=[.2,.3,.5]
        for t in (.3,1,4):
            r=compare(E,t,q);shift=compare([e+3 for e in E],t,q)
            self.assertAlmostEqual(shift['trial']-r['trial'],3)
            self.assertAlmostEqual(shift['equilibrium']-r['equilibrium'],3)
            self.assertAlmostEqual(shift['kl'],r['kl'])
            perm=compare(E[::-1],t,q[::-1]);self.assertAlmostEqual(perm['gap'],r['gap'])
            # dF/dtheta=-H(p): derivada central, fora da rotina de entropia.
            h=1e-5
            derivative=(compare(E,t+h,q)['equilibrium']-compare(E,t-h,q)['equilibrium'])/(2*h)
            H=-sum(x*log(x) for x in r['p'])
            self.assertAlmostEqual(derivative,-H,places=7)
        r=compare([-10,10],.1,[0,1]);self.assertAlmostEqual(r['kl'],200)
        self.assertGreater(r['p'][1],0)
    def test_contracts(self):
        for E,t,q in [([],1,[]),([0],1,[1]),([0,11],1,[.5,.5]),([0,1],0,[.5,.5]),
                      ([0,1],True,[.5,.5]),([0,1],1,[.4,.4]),([0,1],1,[-.1,1.1]),
                      ([0,1],1,[1]),([0,1],1,[True,0]),([0,float('nan')],1,[.5,.5]),
                      ([0,1],float('inf'),[.5,.5]),([0,1],1,[float('nan'),0]),
                      ([0,10**1000],1,[.5,.5]),([0,1],1,['.5',.5])]:
            with self.assertRaises(ValueError):compare(E,t,q)
