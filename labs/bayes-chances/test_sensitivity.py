from fractions import Fraction as F
import unittest
from .experiment import update

class Sensitivity(unittest.TestCase):
    def test_monotonicity_and_direction(self):
        grid=[F(i,10) for i in range(11)]
        for p in grid:
            for b in grid:
                vals=[update(p,a,b)['posterior'] for a in grid]
                vals=[v for v in vals if v is not None]
                self.assertEqual(vals,sorted(vals))
        for a in grid:
            for b in grid:
                vals=[update(p,a,b)['posterior'] for p in grid]
                vals=[v for v in vals if v is not None]
                self.assertEqual(vals,sorted(vals))
                for p in grid[1:-1]:
                    z=update(p,a,b)['posterior']
                    if z is not None:self.assertEqual((z>p)-(z<p),(a>b)-(a<b))
            for p in grid:
                vals=[update(p,a,b)['posterior'] for b in grid]
                vals=[v for v in vals if v is not None]
                self.assertEqual(vals,sorted(vals,reverse=True))

    def test_rectangle_bounds_by_enumeration(self):
        lower=F(7,64);upper=F(9,13)
        self.assertEqual(update(F(5,100),F(70,100),F(30,100))['posterior'],lower)
        self.assertEqual(update(F(20,100),F(90,100),F(10,100))['posterior'],upper)
        for pi in range(5,21):
            for ai in range(70,91):
                for bi in range(10,31):
                    value=update(F(pi,100),F(ai,100),F(bi,100))['posterior']
                    self.assertLessEqual(lower,value);self.assertLessEqual(value,upper)

    def test_boundaries_are_not_filled_by_continuity(self):
        self.assertIsNone(update(0,1,0)['posterior'])
        self.assertEqual(update(F(1,1000000),1,0)['posterior'],1)
        self.assertIsNone(update(1,0,1)['posterior'])
        self.assertEqual(update(F(999999,1000000),0,1)['posterior'],0)
        for p in [F(i,10) for i in range(11)]:
            self.assertIsNone(update(p,0,0)['posterior'])
