import unittest
from fractions import Fraction as F
from .lens import image,ray
class LensTests(unittest.TestCase):
    def test_real_virtual_and_focus(self):
        self.assertEqual(image(10,30),{'kind':'real','q':F(15),'m':F(-1,2)})
        self.assertEqual(image(10,5),{'kind':'virtual','q':F(-10),'m':F(2)})
        self.assertEqual(image(-10,30)['q'],F(-15,2))
        self.assertEqual(image(-10,30)['m'],F(1,4))
        self.assertEqual(image(10,10),{'kind':'collimated','q':None,'m':None})

    def test_ray_intersection_independent_of_aperture(self):
        for f in [-10,-5,5,10]:
            for p in [2,5,10,20,30]:
                state=image(f,p)
                for h in [F(-1),F(0),F(2)]:
                    slopes=[]
                    for y in [-1,0,1]:
                        if state['q'] is None:
                            slopes.append(ray(f,p,h,y,0)[1])
                        else:
                            actual,_=ray(f,p,h,y,state['q'])
                            self.assertEqual(actual,state['m']*h)
                    if slopes:self.assertEqual(len(set(slopes)),1)
                if state['q'] is not None:
                    self.assertEqual(1/F(f),1/F(p)+1/state['q'])

    def test_scale_reciprocity_and_focal_limit(self):
        for k in [F(1,10),F(1),F(10)]:
            s=image(10*k,30*k)
            self.assertEqual(s['q'],15*k);self.assertEqual(s['m'],F(-1,2))
        # Real conjugate positions can be interchanged.
        self.assertEqual(image(10,15)['q'],30)
        for epsilon in [F(1),F(1,10),F(1,100)]:
            self.assertGreater(image(10,10+epsilon)['q'],0)
            self.assertLess(image(10,10-epsilon)['q'],0)
            self.assertEqual(image(10,10+epsilon)['q'],10+100/epsilon)

    def test_contracts(self):
        for f,p in [(0,1),(1,0),(1,-1)]:
            with self.assertRaises(ValueError):image(f,p)
        for f,p in [(True,1),(1,1.0)]:
            with self.assertRaises(TypeError):image(f,p)
if __name__=='__main__':unittest.main()
