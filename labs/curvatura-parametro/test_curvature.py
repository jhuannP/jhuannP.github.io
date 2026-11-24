import unittest
from fractions import Fraction as Q
from itertools import product
from .curvature import curvature_squared,normal_acceleration_squared,reparameterize,parabola

class CurvatureTests(unittest.TestCase):
    def test_parabola_cartesian_oracle(self):
        for u in (Q(k,4) for k in range(-12,13)):
            point,v,a=parabola(u)
            # y=x**2/4, y'=x/2=u, y''=1/2, independent graph formula.
            self.assertEqual(curvature_squared(v,a),1/(4*(1+u*u)**3))
        self.assertEqual(curvature_squared((4,0,0),(4,8,0)),Q(1,4))
        self.assertEqual(curvature_squared((0,2,3),(-2,0,0)),Q(4,169))

    def test_all_integer_jets_gram_oracle(self):
        vectors=list(product((-1,0,1),repeat=3))
        for v in vectors:
            vv=sum(Q(x*x) for x in v)
            if not vv:continue
            for a in vectors:
                aa=sum(Q(x*x) for x in a);va=sum(Q(x*y) for x,y in zip(v,a))
                expected=(vv*aa-va*va)/vv**3
                self.assertEqual(curvature_squared(v,a),expected)
                self.assertEqual(normal_acceleration_squared(v,a)/vv**2,expected)

    def test_chain_rule_with_second_derivative(self):
        # 9 points x4 nonzero first derivatives x3 second derivatives=108 checks.
        for u,p,q in product((Q(k,2) for k in range(-4,5)),(Q(-3),Q(-1,2),Q(2),Q(5,2)),(Q(-2),Q(0),Q(3))):
            _,v,a=parabola(u)
            vn,an=reparameterize(v,a,p,q)
            self.assertEqual(curvature_squared(vn,an),curvature_squared(v,a))
        # Actual polynomial composition phi(s)=2s+s**2 at s=1/2.
        s=Q(1,2);u=2*s+s*s
        _,v,a=parabola(u)
        vn,an=reparameterize(v,a,2+2*s,2)
        self.assertEqual(vn,(4+4*s,8*s+12*s*s+4*s**3,0))
        self.assertEqual(an,(4,8+24*s+12*s*s,0))

    def test_rigid_motion_and_spatial_scale(self):
        def rotate(v):return (Q(3,5)*v[0]-Q(4,5)*v[1],Q(4,5)*v[0]+Q(3,5)*v[1],v[2])
        for u in (Q(-1),Q(0),Q(2)):
            _,v,a=parabola(u);k2=curvature_squared(v,a)
            self.assertEqual(curvature_squared(rotate(v),rotate(a)),k2)
            self.assertEqual(curvature_squared(tuple(-x for x in v),tuple(-x for x in a)),k2)
            for scale in (Q(1,3),Q(2),Q(7)):
                self.assertEqual(curvature_squared(tuple(scale*x for x in v),tuple(scale*x for x in a)),k2/scale**2)

    def test_regular_zero_curvature_vs_stationary_parameter(self):
        self.assertEqual(curvature_squared((1,0,0),(0,0,0)),0)
        self.assertEqual(curvature_squared((1,0,0),(3,0,0)),0)
        _,v,a=parabola(0)
        vn,an=reparameterize(v,a,0,0)
        with self.assertRaises(ValueError):curvature_squared(vn,an)
        for s in (Q(-1,100),Q(1,100)):
            _,v,a=parabola(s**3)
            vn,an=reparameterize(v,a,3*s*s,6*s)
            self.assertEqual(curvature_squared(vn,an),1/(4*(1+s**6)**3))

    def test_contracts(self):
        for v in (None,(1,2),(1,2,3,4),'abc',(True,0,0),(1.0,0,0)):
            with self.assertRaises(TypeError):curvature_squared(v,(0,1,0))
        for a in ((0,1.0,0),(0,'1',0)):
            with self.assertRaises(TypeError):curvature_squared((1,0,0),a)
        with self.assertRaises(ValueError):curvature_squared((0,0,0),(0,1,0))
        with self.assertRaises(TypeError):reparameterize((1,0,0),(0,1,0),True,0)

if __name__=='__main__':unittest.main()
