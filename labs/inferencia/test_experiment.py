import unittest
from fractions import Fraction as Q
from statistics import NormalDist
from .experiment import normal_pvalue, joint_moments

class InferenceMomentTests(unittest.TestCase):
    def test_normal_tails_symmetry_and_reference(self):
        d=NormalDist()
        for z in (-4,-3,-2,-1,0,1,2,3,4):
            self.assertAlmostEqual(normal_pvalue(z,'left'),d.cdf(z))
            self.assertAlmostEqual(normal_pvalue(z,'right'),1-d.cdf(z))
            self.assertAlmostEqual(normal_pvalue(z,'left')+normal_pvalue(z,'right'),1)
            self.assertEqual(normal_pvalue(-z),normal_pvalue(z))
            self.assertAlmostEqual(normal_pvalue(z),2*min(normal_pvalue(z,'left'),normal_pvalue(z,'right')))
        self.assertGreater(normal_pvalue(8),0)
        self.assertAlmostEqual(normal_pvalue(8)/1.2441921148543568e-15,1)

    def test_moments_covariance_identity_and_affine_scaling(self):
        xs=[-2,-1,0,1,2]; weights=[Q(1,5)]*5
        for a in (Q(-2),Q(0),Q(1,2),Q(2)):
            for b in (Q(0),Q(1),Q(2)):
                ys=[a*x+b*x*x for x in xs];r=joint_moments(xs,ys,weights)
                self.assertEqual(r['covariance'],2*a)
                self.assertEqual(r['variance_y'],2*a*a+Q(14,5)*b*b)
                exy=sum(x*y*w for x,y,w in zip(xs,ys,weights))
                self.assertEqual(r['covariance'],exy-r['mean_x']*r['mean_y'])
                changed=joint_moments([3*x+4 for x in xs],[-2*y+10 for y in ys],weights)
                self.assertEqual(changed['covariance'],-6*r['covariance'])
                if r['correlation'] is not None:
                    self.assertAlmostEqual(changed['correlation'],-r['correlation'])
                    self.assertLessEqual(abs(r['correlation']),1+1e-12)

    def test_zero_correlation_dependence_and_constant(self):
        xs=[-2,-1,0,1,2];ys=[x*x for x in xs];weights=[Q(1,5)]*5
        r=joint_moments(xs,ys,weights);self.assertEqual(r['correlation'],0)
        joint=sum(w for x,y,w in zip(xs,ys,weights) if x==0 and y==0)
        px=sum(w for x,w in zip(xs,weights) if x==0);py=sum(w for y,w in zip(ys,weights) if y==0)
        self.assertEqual(joint,Q(1,5));self.assertNotEqual(joint,px*py)
        self.assertIsNone(joint_moments(xs,[3]*5,weights)['correlation'])
        self.assertAlmostEqual(joint_moments(xs,[-2*x+3 for x in xs],weights)['correlation'],-1)

    def test_contracts(self):
        for bad in (True,'2',float('inf'),float('nan')):
            with self.assertRaises(ValueError):normal_pvalue(bad)
        with self.assertRaises(ValueError):normal_pvalue(0,'post-hoc')
        for xs,ys,weights in [([],[],[]),([1],[2],[Q(1,2)]),([1,2],[2],[1]),([True],[1],[1]),([1],[.5],[1]),([1,2],[3,4],[-1,2])]:
            with self.assertRaises(ValueError):joint_moments(xs,ys,weights)

if __name__=='__main__':unittest.main()
