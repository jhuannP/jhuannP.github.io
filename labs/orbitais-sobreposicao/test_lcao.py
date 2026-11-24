import unittest
from fractions import Fraction as Q
from .lcao import modes,metric_inner,rayleigh,shifted

class LcaoTests(unittest.TestCase):
    def test_reference(self):
        r=modes(-1,Q(-2,5),Q(1,5))
        self.assertEqual(r['plus']['energy'],Q(-7,6))
        self.assertEqual(r['minus']['energy'],Q(-3,4))
        self.assertEqual(r['plus']['coefficient_squared'],Q(5,12))
        self.assertEqual(r['minus']['coefficient_squared'],Q(5,8))
        self.assertEqual(r['minus']['energy']-r['plus']['energy'],Q(5,12))
    def test_generalized_residual_metric_and_determinant(self):
        for alpha in (-2,-1,1):
            for beta in (Q(-3,5),Q(-1,5),0,Q(2,5)):
                for s in (Q(-3,4),Q(-1,4),0,Q(1,4),Q(3,4)):
                    r=modes(alpha,beta,s)
                    for m in r.values():
                        x,y=m['vector'];e=m['energy']
                        self.assertEqual((alpha*x+beta*y,beta*x+alpha*y),(e*(x+s*y),e*(s*x+y)))
                        self.assertEqual((alpha-e)**2-(beta-e*s)**2,0)
                        self.assertEqual(m['coefficient_squared']*metric_inner((x,y),(x,y),s),1)
                        self.assertEqual(rayleigh(alpha,beta,s,(x,y)),e)
                    self.assertEqual(metric_inner(r['plus']['vector'],r['minus']['vector'],s),0)
    def test_rayleigh_bounds_and_parity_decomposition(self):
        # Independent decomposition into even/odd unnormalized coordinates.
        alpha,beta,s=Q(-1),Q(-2,5),Q(1,5);r=modes(alpha,beta,s)
        eplus,eminus=r['plus']['energy'],r['minus']['energy']
        for x in range(-3,4):
            for y in range(-3,4):
                if x==y==0: continue
                cplus,cminus=Q(x+y,2),Q(x-y,2)
                wplus=2*(1+s)*cplus*cplus;wminus=2*(1-s)*cminus*cminus
                expected=(wplus*eplus+wminus*eminus)/(wplus+wminus)
                actual=rayleigh(alpha,beta,s,(x,y))
                self.assertEqual(actual,expected)
                self.assertTrue(eplus<=actual<=eminus)
                self.assertEqual(metric_inner((x,y),(x,y),s),wplus+wminus)
    def test_energy_origin_and_basis_phase(self):
        for s in (Q(-1,2),0,Q(1,3)):
            original=modes(-1,Q(-2,5),s)
            for offset in (-3,Q(1,2),2):
                r=modes(*shifted(-1,Q(-2,5),s,offset))
                for name in original:
                    self.assertEqual(r[name]['energy'],original[name]['energy']+offset)
            # Rephasing phi_B -> -phi_B changes s and beta, exchanging labels +/-.
            rephased=modes(-1,Q(2,5),-s)
            self.assertEqual(original['plus']['energy'],rephased['minus']['energy'])
            self.assertEqual(original['minus']['energy'],rephased['plus']['energy'])
        r=modes(-1,Q(-1,5),Q(1,5));self.assertEqual(r['plus']['energy'],r['minus']['energy'])
        # Same symmetry, reversed ordering for a different Hamiltonian.
        r=modes(-1,0,Q(1,5));self.assertLess(r['minus']['energy'],r['plus']['energy'])
    def test_contracts(self):
        for s in (-2,-1,1,2,True,0.2):
            with self.assertRaises(ValueError): modes(-1,0,s)
        for v in ((0,0),(1,),(True,1),(1,0.5)):
            with self.assertRaises(ValueError): rayleigh(-1,0,0,v)
        with self.assertRaises(ValueError): modes(-1.0,0,0)
