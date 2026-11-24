import unittest
from fractions import Fraction as Q
from .experiment import area,best_rectangle,loss

class OptimizationTests(unittest.TestCase):
    def test_complete_square_global_certificate(self):
        for P in (4,8,12,20,40):
            for i in range(21):
                x=Q(P*i,40)
                self.assertEqual(loss(P,x),(x-Q(P,4))**2)
                self.assertLessEqual(area(P,x),Q(P*P,16))
            r=best_rectangle(P)
            self.assertEqual(r['x'],Q(P,4));self.assertEqual(r['y'],r['x'])
            self.assertEqual(r['area'],Q(P*P,16))

    def test_restricted_interval_boundary_against_vertex_projection(self):
        for low in range(11):
            for high in range(low,11):
                r=best_rectangle(20,low,high)
                expected=min(max(5,low),high)
                self.assertEqual(r['x'],expected)
                for k in range(11):
                    x=Q(low)+Q(k,10)*(high-low)
                    self.assertLessEqual(area(20,x),r['area'])
        self.assertEqual(best_rectangle(20,0,3)['x'],3)
        self.assertEqual(best_rectangle(20,7,10)['x'],7)

    def test_scaling_and_nonextremum(self):
        for scale in (2,3,5):
            r=best_rectangle(20*scale)
            self.assertEqual(r['x'],5*scale)
            self.assertEqual(r['area'],25*scale**2)
        for h in (Q(1,2),Q(1,10),Q(1,100)):
            self.assertLess((-h)**3,0);self.assertGreater(h**3,0)
        self.assertEqual(area(20,0),0);self.assertEqual(area(20,10),0)

    def test_contracts(self):
        for args in ((0,0),(-1,0),(20,-1),(20,11),(20,True)):
            with self.assertRaises(ValueError):area(*args)
        for args in ((20,4,3),(20,-1,3),(20,0,11)):
            with self.assertRaises(ValueError):best_rectangle(*args)

if __name__=='__main__':unittest.main()
