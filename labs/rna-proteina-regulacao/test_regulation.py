import unittest,math,itertools
from fractions import Fraction as Q
from .regulation import stationary,compare,protein_clamp

class RegulationTests(unittest.TestCase):
    def test_reference_and_non_identifiability(self):
        base=stationary(10,1,2,Q(1,2))
        a=stationary(10,2,1,Q(1,2));b=stationary(10,2,2,1)
        c=stationary(5,1,1,Q(1,2))
        self.assertEqual(base,dict(rna=Q(10),protein=Q(40),protein_per_rna=Q(4)))
        self.assertEqual(a,b);self.assertEqual(a,c)
        self.assertEqual(compare(base,a),dict(rna=Q(1,2),protein=Q(1,4),protein_per_rna=Q(1,2)))
    def test_balances_on_grid_and_scaling(self):
        count=0
        for alpha,delta,beta,gamma in itertools.product([0,1,3],[Q(1,2),2],[0,1,4],[Q(1,3),3]):
            r=stationary(alpha,delta,beta,gamma)
            self.assertEqual(alpha-delta*r['rna'],0)
            self.assertEqual(beta*r['rna']-gamma*r['protein'],0)
            count+=1
        self.assertEqual(count,36)
    def test_inverse_families_same_observables(self):
        # Construct parameters from prescribed M=5,P=10, not forward formula.
        for delta,gamma in itertools.product([Q(1,4),1,3],[Q(1,5),Q(1,2),2]):
            alpha=5*delta;beta=Q(10)*gamma/5
            r=stationary(alpha,delta,beta,gamma)
            self.assertEqual((r['rna'],r['protein']),(5,10))
    def test_clamped_dynamics_and_independent_euler_refinement(self):
        # Fixed M=5,beta=1,gamma=.5,P0=40. Only protein equation is integrated.
        t=2;ref=protein_clamp(5,1,.5,40,t)
        errors=[]
        for n in [100,200,400]:
            dt=t/n;p=40.
            for _ in range(n):p+=dt*(5-.5*p)
            errors.append(abs(p-ref))
        self.assertGreater(errors[0]/errors[1],1.9);self.assertGreater(errors[1]/errors[2],1.9)
        self.assertLess(errors[-1],.014)
        for gamma in [.5,1,2]:
            self.assertAlmostEqual(protein_clamp(5,0,gamma,40,math.log(2)/gamma),20)
            h=1e-5;now=protein_clamp(5,1,gamma,40,1)
            diff=(protein_clamp(5,1,gamma,40,1+h)-protein_clamp(5,1,gamma,40,1-h))/(2*h)
            self.assertAlmostEqual(diff,5-gamma*now,delta=2e-9)
    def test_zeros_and_contracts(self):
        self.assertEqual(stationary(0,1,2,1)['rna'],0)
        self.assertEqual(stationary(1,1,0,1)['protein'],0)
        for args in [(-1,1,1,1),(1,0,1,1),(1,1,-1,1),(1,1,1,0),(True,1,1,1),(.5,1,1,1)]:
            with self.assertRaises(ValueError):stationary(*args)
        with self.assertRaises(ValueError):compare(stationary(0,1,1,1),stationary(1,1,1,1))
        with self.assertRaises(ValueError):compare(stationary(1,1,1,1),stationary(0,1,1,1))
        with self.assertRaises(ValueError):compare(stationary(1,1,1,1),dict(rna=1,protein=2,protein_per_rna=1))
        for args in [(1,1,0,1,1),(1,1,1,1,-1),(1,1,1,float('inf'),1),(True,1,1,1,1)]:
            with self.assertRaises(ValueError):protein_clamp(*args)
