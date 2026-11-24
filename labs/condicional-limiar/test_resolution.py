import unittest
from fractions import Fraction as Q
from .resolution import intervals,risk,message

class ResolutionTests(unittest.TestCase):
    def test_boundaries_and_messages(self):
        self.assertEqual(intervals(Q(1,2),2),[(Q(0),Q(3,4)),(Q(3,4),Q(1))])
        for x,k in [(Q(0),0),(Q(1,2),0),(Q(3,4),1),(Q(1),1)]:
            self.assertEqual(message(x,Q(1,2),2),k)
    def test_risk_by_independent_quadrature(self):
        # Simpson integrates each quadratic error exactly; separate from cubic risk formula.
        for a in (Q(1,4),Q(1,2),Q(2,3)):
            for m in (1,2,3,4,8):
                cells=intervals(a,m);total=Q(0);mean=Q(0)
                for lo,hi in cells:
                    c=(lo+hi)/2
                    total+=(hi-lo)*((lo-c)**2+4*((lo+hi)/2-c)**2+(hi-c)**2)/6
                    mean+=(hi-lo)*c
                self.assertEqual(total,risk(a,m))
                self.assertEqual(mean,Q(1,2))
                # Nested refinement improves the average; threshold information stays lost.
                self.assertLessEqual(risk(a,2*m),total)
                self.assertGreater(total,a**3/12)
        self.assertEqual(risk(Q(1,2),2),Q(7,192))
        self.assertEqual(risk(Q(1,2),4),Q(1,48))
    def test_contracts(self):
        for a,m in [(0,2),(1,2),(0.5,2),(True,2),(Q(1,2),0),(Q(1,2),True)]:
            with self.assertRaises(ValueError): intervals(a,m)
        with self.assertRaises(ValueError): message(Q(2),Q(1,2),2)
