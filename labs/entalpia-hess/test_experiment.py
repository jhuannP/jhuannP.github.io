import itertools
import unittest
from fractions import Fraction as Q
from .experiment import hess, reaction_enthalpy

class HessTests(unittest.TestCase):
    def test_known_thermal_balance_and_units(self):
        # Processo a p constante: U_f-U_i=Q-p*deltaV, H=U+pV.
        u0, v0, v1, pressure, heat = 10, 2, 5, 3, -7
        u1 = u0+heat-pressure*(v1-v0)
        self.assertEqual((u1+pressure*v1)-(u0+pressure*v0), heat)
        q=hess(20,-30,2)
        self.assertEqual((q['first'],q['second'],q['direct']),(20,-50,-30))
        self.assertEqual(q['total'],-60)
        self.assertEqual(hess(20,-30,2,-1)['total'],60)

    def test_reaction_vectors_cancel_and_reference_is_consistent(self):
        # Reações escritas em vetores: A->B, B->C, A->C.
        ab=(-1,1,0);bc=(0,-1,1);ac=(-1,0,1)
        self.assertEqual(tuple(x+y for x,y in zip(ab,bc)), ac)
        for h in itertools.product((-40,0,25),repeat=3):
            energy=lambda nu: sum(Q(n)*v for n,v in zip(nu,h))
            self.assertEqual(energy(ab)+energy(bc),energy(ac))
            self.assertEqual(energy(tuple(-v for v in ac)),-energy(ac))
            # Um deslocamento comum não altera diferenças entre isômeros 1:1.
            shifted=[v+Q(17,3) for v in h]
            self.assertEqual(sum(n*v for n,v in zip(ac,shifted)),energy(ac))
        hf={'X2':0,'Y2':0,'XY':-15}
        nu={'X2':-1,'Y2':-1,'XY':2}
        self.assertEqual(reaction_enthalpy(nu,hf),-30)
        self.assertEqual(reaction_enthalpy({k:2*v for k,v in nu.items()},hf),-60)
        # A reação fictícia conserva X e Y: [-2+2, -2+2]=[0,0].
        self.assertEqual((2*nu['X2']+nu['XY'],2*nu['Y2']+nu['XY']),(0,0))

    def test_rational_grid_telescoping_inversion_and_extent(self):
        for b,c,x,d in itertools.product((-40,Q(1,3),40),(-60,0,20),(0,Q(1,2),3),(-1,1)):
            q=hess(b,c,x,d)
            self.assertEqual(q['direct'],d*c)
            self.assertEqual(q['first']+q['second'],d*c)
            self.assertEqual(q['cycle'],0)
            self.assertEqual(q['total_first']+q['total_second'],x*d*c)
            opposite=hess(b,c,x,-d)
            self.assertEqual(q['first'],-opposite['second'])
            self.assertEqual(q['total'],-opposite['total'])
            if x==0:self.assertEqual(q['total'],0)

    def test_contract(self):
        for args in ((20,-30,-1,1),(20,-30,1,0),(20.,-30,1,1),(True,-30,1,1)):
            with self.assertRaises(ValueError):hess(*args)
        for nu,h in (({},{}),({'A':1},{'B':2}),({'A':True},{'A':0}),({'A':1},{'A':1.0})):
            with self.assertRaises(ValueError):reaction_enthalpy(nu,h)
