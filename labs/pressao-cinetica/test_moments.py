import unittest
from fractions import Fraction as Q
from itertools import product,permutations
from .moments import population,example


class MomentTests(unittest.TestCase):
    def test_original_example(self):
        a=example()
        self.assertEqual(a['density'],10**25)
        self.assertEqual(a['second'][0][0],30000)
        self.assertEqual(a['normal'],(3000,3000,3000))
        self.assertEqual(a['energy_density'],4500)
        self.assertTrue(a['isotropic_second_moment'])

    def test_individual_round_trip_impulse(self):
        # Média temporal de uma partícula sem colisões intermoleculares em caixa retangular.
        for m,Lx,Ly,Lz,vx in product((1,2),(1,3),(2,4),(1,2),(-3,-1,1,3)):
            area=Ly*Lz;V=Lx*area
            force=Q(2*m*abs(vx))/Q(2*Lx,abs(vx))
            self.assertEqual(force/area,Q(m*vx*vx,V))

    def test_trace_energy_and_permutations(self):
        for w in product((-2,0,3),repeat=3):
            velocities=[w,tuple(-x for x in w)]
            a=population(2,3,velocities)
            self.assertEqual(a['energy_density']*2,3*a['mean_normal'])
            for order in permutations(range(3)):
                b=population(2,3,[tuple(v[i] for i in order) for v in velocities])
                self.assertEqual(b['U'],a['U'])
                self.assertEqual(b['normal'],tuple(a['normal'][i] for i in order))

    def test_anisotropy_and_density_scaling(self):
        a=population(1,2,[(3,0,0),(-3,0,0)])
        self.assertEqual(a['normal'],(9,0,0));self.assertFalse(a['isotropic_second_moment'])
        b=population(1,4,[(3,0,0),(-3,0,0)])
        self.assertEqual(b['normal'][0],a['normal'][0]/2)
        self.assertEqual(b['U'],a['U'])

    def test_contracts(self):
        for m,V,v in [(0,1,[(0,0,0)]),(1,0,[(0,0,0)]),(True,1,[(0,0,0)]),
                      (1,1,[]),(1,1,[(1,0,0)]),(1,1,[(0,0)]),(1,1,[(0.0,0,0)])]:
            with self.assertRaises(ValueError):population(m,V,v)


if __name__=='__main__':unittest.main()
