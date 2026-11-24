import unittest
from fractions import Fraction as Q
from itertools import product
from math import factorial, log, lgamma
from .gas import state


class GasTests(unittest.TestCase):
    def test_reference(self):
        self.assertEqual(state(3, 2, 300, 1), dict(Z=Q(4500000), pressure=Q(1, 50),
            energy=Q(9), cv_over_kB=Q(9, 2), degeneracy=Q(1, 100)))

    def test_control_changes(self):
        for n, t, v in product((1, 3, 7), (Q(1, 2), Q(2)), (Q(300), Q(600))):
            base = state(n, t, v, 1)
            expanded = state(n, t, 2*v, 1)
            hot = state(n, 4*t, v, Q(1, 8))
            self.assertEqual(expanded['Z']/base['Z'], 2**n)
            self.assertEqual(expanded['pressure'], base['pressure']/2)
            self.assertEqual(expanded['energy'], base['energy'])
            self.assertEqual(hot['Z']/base['Z'], 8**n)
            self.assertEqual(hot['energy'], 4*base['energy'])
            self.assertEqual(hot['pressure'], 4*base['pressure'])
            self.assertEqual(hot['degeneracy'], base['degeneracy']/8)

    def test_thermodynamic_derivatives(self):
        # Independent floating log-partition, tau(theta)=theta**(-3/2), not held fixed.
        def lnz(n, t, v):
            return n*(log(v)+1.5*log(t))-lgamma(n+1)
        h = 1e-4
        for n, t, v in product((1, 3, 9), (1., 2., 4.), (10., 100.)):
            s = state(n, Q(t), Q(v), Q(1))
            p = t*(lnz(n,t,v+h)-lnz(n,t,v-h))/(2*h)
            u = t*t*(lnz(n,t+h,v)-lnz(n,t-h,v))/(2*h)
            self.assertAlmostEqual(p, float(s['pressure']), delta=2e-8)
            self.assertAlmostEqual(u, float(s['energy']), delta=2e-7)
        # tau=1 in state above is just a prescribed reference: P,U do not depend on its value.

    def test_multinomial_identity(self):
        # Algebraic occupancy weights, NOT exact Bose/Fermi quantum counting.
        for n, cells in product(range(1, 7), range(1, 5)):
            def compositions(total, slots):
                if slots == 1:
                    yield (total,)
                else:
                    for k in range(total+1):
                        for rest in compositions(total-k, slots-1):
                            yield (k,)+rest
            summed = sum((Q(1, __import__('math').prod(factorial(k) for k in c))
                          for c in compositions(n, cells)), Q(0))
            self.assertEqual(summed, state(n, 1, cells, 1)['Z'])

    def test_old_example_and_challenge(self):
        N,T,V=4,2,8
        p=N*T/V; U=1.5*N*T
        self.assertEqual((p,U),(1,12))
        self.assertEqual((N*T/(2*V))/(N*T/V),.5)
        self.assertEqual(state(N,T,V,1)['energy'],state(N,T,2*V,1)['energy'])

    def test_contracts(self):
        for args in [(0,2,300,1),(101,2,300,1),(3,0,300,1),(3,2,-1,1),(3,2,300,0)]:
            with self.assertRaises(ValueError): state(*args)
        for args in [(True,2,300,1),(3,2.,300,1),(3,2,True,1),(3,2,300,'1')]:
            with self.assertRaises(TypeError): state(*args)
