"""Equilíbrio planar didático: cálculo racional, sem deformação do corpo."""
from fractions import Fraction as Q
from itertools import product
import unittest


def rational(value):
    if isinstance(value,bool) or not isinstance(value,(int,Q)):
        raise ValueError('Use int ou Fraction exatos')
    return Q(value)


def torque(x,y,fx,fy):
    x,y,fx,fy=map(rational,(x,y,fx,fy))
    return x*fy-y*fx


def reactions(length,load,position,weight=0):
    length,load,position,weight=map(rational,(length,load,position,weight))
    if length<=0 or load<0 or weight<0:
        raise ValueError('L>0, P>=0, W>=0')
    right=(load*position+weight*length/2)/length
    left=load+weight-right
    # Negative values are returned for model diagnosis, not clipped to zero.
    return left,right


class Checks(unittest.TestCase):
    def test_examples_and_contact(self):
        self.assertEqual(torque(-2,0,0,-30),60)
        self.assertEqual(torque(3,0,0,-20),-60)
        self.assertEqual(reactions(3,120,1,60),(110,70))
        self.assertEqual(reactions(3,120,4),(Q(-40),Q(160)))
        self.assertLess(reactions(3,120,4)[0],0)
        self.assertEqual(torque(2,0,10,0),0)

    def test_balances_about_multiple_origins(self):
        # 300 loading cases, with four independent moment origins each.
        for length,load,fraction,weight in product(range(1,6),(0,10,60,120),
                                                   (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)),(0,20,60)):
            position=length*fraction
            left,right=reactions(length,load,position,weight)
            self.assertEqual(left+right-load-weight,0)
            self.assertGreaterEqual(left,0);self.assertGreaterEqual(right,0)
            forces=[(Q(0),left),(Q(length),right),(position,-load),(Q(length,2),-weight)]
            for origin in (-length,0,length,2*length):
                self.assertEqual(sum(torque(x-origin,0,0,fy) for x,fy in forces),0)

    def test_origin_shift_identity_and_couple(self):
        for x,y,fx,fy in product(range(-2,3),repeat=4):
            a,b=Q(3,2),Q(-1,2)
            self.assertEqual(torque(x-a,y-b,fx,fy),torque(x,y,fx,fy)-a*fy+b*fx)
        # Opposite forces with noncoincident lines: net force zero, torque not zero.
        self.assertEqual(10-10,0)
        self.assertEqual(torque(0,0,0,10)+torque(1,0,0,-10),-10)

    def test_contracts(self):
        for args in [(0,1,0,0),(1,-1,0,0),(1,1,0,-1),(True,1,0,0),(1,1.0,0,0)]:
            with self.assertRaises(ValueError):reactions(*args)
        with self.assertRaises(ValueError):torque(0,0,0,1.0)


if __name__=='__main__':
    print('Reações A/B, N:',reactions(3,120,1,60))
    print('Extensão formal fora do apoio:',reactions(3,120,4))
    unittest.main()
