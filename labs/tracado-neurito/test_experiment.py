import unittest,math
from .experiment import measure,model

class TraceGeometryTests(unittest.TestCase):
    def test_pythagorean_and_coarse_sampling(self):
        m=model(160,.1,0)
        self.assertEqual(m['length'],40)
        self.assertEqual(m['distance'],24)
        self.assertAlmostEqual(m['ratio'],5/3)
        self.assertEqual(model(160,.1,1)['length'],24)
        self.assertIsNone(measure([(0,0),(1,0),(0,0)],1)['ratio'])
    def test_invariance_and_unit_scaling(self):
        points=[(0,0),(3,4),(6,0)]
        a=measure(points,2)
        for transformed in [[(x+9,y-2) for x,y in points],[(-y,x) for x,y in points],list(reversed(points))]:
            b=measure(transformed,2)
            for key in a:self.assertAlmostEqual(a[key],b[key])
        self.assertEqual(measure(points,4)['length'],2*a['length'])
        self.assertEqual(measure(points,4)['ratio'],a['ratio'])
    def test_refinement_and_projection_lower_bounds(self):
        for h in range(161):
            m=model(h,.1)
            self.assertGreaterEqual(m['length']+1e-12,m['distance'])
            self.assertGreaterEqual(m['full_length']+1e-12,model(h,.1,1)['length'])
            # Pontos3Dcom altura z crescente: projeção2D não aumenta o comprimento.
            actual=2*math.sqrt(120**2+h*h+50**2)*.1
            self.assertLessEqual(m['length'],actual+1e-12)
        self.assertEqual(measure([(0,0),(3,4),(6,8)],1)['length'],10)
    def test_domain_and_zero_segments(self):
        self.assertEqual(measure([(0,0),(0,0),(3,4)],1)['length'],5)
        for points,scale in [([],1),([(0,0)],1),([(0,0),(1,1)],0),([(0,0),(float('inf'),1)],1),([(0,0),(1,1)],True),([(False,0),(1,1)],1)]:
            with self.assertRaises(ValueError):measure(points,scale)
        for args in [(-1,.1,0),(161,.1,0),(0,0,0),(0,.1,2),(0,.1,True)]:
            with self.assertRaises(ValueError):model(*args)
