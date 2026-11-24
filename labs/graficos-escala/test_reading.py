import unittest
from fractions import Fraction as Q
from .reading import relative_change,bar_comparison,rate_change,secant,histogram_density


class ReadingTests(unittest.TestCase):
    def test_fixed_data_two_origins(self):
        normal=bar_comparison(100,110)
        cut=bar_comparison(100,110,90)
        self.assertEqual(normal,dict(absolute=Q(10),relative=Q(1,10),value_ratio=Q(11,10),drawn_ratio=Q(11,10)))
        self.assertEqual(cut['drawn_ratio'],2)
        self.assertEqual(cut['relative'],normal['relative'])

    def test_ratios_over_valid_origins_and_unit_scale(self):
        for a in range(1,11):
            for b in range(1,11):
                ratios=[]
                for origin in range(min(a,b)):
                    r=bar_comparison(a,b,origin);ratios.append(r['drawn_ratio'])
                    self.assertEqual(r['relative'],Q(b-a,a))
                    self.assertEqual(r['value_ratio'],Q(b,a))
                    scaled=bar_comparison(3*a,3*b,3*origin)
                    self.assertEqual(scaled['drawn_ratio'],r['drawn_ratio'])
                    self.assertEqual(scaled['relative'],r['relative'])
                    self.assertEqual(scaled['absolute'],3*r['absolute'])
                if b>a:self.assertTrue(all(x<y for x,y in zip(ratios,ratios[1:])))
                if b<a:self.assertTrue(all(x>y for x,y in zip(ratios,ratios[1:])))

    def test_percent_points_reverse_and_zero(self):
        self.assertEqual(rate_change(20,25),dict(points=Q(5),relative=Q(1,4)))
        self.assertEqual(relative_change(110,100)*100,Q(-100,11))
        self.assertEqual(relative_change(100,0),-1)
        self.assertEqual(rate_change(0,10),dict(points=Q(10),relative=None))

    def test_actual_time_intervals(self):
        first=secant(0,100,1,110);second=secant(1,110,3,120)
        self.assertEqual((first,second),(10,5))
        self.assertEqual(secant(0,100,3,120),Q(20,3))
        self.assertEqual((first*1+second*2)/3,Q(20,3))

    def test_histogram_area_and_unit_conversion(self):
        edges=[0,1,3];counts=[2,2]
        densities=histogram_density(edges,counts)
        self.assertEqual(densities,(Q(1,2),Q(1,4)))
        self.assertEqual(sum(d*(b-a) for a,b,d in zip(edges,edges[1:],densities)),1)
        self.assertEqual(histogram_density([60*x for x in edges],counts),tuple(d/60 for d in densities))
        self.assertEqual(histogram_density([0,1,2],[0,3]),(0,1))

    def test_contracts(self):
        for args in [(0,1),(True,1),(1,1.0),(1,-1)]:
            with self.assertRaises(ValueError):relative_change(*args)
        for args in [(100,110,100),(100,0,0),(1,2,-1)]:
            with self.assertRaises(ValueError):bar_comparison(*args)
        with self.assertRaises(ValueError):secant(1,1,1,2)
        with self.assertRaises(ValueError):rate_change(20,101)
        for edges,counts in [([0,0],[1]),([0,1],[0]),([0,1],[True]),([0,1,2],[1]),([0,1],[1.0])]:
            with self.assertRaises(ValueError):histogram_density(edges,counts)

if __name__=='__main__':unittest.main()
