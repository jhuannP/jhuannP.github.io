import unittest
from fractions import Fraction as Q
from itertools import product
from .split import bubble,dew,split_at_tp,rr_bracket


def manufactured():
    for pA,pB in [(80,20),(30,10),(7,2)]:
        for x,beta in product([Q(1,5),Q(1,3),Q(3,4)],[Q(1,5),Q(1,2),Q(4,5)]):
            # Manufacture from partial pressures and two known phase inventories.
            p_A=x*pA;p_B=(1-x)*pB;P=p_A+p_B;y=p_A/P
            z=(1-beta)*x+beta*y
            yield pA,pB,P,x,y,beta,z


class RaoultSplit(unittest.TestCase):
    def test_original_inventory(self):
        a=split_at_tp(80,20,40,Q(2,5),5)
        expected=dict(regime='two-phase',x=Q(1,3),y=Q(2,3),beta=Q(1,5),
                      nV=1,nL=4,vapor_A=Q(2,3),liquid_A=Q(4,3),
                      vapor_B=Q(1,3),liquid_B=Q(8,3),bubble=44,dew=Q(200,7))
        for key,value in expected.items():self.assertEqual(a[key],value,key)
        b=split_at_tp(80,20,32,Q(2,5),5)
        self.assertEqual((b['x'],b['y'],b['beta']),(Q(1,5),Q(1,2),Q(2,3)))

    def test_manufactured_equilibria_and_both_component_balances(self):
        for pA,pB,P,x,y,beta,z in manufactured():
            a=split_at_tp(pA,pB,P,z,7)
            self.assertEqual((a['x'],a['y'],a['beta']),(x,y,beta))
            self.assertEqual(a['regime'],'two-phase')
            self.assertEqual((y*P,(1-y)*P),(x*pA,(1-x)*pB))
            self.assertEqual(a['liquid_A']+a['vapor_A'],7*z)
            self.assertEqual(a['liquid_B']+a['vapor_B'],7*(1-z))
            self.assertEqual(a['nL']+a['nV'],7)
            self.assertLess(x,y)
            self.assertEqual((y/(1-y))/(x/(1-x)),Q(pA,pB))

    def test_phase_classification_and_incipient_limits(self):
        for pA,pB,z in product([80,100],[10,20],[Q(1,10),Q(2,5),Q(4,5)]):
            pb, pd=bubble(pA,pB,z),dew(pA,pB,z)
            self.assertLess(pd,pb)
            cases=[(pd/2,'vapor',1),(pd,'dew',1),((pd+pb)/2,'two-phase',None),
                   (pb,'bubble',0),(pb*2,'liquid',0)]
            for P,regime,beta in cases:
                a=split_at_tp(pA,pB,P,z)
                self.assertEqual(a['regime'],regime)
                if beta is not None:self.assertEqual(a['beta'],beta)
                if regime=='liquid':self.assertIsNone(a['y']);self.assertEqual(a['x'],z)
                if regime=='vapor':self.assertIsNone(a['x']);self.assertEqual(a['y'],z)
                if regime=='bubble':self.assertEqual(a['x'],z);self.assertGreater(a['y'],z)
                if regime=='dew':self.assertEqual(a['y'],z);self.assertLess(a['x'],z)
        a=split_at_tp(80,20,44,Q(2,5));self.assertEqual(a['y'],Q(8,11))
        a=split_at_tp(80,20,Q(200,7),Q(2,5));self.assertEqual(a['x'],Q(1,7))

    def test_independent_two_component_residual_brackets(self):
        for pA,pB,P,x,y,beta,z in manufactured():
            lo,hi=rr_bracket(pA,pB,P,z)
            self.assertLessEqual(lo,beta);self.assertLessEqual(beta,hi)
            self.assertLessEqual(hi-lo,Q(1,2**60))
            def f(b):
                a,bk=Q(pA)/P-1,Q(pB)/P-1
                return z*a/(1+b*a)+(1-z)*bk/(1+b*bk)
            self.assertGreaterEqual(f(lo),0);self.assertLessEqual(f(hi),0)
            self.assertEqual(f(beta),0)
            self.assertGreater(f(0),f(1))

    def test_pressure_units_and_inventory_scaling(self):
        reference=split_at_tp(80,20,40,Q(2,5),5)
        for scale in [Q(1,10),3,1000]:
            a=split_at_tp(80*scale,20*scale,40*scale,Q(2,5),5)
            for key in ['x','y','beta','nL','nV','liquid_A','vapor_B']:
                self.assertEqual(a[key],reference[key])
        a=split_at_tp(80,20,40,Q(2,5),35)
        for key in ['nL','nV','liquid_A','liquid_B','vapor_A','vapor_B']:
            self.assertEqual(a[key],7*reference[key])
        for end in [0,1]:
            self.assertEqual(bubble(80,20,end),[20,80][end])
            self.assertEqual(dew(80,20,end),[20,80][end])

    def test_contracts_and_degenerate_cases(self):
        good=[80,20,40,Q(2,5),5]
        for i in range(5):
            for bad in [True,1.0,'1',None]:
                args=good.copy();args[i]=bad
                with self.assertRaises(ValueError):split_at_tp(*args)
        for args in [(20,80,40,Q(2,5)),(20,20,20,Q(2,5)),(80,0,40,Q(2,5)),
                     (80,20,0,Q(2,5)),(80,20,40,0),(80,20,40,1),
                     (80,20,40,Q(2,5),0)]:
            with self.assertRaises(ValueError):split_at_tp(*args)
        for comp in [-1,2]:
            with self.assertRaises(ValueError):bubble(80,20,comp)
            with self.assertRaises(ValueError):dew(80,20,comp)
        for steps in [0,129,True,1.5]:
            with self.assertRaises(ValueError):rr_bracket(80,20,40,Q(2,5),steps)
        for pressure in [20,44,80]:
            with self.assertRaises(ValueError):rr_bracket(80,20,pressure,Q(2,5))
