from fractions import Fraction as Q
from itertools import product
import unittest
from .ols import fit,mse,Line

class OLSTests(unittest.TestCase):
    def test_original_and_noisy_examples(self):
        self.assertEqual(fit([(0,1),(1,3),(2,5)]),Line(Q(2),Q(1)))
        data=[(0,1),(1,2),(2,2)];line=fit(data)
        self.assertEqual(line,Line(Q(1,2),Q(7,6)))
        self.assertEqual(mse(line,data),Q(1,18))
        self.assertEqual(line.predict(3),Q(8,3))
        self.assertEqual(mse(line,[(3,4)]),Q(16,9))

    def test_normal_equations_and_exact_loss_decomposition(self):
        for ys in product((-1,0,2),repeat=3):
            data=list(zip((0,1,2),ys));line=fit(data)
            residuals=[line.predict(x)-y for x,y in data]
            self.assertEqual(sum(residuals),0)
            self.assertEqual(sum(x*e for (x,y),e in zip(data,residuals)),0)
            for dw,db in product((Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)),repeat=2):
                perturbed=Line(line.slope+dw,line.intercept+db)
                increase=sum((dw*x+db)**2 for x,y in data)/3
                self.assertEqual(mse(perturbed,data)-mse(line,data),increase)

    def test_equivalent_two_by_two_linear_system(self):
        # Direct normal equations via Cramer's rule; no centering in oracle.
        data=[(Q(-3,2),Q(1)),(Q(1,2),Q(4)),(Q(3),Q(-2)),(Q(4),Q(5))]
        n=len(data);sx=sum(x for x,y in data);sy=sum(y for x,y in data)
        sxx=sum(x*x for x,y in data);sxy=sum(x*y for x,y in data)
        determinant=n*sxx-sx*sx
        self.assertEqual(fit(data),Line((n*sxy-sx*sy)/determinant,(sxx*sy-sx*sxy)/determinant))

    def test_units_offsets_and_order(self):
        data=[(0,1),(1,2),(2,2)];line=fit(data)
        for scale in (Q(1,100),Q(2),Q(100)):
            changed=fit([(scale*x+3,y) for x,y in data])
            for x,y in data:self.assertEqual(changed.predict(scale*x+3),line.predict(x))
        self.assertEqual(fit(list(reversed(data))),line)
        self.assertEqual(fit([(x,100*y) for x,y in data]),Line(100*line.slope,100*line.intercept))

    def test_contracts_and_constant_input(self):
        for bad in ([],[(1,)],[(True,1)],[(.1,1)]):
            with self.assertRaises((ValueError,TypeError)):fit(bad)
        for constant in ([(2,1),(2,3)],[(0,1)]):
            with self.assertRaises(ValueError):fit(constant)
        with self.assertRaises(ValueError):mse(Line(Q(1),Q(0)),[])
        data=[(0,1),(1,2)];fit(data);self.assertEqual(data,[(0,1),(1,2)])

if __name__=='__main__':unittest.main()
