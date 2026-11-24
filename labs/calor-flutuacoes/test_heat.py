import unittest,itertools,math
from .heat import canonical

class HeatTests(unittest.TestCase):
    def test_fixture(self):
        t=1/math.log(3);a=canonical([0,1],t,[1,3])
        self.assertAlmostEqual(a['probabilities'][1],.5);self.assertAlmostEqual(a['U'],.5)
        self.assertAlmostEqual(a['variance'],.25);self.assertAlmostEqual(a['C_over_kB'],math.log(3)**2/4)
        self.assertEqual(canonical([3],1,[4])['C_over_kB'],0)
    def test_microstates_and_derivative(self):
        E=[0,1,3]
        for g in itertools.product((1,2,3),repeat=3):
            micro=[e for e,n in zip(E,g) for _ in range(n)]
            for t in (.3,1,3):
                a=canonical(E,t,g);b=canonical(micro,t)
                self.assertAlmostEqual(a['U'],b['U']);self.assertAlmostEqual(a['variance'],b['variance'])
                h=1e-5*t
                derivative=(canonical(E,t+h,g)['U']-canonical(E,t-h,g)['U'])/(2*h)
                self.assertAlmostEqual(derivative,a['C_over_kB'],delta=1e-7)
    def test_invariance_and_independent_copies(self):
        a=canonical([0,1,3],2,[1,2,1]);b=canonical([7,8,10],2,[1,2,1]);c=canonical([0,3,9],6,[1,2,1])
        self.assertAlmostEqual(a['variance'],b['variance']);self.assertAlmostEqual(b['U'],a['U']+7)
        self.assertAlmostEqual(c['C_over_kB'],a['C_over_kB']);self.assertAlmostEqual(c['variance'],9*a['variance'])
        t=1/math.log(3)
        for n in range(1,6):
            # Microestados distinguishíveis com degenerescência3 por excitação.
            E=[];g=[]
            for states in itertools.product((0,1),repeat=n):E.append(sum(states));g.append(3**sum(states))
            q=canonical(E,t,g) if n<=4 else None
            # n5 excede30níveis:consolida pelo número de excitações.
            if q is None:q=canonical(range(n+1),t,[math.comb(n,k)*3**k for k in range(n+1)])
            self.assertAlmostEqual(q['U'],n/2);self.assertAlmostEqual(q['variance'],n/4)
            self.assertAlmostEqual(q['C_over_kB'],n*math.log(3)**2/4)
    def test_contracts(self):
        for E,t,g in [([],1,None),([True],1,None),([0],0,None),([0],1,[0]),([0],1,[True]),([0],1,[]),([float('inf')],1,None),([0],1e-8,None)]:
            with self.assertRaises(ValueError):canonical(E,t,g)
