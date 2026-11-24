import copy,itertools,random,unittest
from fractions import Fraction as Q
from .exact import solve,residual,small_pivot_demo
from .float_solver import gauss_pivoteamento,residuo

class GaussianTests(unittest.TestCase):
    def test_two_by_two_against_cramer(self):
        count=0
        for a,b,c,d in itertools.product(range(-2,3),repeat=4):
            det=a*d-b*c
            if not det:continue
            A=[[a,b],[c,d]];rhs=[3,-1];before=copy.deepcopy(A)
            expected=[Q(3*d+b,det),Q(-a-3*c,det)]
            result=solve(A,rhs)
            self.assertEqual(result['x'],expected);self.assertEqual(A,before)
            self.assertEqual(residual(A,expected,rhs),[0,0])
            float_x=gauss_pivoteamento(A,rhs)
            for x,y in zip(float_x,expected):self.assertAlmostEqual(x,float(y),places=12)
            for step in result['steps']:
                for _,m in step['multipliers']:self.assertLessEqual(abs(m),1)
            count+=1
        self.assertGreater(count,400)

    def test_constructed_nonsingular_three_by_three(self):
        rng=random.Random(20261027)
        # Parta de identidade; operações invertíveis geram matrizes não singulares.
        for _ in range(40):
            A=[[int(i==j) for j in range(3)] for i in range(3)]
            for step in range(8):
                i,j=rng.sample(range(3),2);m=rng.choice((-2,-1,1,2))
                A[i]=[a+m*b for a,b in zip(A[i],A[j])]
            x=[Q(rng.randrange(-5,6),3) for _ in range(3)]
            b=[sum(a*z for a,z in zip(row,x)) for row in A]
            result=solve(A,b);self.assertEqual(result['x'],x)
            y=gauss_pivoteamento(A,b)
            for actual,expected in zip(y,x):self.assertAlmostEqual(actual,float(expected),places=9)

    def test_trace_and_deterministic_ties(self):
        r=solve([[1,2],[3,5]],[5,13])
        self.assertEqual(r['steps'][0]['pivot_row'],1)
        self.assertEqual(r['steps'][0]['multipliers'],((1,Q(1,3)),))
        self.assertEqual(r['rhs'],[13,Q(2,3)])
        self.assertEqual(solve([[-2,1],[2,3]],[0,1])['steps'][0]['pivot_row'],0)

    def test_small_pivot_and_residual_not_error(self):
        d=small_pivot_demo();self.assertEqual(d['naive'],[0.,1.])
        x=gauss_pivoteamento(d['A'],d['b']);self.assertEqual(x,[1.,1.])
        self.assertEqual(residuo(d['A'],x,d['b']),[0.,0.])
        # Resíduo float zero não implica igualdade racional exata.
        exact_r=residual(d['A'],[Q.from_float(v) for v in x],d['b'])
        self.assertEqual(exact_r,[-Q(1,2**60),0])
        delta=Q(1,1000);A=[[1,1],[1,1+delta]];b=[2,2+delta]
        self.assertEqual(solve(A,b)['x'],[1,1])
        self.assertEqual(residual(A,[2,0],b),[0,delta])

    def test_contracts_and_singular_cases(self):
        for A,b in (([],[]),([[1,2]],[1]),([[1]],[])):
            with self.assertRaises(ValueError):solve(A,b)
        for x in (True,1.,'1'):
            with self.assertRaises(ValueError):solve([[x]],[1])
        for b in ([3,6],[3,7]):
            with self.assertRaises(ArithmeticError):solve([[1,2],[2,4]],b)
        for bad in (True,float('nan'),float('inf')):
            with self.assertRaises(ValueError):gauss_pivoteamento([[bad]],[1])
