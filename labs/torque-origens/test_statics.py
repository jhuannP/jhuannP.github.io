import unittest
from fractions import Fraction as Q
from itertools import product
from .statics import resultant,beam,cross


class StaticsTests(unittest.TestCase):
    def test_beam_reference_and_infeasible_contact(self):
        s=beam(6,12,6,5)
        self.assertEqual(s,dict(RA=Q(7),RB=Q(11),unilateral_ok=True))
        loads=[((0,0),(0,7)),((6,0),(0,11)),((3,0),(0,-12)),((5,0),(0,-6))]
        for o in [(0,0),(6,0),(-2,3)]:self.assertEqual(resultant(loads,o),dict(force=(0,0),torque=0))
        self.assertEqual(beam(6,12,6,15),dict(RA=Q(-3),RB=Q(21),unilateral_ok=False))

    def test_origin_and_line_of_action(self):
        # 81 force pairs x 9 origin displacements = 729 transformations.
        for a,b,c,d in product((-2,0,3),repeat=4):
            loads=[((2,1),(a,b)),((-1,3),(c,d))]
            base=resultant(loads)
            for ox,oy in product((-1,0,2),repeat=2):
                shifted=resultant(loads,(ox,oy))
                expected=base['torque']-ox*(b+d)+oy*(a+c)
                self.assertEqual(shifted['torque'],expected)
                self.assertEqual(shifted['force'],base['force'])
        for k in (-2,Q(1,2),3):
            r=(2,1);f=(3,-2);shift=(r[0]+k*f[0],r[1]+k*f[1])
            self.assertEqual(cross(shift,f),cross(r,f))

    def test_couple_and_non_equilibrium_counterexamples(self):
        loads=[((2,0),(0,3)),((0,0),(0,-3))]
        for origin in [(0,0),(3,2),(-5,7)]:
            self.assertEqual(resultant(loads,origin),dict(force=(0,0),torque=6))
        self.assertEqual(resultant([((0,0),(0,3))]),dict(force=(0,3),torque=0))
        self.assertEqual(resultant([((0,0),(0,3)),((2,0),(0,3))]),dict(force=(0,6),torque=6))

    def test_beam_balances_and_virtual_rotation(self):
        # 81 candidates; independent moments about B, and direct force sums.
        for L,W,P,ratio in product((2,4,6),(0,6,12),(0,3,6),(Q(1,4),Q(1,2),Q(3,2))):
            x=L*ratio;s=beam(L,W,P,x)
            self.assertEqual(s['RA']+s['RB']-W-P,0)
            self.assertEqual(-L*s['RA']+L*W/2+(L-x)*P,0)
        # delta r / delta theta = (-y,x) for infinitesimal planar rotation.
        for x,y,fx,fy in product((-2,0,3),repeat=4):
            virtual_work_per_radian=fx*(-y)+fy*x
            self.assertEqual(virtual_work_per_radian,cross((x,y),(fx,fy)))

    def test_old_material_geometry_and_contracts(self):
        x,y,Fx,Fy=2,0,0,3
        self.assertEqual(x*Fy-y*Fx,6)
        self.assertEqual(cross((2,0),(3,0)),0)
        # Norms squared: r=(2,1), F=(0,3) => tau6; b²=tau²/|F|²=4 != |r|²5.
        self.assertEqual(cross((2,1),(0,3))**2/Q(9),4)
        self.assertEqual(resultant([]),dict(force=(0,0),torque=0))
        for args in [(0,12,6,5),(6,-1,6,5),(6,12,-1,5),(6,12,6,-1)]:
            with self.assertRaises(ValueError):beam(*args)
        for v in [True,1.0,'1']:
            with self.assertRaises(TypeError):cross((v,0),(0,1))
        with self.assertRaises(ValueError):cross((1,2,3),(0,1))
