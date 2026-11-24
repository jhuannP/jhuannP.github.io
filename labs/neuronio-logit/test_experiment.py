import unittest
import math
from itertools import product
from .experiment import sigmoid,bce_logit,affine,loss_and_grad,step

class LogisticUnitTests(unittest.TestCase):
    def test_lesson_update(self):
        x,w,b,y=(2,1),(1,-1),-1,1
        loss,p,gw,gb=loss_and_grad(x,w,b,y)
        self.assertAlmostEqual(loss,math.log(2),places=14)
        self.assertEqual((p,gw,gb),(.5,(-1,-.5),-.5))
        nw,nb=step(x,w,b,y,.2)
        self.assertEqual(nw,(1.2,-.9));self.assertEqual(nb,-.9)
        self.assertAlmostEqual(affine(x,nw,nb),.6,places=14)
        self.assertLess(loss_and_grad(x,nw,nb,y)[0],loss)

    def test_gradients_by_central_differences(self):
        x=(2.,-1.);h=1e-5
        for a,bias,y in product((-.7,.2),(-.3,.6),(0,1)):
            w=(a,.4);_,_,gw,gb=loss_and_grad(x,w,bias,y)
            for j in range(2):
                up=list(w);down=list(w);up[j]+=h;down[j]-=h
                finite=(bce_logit(affine(x,up,bias),y)-bce_logit(affine(x,down,bias),y))/(2*h)
                self.assertAlmostEqual(finite,gw[j],places=8)
            finite=(bce_logit(affine(x,w,bias+h),y)-bce_logit(affine(x,w,bias-h),y))/(2*h)
            self.assertAlmostEqual(finite,gb,places=8)

    def test_stability_symmetry_and_naive_agreement(self):
        for z in (-1000,-100,-1,0,1,100,1000):
            self.assertTrue(math.isfinite(sigmoid(z)))
            for y in (0,1):
                value=bce_logit(z,y)
                self.assertTrue(math.isfinite(value));self.assertGreaterEqual(value,0)
                self.assertAlmostEqual(value,bce_logit(-z,1-y),places=12)
        for z in (-5,-1,0,1,5):
            p=sigmoid(z)
            for y in (0,1):self.assertAlmostEqual(bce_logit(z,y),-y*math.log(p)-(1-y)*math.log1p(-p),places=12)
        self.assertEqual(bce_logit(1000,0),1000)
        self.assertEqual(bce_logit(-1000,1),1000)

    def test_logit_gradient_and_zero_step(self):
        for y in (0,1):
            _,p,gw,gb=loss_and_grad((1,),(1000,),0,y)
            self.assertEqual(gb,p-y);self.assertEqual(gw,(gb,))
        self.assertEqual(step((2,1),(1,-1),-1,1,0),((1,-1),-1))
        self.assertEqual(sigmoid(0),.5)

    def test_contract(self):
        for x,w,b,y in [((),(),0,1),((1,),(1,2),0,1),((True,),(1,),0,1),((1,),(1,),0,True),((1,),(1,),0,2),((1,),(1,),float('nan'),1)]:
            with self.assertRaises(ValueError):loss_and_grad(x,w,b,y)
        with self.assertRaises(ValueError):step((1,),(1,),0,1,-.1)
        with self.assertRaises(ValueError):sigmoid(float('inf'))
