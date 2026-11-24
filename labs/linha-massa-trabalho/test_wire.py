import unittest
from math import pi
from .wire import integrate_wire,simpson

class WireTests(unittest.TestCase):
    def test_analytic_moments(self):
        for R in (.5,2,5):
            for lam in (1,3):
                for mode in ('forward','reverse','nonlinear'):
                    z=integrate_wire(R,lam,mode=mode,n=1024)
                    self.assertAlmostEqual(z.length/(R*pi),1,places=10)
                    self.assertAlmostEqual(z.mass/(1.5*pi*R*lam),1,places=9)
                    self.assertAlmostEqual(z.x_center/R,0,places=9)
                    self.assertAlmostEqual(z.y_center/R,16/(9*pi),places=9)

    def test_orientation_and_retracing(self):
        f=integrate_wire();r=integrate_wire(mode='reverse');q=integrate_wire(mode='out-and-back')
        self.assertAlmostEqual(f.mass,r.mass,places=10)
        self.assertAlmostEqual(f.work,4*pi,places=10)
        self.assertAlmostEqual(r.work,-4*pi,places=10)
        self.assertAlmostEqual(q.mass,2*f.mass,places=10)
        self.assertAlmostEqual(q.length,2*f.length,places=10)
        self.assertAlmostEqual(q.work,0,places=10)
        self.assertAlmostEqual(q.y_center,f.y_center,places=10)

    def test_units_scaling_and_independent_fields(self):
        base=integrate_wire();z=integrate_wire(4,6,-2)
        self.assertAlmostEqual(z.mass/base.mass,4,places=10)
        self.assertAlmostEqual(z.length/base.length,2,places=10)
        self.assertAlmostEqual(z.y_center/base.y_center,2,places=10)
        self.assertAlmostEqual(z.work/base.work,-8,places=10)
        self.assertEqual(integrate_wire(field_scale=0).work,0)

    def test_quadrature_and_refinement(self):
        # Polinômios: regra exata até grau3, ponto de verificação independente.
        for degree in range(4):
            self.assertAlmostEqual(simpson(lambda t:t**degree,0,1,8),1/(degree+1),places=14)
        errors=[]
        for n in (16,32,64):
            z=integrate_wire(mode='nonlinear',n=n)
            errors.append(abs(z.mass-9*pi))
        self.assertLess(errors[1],errors[0]/10)
        self.assertLess(errors[2],errors[1]/10)
        self.assertLess(errors[-1],1e-4)

    def test_contracts(self):
        for bad in (True,'2',None):
            with self.assertRaises(TypeError):integrate_wire(radius=bad)
        for bad in (0,-1,float('inf'),float('nan')):
            with self.assertRaises(ValueError):integrate_wire(radius=bad)
        for n in (0,1,3,100002):
            with self.assertRaises(ValueError):integrate_wire(n=n)
        with self.assertRaises(TypeError):integrate_wire(n=True)
        with self.assertRaises(ValueError):integrate_wire(mode='unknown')
        with self.assertRaises(ValueError):integrate_wire(density=0)

if __name__=='__main__':unittest.main()
