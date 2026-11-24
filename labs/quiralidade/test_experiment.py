import itertools,math,unittest
from fractions import Fraction as F
from .experiment import BASE,determinant,oriented,matching_rotations,model


class ChiralityTests(unittest.TestCase):
    def test_all_permutations_and_independent_volume(self):
        a,b,c,d=BASE
        x=tuple(a[i]-d[i] for i in range(3));y=tuple(b[i]-d[i] for i in range(3));z=tuple(c[i]-d[i] for i in range(3))
        cross=(y[1]*z[2]-y[2]*z[1],y[2]*z[0]-y[0]*z[2],y[0]*z[1]-y[1]*z[0])
        self.assertEqual(sum(v*w for v,w in zip(x,cross)),16)
        for p in itertools.permutations(range(4)):
            inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
            points=[BASE[i] for i in p]
            self.assertEqual(oriented(points),16*(-1)**inv)
            translated=[tuple(v+t for v,t in zip(row,(7,-3,2))) for row in points]
            self.assertEqual(oriented(translated),oriented(points))
            self.assertEqual(bool(matching_rotations(points,('A','B','C','D'))),inv%2==0)
            self.assertTrue(matching_rotations(points,('A','A','C','D')))

    def test_matching_matrix_is_proper_and_reproduces_all_points(self):
        for kind in (0,1):
            for mirror in (0,1):
                for swap in (0,1):
                    for angle in range(0,361,30):
                        s=model(kind,mirror,swap,angle)
                        self.assertEqual(s['superposable'],kind==1 or mirror==swap)
                        self.assertAlmostEqual(s['orientation'],16*(-1)**(mirror+swap),places=12)
                        if s['match']:
                            Q=s['match']['matrix'];p=s['match']['assignment']
                            self.assertAlmostEqual(determinant(Q),1,places=13)
                            for i in range(3):
                                for j in range(3):self.assertAlmostEqual(sum(Q[k][i]*Q[k][j] for k in range(3)),float(i==j),places=13)
                            for t in range(4):
                                self.assertEqual(s['labels'][t],s['labels'][p[t]])
                                for i in range(3):self.assertAlmostEqual(sum(Q[i][j]*BASE[t][j] for j in range(3)),s['points'][p[t]][i],places=13)

    def test_arbitrary_proper_quaternion_rotation(self):
        # Integer quaternion (1,2,3,4), normalized through its squared norm 30.
        w,x,y,z=map(F,(1,2,3,4));n=w*w+x*x+y*y+z*z
        Q=(((w*w+x*x-y*y-z*z)/n,2*(x*y-w*z)/n,2*(x*z+w*y)/n),
           (2*(x*y+w*z)/n,(w*w-x*x+y*y-z*z)/n,2*(y*z-w*x)/n),
           (2*(x*z-w*y)/n,2*(y*z+w*x)/n,(w*w-x*x-y*y+z*z)/n))
        self.assertEqual(determinant(Q),1)
        points=[tuple(sum(Q[i][j]*r[j] for j in range(3)) for i in range(3)) for r in BASE]
        self.assertEqual(oriented(points),16)
        matches=matching_rotations(points,('A','B','C','D'))
        self.assertEqual(len(matches),1)
        self.assertEqual(matches[0]['matrix'],[list(row) for row in Q])

    def test_distances_duplicate_groups_and_contract(self):
        for angle in (0,30,120,270,360):
            points=model(angle=angle)['points']
            for i in range(4):
                for j in range(i):self.assertAlmostEqual(sum((a-b)**2 for a,b in zip(points[i],points[j])),8,places=13)
        self.assertEqual(model(kind=1)['orientation'],-16)
        self.assertTrue(model(kind=1)['superposable'])
        H=((1,0,0),(0,0,-1),(0,-1,0)) # Mirror plane y+z=0.
        self.assertEqual(determinant(H),-1)
        reflected=[tuple(sum(H[i][j]*r[j] for j in range(3)) for i in range(3)) for r in BASE]
        self.assertEqual(reflected,[BASE[1],BASE[0],BASE[2],BASE[3]])
        for args in ((2,0,0,0),(0,2,0,0),(0,0,2,0),(0,0,0,361)):
            with self.assertRaises(ValueError):model(*args)
