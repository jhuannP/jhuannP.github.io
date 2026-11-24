import unittest
from fractions import Fraction as Q
from math import sqrt
from .clocks import journey,earth_simultaneous


class ClockTests(unittest.TestCase):
    def test_reunion_and_simultaneity(self):
        r=journey([(5,Q(3,5)),(5,Q(-3,5))])
        self.assertEqual((r['elapsed'],r['displacement']),(10,0))
        self.assertEqual(r['proper'],8)
        self.assertEqual(r['events'][1],{'t':5,'x':3,'tau':4})
        out=earth_simultaneous(5,3,Q(3,5));back=earth_simultaneous(5,3,Q(-3,5))
        self.assertEqual((out,back,back-out),(Q(16,5),Q(34,5),Q(18,5)))
        self.assertEqual(out+(back-out)+(10-back),10)

    def test_single_segments_and_reversal(self):
        for beta in (Q(0),Q(3,5),Q(-3,5),Q(4,5),Q(5,13)):
            for dt in (Q(0),Q(1,2),1,5):
                r=journey([(dt,beta)]);s=r['segments'][0]
                self.assertEqual(s['proper_squared'],dt**2*(1-beta**2))
                self.assertAlmostEqual(s['proper']**2,float(s['proper_squared']))
                self.assertLessEqual(r['proper'],float(dt))
                self.assertEqual(journey([(dt,-beta)])['proper'],r['proper'])
        self.assertEqual(journey([(5,0),(5,0)])['proper'],10)

    def test_inertial_comparison_for_finite_cases(self):
        segments=[(dt,beta) for dt in (1,2,5) for beta in (Q(-4,5),Q(-3,5),Q(0),Q(3,5),Q(4,5))]
        for first in segments:
            for second in segments:
                r=journey([first,second]);T=r['elapsed'];X=r['displacement']
                straight=sqrt(float(T*T-X*X))
                self.assertLessEqual(r['proper'],straight+1e-12)

    def test_contracts(self):
        for segments in ([],[(1,1)],[(1,-1)],[(-1,0)],[(True,0)],[(1,.6)],[[1,0]],[(10**7,0)],[(1,0)]*65):
            with self.assertRaises(ValueError):journey(segments)
        with self.assertRaises(ValueError):earth_simultaneous(1,0,True)


if __name__=='__main__':unittest.main()
