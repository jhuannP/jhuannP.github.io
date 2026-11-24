import unittest
from fractions import Fraction as Q
from itertools import product
from .impact import impact


def models():
    for masses,n,normal,tangent,e in product([(1,1),(2,3)],[(1,0),(Q(3,5),Q(4,5)),(Q(-5,13),Q(12,13))],
            [(3,-1),(0,2),(1,1),(2,0)],[(0,0),(1,-2)],[0,Q(1,2),1]):
        t=(-n[1],n[0]);a,b=normal;c,d=tangent
        u1=tuple(a*n[i]+c*t[i] for i in range(2));u2=tuple(b*n[i]+d*t[i] for i in range(2))
        yield masses,n,normal,tangent,e,u1,u2


class ObliqueImpact(unittest.TestCase):
    def test_original_numbers(self):
        a=impact(2,3,(3,1),(-1,0),(Q(3,5),Q(4,5)),Q(1,2))
        fixture=dict(v1=(Q(159,125),Q(-163,125)),v2=(Q(19,125),Q(192,125)),
                     impulse=Q(144,25),closing=Q(16,5),relative_normal_after=Q(-8,5),
                     P_before=(3,2),P_after=(3,2),K_before=Q(23,2),K_after=Q(1723,250),loss=Q(576,125))
        for k,v in fixture.items():self.assertEqual(a[k],v,k)

    def test_independent_normal_cm_oracle(self):
        for (m1,m2),n,(a,b),(c,d),e,u1,u2 in models():
            x=impact(m1,m2,u1,u2,n,e)
            if a>b:
                cm=Q(m1*a+m2*b,m1+m2);rel=-e*(a-b)
                an=cm+Q(m2,m1+m2)*rel;bn=cm-Q(m1,m1+m2)*rel
            else:an,bn=a,b
            t=(-n[1],n[0])
            expected1=tuple(an*n[i]+c*t[i] for i in range(2))
            expected2=tuple(bn*n[i]+d*t[i] for i in range(2))
            self.assertEqual((x['v1'],x['v2']),(expected1,expected2))
            self.assertEqual(x['tangent_after'],(c,d))

    def test_momentum_energy_and_impulse_work(self):
        for (m1,m2),n,(a,b),t,e,u1,u2 in models():
            x=impact(m1,m2,u1,u2,n,e);mu=Q(m1*m2,m1+m2)
            self.assertEqual(x['P_after'],x['P_before'])
            self.assertEqual(x['loss'],mu*(1-e*e)*max(a-b,0)**2/2)
            self.assertGreaterEqual(x['loss'],0)
            J=x['impulse']
            self.assertEqual(x['K_after']-x['K_before'],-J*(a-b)+J*J/(2*mu))

    def test_rotations_boosts_and_swapping_labels(self):
        n=(Q(3,5),Q(4,5));u1=(3,1);u2=(-1,0);e=Q(1,2)
        base=impact(2,3,u1,u2,n,e)
        transforms=[lambda v:v,lambda v:(-v[1],v[0]),
                    lambda v:(Q(3,5)*v[0]-Q(4,5)*v[1],Q(4,5)*v[0]+Q(3,5)*v[1]),
                    lambda v:(-v[0],v[1])]
        for R in transforms:
            for boost in [(0,0),(2,-3),(Q(1,2),Q(-1,3))]:
                move=lambda v:tuple(R(v)[i]+boost[i] for i in range(2))
                x=impact(2,3,move(u1),move(u2),R(n),e)
                self.assertEqual((x['v1'],x['v2']),(move(base['v1']),move(base['v2'])))
                self.assertEqual((x['impulse'],x['loss']),(base['impulse'],base['loss']))
                self.assertEqual(x['K_before']-x['K_after'],base['loss'])
        switched=impact(3,2,u2,u1,tuple(-a for a in n),e)
        self.assertEqual((switched['v1'],switched['v2']),(base['v2'],base['v1']))

    def test_limits_and_no_attractive_impulse(self):
        stuck=impact(1,1,(4,0),(0,0),(1,0),0)
        self.assertEqual((stuck['v1'],stuck['v2'],stuck['loss']),((2,0),(2,0),4))
        elastic=impact(1,1,(4,0),(0,0),(1,0),1)
        self.assertEqual((elastic['v1'],elastic['v2'],elastic['loss']),((0,0),(4,0),0))
        oblique=impact(2,3,(3,1),(-1,0),(Q(3,5),Q(4,5)),0)
        self.assertEqual(oblique['relative_normal_after'],0)
        self.assertNotEqual(oblique['v1'],oblique['v2'])
        self.assertEqual(oblique['tangent_after'],oblique['tangent_before'])
        for u1,u2 in [((0,0),(1,0)),((0,2),(0,-3))]:
            x=impact(1,2,u1,u2,(1,0),Q(1,2))
            self.assertEqual((x['v1'],x['v2'],x['impulse'],x['loss']),(u1,u2,0,0))

    def test_contracts(self):
        good=[2,3,(3,1),(-1,0),(Q(3,5),Q(4,5)),Q(1,2)]
        for i in [0,1,5]:
            args=good.copy();args[i]=True
            with self.assertRaises(ValueError):impact(*args)
        for i in [0,1]:
            for bad in [0,-1,1.0]:
                args=good.copy();args[i]=bad
                with self.assertRaises(ValueError):impact(*args)
        for i in [2,3,4]:
            for bad in [(1,),(1,2,3),(True,0),(1.0,0),'xy']:
                args=good.copy();args[i]=bad
                with self.assertRaises(ValueError):impact(*args)
        for n in [(0,0),(1,1),(Q(3,5),Q(3,5))]:
            args=good.copy();args[4]=n
            with self.assertRaises(ValueError):impact(*args)
        for e in [-1,2]:
            args=good.copy();args[5]=e
            with self.assertRaises(ValueError):impact(*args)
