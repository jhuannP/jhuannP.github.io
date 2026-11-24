import unittest
from fractions import Fraction as Q
from .forms import Symmetric2,family,principal_value

class FormTests(unittest.TestCase):
    def test_expansion_against_matrix_action(self):
        # 125 matrizes x 25 vetores; produto matricial e quadrado completado.
        for a in range(-2,3):
            for b in range(-2,3):
                for c in range(-2,3):
                    m=Symmetric2(a,b,c)
                    for x in range(-2,3):
                        for y in range(-2,3):
                            av=m.apply((x,y));direct=x*av[0]+y*av[1]
                            self.assertEqual(m.quadratic((x,y)),direct)
                            if a:self.assertEqual(m.completed_square((x,y)),direct)

    def test_classification_against_spectral_invariants(self):
        # Sinais das raízes reais via soma/produto; sem busca finita de direções.
        for a in range(-3,4):
            for b in range(-3,4):
                for c in range(-3,4):
                    det=a*c-b*b;trace=a+c
                    if det<0:expected='indefinida'
                    elif det>0:expected='positiva definida' if trace>0 else 'negativa definida'
                    elif trace>0:expected='positiva semidefinida'
                    elif trace<0:expected='negativa semidefinida'
                    else:expected='nula'
                    self.assertEqual(Symmetric2(a,b,c).classify(),expected)
        self.assertEqual(Symmetric2(0,0,-1).classify(),'negativa semidefinida')
        self.assertEqual(Symmetric2(-1,0,-1).classify(),'negativa definida')

    def test_family_axes_and_identity(self):
        for t in [Q(k,2) for k in range(-8,9)]:
            a=family(t)
            self.assertEqual(a.apply((1,1)),(2+t,2+t))
            self.assertEqual(a.apply((1,-1)),(2-t,t-2))
            for x in range(-3,4):
                for y in range(-3,4):
                    self.assertEqual(a.quadratic((x,y)),principal_value(t,(x,y)))
                    if abs(t)<2 and (x or y):self.assertGreater(a.quadratic((x,y)),0)
        self.assertEqual(family(2).quadratic((1,-1)),0)
        self.assertLess(family(3).quadratic((1,-1)),0)
        self.assertGreater(family(3).quadratic((1,1)),0)

    def test_energy_minimizer_and_gap(self):
        for t in [Q(-3,2),Q(-1,2),Q(0),Q(1),Q(3,2)]:
            m=family(t)
            for f in [(1,0),(0,1),(2,-3)]:
                z=m.minimizer(f);self.assertEqual(m.apply(z),f)
                for h in [(1,0),(0,-1),(2,-3),(Q(1,3),Q(-2,5))]:
                    zh=tuple(x+y for x,y in zip(z,h))
                    gap=m.energy(zh,f)-m.energy(z,f)
                    self.assertEqual(gap,m.quadratic(h)/2)
                    self.assertGreater(gap,0)
        self.assertEqual(family(1).energy((Q(2,3),Q(-1,3)),(1,0)),Q(-1,3))

    def test_counterexamples_and_contracts(self):
        m=Symmetric2(1,2,1)
        self.assertGreater(m.quadratic((1,0)),0);self.assertGreater(m.quadratic((0,1)),0)
        self.assertEqual(m.quadratic((1,-1)),-2)
        self.assertEqual(m.classify(),'indefinida')
        for bad in [True,0.5,'1',None]:
            with self.assertRaises(TypeError):family(bad)
        with self.assertRaises(ValueError):family(1).quadratic((1,))
        with self.assertRaises(ValueError):Symmetric2(0,0,1).completed_square((1,2))
        for t in (2,3):
            with self.assertRaises(ValueError):family(t).minimizer((1,0))

if __name__=='__main__':unittest.main()
