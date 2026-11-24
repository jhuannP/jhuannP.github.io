import math
import unittest
from itertools import product
from fractions import Fraction as Q
from .force import force,cross,dot
from .audit import helix,euler_orbit

class MagneticTests(unittest.TestCase):
    def test_basis_known_case_and_charge_sign(self):
        ex,ey,ez=(1,0,0),(0,1,0),(0,0,1)
        self.assertEqual(cross(ex,ey),ez)
        self.assertEqual(cross(ey,ex),(0,0,-1))
        self.assertEqual(force(2,(3,0,0),(0,0,4)),(0,-24,0))
        self.assertEqual(force(-2,(3,0,0),(0,0,4)),(0,24,0))
        self.assertEqual(force(2,(3,0,4),(0,0,4)),(0,-24,0))
        self.assertEqual(force(0,(3,0,4),(0,0,4)),(0,0,0))

    def test_orthogonality_and_electric_power_on_vector_grid(self):
        vectors=list(product((-1,0,1),repeat=3))
        e=(2,-1,3)
        for v in vectors:
            for b in vectors:
                magnetic=force(-2,v,b)
                self.assertEqual(dot(magnetic,v),0)
                self.assertEqual(dot(magnetic,b),0)
                total=force(-2,v,b,e)
                self.assertEqual(dot(total,v),-2*dot(e,v))
                self.assertEqual(cross(v,b),tuple(-x for x in cross(b,v)))

    def test_analytic_helix_satisfies_motion_and_speed(self):
        dt=1e-5
        for t in (.0,.07,.15,.3,.5,.9):
            r,v=helix(t)
            rm,vm=helix(t-dt);rp,vp=helix(t+dt)
            for i in range(3):self.assertAlmostEqual((rp[i]-rm[i])/(2*dt),v[i],delta=1e-7)
            acceleration=(8*v[1],-8*v[0],0)
            for i in range(3):self.assertAlmostEqual((vp[i]-vm[i])/(2*dt),acceleration[i],delta=1e-6)
            self.assertAlmostEqual(sum(x*x for x in v),25,places=12)
            self.assertAlmostEqual(r[0]**2+(r[1]+3/8)**2,(3/8)**2,places=12)
        r,v=helix(math.pi/4)
        self.assertAlmostEqual(r[2],math.pi)
        self.assertAlmostEqual(r[0],0,places=12)
        self.assertAlmostEqual(r[1],0,places=12)

    def test_euler_energy_growth_is_numerical(self):
        for i,(t,y) in enumerate(euler_orbit()):
            perpendicular2=y[3]**2+y[4]**2
            self.assertEqual(perpendicular2,9*2**i)
            self.assertEqual(y[5],4)
            self.assertEqual(sum(x*x for x in y[3:]),9*2**i+16)
        self.assertGreater(sum(x*x for x in euler_orbit()[-1][1][3:]),25)

    def test_exact_contracts(self):
        for q in (True,2.,float('nan'),None):
            with self.assertRaises(TypeError):force(q,(1,0,0),(0,0,1))
        for v in ((1,2),(),(1,2,3,4),'123'):
            with self.assertRaises(ValueError):force(1,v,(0,0,1))
        with self.assertRaises(TypeError):force(1,(1.,0,0),(0,0,1))
        self.assertEqual(force(Q(1,2),(Q(3,2),0,0),(0,0,2)),(0,Q(-3,2),0))

if __name__ == "__main__":unittest.main()
