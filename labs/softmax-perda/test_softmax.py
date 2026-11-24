import unittest
import math
import itertools
import deep_ops
from .softmax import softmax,cross_entropy,loss_gradient,batch_loss_gradient

class SoftmaxTests(unittest.TestCase):
    def test_references_and_regression(self):
        for loss in [cross_entropy,deep_ops.cross_entropy]:
            for shift in [0,1000,1e20,-1e20]:
                self.assertAlmostEqual(loss([shift]*3,1),math.log(3),places=14)
            self.assertEqual(loss([1000,0,-1000],2),2000)
            self.assertAlmostEqual(loss([50,0],0),math.log1p(math.exp(-50)),delta=1e-35)
            self.assertEqual(loss([1000],0),0)
        for z in itertools.product([-2.,0.,3.],repeat=3):
            for target in range(3):
                direct=-math.log(math.exp(z[target])/sum(math.exp(v) for v in z))
                self.assertAlmostEqual(cross_entropy(z,target),direct,places=13)
                self.assertEqual(cross_entropy(z,target),deep_ops.cross_entropy(z,target))
        self.assertEqual(softmax([1000,0,-1000])[2],0)

    def test_gradient_and_jacobian(self):
        h=1e-5
        for z in [[0.,0.,0.],[.3,-.5,1.2],[-4.,2.,1.],[math.log(2),0,0]]:
            prob=softmax(z)
            for target in range(3):
                loss,g=loss_gradient(z,target)
                self.assertAlmostEqual(sum(g),0,places=14)
                for j in range(3):
                    a=z.copy();b=z.copy();a[j]+=h;b[j]-=h
                    fd=(cross_entropy(a,target)-cross_entropy(b,target))/(2*h)
                    self.assertAlmostEqual(fd,g[j],delta=2e-10)
                    pa,pb=softmax(a),softmax(b)
                    for i in range(3):
                        jac=prob[i]*(int(i==j)-prob[j])
                        self.assertAlmostEqual((pa[i]-pb[i])/(2*h),jac,delta=2e-10)

    def test_invariance_and_input_resolution(self):
        z=[-2,0,3];p=softmax(z)
        for shift in [-1000,1000]:
            q=softmax([x+shift for x in z])
            for a,b in zip(p,q):self.assertAlmostEqual(a,b,places=14)
            self.assertAlmostEqual(cross_entropy(z,0),cross_entropy([x+shift for x in z],0),places=14)
        # Informação perdida na entrada não é recuperada pela estabilização.
        self.assertEqual(1e20+1,1e20)
        self.assertNotEqual(softmax([0,1]),softmax([1e20,1e20+1]))
        self.assertAlmostEqual(cross_entropy([.5,.25,.25],0),math.log(1+2*math.exp(-.25)),places=14)
        self.assertNotAlmostEqual(cross_entropy([.5,.25,.25],0),math.log(2),places=5)

    def test_batch_reduction(self):
        rows=[[math.log(2),0,0],[0,math.log(2),0]];targets=[0,1]
        mean,gm=batch_loss_gradient(rows,targets,'mean')
        total,gs=batch_loss_gradient(rows,targets,'sum')
        self.assertAlmostEqual(mean,math.log(2),places=14)
        self.assertAlmostEqual(total,2*mean,places=14)
        for a,b in zip(gm,gs):
            for u,v in zip(a,b):self.assertEqual(2*u,v)
        h=1e-5
        for i in range(2):
            for j in range(3):
                a=[r.copy() for r in rows];b=[r.copy() for r in rows]
                a[i][j]+=h;b[i][j]-=h
                fd=(batch_loss_gradient(a,targets)[0]-batch_loss_gradient(b,targets)[0])/(2*h)
                self.assertAlmostEqual(fd,gm[i][j],delta=2e-10)

    def test_masks_and_contracts(self):
        self.assertEqual(softmax([1,2,3],[False,True,False]),[0,1,0])
        for z,mask in [([],None),([1,2],[False,False]),([1,2],[True]),([1,2],[1,0])]:
            with self.assertRaises(ValueError):softmax(z,mask)
        for z,t in [([],0),([1,2],True),([1,2],2),([1,2],-1),([math.inf,0],0),([math.nan,0],0),([True,0],0),([1e308,-1e308],1)]:
            with self.assertRaises(ValueError):cross_entropy(z,t)
        for rows,targets in [([],[]),([[0,1]],[]),([[0,1],[0]],[0,0])]:
            with self.assertRaises(ValueError):batch_loss_gradient(rows,targets)
        with self.assertRaises(ValueError):batch_loss_gradient([[1,2]],[0],'other')

if __name__=='__main__':unittest.main()
