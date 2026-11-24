import unittest
from math import exp, factorial, fsum, sqrt, pi
from .progression import progression, lines


class ProgressionTests(unittest.TestCase):
    def test_weights_and_moments(self):
        for S in (0, .1, .5, 1, 1.5, 2, 5, 10, 20):
            r = progression(S, 200)
            for n, w in enumerate(r['weights'][:31]):
                self.assertAlmostEqual(w, exp(-S)*S**n/factorial(n), places=14)
                self.assertGreaterEqual(w, 0)
            self.assertAlmostEqual(r['sum'], 1, places=13)
            self.assertAlmostEqual(fsum(n*w for n,w in enumerate(r['weights'])),S,places=12)
            self.assertAlmostEqual(fsum((n-S)**2*w for n,w in enumerate(r['weights'])),S,places=11)

    def test_gaussian_overlap_independent_quadrature(self):
        # x adimensional; domínio finito e erro numérico, não quadratura certificada.
        for S in (0, .5, 1.5, 3):
            delta = sqrt(2*S)
            dx = 24/12000
            amp = dx*fsum(exp(-(((-12+(i+.5)*dx)**2)+(-12+(i+.5)*dx-delta)**2)/2)
                          /sqrt(pi) for i in range(12000))
            self.assertAlmostEqual(amp*amp, progression(S,0)['weights'][0], places=11)

    def test_example_truncation_and_energies(self):
        r = progression(1.5,4)
        self.assertAlmostEqual(r['sum'], .9814240637778593)
        self.assertAlmostEqual(r['omitted'], .0185759362221407)
        self.assertEqual(max(range(5), key=r['weights'].__getitem__),1)
        self.assertAlmostEqual(r['weights'][2]/r['weights'][1],.75)
        self.assertEqual(progression(0,4)['weights'],[1,0,0,0,0])
        self.assertGreater(progression(1.5,4)['omitted'],progression(1.5,12)['omitted'])
        table=lines(1.5,2,.1,4)
        self.assertAlmostEqual(table[1][1],2.1)
        self.assertAlmostEqual(fsum(e*w for _,e,w in lines(1.5,2,.1,100)),2.15)

    def test_contracts(self):
        for S in (True,-1,21,float('nan'),float('inf'),'1'):
            with self.assertRaises(ValueError):progression(S)
        for last in (True,-1,201,2.0):
            with self.assertRaises(ValueError):progression(1,last)
        for E,q in ((0,1),(1,0),(-1,1),(True,1),(1,float('inf'))):
            with self.assertRaises(ValueError):lines(1,E,q)


if __name__ == '__main__': unittest.main()
