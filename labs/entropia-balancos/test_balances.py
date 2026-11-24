import unittest
from fractions import Fraction as Q
from itertools import product
from math import isclose,log
from .balances import candidate,free_entropy

class EntropyTests(unittest.TestCase):
    def test_three_candidates(self):
        expected=[(600,600,Q(1,2),Q(0),True),(800,400,Q(1,3),Q(2,3),True),(400,800,Q(2,3),Q(-2,3),False)]
        for QC,W,eta,ds,allowed in expected:
            r=candidate(TH=600,TC=300,QH=1200,QC=QC)
            self.assertEqual((r['work'],r['eta'],r['ds_total'],r['not_excluded_by_entropy']),(W,eta,ds,allowed))
            self.assertEqual(r['ds_hot'],-2)

    def test_carnot_inequality_equivalence(self):
        for TH,TC,QH,fraction in product((400,600,800),(100,200,300),(100,600,1200),(Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1))):
            r=candidate(TH=TH,TC=TC,QH=QH,QC=QH*fraction)
            self.assertEqual(r['work']+QH*fraction,QH)
            self.assertEqual(r['not_excluded_by_entropy'],r['eta']<=r['carnot_limit'])
            self.assertEqual(r['ds_total'],Q(QH,TC)*(r['carnot_limit']-r['eta']))

    def test_scalings_and_boundary(self):
        a=candidate(TH=600,TC=300,QH=1200,QC=800)
        b=candidate(TH=600,TC=300,QH=2400,QC=1600)
        self.assertEqual(b['eta'],a['eta'])
        self.assertEqual(b['ds_total'],2*a['ds_total'])
        c=candidate(TH=1200,TC=600,QH=1200,QC=800)
        self.assertEqual(c['eta'],a['eta'])
        self.assertEqual(c['ds_total'],a['ds_total']/2)
        self.assertFalse(candidate(TH=600,TC=300,QH=1200,QC=0)['not_excluded_by_entropy'])
        self.assertEqual(candidate(TH=600,TC=300,QH=1200,QC=1200)['work'],0)

    def test_free_entropy_and_reversible_reference(self):
        ds=free_entropy(2,2)
        self.assertTrue(isclose(ds,2*log(2),rel_tol=1e-14))
        self.assertGreater(ds,0)
        # Auxiliary reversible isotherm at T=300 K: Qrev/T cancels nRT scale.
        self.assertTrue(isclose(ds,600*log(2)/300,rel_tol=1e-14))
        self.assertEqual(free_entropy(2,1),0)
        self.assertTrue(isclose(free_entropy(2,2)+free_entropy(2,3),free_entropy(2,6),rel_tol=1e-14))

    def test_reference_integral_refines(self):
        expected=free_entropy(2,2);errors=[]
        for n in (50,100,200):
            h=1/n;estimate=2*h*sum(1/(1+(j+.5)*h) for j in range(n))
            errors.append(abs(estimate-expected))
        self.assertTrue(errors[1]<errors[0]/3 and errors[2]<errors[1]/3)
        self.assertLess(errors[-1],1e-5)

    def test_contracts(self):
        base=dict(TH=600,TC=300,QH=1200,QC=600)
        for key in base:
            for bad in (True,1.0,'1'):
                with self.assertRaises(ValueError):candidate(**dict(base,**{key:bad}))
        for changes in ({'TH':0},{'TC':0},{'TC':600},{'QH':0},{'QC':-1},{'QC':1300}):
            with self.assertRaises(ValueError):candidate(**dict(base,**changes))
        for nR,ratio in ((True,2),(2,True),(0,2),(2,.5),(float('inf'),2),(2,float('nan')),(10**400,2)):
            with self.assertRaises(ValueError):free_entropy(nR,ratio)
        with self.assertRaises(ArithmeticError):free_entropy(1e308,1e308)
        with self.assertRaises(ArithmeticError):free_entropy(float.fromhex("0x0.0000000000001p-1022"),1.0000001)
