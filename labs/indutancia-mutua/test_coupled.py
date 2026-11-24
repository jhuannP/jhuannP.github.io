import unittest
from fractions import Fraction as Q
from itertools import product
from .coupled import coefficients,flux,energy,voltages

class Tests(unittest.TestCase):
    def test_original_fixture_and_open_port(self):
        self.assertEqual(energy(4,9,3,[2,-1]),Q(13,2))
        self.assertEqual(flux(4,9,3,[2,-1]),(5,-3))
        self.assertEqual(voltages(4,9,3,[2,0]),(8,6))
        self.assertEqual(energy(4,9,0,[2,-1]),Q(25,2))
    def test_completed_square_and_orientation(self):
        count=0
        for m in (-6,-3,-1,0,1,3,6):
            for i,j in product(range(-3,4),repeat=2):
                u=energy(4,9,m,[i,j]);independent=2*(Q(i)+Q(m,4)*j)**2+(Q(9)-Q(m*m,4))*j*j/2
                self.assertEqual(u,independent);self.assertGreaterEqual(u,0)
                self.assertEqual(energy(4,9,-m,[i,-j]),u)
                self.assertEqual(energy(4,9,m,[2*i,2*j]),4*u);count+=1
        self.assertEqual(count,343)
        self.assertEqual(energy(4,9,6,[3,-2]),0) # limite ideal semidefinido
    def test_work_along_distinct_paths_and_gradient(self):
        def work(start,end):
            di,dj=(Q(end[k])-Q(start[k]) for k in range(2))
            v=voltages(4,9,3,[di,dj]) # rampa de1 segundo
            return sum(v[k]*(Q(start[k])+Q(end[k]))/2 for k in range(2))
        for i,j in product(range(-2,3),repeat=2):
            expected=energy(4,9,3,[i,j]);direct=work([0,0],[i,j])
            first=work([0,0],[i,0])+work([i,0],[i,j])
            second=work([0,0],[0,j])+work([0,j],[i,j])
            self.assertEqual(direct,expected);self.assertEqual(first,expected);self.assertEqual(second,expected)
            h=Q(1,100);grad=[]
            for k in range(2):
                plus=[Q(i),Q(j)];minus=plus.copy();plus[k]+=h;minus[k]-=h
                grad.append((energy(4,9,3,plus)-energy(4,9,3,minus))/(2*h))
            self.assertEqual(tuple(grad),flux(4,9,3,[i,j]))
    def test_contracts(self):
        for a,b,m in [(0,9,3),(4,-1,0),(4,9,7),(4,9,-7),(True,9,0),(4.,9,3),(1001,9,0)]:
            with self.assertRaises(ValueError):coefficients(a,b,m)
        for pair in ([1],[1,2,3],[101,0],[True,0],[.5,0]):
            with self.assertRaises(ValueError):energy(4,9,3,pair)
        with self.assertRaises(ValueError):voltages(4,9,3,[1001,0])
