import unittest,math
from .experiment import model

class ButaneNewmanTests(unittest.TestCase):
    def test_3d_geometry_and_projected_overlap(self):
        for phi in range(0,361,60):
            m=model(phi)
            for name in ('front','back'):
                vec=m[name]
                for u in vec:self.assertAlmostEqual(sum(x*x for x in u),1)
                for i in range(3):
                    for j in range(i):self.assertAlmostEqual(sum(a*b for a,b in zip(vec[i],vec[j])),-1/3)
            counts={'HH':0,'MH':0,'MM':0}
            for i,u in enumerate(m['front']):
                for j,v in enumerate(m['back']):
                    if math.hypot(u[0]-v[0],u[1]-v[1])<1e-12:
                        counts['MM' if i==j==0 else ('HH' if i and j else 'MH')]+=1
            self.assertEqual(counts,m['eclipsed'])
    def test_six_distinct_orientations_and_equivalence(self):
        self.assertEqual([model(p)['kind'] for p in range(0,360,60)],['eclipsada','gauche','eclipsada','anti','eclipsada','gauche'])
        for p in (0,360):self.assertEqual(model(p)['eclipsed'],{'HH':2,'MH':0,'MM':1})
        for p in (120,240):self.assertEqual(model(p)['eclipsed'],{'HH':1,'MH':2,'MM':0})
        self.assertNotEqual(model(0)['eclipsed'],model(120)['eclipsed'])
        self.assertEqual(model(60)['methyl_separation'],model(300)['methyl_separation'])
    def test_methyl_angle_independent_dot_product(self):
        for p in range(0,361,60):
            m=model(p);u=m['front'][0];v=m['back'][0]
            cosine=(u[0]*v[0]+u[1]*v[1])/(8/9)
            self.assertAlmostEqual(math.degrees(math.acos(max(-1,min(1,cosine)))),m['methyl_separation'],places=6)
    def test_contract(self):
        for p in (-60,30,420,True,180.0,'180',None):
            with self.assertRaises(ValueError):model(p)
