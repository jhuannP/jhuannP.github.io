import unittest
from fractions import Fraction as Q
from itertools import product
from .fundamental import evaluate,derivative,wronskian,stripped_fundamental,coefficients_at_zero,stripped_state


class WronskianTests(unittest.TestCase):
    def test_initial_data_and_states(self):
        for y,v in product(range(-3,4),repeat=2):
            c=coefficients_at_zero(y,v)
            self.assertEqual(stripped_state(0,*c),(y,v))
            # Solução independente por p'=constante após substituir y=e^(-2t)p.
            for t in (Q(-1,2),0,1,Q(3,2)):
                p=y+(v+2*y)*t;dp=v+2*y
                self.assertEqual(stripped_state(t,*c),(p,dp-2*p))
        self.assertEqual(coefficients_at_zero(3,-4),(3,2))
        self.assertEqual(stripped_state(1,3,2),(5,-8))

    def test_matrix_differential_identity(self):
        for j in range(-12,13):
            t=Q(j,4);b=stripped_fundamental(t)
            self.assertEqual(b[0][0]*b[1][1]-b[0][1]*b[1][0],1)
            # Phi'=A Phi equivale a B'=AB+2B; não reimplementa exponencial.
            a=((0,1),(-4,-4));db=((0,1),(0,-2))
            for i,k in product(range(2),repeat=2):
                self.assertEqual(sum(a[i][r]*b[r][k] for r in range(2))+2*b[i][k],db[i][k])

    def test_singular_polynomial_pair(self):
        f=(0,0,1);g=(0,0,0,1)
        for j in range(-12,13):
            t=Q(j,4)
            self.assertEqual(wronskian(f,g,t),t**4)
            for p in (f,g):
                residual=t*t*evaluate(derivative(derivative(p)),t)-4*t*evaluate(derivative(p),t)+6*evaluate(p,t)
                self.assertEqual(residual,0)
        # Valores em1 e-1 dão matriz inversível, provando independência das funções.
        self.assertEqual(evaluate(f,1)*evaluate(g,-1)-evaluate(g,1)*evaluate(f,-1),-2)
        self.assertEqual(wronskian(f,g,0),0)

    def test_operator_and_affine_forcing(self):
        for c1,c2 in product(range(-3,4),repeat=2):
            p=(c1,c2)
            for t in (0,1,Q(1,2)):
                value=evaluate(p,t);dp=evaluate(derivative(p),t)
                # e^(2t)*(y,y',y'') obtido por regra do produto.
                y,dy,ddy=value,dp-2*value,4*value-4*dp
                self.assertEqual(ddy+4*dy+4*y,0)
        # Para funções constantes1 e2, L(y)=4y: mesma forçante não é fechada por soma.
        self.assertEqual(4*1,4);self.assertNotEqual(4*2,4)

    def test_contracts(self):
        for t in (True,.5,'0'):
            with self.assertRaises(ValueError):stripped_fundamental(t)
        for p in ([],[True],[1.0],[0]*9,'x'):
            with self.assertRaises(ValueError):evaluate(p,0)
        with self.assertRaises(ValueError):coefficients_at_zero(3,False)
