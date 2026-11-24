"""Experimentos racionais próprios: varreduras e diagnóstico, sem floats."""
from fractions import Fraction as Q
from itertools import product
import unittest

A = ((Q(4), Q(1)), (Q(1), Q(3)))
B = (Q(1), Q(2))
EXACT = (Q(1, 11), Q(7, 11))


def rational(v):
    if isinstance(v, bool) or not isinstance(v, (int, Q)):
        raise TypeError('Use int ou Fraction; não há conversão silenciosa de float')
    return Q(v)


def data(matrix, b, x):
    n = len(matrix)
    if n == 0 or len(b) != n or len(x) != n or any(len(row) != n for row in matrix):
        raise ValueError('Sistema quadrado não vazio e vetores compatíveis')
    matrix = tuple(tuple(rational(v) for v in row) for row in matrix)
    b, x = tuple(map(rational, b)), tuple(map(rational, x))
    if any(matrix[i][i] == 0 for i in range(n)):
        raise ArithmeticError('Diagonal zero: atualização direta não definida')
    return matrix, b, x


def norm(v):
    return max(map(abs, v), default=Q(0))


def difference(x, y):
    if len(x) != len(y): raise ValueError('Dimensões diferentes')
    return tuple(a-b for a, b in zip(x, y))


def residual(matrix, b, x):
    n = len(matrix)
    if n == 0 or len(b) != n or len(x) != n or any(len(row) != n for row in matrix):
        raise ValueError('Sistema e vetores incompatíveis no resíduo')
    return tuple(rational(bi)-sum(rational(aij)*rational(xj) for aij, xj in zip(row, x))
                 for row, bi in zip(matrix, b))


def step(matrix, b, x, method='jacobi'):
    matrix, b, old = data(matrix, b, x)
    if method not in ('jacobi', 'gauss-seidel'): raise ValueError('Método desconhecido')
    new = list(old)  # Lista independente; old é tupla imutável.
    for i, row in enumerate(matrix):
        sigma = sum(aij*(new[j] if method == 'gauss-seidel' and j < i else old[j])
                    for j, aij in enumerate(row) if j != i)
        new[i] = (b[i]-sigma)/row[i]
    return tuple(new)


def solve(matrix, b, x, method='jacobi', tol=Q(1, 10**8), max_iter=100):
    matrix, b, x = data(matrix, b, x)
    tol = rational(tol)
    if tol <= 0 or type(max_iter) is not int or max_iter < 0:
        raise ValueError('Tolerância positiva; orçamento inteiro não negativo')
    if method not in ('jacobi', 'gauss-seidel'): raise ValueError('Método desconhecido')
    r = norm(residual(matrix, b, x))
    trace = [(x, None, r)]
    if r == 0:
        return dict(x=x, iterations=0, converged=True, reason='solucao-exata-inicial', trace=trace)
    for k in range(1, max_iter+1):
        new = step(matrix, b, x, method)
        delta = norm(difference(new, x))
        r = norm(residual(matrix, b, new))
        trace.append((new, delta, r))
        x = new
        if delta <= tol*(1+norm(x)) and r <= tol*(1+norm(b)):
            return dict(x=x, iterations=k, converged=True, reason='passo-e-residuo', trace=trace)
    return dict(x=x, iterations=max_iter, converged=False, reason='orcamento', trace=trace)


