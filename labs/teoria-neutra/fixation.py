"""Modelo neutro finito; probabilidades exatas, sem dados de espécies."""
from fractions import Fraction as Q
from math import comb
import unittest


def transitions(M):
    if isinstance(M,bool) or not isinstance(M,int) or not 2<=M<=12:
        raise ValueError('Laboratório limitado a2..12 cópias')
    return [[Q(comb(M,j))*Q(i,M)**j*(1-Q(i,M))**(M-j)
             for j in range(M+1)] for i in range(M+1)]


def solve(A,b):
    # Exact Gauss-Jordan elimination, used only on the small transient system.
    rows=[list(row)+[value] for row,value in zip(A,b)]
    n=len(rows)
    for k in range(n):
        pivot=next((i for i in range(k,n) if rows[i][k]),None)
        if pivot is None:raise ValueError('Sistema singular')
        rows[k],rows[pivot]=rows[pivot],rows[k]
        scale=rows[k][k]
        rows[k]=[x/scale for x in rows[k]]
        for i in range(n):
            if i!=k:
                scale=rows[i][k]
                rows[i]=[a-scale*b for a,b in zip(rows[i],rows[k])]
    return [row[-1] for row in rows]


def eventual(M):
    P=transitions(M)
    A=[[Q(i==j)-P[i][j] for j in range(1,M)] for i in range(1,M)]
    h=solve(A,[P[i][M] for i in range(1,M)])
    return [Q(0),*h,Q(1)]


def finite(M,i,steps):
    P=transitions(M)
    if isinstance(i,bool) or not isinstance(i,int) or not 0<=i<=M:
        raise ValueError('Contagem inicial válida')
    if isinstance(steps,bool) or not isinstance(steps,int) or steps<0:
        raise ValueError('Número inteiro não negativo de gerações')
    distribution=[Q(j==i) for j in range(M+1)]
    for _ in range(steps):
        distribution=[sum(distribution[k]*P[k][j] for k in range(M+1)) for j in range(M+1)]
    return distribution[M]


def destined_origins(N,mu):
    if isinstance(N,bool) or not isinstance(N,int) or N<1:
        raise ValueError('N diploide positivo')
    if isinstance(mu,bool) or not isinstance(mu,(int,Q)) or not 0<=mu<=1:
        raise ValueError('Taxa racional por cópia em[0,1]')
    M=2*N
    entry=M*Q(mu)
    chance=Q(1,M)
    return entry,chance,entry*chance


class Checks(unittest.TestCase):
    def test_absorption_solve_and_harmonic_equations(self):
        for M in range(2,11):
            P=transitions(M)
            h=eventual(M)
            self.assertEqual(h,[Q(i,M) for i in range(M+1)])
            for i,row in enumerate(P):
                self.assertEqual(sum(row),1)
                self.assertEqual(sum(p*j for j,p in enumerate(row)),i)
                self.assertEqual(sum(p*x for p,x in zip(row,h)),h[i])

    def test_finite_is_not_eventual(self):
        self.assertEqual(finite(4,1,1),Q(1,256))
        self.assertEqual(eventual(4)[1],Q(1,4))
        for M in range(2,7):
            for i in range(1,M):
                values=[finite(M,i,t) for t in (0,1,2,5,10)]
                self.assertEqual(values,sorted(values))
                self.assertLessEqual(values[-1],Q(i,M))

    def test_rate_product_units(self):
        for N in (5,50,100,500):
            for mu in (Q(0),Q(1,10**7),Q(1,10**6)):
                entry,p,eventual_rate=destined_origins(N,mu)
                self.assertEqual(eventual_rate,mu)
                doubled=destined_origins(2*N,mu)
                self.assertEqual(doubled[0],2*entry)
                self.assertEqual(doubled[1],p/2)
        self.assertEqual(destined_origins(50,Q(1,100000)),(Q(1,1000),Q(1,100),Q(1,100000)))

    def test_contracts(self):
        for M in (1,13,True,4.0):
            with self.assertRaises(ValueError):transitions(M)
        for args in ((0,Q(1,100)),(True,Q(1,100)),(5,.1),(5,Q(-1))):
            with self.assertRaises(ValueError):destined_origins(*args)


if __name__=='__main__':
    print('Destino eventual,M4:',eventual(4))
    print('Fixação na próxima geração,M4,i1:',finite(4,1,1))
    print('Entradas,chance,produto:',destined_origins(50,Q(1,100000)))
    unittest.main()
