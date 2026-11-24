import unittest,itertools
from fractions import Fraction as Q
from .pumping import layer,full_riemann

class PumpingTests(unittest.TestCase):
    def test_reference_full_and_partial(self):
        r=layer(4,Q(1,2),6,0,4)
        self.assertEqual(r['volume_pi'],Q(16,3));self.assertEqual(r['centroid'],3)
        self.assertEqual(r['work_pi'],160000)
        self.assertEqual(layer(4,Q(1,2),6,0,2)['work_pi'],30000)
        self.assertEqual(layer(4,Q(1,2),6,2,4)['work_pi'],130000)
        self.assertEqual(full_riemann(4),(120000,200000))
    def test_independent_simpson_on_cubic_work_density(self):
        count=0
        for height,c,extra in itertools.product([2,4],[Q(1,3),Q(1,2),1],[0,2]):
            outlet=height+extra
            for low,high in [(Q(0),Q(height)),(Q(height,2),Q(height))]:
                middle=(low+high)/2
                density=lambda y:10000*(c*y)**2*(outlet-y)
                independent=(high-low)*(density(low)+4*density(middle)+density(high))/6
                self.assertEqual(layer(height,c,outlet,low,high)['work_pi'],independent);count+=1
        self.assertEqual(count,24)
    def test_energy_balance_and_additivity(self):
        for cut in [Q(i,8) for i in range(33)]:
            a=layer(4,Q(1,2),6,0,cut);b=layer(4,Q(1,2),6,cut,4);total=layer(4,Q(1,2),6,0,4)
            for key in ['volume_pi','weight_pi','work_pi']:self.assertEqual(a[key]+b[key],total[key])
            if a['centroid'] is not None:self.assertEqual(a['work_pi'],a['weight_pi']*(6-a['centroid']))
        # Extra outlet height adds weight times extra distance.
        a=layer(4,Q(1,2),6,0,4);b=layer(4,Q(1,2),7,0,4)
        self.assertEqual(b['work_pi']-a['work_pi'],a['weight_pi'])
    def test_riemann_bounds_and_refinement(self):
        previous=None
        for n in [1,2,4,8,16,32]:
            lower,upper=full_riemann(n)
            self.assertLessEqual(lower,160000);self.assertGreaterEqual(upper,160000)
            self.assertEqual(upper-lower,Q(320000,n))
            if previous:
                self.assertGreaterEqual(lower,previous[0]);self.assertLessEqual(upper,previous[1])
            previous=(lower,upper)
    def test_length_density_scaling_and_contracts(self):
        base=layer(4,Q(1,2),6,0,4)
        scaled=layer(8,Q(1,2),12,0,8)
        self.assertEqual(scaled['volume_pi'],8*base['volume_pi'])
        self.assertEqual(scaled['work_pi'],16*base['work_pi'])
        self.assertEqual(layer(4,Q(1,2),6,0,4,20000)['work_pi'],2*base['work_pi'])
        zero=layer(4,Q(1,2),6,2,2);self.assertEqual(zero['work_pi'],0);self.assertIsNone(zero['centroid'])
        for args in [(0,1,1,0,0),(4,0,6,0,4),(4,1,3,0,4),(4,1,6,-1,4),(4,1,6,3,2),(4,.5,6,0,4),(True,1,6,0,1)]:
            with self.assertRaises(ValueError):layer(*args)
        for n in [0,4097,True,1.5]:
            with self.assertRaises(ValueError):full_riemann(n)
