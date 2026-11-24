import unittest
from fractions import Fraction as F
from .bars import bar,series,parallel,element


class BarTests(unittest.TestCase):
    def test_uniform_literal_SI(self):
        b=bar(120,2,F(3,10**6),40*10**9)
        self.assertEqual(b,dict(stress=F(40*10**6),strain=F(1,1000),extension=F(1,500),stiffness=F(60000),energy=F(3,25)))
        self.assertEqual(bar(0,2,F(3,10**6),40*10**9)['extension'],0)

    def test_geometric_scaling(self):
        for L in (1,2,5):
            for A in (F(2,10**6),F(3,10**6)):
                base=bar(120,L,A,40*10**9)
                longer=bar(120,2*L,A,40*10**9);wider=bar(120,L,2*A,40*10**9)
                self.assertEqual(longer['stiffness'],base['stiffness']/2)
                self.assertEqual(longer['extension'],2*base['extension'])
                self.assertEqual(longer['strain'],base['strain'])
                self.assertEqual(wider['stiffness'],2*base['stiffness'])
                self.assertEqual(wider['stress'],base['stress']/2)

    def test_series_parallel_literal_and_partition(self):
        E=40*10**9;parts=[(1,F(2,10**6),E),(1,F(4,10**6),E)]
        s=series(120,parts);p=parallel(120,parts)
        self.assertEqual((s['stiffness'],s['extension'],s['energy']),(F(160000,3),F(9,4000),F(27,200)))
        self.assertEqual(tuple(x['stress'] for x in s['elements']),(F(60*10**6),F(30*10**6)))
        self.assertEqual((p['stiffness'],p['extension'],p['forces'],p['energy']),(F(240000),F(1,2000),(F(40),F(80)),F(3,100)))
        self.assertEqual(sum(p['forces']),120)
        for count in (1,2,3,7):
            whole=bar(120,2,F(3,10**6),E)
            split=series(120,[(F(2,count),F(3,10**6),E)]*count)
            for key in ('stiffness','extension','energy'):self.assertEqual(whole[key],split[key])

    def test_nodal_energy_reference(self):
        # Independent prescribed-end-displacement potential, using literal k1=80000,k2=160000.
        delta=F(9,4000);u=F(3,2000)
        def energy(joint):return (80000*joint**2+160000*(delta-joint)**2)/2
        self.assertEqual(energy(u),F(27,200))
        self.assertEqual(80000*u,120);self.assertEqual(160000*(delta-u),120)
        for h in (F(-1,10000),F(1,10000),F(1,2000),F(-1,1000)):
            self.assertEqual(energy(u+h)-energy(u),120000*h*h)
            self.assertGreater(energy(u+h),energy(u))
        step=F(1,10000)
        self.assertEqual((energy(u+step)-energy(u-step))/(2*step),0)

    def test_contracts(self):
        for args in [(-1,1,1,1),(1,0,1,1),(1,1,0,1),(1,1,1,0),(True,1,1,1),(1,1.,1,1)]:
            with self.assertRaises(ValueError):bar(*args)
        for parts in [[],[(1,1)],[(1,1,-1)],[(1,1,True)],[(1,1,1)]*65]:
            with self.assertRaises(ValueError):series(1,parts)
        with self.assertRaises(ValueError):parallel(-1,[(1,1,1)])

if __name__=='__main__':unittest.main()
