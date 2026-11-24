import unittest
from math import pi,sqrt
from .charts import chart,cross,integrate

class ChartTests(unittest.TestCase):
    def test_differentials_by_finite_difference(self):
        step=1e-6
        for b in [-3,0,5]:
            for sign in [-1,1]:
                for u,v in [(.2,.3),(.6,.7)]:
                    _,du,dv=chart(u,v,twist=b,direction=sign)
                    for axis,expected in [(0,du),(1,dv)]:
                        plus=[u,v];minus=[u,v];plus[axis]+=step;minus[axis]-=step
                        pp=chart(*plus,twist=b,direction=sign)[0]
                        pm=chart(*minus,twist=b,direction=sign)[0]
                        for a,c,e in zip(pp,pm,expected):self.assertAlmostEqual((a-c)/(2*step),e,places=6)
    def test_quadrature_invariance_and_multiplicity(self):
        for r in [.5,2]:
            for h in [1,3]:
                for b in [-3,0,5]:
                    for turns in [1,2,3]:
                        for sign in [-1,1]:
                            out=integrate(r,h,b,turns,sign,n=8)
                            self.assertAlmostEqual(out['parameter_area_m2'],turns*2*pi*r*h,places=9)
                            self.assertAlmostEqual(out['induced_flux_m3_s'],sign*turns*2*pi*r*r*h,places=9)
    def test_normal_and_velocity_scaling(self):
        for u,v in [(.1,.2),(.4,.6),(.9,.8)]:
            point,du,dv=chart(u,v,twist=7)
            normal=cross(du,dv)
            self.assertAlmostEqual(normal[2],0)
            self.assertGreater(normal[0]*point[0]+normal[1]*point[1],0)
            self.assertAlmostEqual(sqrt(sum(x*x for x in normal)),12*pi)
        a=integrate(kappa=1);b=integrate(kappa=-2)
        self.assertEqual(a['parameter_area_m2'],b['parameter_area_m2'])
        self.assertAlmostEqual(b['induced_flux_m3_s'],-2*a['induced_flux_m3_s'])
    def test_contracts(self):
        for kwargs in [dict(radius=0),dict(height=-1),dict(twist=101),dict(turns=0),dict(turns=1.5),dict(turns=True),dict(direction=0),dict(direction=True),dict(radius=float('nan'))]:
            with self.assertRaises(ValueError):chart(.5,.5,**kwargs)
        for kwargs in [dict(n=0),dict(n=True),dict(n=129),dict(kappa=float('inf'))]:
            with self.assertRaises(ValueError):integrate(**kwargs)
        for uv in [(-.1,.5),(.5,1.1),(True,.5)]:
            with self.assertRaises(ValueError):chart(*uv)
if __name__=='__main__':unittest.main()
