import math,unittest
from fractions import Fraction as F
from .experiment import acceleration,direction,response,model


class NewtonTests(unittest.TestCase):
    def test_independent_active_constraint_candidates(self):
        for m in map(F,(1,2,4)):
            for fx in map(F,(-30,0,12)):
                for fy in map(F,(-20,0,10,20,30,40,50)):
                    # Solve both candidate equations, retaining admissible N>=0 and ay>=0.
                    candidates=set()
                    contactN=10*m-fy
                    if contactN>=0:candidates.add((contactN,F(0)))
                    freeAy=fy/m-10
                    if freeAy>=0:candidates.add((F(0),freeAy))
                    self.assertEqual(len(candidates),1)
                    s=response(m,fx,fy)
                    self.assertEqual((s['normal'],s['ay']),next(iter(candidates)))
                    self.assertEqual(m*s['ax'],fx)
                    self.assertEqual(m*s['ay'],fy+s['normal']-10*m)
                    self.assertEqual(s['normal']*s['ay'],0)

    def test_work_energy_from_finite_displacement(self):
        for m,fx,fy,vx in ((F(2),F(6),F(0),F(-2)),(F(1),F(-8),F(15),F(3)),(F(2),F(0),F(20),F(0))):
            s=response(m,fx,fy,vx);t=F(1,8)
            dx=vx*t+s['ax']*t*t/2;dy=s['ay']*t*t/2
            finalK=m*((vx+s['ax']*t)**2+(s['ay']*t)**2)/2
            work=fx*dx+(fy+s['normal']-10*m)*dy
            self.assertEqual(finalK-s['kinetic'],work)
            # Exact symmetric difference gives initial instantaneous dK/dt.
            K=lambda dt:m*((vx+s['ax']*dt)**2+(s['ay']*dt)**2)/2
            self.assertEqual((K(t)-K(-t))/(2*t),s['power'])

    def test_angles_and_reference_frames(self):
        for angle in range(-180,181,15):
            c,s=direction(angle);self.assertAlmostEqual(c*c+s*s,1,places=14)
            for vx in range(-4,5):
                a=model(2,6,angle,vx);b=model(2,6,angle,0)
                self.assertEqual((a['ax'],a['ay'],a['normal']),(b['ax'],b['ay'],b['normal']))
        self.assertEqual(model(1,20,30)['state'],'limite')
        self.assertEqual(model(2,20,90)['state'],'limite')
        self.assertEqual(model(2,30,90)['state'],'separacao')
        self.assertEqual(model(2,6,180)['ax'],-3)
        self.assertEqual(acceleration((10,-4),2),3)

    def test_boundary_continuity_and_domain(self):
        for fy in (20-1e-6,20,20+1e-6):
            s=response(2,0,fy)
            self.assertLessEqual(abs(s['normal']),1.1e-6)
            self.assertLessEqual(abs(s['ay']),.6e-6)
        self.assertEqual(response(2,6,0,-2)['power'],-12)
        self.assertEqual(response(2,6,0,0)['power'],0)
        for args in ((0,6,0,0),(2,-1,0,0),(2,41,0,0),(2,6,181,0),(2,6,0,5)):
            with self.assertRaises(ValueError):model(*args)
        with self.assertRaises(ValueError):response(1,float('nan'),0)
