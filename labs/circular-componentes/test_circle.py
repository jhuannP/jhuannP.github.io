import unittest,math
from .circle import state,friction

class CircularTests(unittest.TestCase):
    def test_uniform_reference_and_orientation(self):
        s=state(2,2,0)
        self.assertEqual(s['position'],(2,0));self.assertEqual(s['velocity'],(0,4))
        self.assertEqual(s['acceleration'],(-8,0))
        reverse=state(2,-2,0)
        self.assertEqual(reverse['velocity'],(0,-4))
        self.assertEqual(reverse['acceleration'],(-8,0))
        for t in [0,.1,.5,1,2]:
            s=state(2,2,t)
            self.assertAlmostEqual(math.hypot(*s['position']),2,places=13)
            self.assertAlmostEqual(math.hypot(*s['velocity']),4,places=13)
            self.assertAlmostEqual(sum(a*b for a,b in zip(s['velocity'],s['acceleration'])),0,places=12)

    def test_derivatives_against_finite_differences(self):
        h=1e-4
        count=0
        for r in [1,2]:
            for w in [-2,0,1]:
                for alpha in [-.5,0,1]:
                    for t in [-.2,0,.4]:
                        s=state(r,w,t,alpha,.3)
                        before=state(r,w,t-h,alpha,.3);after=state(r,w,t+h,alpha,.3)
                        for j in range(2):
                            v=(after['position'][j]-before['position'][j])/(2*h)
                            a=(after['position'][j]-2*s['position'][j]+before['position'][j])/(h*h)
                            self.assertAlmostEqual(v,s['velocity'][j],delta=2e-7)
                            self.assertAlmostEqual(a,s['acceleration'][j],delta=2e-6)
                        expected=s['radial']**2+s['tangent']**2
                        self.assertAlmostEqual(sum(a*a for a in s['acceleration']),expected,places=11)
                        count+=1
        self.assertEqual(count,54)

    def test_nonuniform_components_and_power(self):
        s=state(2,1,0,.5)
        self.assertEqual(s['acceleration'],(-2,1))
        self.assertEqual(s['velocity'],(0,2))
        mass=3
        power=mass*sum(a*v for a,v in zip(s['acceleration'],s['velocity']))
        self.assertEqual(power,6)
        # dK/dt=m R² omega alpha, mesma grandeza por rota angular.
        self.assertEqual(power,mass*2**2*1*.5)
        # Num instante de omega=0 ainda pode existir aceleração tangencial.
        stopped=state(2,0,0,1)
        self.assertEqual(stopped['speed'],0)
        self.assertEqual(stopped['acceleration'],(0,2))

    def test_horizontal_friction_and_mass_scaling(self):
        low=friction(.5,2,2,0,.5);high=friction(.5,2,4,0,.5)
        self.assertEqual(low['required'],1);self.assertEqual(low['limit'],2.5)
        self.assertTrue(low['feasible']);self.assertFalse(high['feasible'])
        self.assertEqual(high['required'],4)
        self.assertTrue(friction(1,2,2,3,.5)['feasible'])
        self.assertFalse(friction(1,2,3,3,.5)['feasible'])
        for scale in [1,2,10]:
            r=friction(scale,2,2,3,.5)
            self.assertAlmostEqual(r['required']/scale,math.sqrt(13),places=13)
            self.assertTrue(r['feasible'])
        self.assertTrue(friction(1,2,2,0,.2)['feasible']) # igualdade 2N

    def test_contracts(self):
        for args in [(0,1,0),(-1,1,0),(1,math.inf,0),(1,1,math.nan),(1,True,0),(1,1e308,1e308)]:
            with self.assertRaises(ValueError):state(*args)
        for args in [(0,1,1,0,1),(1,0,1,0,1),(1,1,-1,0,1),(1,1,1,0,-1)]:
            with self.assertRaises(ValueError):friction(*args)

if __name__=='__main__':unittest.main()
