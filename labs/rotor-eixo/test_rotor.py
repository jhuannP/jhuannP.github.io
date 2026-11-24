import unittest,json
from pathlib import Path
from fractions import Fraction as Q
from .rotor import inertia,driven,rearranged

class RotorTests(unittest.TestCase):
    def test_reference_three_balances(self):
        I=inertia(((1,2,0),(1,-2,0)));self.assertEqual(I,8)
        r=driven(I,1,4,2)
        self.assertEqual((r['alpha'],r['w'],r['theta']),(Q(1,2),2,3))
        self.assertEqual((r['L0'],r['L'],r['impulse']),(8,16,8))
        self.assertEqual((r['K0'],r['K'],r['work']),(4,16,12))
        self.assertEqual((r['power0'],r['power']),(4,8))

    def test_particle_energy_and_torque_work_independent(self):
        particles=((2,1,0),(3,0,2),(1,-1,1));I=inertia(particles)
        for w0 in (-2,0,1):
            for tau in (-3,0,4):
                for t in (0,Q(1,3),2):
                    r=driven(I,w0,tau,t)
                    # Particle velocities(vx,vy)=(-w*y,w*x),independent kinetic sum.
                    kinetic=sum(Q(m,2)*((-r['w']*y)**2+(r['w']*x)**2) for m,x,y in particles)
                    self.assertEqual(kinetic,r['K'])
                    self.assertEqual(r['L']-r['L0'],r['impulse'])
                    self.assertEqual(r['K']-r['K0'],r['work'])
                    # Integral of linearly varying power is trapezoidal exactly.
                    self.assertEqual((r['power0']+r['power'])*t/2,r['work'])

    def test_axis_and_geometry_scalings(self):
        self.assertEqual(inertia(((1,3,0),(1,-1,0))),10)
        for k in (Q(1,2),2,3):
            self.assertEqual(inertia(((1,2*k,0),(1,-2*k,0))),8*k*k)
            self.assertEqual(inertia(((k,2,0),(k,-2,0))),8*k)

    def test_rearrangement_and_previous_material(self):
        for I1 in (1,4,8):
            for I2 in (2,4,10):
                for w in (-2,0,1):
                    r=rearranged(I1,I2,w)
                    self.assertEqual(I2*r['w2'],I1*w)
                    self.assertEqual(r['K2'],r['L']**2/(2*I2))
        r=rearranged(8,4,1);self.assertEqual((r['w2'],r['K1'],r['K2'],r['deltaK']),(2,4,8,4))
        root=Path(__file__).resolve().parents[2]
        l=next(l for l in json.loads((root/'content/lessons.json').read_text()) if l['id']=='f1-rotacao')
        exec(l['python'],{});exec(l['codingPractice']['solution'],{})

    def test_contracts(self):
        for data in ((),((0,1,0),),((1,0,0),),((True,1,0),),((1.,1,0),),((1,2),)):
            with self.assertRaises(ValueError):inertia(data)
        for args in ((0,1,1,1),(1,1,1,-1),(True,1,1,1),(1,1.,1,1)):
            with self.assertRaises(ValueError):driven(*args)
        with self.assertRaises(ValueError):rearranged(1,0,1)
