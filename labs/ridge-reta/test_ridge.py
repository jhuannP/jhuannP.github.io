from fractions import Fraction as Q
from itertools import product
import unittest
from .ridge import Fit,fit_ridge,predict,sse,objective


def raw_normal_equations(x,y,lam):
    # Solução independente por Cramer, sem centralizar.
    n=len(x);sx=sum(x);sy=sum(y)
    ax=sum(v*v for v in x)+lam;c=sum(u*v for u,v in zip(x,y))
    det=ax*n-sx*sx
    return Fit(Q(c*n-sx*sy,det),Q(ax*sy-sx*c,det))


class RidgeTests(unittest.TestCase):
    def test_normal_equations_and_global_objective_decomposition(self):
        for x in ([-1,0,1],[0,1,3]):
            mx=Q(sum(x),len(x));sxx=sum((Q(v)-mx)**2 for v in x)
            for y in product((-2,0,3),repeat=3):
                for lam in (Q(0),Q(1,2),Q(2),Q(10)):
                    model=fit_ridge(x,y,lam)
                    self.assertEqual(model,raw_normal_equations(x,y,lam))
                    residual=[predict(model,u)-v for u,v in zip(x,y)]
                    self.assertEqual(sum(residual),0)
                    self.assertEqual(sum(u*r for u,r in zip(x,residual)),-lam*model.w)
                    baseline=objective(x,y,model,lam)
                    for dw,db in product((Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)),repeat=2):
                        changed=objective(x,y,Fit(model.w+dw,model.b+db),lam)
                        gap=(sxx+lam)*dw*dw+len(x)*(db+mx*dw)**2
                        self.assertEqual(changed-baseline,gap)
                        if dw or db:self.assertGreater(gap,0)

    def test_units_translation_and_replication(self):
        x=[-1,0,1];y=[-2,0,2];lam=Q(2);base=fit_ridge(x,y,lam)
        for scale,shift in ((Q(100),Q(0)),(Q(3),Q(5)),(Q(-2),Q(1))):
            converted=fit_ridge([scale*v+shift for v in x],y,scale*scale*lam)
            self.assertEqual(converted,Fit(base.w/scale,base.b-base.w*shift/scale))
            for v in (-3,0,4):self.assertEqual(predict(converted,scale*v+shift),predict(base,v))
        wrong=fit_ridge([100*v for v in x],y,2)
        self.assertEqual(wrong.w,Q(200,10001))
        self.assertNotEqual(predict(wrong,100),predict(base,1))
        self.assertEqual(fit_ridge(x+x,y+y,4),base)
        self.assertEqual(fit_ridge(x+x,y+y,2).w,Q(4,3))
        shifted=fit_ridge(x,[v+7 for v in y],lam)
        self.assertEqual(shifted,Fit(base.w,base.b+7))

    def test_examples_sensitivity_and_no_test_guarantee(self):
        x=[-1,0,1];y=[-2,0,2]
        ols=fit_ridge(x,y,0);ridge=fit_ridge(x,y,2)
        self.assertEqual(ols,Fit(2,0));self.assertEqual(ridge,Fit(1,0))
        self.assertEqual(sse(x,y,ols),0);self.assertEqual(sse(x,y,ridge),2)
        self.assertEqual(objective(x,y,ridge,2),4)
        self.assertEqual(objective(x,y,ols,2),8)
        for delta in (Q(-1),Q(1,10),Q(2)):
            changed=fit_ridge(x,[-2,0,2+delta],2)
            self.assertEqual(changed.w-ridge.w,delta/4)
            self.assertEqual(changed.b-ridge.b,delta/3)
        self.assertEqual((predict(ridge,2)-4)**2,4)
        self.assertEqual((predict(ols,2)-4)**2,0)
        n=len(x);mu=Q(2,n)
        for w,b in product(range(-2,3),repeat=2):
            model=Fit(w,b)
            self.assertEqual(sse(x,y,model)/n+mu*w*w,objective(x,y,model,2)/n)

    def test_constant_inputs_and_nonunique_unregularized_case(self):
        with self.assertRaises(ArithmeticError):fit_ridge([2,2,2],[1,2,3],0)
        self.assertEqual(fit_ridge([2,2,2],[1,2,3],2),Fit(0,2))
        # Quando lambda=0 há infinitos mínimos, não ausência de solução.
        for w in (-5,0,7):self.assertEqual(sse([2,2,2],[1,2,3],Fit(w,2-2*w)),2)
        self.assertEqual(fit_ridge([3],[7],1),Fit(0,7))

    def test_contracts_and_input_preservation(self):
        for x,y in (([],[]),([1],[1,2])):
            with self.assertRaises(ValueError):fit_ridge(x,y)
        for x in ([True],[.1],['1']):
            with self.assertRaises(TypeError):fit_ridge(x,[1],2)
        with self.assertRaises(ValueError):fit_ridge([0,1],[0,1],-1)
        with self.assertRaises(TypeError):fit_ridge([0,1],[0,1],.1)
        with self.assertRaises(TypeError):Fit(1,.5)
        with self.assertRaises(TypeError):predict({},1)
        x=[-1,0,1];y=[-2,0,2]
        fit_ridge(x,y,2)
        self.assertEqual((x,y),([-1,0,1],[-2,0,2]))

if __name__=="__main__":unittest.main()
