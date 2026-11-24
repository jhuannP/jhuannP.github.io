import unittest
from fractions import Fraction as Q
from .experiment import motion,kmh_to_ms

class MRUTests(unittest.TestCase):
    def test_units_and_known_cases(self):
        self.assertEqual(kmh_to_ms(72),20)
        self.assertEqual(kmh_to_ms(-18),-5)
        self.assertEqual(motion(30,kmh_to_ms('-7.2'),9,4),{'position':20,'displacement':-10,'distance':10,'elapsed':5})
        self.assertEqual(motion(0,kmh_to_ms(72),10)['distance'],200)

    def test_independent_step_accumulation(self):
        for x0 in (-30,0,30):
            for v in (-5,0,2):
                for dt in (0,1,5,10):
                    x=Q(x0)
                    for _ in range(dt*4): x+=Q(v,4)
                    r=motion(x0,v,4+dt,4)
                    self.assertEqual(r['position'],x)
                    self.assertEqual(r['distance'],sum([abs(Q(v,4))]*(dt*4)))

    def test_reference_changes_and_composition(self):
        for v in (-5,0,2):
            r=motion(30,v,9,4)
            self.assertEqual(r,motion(30,v,109,104))
            shifted=motion(-70,v,9,4)
            self.assertEqual(shifted['position'],r['position']-100)
            self.assertEqual(shifted['displacement'],r['displacement'])
            first=motion(30,v,6,4); second=motion(first['position'],v,9,6)
            self.assertEqual(second['position'],r['position'])
            self.assertEqual(first['distance']+second['distance'],r['distance'])

    def test_zero_direction_and_domain(self):
        self.assertEqual(motion(-5,0,20,4)['position'],-5)
        self.assertEqual(motion(-5,-3,4,4)['distance'],0)
        for args in [(0,1,0,1),(float('nan'),1,2,0),(0,float('inf'),2,0)]:
            with self.assertRaises(ValueError):motion(*args)

if __name__=='__main__':unittest.main()
