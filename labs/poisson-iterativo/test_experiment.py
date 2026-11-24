import unittest
from math import sin,cos,pi
from .experiment import solve
from numerics4 import poisson_2d

class PoissonIterationTests(unittest.TestCase):
    def test_dense_reference_and_exact_discrete_mode(self):
        for n in (4,8):
            q=solve(n,1000,'gs')
            dense=poisson_2d(n,lambda x,y:2*pi*pi*sin(pi*x)*sin(pi*y))
            for i in range(n+1):
                for j in range(n+1):
                    self.assertAlmostEqual(q['discrete'][i][j],dense[i][j],places=11)
                    self.assertAlmostEqual(q['u'][i][j],dense[i][j],places=11)
            self.assertLess(q['residual'],1e-10)

    def test_jacobi_independent_modal_recurrence(self):
        for n in (4,8,16):
            rho=cos(pi/n)
            for k in (0,1,10,40):
                q=solve(n,k)
                self.assertAlmostEqual(q['algebraic'],q['factor']*rho**k,places=11)
                self.assertAlmostEqual(q['residual'],2*pi*pi*rho**k,places=10)
                self.assertAlmostEqual(q['u'][n//2][n//2],q['factor']*(1-rho**k),places=11)

    def test_two_errors_boundaries_and_refinement(self):
        errors=[]
        for n in (4,8,16,32):
            q=solve(n,0);errors.append(q['grid_error'])
            self.assertGreater(q['grid_error'],0)
            self.assertAlmostEqual(q['total'],1)
        for i in range(3):self.assertTrue(3.7<errors[i]/errors[i+1]<4.3)
        for method in ('jacobi','gs'):
            q=solve(8,60,method)
            self.assertLessEqual(q['total'],q['algebraic']+q['grid_error']+1e-14)
            self.assertTrue(all(v==0 for v in q['u'][0]+q['u'][-1]))
            self.assertTrue(all(row[0]==row[-1]==0 for row in q['u']))
        self.assertLess(solve(8,40,'gs')['algebraic'],solve(8,40,'jacobi')['algebraic'])

    def test_contract_and_one_sweep_ordering(self):
        j=solve(4,1,'jacobi');g=solve(4,1,'gs')
        self.assertAlmostEqual(j['u'][1][1],g['u'][1][1])
        self.assertGreater(g['u'][1][2],j['u'][1][2])
        for args in ((True,0),(3,1),(34,1),(4,-1),(4,True),(4,5001),(4,0,'other')):
            with self.assertRaises(ValueError):solve(*args)
