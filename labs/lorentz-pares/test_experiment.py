import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import boost

class LorentzPairTests(unittest.TestCase):
    def test_reference_temporal_spatial_and_light(self):
        t=boost(5,3,Q(3,5));s=boost(1,2,Q(3,5));l=boost(1,1,Q(3,5))
        self.assertEqual((t["ct"],t["x"],t["interval"]),(4,0,16))
        self.assertEqual((s["ct"],s["x"],s["interval"]),(Q(-1,4),Q(7,4),-3))
        self.assertEqual((l["ct"],l["x"],l["interval"]),(Q(1,2),Q(1,2),0))
        self.assertEqual(boost(0,0,Q(3,5))["kind"],"coincidente")
        self.assertEqual(l["kind"],"luz")

    def test_invariant_inverse_and_matrix_identity(self):
        betas=(Q(0),Q(3,5),Q(-3,5),Q(4,5),Q(-4,5),Q(5,13),Q(-5,13),Q(12,13),Q(-12,13))
        for beta,ct,x in product(betas,range(-2,3),range(-2,3)):
            r=boost(ct,x,beta);back=boost(r["ct"],r["x"],-beta)
            self.assertEqual(r["interval"],r["transformed_interval"])
            self.assertEqual((back["ct"],back["x"]),(ct,x))
            self.assertEqual(r["gamma"]**2*(1-beta**2),1)
        # Orthogonality for Minkowski metric: columns have norms +1,-1 and mutual product zero.
        for beta in betas:
            a,b=boost(1,0,beta),boost(0,1,beta)
            self.assertEqual(a["ct"]*b["ct"]-a["x"]*b["x"],0)
            self.assertEqual(a["interval"],1);self.assertEqual(b["interval"],-1)

    def test_pair_difference_is_independent_of_common_translation(self):
        for beta in (Q(0),Q(3,5),Q(-4,5)):
            for a,b,shift in (((0,0),(5,3),(7,-2)),((2,-3),(3,-1),(-1,4))):
                aa=boost(a[0]+shift[0],a[1]+shift[1],beta)
                bb=boost(b[0]+shift[0],b[1]+shift[1],beta)
                d=boost(b[0]-a[0],b[1]-a[1],beta)
                self.assertEqual((bb["ct"]-aa["ct"],bb["x"]-aa["x"]),(d["ct"],d["x"]))

    def test_future_causal_order_and_simultaneity(self):
        for beta in (Q(3,5),Q(-4,5),Q(12,13)):
            for ct in (1,2,3):
                for x in range(-ct,ct+1):self.assertGreater(boost(ct,x,beta)["ct"],0)
        self.assertEqual(boost(1,2,Q(3,5))["ct"],Q(-1,4))
        # Spacelike pair (ct=3,x=5) is simultaneous in the beta=3/5 frame.
        self.assertEqual(boost(3,5,Q(3,5))["ct"],0)
        self.assertEqual(boost(0,2,Q(3,5))["ct"],Q(-3,2))

    def test_contracts_and_irrational_gamma_limit(self):
        for args in ((1,2,1),(1,2,-1),(True,2,0),(1.,2,0),(1,2,.6),(1,2,Q(1,2))):
            with self.assertRaises(ValueError):boost(*args)
