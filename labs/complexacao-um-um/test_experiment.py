import unittest
from fractions import Fraction as Q
from itertools import product
from .experiment import equilibrium

class ComplexationTests(unittest.TestCase):
    def test_reference_and_exact_manufactured_roots(self):
        for x,m,l in product((Q(1,4),Q(1),Q(3)),repeat=3):
            k=x/(m*l)
            r=equilibrium(m+x,l+x,k)
            self.assertLessEqual(r["lower"],x)
            self.assertGreaterEqual(r["upper"],x)
            self.assertLessEqual(r["upper"]-r["lower"],min(m+x,l+x)/2**80)
        r=equilibrium(2,3,Q(1,2))
        self.assertAlmostEqual(float(r["complex"]),1,places=14)
        self.assertAlmostEqual(float(r["fraction"]),.5,places=14)

    def test_mass_balance_and_residual_brackets(self):
        for a,b,k in product((Q(0),Q(1,10),Q(2),Q(5)),repeat=3):
            r=equilibrium(a,b,k)
            lo,hi,x=r["lower"],r["upper"],r["complex"]
            self.assertGreaterEqual(lo,0)
            self.assertLessEqual(hi,min(a,b))
            self.assertEqual(r["metal_free"]+x,a)
            self.assertEqual(r["ligand_free"]+x,b)
            self.assertGreaterEqual(k*(a-lo)*(b-lo)-lo,0)
            self.assertLessEqual(k*(a-hi)*(b-hi)-hi,0)

    def test_units_and_monotonicity(self):
        for k in (Q(1,10),Q(1),Q(10)):
            mM=equilibrium(2,3,k)
            molar=equilibrium(Q(2,1000),Q(3,1000),k*1000)
            self.assertEqual(mM["complex"]/1000,molar["complex"])
            self.assertEqual(mM["fraction"],molar["fraction"])
        xs=[equilibrium(2,3,k)["complex"] for k in (Q(1,10),Q(1),Q(10))]
        self.assertLess(xs[0],xs[1]);self.assertLess(xs[1],xs[2])
        ys=[equilibrium(2,b,1)["complex"] for b in (1,2,3)]
        self.assertLess(ys[0],ys[1]);self.assertLess(ys[1],ys[2])

    def test_excess_approximation_and_refinement(self):
        # Free ligand is below total ligand, so the reservoir formula overestimates ML.
        for b in (Q(3),Q(20),Q(200)):
            r=equilibrium(2,b,Q(1,2))
            reservoir=2*(b/2)/(1+b/2)
            self.assertGreater(reservoir,r["upper"])
        coarse=equilibrium(2,3,Q(1),steps=10)
        fine=equilibrium(2,3,Q(1),steps=20)
        self.assertGreaterEqual(fine["lower"],coarse["lower"])
        self.assertLessEqual(fine["upper"],coarse["upper"])
        self.assertLess(fine["upper"]-fine["lower"],coarse["upper"]-coarse["lower"])
        self.assertIsNone(equilibrium(0,3,1)["fraction"])

    def test_contracts(self):
        for a,b,k,n in ((-1,2,1,80),(1,2,-1,80),(1.,2,1,80),
                        (True,2,1,80),(1,2,1,0),(1,2,1,True),(1,2,1,257)):
            with self.assertRaises(ValueError):equilibrium(a,b,k,n)
