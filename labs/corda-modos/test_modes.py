import unittest
from math import pi,sin
from fractions import Fraction as Q
from .modes import spectrum,profile

class Tests(unittest.TestCase):
    def test_fixture_and_counts(self):
        m=spectrum(Q(6,5),48,3)
        self.assertEqual(m['wavelength'],Q(4,5));self.assertEqual(m['frequency'],60)
        self.assertEqual(m['nodes'],(0,Q(2,5),Q(4,5),Q(6,5)))
        self.assertEqual(m['antinodes'],(Q(1,5),Q(3,5),1))
        self.assertEqual(spectrum(Q(6,5),48,1)['frequency'],20)
    def test_nodes_antinodes_time_and_adjacent_phase(self):
        A=Q(1,10000)
        for n in range(1,13):
            m=spectrum(2,30,n);period=1/m['frequency']
            for x in m['nodes']:
                for t in (0,period/8,period/4,period/2):
                    self.assertAlmostEqual(profile(2,30,n,x,t,A),0,places=13)
            for j,x in enumerate(m['antinodes']):
                self.assertAlmostEqual(profile(2,30,n,x,0,A),(-1)**j*2*float(A))
                self.assertAlmostEqual(profile(2,30,n,x,period/4,A),0,places=13)
                self.assertAlmostEqual(profile(2,30,n,x,period/2,A),-profile(2,30,n,x,0,A))
                self.assertAlmostEqual(profile(2,30,n,x,period,A),profile(2,30,n,x,0,A))
    def test_traveling_sum_and_scaling(self):
        count=0;A=Q(1,10000);L=Q(6,5);v=48
        for n in (1,2,3,5):
            m=spectrum(L,v,n);period=1/m['frequency']
            for j in range(25):
                x=L*j/24
                for k in range(9):
                    t=period*k/8
                    # Oráculo pela soma de ondas, não produto seno/cosseno.
                    a=2*pi*float(x/m['wavelength']);b=2*pi*float(m['frequency']*t)
                    direct=float(A)*(sin(a-b)+sin(a+b))
                    self.assertAlmostEqual(profile(L,v,n,x,t,A),direct,places=13);count+=1
            self.assertEqual(spectrum(2*L,v,n)['frequency'],m['frequency']/2)
            self.assertEqual(spectrum(L,2*v,n)['frequency'],2*m['frequency'])
            self.assertEqual(len(m['nodes']),n+1);self.assertEqual(len(m['antinodes']),n)
        self.assertEqual(count,900)
    def test_contracts(self):
        for L,v,n in [(0,48,3),(1,0,3),(11,48,3),(1,1001,3),(1,48,0),(1,48,21),
                      (1,48,True),(1,48,3.),(1.2,48,3),(True,48,3)]:
            with self.assertRaises(ValueError):spectrum(L,v,n)
        for x,t,A in [(-1,0,Q(1,1000)),(2,0,Q(1,1000)),(0,-1,Q(1,1000)),
                      (0,11,Q(1,1000)),(0,0,0),(0,0,Q(1,10)),(.2,0,Q(1,1000))]:
            with self.assertRaises(ValueError):profile(1,48,3,x,t,A)
