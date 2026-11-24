"""Verificações finitas de identidades; convergência requer as provas da aula."""
from fractions import Fraction as Q
import unittest


def index(n):
    if type(n) is not int or n < 0: raise ValueError('Índice inteiro não negativo')
    return n


def harmonic(n):
    return sum((Q(1, k) for k in range(1, index(n)+1)), Q(0))


def telescoping(n):
    return sum((Q(1, k*(k+1)) for k in range(1, index(n)+1)), Q(0))


def cut(epsilon, strict=True):
    if isinstance(epsilon, bool) or not isinstance(epsilon, (int, Q)):
        raise TypeError('Use tolerância exata int ou Fraction')
    epsilon = Q(epsilon)
    if epsilon <= 0 or type(strict) is not bool: raise ValueError('Tolerância positiva e strict booleano')
    reciprocal = 1/epsilon
    if strict: return max(1, reciprocal.numerator//reciprocal.denominator)
    ceiling = -(-reciprocal.numerator//reciprocal.denominator)
    return max(1, ceiling-1)


class Checks(unittest.TestCase):
    def test_harmonic_blocks(self):
        for n in range(1, 161):
            direct = sum((Q(1, k) for k in range(n+1, 2*n+1)), Q(0))
            self.assertEqual(direct, harmonic(2*n)-harmonic(n))
            self.assertGreaterEqual(direct, Q(1, 2))
        for k in range(1, 11):
            self.assertGreaterEqual(harmonic(2**k), 1+Q(k, 2))
        self.assertEqual(harmonic(8)-harmonic(4), Q(533, 840))

    def test_telescoping_all_later_tails(self):
        for n in range(1, 101):
            self.assertEqual(telescoping(n), 1-Q(1, n+1))
        for n in range(1, 51):
            for m in range(n+1, n+11):
                tail = telescoping(m)-telescoping(n)
                self.assertEqual(tail, Q(1, n+1)-Q(1, m+1))
                self.assertGreaterEqual(tail, 0)
                self.assertLessEqual(tail, Q(1, n+1))

    def test_minimal_cuts_by_search(self):
        for e in (Q(2), Q(3, 2), Q(1), Q(2, 3), Q(1, 3), Q(1, 100), Q(3, 100)):
            for strict in (True, False):
                accepts = (lambda x: x < e) if strict else (lambda x: x <= e)
                found = next(n for n in range(1, 1001) if accepts(1-telescoping(n)))
                self.assertEqual(cut(e, strict), found)
        self.assertEqual(cut(Q(1, 100)), 100)
        self.assertEqual(cut(Q(1, 100), False), 99)

    def test_subsequences_and_float_stagnation(self):
        total = 0
        for n in range(1, 201):
            total += (-1)**(n+1)
            self.assertEqual(total, n % 2)
        direct = float(10**16)
        for n in range(1, 1001): direct += 1/n
        exact_increase = harmonic(1000)
        self.assertEqual(direct, float(10**16))
        self.assertGreater(exact_increase, 7)
        self.assertLess(exact_increase, 8)
        self.assertGreater(Q(10**16)+exact_increase, Q(10**16))
        print('Float observado:', direct, '; aumento racional:', float(exact_increase))

    def test_contracts(self):
        self.assertEqual(harmonic(0), 0)
        self.assertEqual(telescoping(0), 0)
        for n in (-1, True, .5, float('nan')):
            with self.assertRaises(ValueError): harmonic(n)
        for e in (Q(0), Q(-1)):
            with self.assertRaises(ValueError): cut(e)
        for e in (True, .01):
            with self.assertRaises(TypeError): cut(e)


if __name__ == '__main__':
    print('Bloco5..8:', harmonic(8)-harmonic(4))
    print('Corte estrito:', cut(Q(1, 100)))
    unittest.main()
