import unittest,json,math,contextlib,io
from pathlib import Path
from fractions import Fraction as F
from .penalty import penalty,quadratic,step


class PenaltyTests(unittest.TestCase):
    def test_exact_derivatives_and_stationary_points(self):
        a=(1,4,2);t=(2,-1,3);mask=(True,True,False)
        for lam in (F(0),F(1,2),F(2),F(10)):
            optimum=tuple(F(c)*v/(c+lam*m) for c,v,m in zip(a,t,mask))
            for w in ((F(2),F(-1),F(3)),(F(0),F(0),F(0)),optimum):
                for j in range(3):
                    plus=list(w);minus=list(w);h=F(1,100)
                    plus[j]+=h;minus[j]-=h
                    central=(quadratic(plus,t,a,lam,mask)-quadratic(minus,t,a,lam,mask))/(2*h)
                    self.assertEqual(central,a[j]*(w[j]-t[j])+lam*w[j]*mask[j])
            self.assertTrue(all(c*(w-y)+lam*w*m==0 for c,w,y,m in zip(a,optimum,t,mask)))
        w=(F(4,3),F(-8,9),F(3))
        self.assertEqual(quadratic(w,t,a,F(1,2),mask),F(8,9))

    def test_updates_and_diagonal_counterexample(self):
        mask=(True,True,False)
        for w in [(2,-1,3),(0,2,-4),(-3,0,1)]:
            for eta in (F(0),F(1,10),F(2)):
                for lam in (F(0),F(1,5),F(3)):
                    args=(w,(1,2,-4),eta,lam,mask)
                    self.assertEqual(step(*args),step(*args,decoupled=True))
        args=((2,-1,3),(1,2,-4),F(1,10),F(1,5),mask)
        coupled=step(*args,preconditioner=(1,F(1,4),2))
        decoupled=step(*args,preconditioner=(1,F(1,4),2),decoupled=True)
        self.assertEqual(coupled,(F(93,50),F(-209,200),F(19,5)))
        self.assertEqual(decoupled,(F(93,50),F(-103,100),F(19,5)))
        self.assertEqual(coupled[1]-decoupled[1],F(-3,200))

    def test_decay_without_data_and_mask(self):
        w=(F(2),F(-1),F(3));initial=w
        for k in range(1,8):
            w=step(w,(0,0,0),F(1,2),F(1,2),(True,True,False))
            self.assertEqual(w,(initial[0]*F(3,4)**k,initial[1]*F(3,4)**k,F(3)))
        self.assertEqual(step((2,),(0,),2,1,(True,)),(F(-2),))
        self.assertEqual(step((2,),(0,),3,1,(True,)),(F(-4),))
        self.assertEqual(penalty((2,-1,300),F(1,5),(True,True,False)),F(1,2))

    def test_existing_mlp_full_objective(self):
        lesson=next(x for x in json.loads((Path(__file__).resolve().parents[2]/'content/lessons.json').read_text()) if x['id']=='dl-regularizacao-pesos')
        scope={}
        with contextlib.redirect_stdout(io.StringIO()): exec(lesson['python'],scope)
        X=[[0,0],[1,0],[0,1],[1,1]];y=[0,1,1,0];lam=.125
        def objective(model):
            logits=[scope['forward'](model,x)['logit'] for x in X]
            data=sum(max(z,0)-z*v+math.log1p(math.exp(-abs(z))) for z,v in zip(logits,y))/len(y)
            return data+lam/2*(sum(v*v for row in model['W'] for v in row)+sum(v*v for v in model['v']))
        for hidden in (1,3):
            m=scope['initialize'](hidden,7);g=scope['gradients'](m,X,y,lam);base=scope['gradients'](m,X,y,0)
            for key in ('W','b','v','c'):
                paths=[(j,k) for j in range(hidden) for k in range(2)] if key=='W' else ([(j,) for j in range(hidden)] if key!='c' else [()])
                for path in paths:
                    def location(obj):
                        if key=='c': return obj,key
                        a=obj[key]
                        for ix in path[:-1]:a=a[ix]
                        return a,path[-1]
                    arr,idx=location(m);old=arr[idx];h=1e-5
                    arr[idx]=old+h;plus=objective(m);arr[idx]=old-h;minus=objective(m);arr[idx]=old
                    grad,ix=location(g);plain,jx=location(base)
                    self.assertAlmostEqual(grad[ix],(plus-minus)/(2*h),places=8)
                    self.assertAlmostEqual(grad[ix]-plain[jx],lam*old if key in ('W','v') else 0,places=12)

    def test_contracts(self):
        for args in [((1,),-1,(True,)),((True,),1,(True,)),((1.0,),1,(True,)),((1,),1,(1,)),((1,),1,(True,False))]:
            with self.assertRaises(ValueError):penalty(*args)
        for kwargs in [dict(eta=-1),dict(lam=-1),dict(preconditioner=(0,)),dict(preconditioner=(1,2)),dict(decoupled=1)]:
            base=dict(w=(1,),gradient=(0,),eta=1,lam=1,mask=(True,));base.update(kwargs)
            with self.assertRaises(ValueError):step(**base)

if __name__=='__main__':unittest.main()
