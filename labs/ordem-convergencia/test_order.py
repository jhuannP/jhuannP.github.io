import unittest
from fractions import Fraction as Q
from math import factorial
from .order import diagnostics,power_errors,mesh_comparison


class OrderTests(unittest.TestCase):
    def test_linear_and_quadratic_closed_forms(self):
        linear=power_errors(Q(1,2),Q(1,2),1,12)
        self.assertEqual(linear,tuple(Q(1,2**(n+1)) for n in range(13)))
        self.assertEqual(diagnostics(linear,0)['ratios'],(Q(1,2),)*12)
        quadratic=power_errors(Q(1,2),1,2,8)
        self.assertEqual(quadratic,tuple(Q(1,2**(2**n)) for n in range(9)))
        self.assertEqual(diagnostics(quadratic,0,2)['ratios'],(Q(1),)*8)

    def test_superlinear_not_quadratic_and_sublinear(self):
        errors=tuple(Q(1,factorial(n+1)) for n in range(10))
        d=diagnostics(errors,0)
        self.assertEqual(d['ratios'],tuple(Q(1,n+2) for n in range(9)))
        q=diagnostics(errors,0,2)['ratios']
        self.assertEqual(q,tuple(Q(factorial(n+1),n+2) for n in range(9)))
        self.assertGreater(q[-1],q[2])
        algebraic=tuple(Q(1,n+1) for n in range(10))
        self.assertEqual(diagnostics(algebraic,0)['ratios'],tuple(Q(n+1,n+2) for n in range(9)))

    def test_steps_do_not_prove_correct_target(self):
        xs=tuple(1+Q(1,2**n) for n in range(10))
        d=diagnostics(xs,0)
        self.assertEqual(d['steps'],tuple(Q(1,2**(n+1)) for n in range(9)))
        self.assertTrue(all(e>1 for e in d['errors']))
        self.assertEqual(diagnostics(xs,1)['errors'],tuple(Q(1,2**n) for n in range(10)))

    def test_translation_scale_and_zero(self):
        errors=power_errors(Q(1,2),1,2,4)
        shifted=tuple(7+3*e for e in errors)
        self.assertEqual(diagnostics(shifted,7,2)['ratios'],(Q(1,3),)*4)
        self.assertEqual(diagnostics([2,1,1],1)['ratios'],(Q(0),None))
        self.assertEqual(power_errors(1,1,2,3),(1,1,1,1))
        self.assertEqual(power_errors(1,2,1,3),(1,2,4,8))

    def test_mesh_order_and_error_floor(self):
        for p in range(1,5):
            for n in range(1,12):
                r=mesh_comparison(Q(1,2**n),p,coefficient=3)
                self.assertEqual(r['ratio'],2**p)
        floor=Q(1,1024)
        r=mesh_comparison(Q(1,32),floor=floor)
        self.assertEqual(r,dict(coarse=Q(1,512),fine=Q(5,4096),ratio=Q(8,5)))
        ratios=[mesh_comparison(Q(1,2**n),floor=floor)['ratio'] for n in range(1,16)]
        self.assertTrue(all(a>b>1 for a,b in zip(ratios,ratios[1:])))

    def test_identical_finite_prefix_can_hide_stagnation(self):
        prefix=power_errors(Q(1,2),Q(1,2),1,5)
        continued=prefix+(prefix[-1]/2,prefix[-1]/4)
        frozen=prefix+(prefix[-1],prefix[-1])
        self.assertEqual(diagnostics(continued[:6],0),diagnostics(frozen[:6],0))
        self.assertEqual(diagnostics(frozen,0)['ratios'][-2:],(1,1))
        self.assertEqual(diagnostics(continued,0)['ratios'][-2:],(Q(1,2),Q(1,2)))

    def test_contracts(self):
        for xs,target,p in [([1],0,1),([True,1],0,1),([1.,0],0,1),([1,2],False,1),([1,2],0,True),([1,2],0,0)]:
            with self.assertRaises(ValueError):diagnostics(xs,target,p)
        for args in [(0,1,1,1),(1,0,1,1),(1,1,1,-1),(1,1,2,True)]:
            with self.assertRaises(ValueError):power_errors(*args)
        for args in [(0,2,1,0),(1,2,1,-1),(1,False,1,0),(1,2,0,0)]:
            with self.assertRaises(ValueError):mesh_comparison(*args)

if __name__=='__main__':unittest.main()
