import importlib.util
import math
import unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('gauss',Path(__file__).with_name('experiment.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class GaussTests(unittest.TestCase):
    def test_volume_and_area_scaling(self):
        # Integração radial da densidade, independente do cálculo Q*r³.
        for q in [-2,0,1,2]:
            density=3*q/(4*math.pi)
            for r in [0,.25,.5,1,2,3]:
                s=m.sphere(0,q,r)
                b=min(r,1); n=100; h=b/n
                enclosed=h/3*sum((1 if j in [0,n] else 4 if j%2 else 2)*4*math.pi*density*(j*h)**2 for j in range(n+1))
                self.assertAlmostEqual(s['inside'],enclosed)
                self.assertAlmostEqual(4*math.pi*r*r*s['field'],s['flux'])
        self.assertAlmostEqual(m.sphere(0,1,.5)['inside'],1/8)
        self.assertAlmostEqual(m.sphere(0,1,2)['field']/m.sphere(0,1,1)['field'],1/4)

    def test_coulomb_shell_angular_quadrature(self):
        for q in [-2,1,2]:
            for r in [0,.25,.5,1.5,2,3]:
                self.assertAlmostEqual(m.shell_coulomb(r,q),m.sphere(1,q,r)['field'],delta=2e-10)

    def test_limits_jump_and_same_exterior(self):
        for q in [-2,0,1,2]:
            a=m.sphere(1,q,1)
            if q:
                self.assertTrue(a['boundary']); self.assertIsNone(a['field']);self.assertIsNone(a['flux'])
            else:
                self.assertFalse(a['boundary']);self.assertEqual(a['field'],0)
            surface_density=q/(4*math.pi)
            self.assertAlmostEqual(a['outer_limit']-a['inner_limit'],surface_density)
            self.assertEqual(m.sphere(0,q,1)['inner_limit'],m.sphere(0,q,1)['outer_limit'])
            for r in [1.1,2,3]: self.assertEqual(m.sphere(0,q,r)['field'],m.sphere(1,q,r)['field'])
            self.assertEqual(m.sphere(0,q,0)['field'],0)
            self.assertEqual(m.sphere(1,q,.5)['field'],0)

    def test_zero_flux_nonzero_field_and_domain(self):
        # Campo uniforme E=(0,0,2), cubo de lado 3: duas faces ±18, outras zero.
        flux_faces=[0,0,0,0,18,-18]
        self.assertEqual(sum(flux_faces),0)
        self.assertGreater(max(map(abs,flux_faces)),0)
        for args in [(2,1,1),(0,float('nan'),1),(0,1,-1)]:
            with self.assertRaises(ValueError):m.sphere(*args)
        with self.assertRaises(ValueError):m.shell_coulomb(1)

if __name__=='__main__':unittest.main()
