"""Exemplos racionais específicos; não é resolvedor de domínio ou raiz geral."""
from fractions import Fraction as Q
import unittest


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise ValueError('Use int ou Fraction')
    return Q(x)


def affine(x):return 2*rational(x)+3

def inverse_affine(y):return (rational(y)-3)/2

def square(x):return rational(x)**2


def reciprocal_shift(x):
    x=rational(x)
    if x==1:raise ValueError('Entrada1 excluída')
    return 1/(x-1)


def compose(outer,inner,x):
    return outer(inner(x))


class Checks(unittest.TestCase):
    def test_order_and_domains(self):
        for x in (Q(k,4) for k in range(-20,21)):
            self.assertEqual(compose(affine,square,x),2*x*x+3)
            self.assertEqual(compose(square,affine,x),(2*x+3)**2)
            if x in (-1,1):
                with self.assertRaises(ValueError):compose(reciprocal_shift,square,x)
            else:self.assertEqual(compose(reciprocal_shift,square,x),1/(x*x-1))
            if x==1:
                with self.assertRaises(ValueError):compose(square,reciprocal_shift,x)
            else:self.assertEqual(compose(square,reciprocal_shift,x),1/(x-1)**2)
        self.assertEqual(compose(affine,square,2),11)
        self.assertEqual(compose(square,affine,2),49)
        self.assertEqual(compose(square,reciprocal_shift,-1),Q(1,4))

    def test_affine_inverse_both_orders(self):
        for x in (Q(k,4) for k in range(-20,21)):
            self.assertEqual(inverse_affine(affine(x)),x)
            self.assertEqual(affine(inverse_affine(x)),x)

    def test_square_restriction_and_reciprocal(self):
        # For rational x, |x| is a nonnegative candidate root of x².
        # No generic sqrt routine or representation of irrational roots is claimed.
        for x in (Q(k,4) for k in range(-20,21)):
            candidate=abs(x)
            self.assertGreaterEqual(candidate,0)
            self.assertEqual(square(candidate),square(x))
            if x<0:self.assertNotEqual(candidate,x)
            else:self.assertEqual(candidate,x)
        self.assertEqual(square(-2),square(2))
        self.assertEqual(square(2),4)
        self.assertEqual(1/square(4),Q(1,16))
        self.assertNotEqual(Q(2),1/square(4))

    def test_contracts(self):
        for x in (True,.5,'1/2',None):
            with self.assertRaises(ValueError):affine(x)
            with self.assertRaises(ValueError):square(x)
        with self.assertRaises(ValueError):reciprocal_shift(1)


if __name__=='__main__':
    print('f(g(2)),g(f(2)):',compose(affine,square,2),compose(square,affine,2))
    unittest.main()
