import unittest
from fractions import Fraction as Q
from .pair import reduced,at_distance

class Tests(unittest.TestCase):
    def test_fixture_and_zero_energy_not_equilibrium(self):
        self.assertEqual(reduced(1),dict(energy=0,rforce=24))
        self.assertEqual(reduced(Q(1,2)),dict(energy=-1,rforce=0))
        self.assertEqual(reduced(Q(1,4)),dict(energy=Q(-3,4),rforce=-3))
        self.assertEqual(reduced(2)['energy'],8)
    def test_completed_square_and_force_sign(self):
        for j in range(1,129):
            q=Q(j,16);r=reduced(q)
            self.assertEqual(r['energy']+1,4*(q-Q(1,2))**2)
            self.assertGreaterEqual(r['energy'],-1)
            self.assertEqual((r['rforce']>0)-(r['rforce']<0),(q>Q(1,2))-(q<Q(1,2)))
        for x in (Q(1,2),1,Q(6,5),2,4):
            self.assertEqual(at_distance(x)['energy'],4*(1/x**12-1/x**6))
    def test_force_vs_independent_energy_derivative(self):
        for x in (Q(1),Q(6,5),Q(3,2),Q(2),Q(3)):
            actual=at_distance(x)['force'];errors=[]
            for h in (Q(1,1000),Q(1,2000)):
                finite=-(at_distance(x+h)['energy']-at_distance(x-h)['energy'])/(2*h)
                errors.append(abs(finite-actual))
            self.assertLess(float(errors[1]),float(errors[0])/3.9)
            self.assertLess(float(errors[1]),.001)
        # Em um mínimo suave, curvatura em x positiva: U''(x*)=72/x*².
        # x* irracional não é inferido da malha; identidade provada na aula.
    def test_contracts(self):
        for q in (0,-1,65,Q(1,5000),True,.5):
            with self.assertRaises(ValueError):reduced(q)
        for x in (0,Q(1,3),5,True,1.):
            with self.assertRaises(ValueError):at_distance(x)
