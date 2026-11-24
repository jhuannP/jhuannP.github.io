import unittest,math
from .mix import mix,R

class MixTests(unittest.TestCase):
    def test_fixture_endpoints(self):
        m=mix(1,1)
        self.assertAlmostEqual(m['G'],-2*R*300*math.log(2))
        self.assertAlmostEqual(m['S'],2*R*math.log(2))
        self.assertAlmostEqual((mix(2,1)['G']-m['G'])/(R*300),2*math.log(2/3)+math.log(1/3)+2*math.log(2))
        self.assertIsNone(mix(0,2)['muA']);self.assertEqual(mix(0,2)['G'],0)
        self.assertEqual(mix(2,0)['muA'],0)
    def test_euler_scaling_and_symmetry(self):
        for a in range(1,11):
            for b in range(1,11):
                m=mix(a,b);q=mix(b,a);s=mix(3*a,3*b)
                self.assertAlmostEqual(m['G'],a*m['muA']+b*m['muB'])
                self.assertAlmostEqual(m['G'],q['G']);self.assertAlmostEqual(s['G'],3*m['G'])
                self.assertAlmostEqual(s['muA'],m['muA']);self.assertLess(m['G'],0)
                self.assertAlmostEqual(m['G'],-300*m['S'])
    def test_partial_derivatives_and_convexity(self):
        for a in (0.5,1,2,4):
            for b in (0.5,1,3):
                eps=1e-4;m=mix(a,b)
                fd=(mix(a+eps,b)['G']-mix(a-eps,b)['G'])/(2*eps)
                self.assertAlmostEqual(fd,m['muA'],delta=2e-5)
        # Curva molar convexa: valor na média não excede média dos valores.
        for i in range(1,10):
            for j in range(1,10):
                x,y=i/10,j/10;z=(x+y)/2
                self.assertLessEqual(mix(z,1-z)['h'],(mix(x,1-x)['h']+mix(y,1-y)['h'])/2+1e-14)
    def test_contracts(self):
        for args in [(0,0,300),(-1,2,300),(1,1,0),(True,1,300),(1,1,float('nan')),(1,float('inf'),300),(1e308,1e308,300)]:
            with self.assertRaises(ValueError):mix(*args)
