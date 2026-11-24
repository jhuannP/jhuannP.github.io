import unittest
from fractions import Fraction as Q
from math import comb
from .experiment import kernel, distribution

class WrightFisherTests(unittest.TestCase):
    def test_exact_small_chain_and_known_values(self):
        self.assertEqual(distribution(1,1,1)['distribution'],[.25,.5,.25])
        self.assertEqual(distribution(1,1,2)['distribution'],[.375,.25,.375])
        # Referência racional independente, sem usar o kernel de ponto flutuante.
        for N in (1,2,3):
            M=2*N
            P=[[Q(comb(M,j)*i**j*(M-i)**(M-j), M**M) for j in range(M+1)] for i in range(M+1)]
            for k in range(M+1):
                q=[Q(i==k) for i in range(M+1)]
                for t in range(5):
                    actual=distribution(N,k,t)['distribution']
                    for a,b in zip(actual,q):self.assertAlmostEqual(a,float(b),places=13)
                    q=[sum(q[i]*P[i][j] for i in range(M+1)) for j in range(M+1)]

    def test_rows_conditional_moments_and_harmonic_fixation(self):
        for N in (1,2,5,10,20):
            M=2*N
            for i,row in enumerate(kernel(N)):
                self.assertAlmostEqual(sum(row),1,places=13)
                self.assertTrue(all(p>=0 for p in row))
                p=i/M
                # f(i)=i/M é harmônica, com f(0)=0 e f(M)=1.
                self.assertAlmostEqual(sum(j/M*row[j] for j in range(M+1)),p,places=13)
                self.assertAlmostEqual(sum((j/M-p)**2*row[j] for j in range(M+1)),p*(1-p)/M,places=13)
            self.assertEqual(kernel(N)[0][0],1);self.assertEqual(kernel(N)[M][M],1)

    def test_moments_diversity_symmetry_and_absorption_mass(self):
        for N in (2,5,10,20):
            M=2*N;k=N//2+1
            previous=-1
            for t in (0,1,5,10,40):
                q=distribution(N,k,t);r=distribution(N,M-k,t);p=k/M;decay=(1-1/M)**t
                self.assertAlmostEqual(q['mass'],1,places=12)
                self.assertAlmostEqual(q['mean'],p,places=12)
                self.assertAlmostEqual(q['variance'],p*(1-p)*(1-decay),places=12)
                self.assertAlmostEqual(q['heterozygosity'],2*p*(1-p)*decay,places=12)
                self.assertGreaterEqual(q['loss']+q['fixation'],previous-1e-14)
                previous=q['loss']+q['fixation']
                for a,b in zip(q['distribution'],reversed(r['distribution'])):self.assertAlmostEqual(a,b,places=12)
                for end in (0,M):
                    boundary=distribution(N,end,t)
                    self.assertEqual(boundary['distribution'][end],1)
                    self.assertEqual(boundary['variance'],0)

    def test_contract(self):
        for args in ((0,0,0),(21,0,0),(2,-1,0),(2,5,0),(2,1,-1),(2,1,101),(True,1,1),(2,1.0,1),(2,1,True)):
            with self.assertRaises(ValueError):distribution(*args)
