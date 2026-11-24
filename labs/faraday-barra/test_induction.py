import unittest,itertools,math
from .induction import rod,circular_e

class InductionTests(unittest.TestCase):
    def test_reference_signs_and_power(self):
        r=rod(.5,.2,3,2)
        for key,v in [('emf',-.3),('current',-.15),('magnetic_force_x',-.015),('external_force_x',.015),('joule_power',.045),('external_power',.045)]:self.assertAlmostEqual(r[key],v)
        self.assertAlmostEqual(circular_e(.05,.1,.2)['e_phi'],-.005)
        self.assertAlmostEqual(circular_e(.1,.1,.2)['e_phi'],-.01)
        self.assertAlmostEqual(circular_e(.2,.1,.2)['e_phi'],-.005)
    def test_lorentz_geometry_and_energy_grid(self):
        count=0
        for b,length,v,resistance in itertools.product([-.5,0,.5],[.1,.4],[-3,0,2],[1,4]):
            r=rod(b,length,v,resistance)
            # u=(v,0,0), B=(0,0,b): u cross B points -y; positive path up rod.
            magnetic_emf=-v*b*length
            self.assertAlmostEqual(r['emf'],magnetic_emf)
            self.assertLessEqual(r['magnetic_force_x']*v,0)
            self.assertAlmostEqual(r['external_power'],r['joule_power'])
            self.assertAlmostEqual(r['magnetic_force_x']*v,-r['joule_power']);count+=1
        self.assertEqual(count,36)
        r=rod(.5,.2,3,2);r2=rod(-.5,.2,3,2)
        self.assertAlmostEqual(r['current'],-r2['current'])
        self.assertAlmostEqual(r['magnetic_force_x'],r2['magnetic_force_x'])
    def test_circular_circulation_by_vector_quadrature(self):
        for radius,rate in itertools.product([.02,.05,.1,.2,.4],[-.2,0,.3]):
            r=circular_e(radius,.1,rate);h=2*math.pi/128;total=0
            # Cartesian E=(-Ephi sin,Ephi cos), dr=(-r sin,r cos) dtheta.
            for i in range(128):
                t=(i+.5)*h;e=r['e_phi']
                ex,ey=-e*math.sin(t),e*math.cos(t)
                dx,dy=-radius*math.sin(t),radius*math.cos(t)
                total+=(ex*dx+ey*dy)*h
            self.assertAlmostEqual(total,-math.pi*min(radius,.1)**2*rate,places=14)
            self.assertAlmostEqual(total,r['emf'],places=14)
    def test_radial_curl_continuity_and_flux_derivative(self):
        a=.1;rate=.2;h=1e-7
        for radius in [.03,.07,.2,.4]:
            # curl_z=(1/r) d(r Ephi)/dr. Boundary r=a excluded.
            derivative=((radius+h)*circular_e(radius+h,a,rate)['e_phi']-(radius-h)*circular_e(radius-h,a,rate)['e_phi'])/(2*h*radius)
            self.assertAlmostEqual(derivative,-rate if radius<a else 0,delta=1e-9)
        left=circular_e(a-1e-9,a,rate)['e_phi'];right=circular_e(a+1e-9,a,rate)['e_phi']
        self.assertAlmostEqual(left,right,delta=3e-10)
        # Independent difference in B for flux, fixed radius.
        for radius in [.05,.2]:
            b0=.3;dt=1e-4;area=math.pi*min(radius,a)**2
            change=(area*(b0+rate*dt)-area*b0)/dt
            self.assertAlmostEqual(change,circular_e(radius,a,rate)['flux_rate'],places=12)
    def test_zeros_and_contracts(self):
        self.assertEqual(circular_e(0,.1,.2)['e_phi'],0)
        self.assertEqual(rod(0,.2,3,2)['joule_power'],0)
        for args in [(.5,0,1,1),(.5,1,1,0),(True,1,1,1),(.5,1,float('inf'),1)]:
            with self.assertRaises(ValueError):rod(*args)
        for args in [(-1,1,1),(1,0,1),(1,1,float('nan'))]:
            with self.assertRaises(ValueError):circular_e(*args)
