import unittest
from datetime import date, timedelta
from fractions import Fraction as Q
from .calendar_jd import jd_ut1

class JulianDateTests(unittest.TestCase):
    def test_published_usno_examples(self):
        self.assertEqual(jd_ut1(1978, 1, 1), Q(4887019, 2))
        self.assertEqual(jd_ut1(1978, 7, 21, 15*3600), Q(19549689, 8))
        self.assertEqual(jd_ut1(1970, 1, 1, 12*3600), 2440588)

    def test_noon_origin_and_day_boundary(self):
        self.assertEqual(jd_ut1(2000, 1, 1), Q(4903089, 2))
        self.assertEqual(jd_ut1(2000, 1, 1, 12*3600), 2451545)
        self.assertEqual(jd_ut1(2000, 1, 1, 6*3600), Q(9806179, 4))
        self.assertEqual(jd_ut1(2000, 1, 2), Q(4903091, 2))
        last = jd_ut1(1999, 12, 31, Q(172799, 2))
        self.assertEqual(jd_ut1(2000, 1, 1)-last, Q(1, 172800))

    def test_gregorian_leap_day(self):
        self.assertEqual(jd_ut1(2000, 3, 1)-jd_ut1(2000, 2, 28), 2)
        self.assertEqual(jd_ut1(2001, 3, 1)-jd_ut1(2001, 2, 28), 1)
        with self.assertRaises(ValueError):jd_ut1(2001, 2, 29)

    def test_all_dates_against_usno_positive_integer_formula(self):
        # USNO 1801..2099 formula, reduced for dates after 1900-02-28.
        # In this domain every division operand is positive: // == truncation.
        current, end = date(1901, 1, 1), date(2099, 12, 31)
        while current <= end:
            y, m, d = current.year, current.month, current.day
            noon = 367*y - 7*(y+(m+9)//12)//4 + 275*m//9 + d + 1721014
            self.assertEqual(jd_ut1(y,m,d), Q(2*noon-1,2), current.isoformat())
            current += timedelta(days=1)

    def test_contracts(self):
        for t in (True, 0.0, '0', None, -1, 86400, Q(172801,2)):
            with self.assertRaises(ValueError):jd_ut1(2000,1,1,t)
        for y,m,d in ((1900,1,1),(2100,1,1),(2000,0,1),(2000,1,32),(True,1,1),(2000,1.,1)):
            with self.assertRaises(ValueError):jd_ut1(y,m,d)

if __name__ == '__main__':unittest.main()
