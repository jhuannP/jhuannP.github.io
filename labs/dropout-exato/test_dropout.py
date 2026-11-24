import unittest,itertools
from fractions import Fraction as Q
from .dropout import apply,states,scalar_moments

class ExactDropoutTests(unittest.TestCase):
    def test_reference_states_and_original_scalar(self):
        rows=states([2,-1],Q(1,2))
        self.assertEqual([r[0] for r in rows],[Q(1,4)]*4)
        self.assertEqual([r[2] for r in rows],[(0,0),(0,-2),(4,0),(4,-2)])
        self.assertEqual(scalar_moments([2,-1],Q(1,2),sum),(1,5))
        self.assertEqual(scalar_moments([2,-1],Q(1,2),lambda v:max(0,sum(v)))[0],Q(3,2))
        self.assertEqual(scalar_moments([3],Q(1,2),sum),(3,9))
    def test_means_variances_covariances_exact_grid(self):
        count=0
        for xs in itertools.product([-2,0,3],repeat=3):
            for p in [Q(0),Q(1,4),Q(1,2),Q(3,4)]:
                rows=states(xs,p);self.assertEqual(sum(r[0] for r in rows),1)
                for i,x in enumerate(xs):
                    mean,var=scalar_moments(xs,p,lambda v:v[i])
                    self.assertEqual(mean,x);self.assertEqual(var,x*x*p/(1-p))
                for i,j in [(0,1),(0,2),(1,2)]:
                    cross=sum(m*v[i]*v[j] for m,_,v in rows)
                    self.assertEqual(cross-xs[i]*xs[j],0)
                count+=1
        self.assertEqual(count,108)
    def test_linear_squared_loss_decomposition(self):
        for xs,ws,p,y in itertools.product([(2,-1),(0,3)],[(1,1),(-2,1)],[Q(1,4),Q(1,2)],[0,2]):
            z=sum(x*w for x,w in zip(xs,ws))
            expected=sum(m*(sum(w*a for w,a in zip(ws,v))-y)**2 for m,_,v in states(xs,p))
            penalty=p/(1-p)*sum(w*w*x*x for w,x in zip(ws,xs))
            self.assertEqual(expected,(z-y)**2+penalty)
    def test_independent_batch_vs_shared_masks(self):
        rows=states([2,-1],Q(1,2))
        means=[]
        for (mass1,_,v1),(mass2,_,v2) in itertools.product(rows,repeat=2):
            means.append((mass1*mass2,(sum(v1)+sum(v2))/2))
        mean=sum(m*v for m,v in means)
        variance=sum(m*(v-mean)**2 for m,v in means)
        self.assertEqual(mean,1);self.assertEqual(variance,Q(5,2))
        shared=scalar_moments([2,-1],Q(1,2),sum)
        self.assertEqual(shared[1],5)
    def test_eval_zero_dropout_fixed_mask_gradient_and_contracts(self):
        xs=[2,-1];p=Q(1,2);mask=[1,0]
        self.assertEqual(apply(xs,p,training=False),(2,-1))
        self.assertEqual(apply(xs,0,[1,1]),(2,-1))
        self.assertEqual(len(states(xs,0)),1)
        # Finite difference for fixed-mask input map in exact arithmetic.
        h=Q(1,100);base=apply(xs,p,mask)
        plus=apply([Q(2)+h,-1],p,mask);minus=apply([Q(2)-h,-1],p,mask)
        self.assertEqual((plus[0]-minus[0])/(2*h),2)
        self.assertEqual(base[1],0)
        for args in [([],p),([1]*11,p),([1],1),([True],p),([1],.5)]:
            with self.assertRaises(ValueError):states(*args)
        with self.assertRaises(ValueError):apply(xs,p,[1])
        with self.assertRaises(ValueError):apply(xs,p,[True,0])
        with self.assertRaises(ValueError):apply(xs,p,[1,1],training=1)
