import unittest
from fractions import Fraction as F
from .experiment import affine,coefficients,model,preco


class AffineTests(unittest.TestCase):
    def test_exact_increment_and_reconstruction(self):
        for a in map(F,(-3,-1,0,2,3)):
            for b in map(F,(-3,0,6)):
                for x in map(F,(-3,-1,0,1,3)):
                    for y in map(F,(-3,-1,0,1,3)):
                        delta=affine(a,b,y)-affine(a,b,x)
                        self.assertEqual(delta,a*(y-x))
                        if x!=y:self.assertEqual(coefficients(x,affine(a,b,x),y,affine(a,b,y)),(a,b))
                        else:
                            with self.assertRaises(ValueError):coefficients(x,affine(a,b,x),y,affine(a,b,y))

    def test_independent_barycentric_interpolation(self):
        for x1 in map(F,(-2,0,1)):
            for x2 in map(F,(-1,2,3)):
                for y1 in map(F,(-3,0,4)):
                    for y2 in map(F,(-3,0,4)):
                        a,b=coefficients(x1,y1,x2,y2)
                        for z in (F(-3),F(0),F(1,2),F(4)):
                            expected=((x2-z)*y1+(z-x1)*y2)/(x2-x1)
                            self.assertEqual(affine(a,b,z),expected)

    def test_domain_zero_and_coincident_points(self):
        self.assertEqual(model(2,6,0,2,1)['zero_kind'],'fora')
        self.assertEqual(model(-2,6,0,2,1)['root'],3)
        self.assertEqual(model(0,0)['zero_kind'],'todos')
        self.assertEqual(model(0,2)['zero_kind'],'nenhum')
        self.assertIsNone(model(x1=1,x2=1)['slope'])
        self.assertIsNone(model(x1=-1,domain=1)['y1'])
        self.assertIsNone(model(x1=-1,domain=1)['slope'])
        for a in (-2,0,2):
            for b in (-2,0,4):
                s=model(a,b)
                if a:self.assertAlmostEqual(affine(a,b,s['root']),0)
                self.assertEqual(s['monotonic'],'crescente' if a>0 else 'decrescente' if a<0 else 'constante')
        self.assertEqual(preco(5),16)
        with self.assertRaises(ValueError):preco(-1)

    def test_units_origin_and_contract(self):
        for a,b in ((F(2),F(6)),(F(-1,2),F(3)),(F(0),F(4))):
            for x in map(F,(-3,0,2)):
                for c in (F(1,1000),F(1000)):
                    self.assertEqual(affine(a/c,b,c*x),affine(a,b,x))
                for h in map(F,(-2,1)):
                    self.assertEqual(affine(a,a*h+b,x-h),affine(a,b,x))
        for args in ((4,1,0,2,0),(2,7,0,2,0),(2,1,4,2,0),(2,1,0,2,2)):
            with self.assertRaises(ValueError):model(*args)
        with self.assertRaises(ValueError):coefficients(1,2,1,4)