class Checks(unittest.TestCase):
    def test_first_two_sweeps(self):
        j1 = step(A, B, (0, 0)); g1 = step(A, B, (0, 0), 'gauss-seidel')
        self.assertEqual(j1, (Q(1, 4), Q(2, 3)))
        self.assertEqual(g1, (Q(1, 4), Q(7, 12)))
        self.assertEqual(step(A, B, j1), (Q(1, 12), Q(7, 12)))
        self.assertEqual(step(A, B, g1, 'gauss-seidel'), (Q(5, 48), Q(91, 144)))
        self.assertEqual(residual(A, B, g1), (Q(-7, 12), 0))

    def test_affine_error_and_bounds(self):
        count = 0
        for i, j in product(range(-3, 4), repeat=2):
            for method, q in (('jacobi', Q(1, 3)), ('gauss-seidel', Q(1, 4))):
                x = (Q(i, 2), Q(j, 2))
                for _ in range(8):
                    error = difference(x, EXACT)
                    expected = (-error[1]/4, -error[0]/3) if method == 'jacobi' else (-error[1]/4, error[1]/12)
                    new = step(A, B, x, method)
                    new_error = difference(new, EXACT)
                    self.assertEqual(new_error, expected)
                    self.assertLessEqual(norm(new_error), q*norm(error))
                    delta = norm(difference(new, x))
                    self.assertLessEqual(norm(new_error), q*delta/(1-q))
                    self.assertLessEqual(norm(new_error), Q(5, 11)*norm(residual(A, B, new)))
                    x = new; count += 1
        self.assertEqual(count, 784)

    def test_non_dominant_convergent_case(self):
        matrix = ((1, 2), (Q(1, 10), 1)); b = (3, Q(11, 10)); exact = (1, 1)
        for i, j in product(range(-3, 4), repeat=2):
            x = (Q(i), Q(j))
            for _ in range(5):
                twice = step(matrix, b, step(matrix, b, x))
                self.assertEqual(difference(twice, exact), tuple(e/5 for e in difference(x, exact)))
                x = twice

    def test_divergent_trace_and_budget(self):
        matrix = ((1, 2), (2, 1)); b = (1, 1); x = (0, 0)
        for k in range(1, 11):
            x = step(matrix, b, x)
            y = Q(1, 3)-Q((-2)**k, 3)
            self.assertEqual(x, (y, y))
        result = solve(matrix, b, (0, 0), max_iter=10)
        self.assertFalse(result['converged'])
        self.assertEqual(result['reason'], 'orcamento')
        # Orçamento curto também ocorre em um sistema convergente.
        self.assertFalse(solve(A, B, (0, 0), max_iter=1)['converged'])

    def test_stop_and_preserve_inputs(self):
        matrix = [[4, 1], [1, 3]]; b = [1, 2]; x = [0, 0]
        before = ([row[:] for row in matrix], b[:], x[:])
        for method in ('jacobi', 'gauss-seidel'):
            result = solve(matrix, b, x, method)
            self.assertTrue(result['converged'])
            self.assertEqual(result['reason'], 'passo-e-residuo')
            _, delta, r = result['trace'][-1]
            self.assertLessEqual(delta, Q(1, 10**8)*(1+norm(result['x'])))
            self.assertLessEqual(r, Q(1, 10**8)*(1+norm(b)))
            self.assertLess(norm(difference(result['x'], EXACT)), Q(1, 10**7))
        self.assertEqual((matrix, b, x), before)
        self.assertTrue(solve(A, B, EXACT, max_iter=0)['converged'])
        self.assertEqual(solve(A, B, (0, 0), max_iter=0)['reason'], 'orcamento')

    def test_contracts(self):
        for matrix, b, x in (([], [], []), ([[1, 2]], [1], [0]), ([[1]], [1, 2], [0])):
            with self.assertRaises(ValueError): step(matrix, b, x)
        with self.assertRaises(ArithmeticError): step(((0, 1), (1, 0)), (1, 1), (0, 0))
        with self.assertRaises(TypeError): step(A, B, (0., 0))
        with self.assertRaises(TypeError): step(A, B, (True, 0))
        with self.assertRaises(ValueError): solve(A, B, (0, 0), method='outro')
        for bad in (-1, True, Q(1, 2)):
            with self.assertRaises(ValueError): solve(A, B, (0, 0), max_iter=bad)
        with self.assertRaises(ValueError): solve(A, B, (0, 0), tol=0)
        with self.assertRaises(ValueError): residual(A, B, (0,))
        self.assertEqual(residual(((0, 1), (1, 0)), (1, 1), (0, 0)), (1, 1))


if __name__ == '__main__':
    for method in ('jacobi', 'gauss-seidel'):
        result = solve(A, B, (0, 0), method)
        print(method, 'passos:', result['iterations'], 'motivo:', result['reason'])
    unittest.main()
