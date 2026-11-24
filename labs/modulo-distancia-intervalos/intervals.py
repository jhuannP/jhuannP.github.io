"""Soluções de |Ax+B| comparado a r,com coeficientes racionais exatos.
Intervalo=(limite inferior,superior,inclui inferior,inclui superior).
None denota ausência de limite;um ponto tem dois extremos iguais fechados.
"""
from fractions import Fraction as Q
from itertools import product
import operator
import unittest

OPS={'<':operator.lt,'<=':operator.le,'>':operator.gt,'>=':operator.ge,'=':operator.eq}
ALL=((None,None,False,False),)


def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise TypeError('Use int ou Fraction')
    return Q(x)


def solve(a,b,r,op):
    a,b,r=map(rational,(a,b,r))
    if op not in OPS:raise ValueError('Comparador não suportado')
    if a==0:return ALL if OPS[op](abs(b),r) else ()
    if r<0:return ALL if op in ('>','>=') else ()
    center=-b/a
    if r==0:
        if op=='<':return ()
        if op=='>=':return ALL
        if op in ('=','<='):return ((center,center,True,True),)
        return ((None,center,False,False),(center,None,False,False))
    radius=r/abs(a);low,high=center-radius,center+radius
    if op=='=':return ((low,low,True,True),(high,high,True,True))
    if op in ('<','<='):
        closed=op=='<='
        return ((low,high,closed,closed),)
    closed=op=='>='
    return ((None,low,False,closed),(high,None,closed,False))


def contains(intervals,x):
    x=rational(x)
    for low,high,lc,hc in intervals:
        lower=low is None or x>low or (lc and x==low)
        upper=high is None or x<high or (hc and x==high)
        if lower and upper:return True
    return False


class Checks(unittest.TestCase):
    def test_parameter_grid_against_original(self):
        cases=points=0
        for a,b,r,op in product(range(-3,4),range(-3,4),range(-2,4),OPS):
            solution=solve(a,b,r,op)
            for i in range(-24,25):
                x=Q(i,4)
                self.assertEqual(contains(solution,x),OPS[op](abs(a*x+b),r))
                points+=1
            cases+=1
        self.assertEqual(cases,1470)
        self.assertEqual(points,72030)
        print('Configurações:',cases,';comparações exatas:',points)

    def test_rational_boundaries(self):
        # |3x+1| comparado a2 tem fronteiras−1 e1/3.
        boundaries=(Q(-1),Q(1,3))
        for op in OPS:
            solution=solve(3,1,2,op)
            for edge in boundaries:
                for x in (edge-Q(1,100),edge,edge+Q(1,100)):
                    self.assertEqual(contains(solution,x),OPS[op](abs(3*x+1),2))
        self.assertEqual(solve(-3,6,6,'<='),((Q(0),Q(4),True,True),))
        self.assertEqual(solve(1,-3,2,'='),((Q(1),Q(1),True,True),(Q(5),Q(5),True,True)))

    def test_zero_and_negative_thresholds(self):
        self.assertEqual(solve(0,2,2,'<='),ALL)
        self.assertEqual(solve(0,2,2,'<'),())
        self.assertEqual(solve(1,-3,0,'<'),())
        self.assertEqual(solve(1,-3,0,'<='),((Q(3),Q(3),True,True),))
        self.assertEqual(solve(1,-3,0,'>='),ALL)
        self.assertEqual(solve(1,-3,-2,'<='),())
        self.assertEqual(solve(1,-3,-2,'>'),ALL)

    def test_triangle_and_extraneous_candidate(self):
        for u,v in product((Q(i,4) for i in range(-20,21)),repeat=2):
            self.assertLessEqual(abs(u+v),abs(u)+abs(v))
        x=Q(-1)
        self.assertEqual((x+2)**2,x*x)
        self.assertNotEqual(abs(x+2),x)
        self.assertEqual(abs(Q(1)-2),Q(1))

    def test_contracts(self):
        for value in (True,.5,None,'1/2'):
            with self.assertRaises(TypeError):solve(value,0,1,'<=')
        with self.assertRaises(ValueError):solve(1,0,1,'!=')


if __name__=='__main__':
    print('|−3x+6|≤6:',solve(-3,6,6,'<='))
    unittest.main()
