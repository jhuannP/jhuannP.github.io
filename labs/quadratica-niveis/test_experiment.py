import unittest
from fractions import Fraction as F
from itertools import product
from .experiment import model

class QuadraticLevels(unittest.TestCase):
    def test_square_completion_and_extremum(self):
        for a,b,c in product([-2,-1,1,2],range(-4,5),range(-3,4)):
            r=model(a,b,c);h,k=r['vertex']
            for x in [F(i,2) for i in range(-10,11)]:
                value=a*x*x+b*x+c
                self.assertEqual(value,a*(x-h)**2+k)
                self.assertTrue(value>=k if a>0 else value<=k)
                self.assertEqual(a*(h+x)**2+b*(h+x)+c,a*(h-x)**2+b*(h-x)+c)

    def test_all_level_cases(self):
        for a,b,c,l in product(range(-2,3),range(-4,5),range(-3,4),range(-4,5)):
            r=model(a,b,c,l);answer=r['level']
            if a:
                h,k=r['vertex'];radius2=F(l-k,a)
                expected='none' if radius2<0 else 'one' if radius2==0 else 'two'
                self.assertEqual(answer['kind'],expected)
                self.assertEqual(answer['discriminant'],4*a*a*radius2)
            else:self.assertEqual(answer['kind'],'one' if b else 'all' if c==l else 'none')
            for x in answer['roots']:self.assertAlmostEqual(a*x*x+b*x+c,l,delta=1e-10)
            if answer['kind']=='two':
                x,y=answer['roots'];self.assertLess(x,y)
                self.assertAlmostEqual(x+y,-b/a);self.assertAlmostEqual(x*y,(c-l)/a)

    def test_examples_degeneracy_and_window(self):
        self.assertEqual(model()['vertex'],(2,-1));self.assertEqual(model()['zeros']['roots'],(1,3))
        self.assertEqual(model(0,2,1,3)['level']['roots'],(1,))
        self.assertEqual(model(0,0,3,3)['level']['kind'],'all')
        self.assertEqual(model(0,0,3,0)['level']['kind'],'none')
        self.assertIsNone(model(0,1,2)['vertex']);self.assertEqual(model(0,1,2)['image'],'all')
        self.assertEqual(model(0,0,3)['image'],'constant')
        r=model(1,-4,-3,4);self.assertTrue(any(x<r['window'][0] or x>r['window'][1] for x in r['level']['roots']))

    def test_contracts_and_optional_example(self):
        for args in [(3,0,0,0),(1,5,0,0),(1,0,4,0),(1,0,0,5),(True,0,0,0),(1,0,0,.5)]:
            with self.assertRaises(ValueError):model(*args)
        f=lambda x:x*x-4*x+3
        self.assertEqual(min(f(F(i,100)) for i in range(101)),0)  # restricted [0,1], not all R
