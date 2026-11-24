import unittest
from itertools import permutations, product
from fractions import Fraction as Q
from .cofactors import determinant,adjugate,expansion

def leibniz(a):
    n=len(a);result=Q(0)
    for perm in permutations(range(n)):
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        term=Q((-1)**inversions)
        for i,j in enumerate(perm):term*=a[i][j]
        result+=term
    return result

def gauss(a):
    a=[list(map(Q,row)) for row in a];n=len(a);answer=Q(1)
    for i in range(n):
        pivot=next((k for k in range(i,n) if a[k][i]),None)
        if pivot is None:return Q(0)
        if pivot!=i:a[i],a[pivot]=a[pivot],a[i];answer=-answer
        answer*=a[i][i]
        for k in range(i+1,n):
            factor=a[k][i]/a[i][i]
            for j in range(i,n):a[k][j]-=factor*a[i][j]
    return answer

def multiply(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

class CofactorTests(unittest.TestCase):
    def test_exhaustive_two(self):
        for entries in product((-1,0,1),repeat=4):
            a=[entries[:2],entries[2:]]
            self.assertEqual(determinant(a),leibniz(a))
    def test_larger_independent_oracles(self):
        for n in range(1,7):
            for seed in range(8):
                a=[[Q(((i+1)*(j+3)+seed*(i-j+2))%7-3,(i+j)%2+1) for j in range(n)] for i in range(n)]
                expected=gauss(a)
                self.assertEqual(determinant(a),expected)
                self.assertEqual(leibniz(a),expected)
                for row in range(n):self.assertEqual(sum(expansion(a,row)),expected)
    def test_both_adjugate_products(self):
        for n in range(1,6):
            for seed in range(5):
                a=[[Q(((i+seed+1)*(j+2))%5-2) for j in range(n)] for i in range(n)]
                adj=adjugate(a);det=gauss(a)
                expected=[[det if i==j else 0 for j in range(n)] for i in range(n)]
                self.assertEqual(multiply(a,adj),expected)
                self.assertEqual(multiply(adj,a),expected)
    def test_landmarks(self):
        a=[[2,1,0],[0,3,1],[1,0,2]]
        self.assertEqual(determinant(a),13)
        self.assertEqual(expansion(a),(12,1,0))
        self.assertEqual(adjugate(a)[0][1],-2)
        self.assertEqual(determinant([]),1)
        self.assertEqual(adjugate([[0]]),((1,),))
        self.assertEqual(adjugate([[1,2],[2,4]]),((4,-2),(-2,1)))
    def test_contracts(self):
        for a in ([[1,2]],[[1.0]],[[True]],[[0]*7 for _ in range(7)]):
            with self.assertRaises(ValueError):determinant(a)
        for row in (-1,2,True):
            with self.assertRaises(ValueError):expansion([[1,0],[0,1]],row)
        with self.assertRaises(ValueError):expansion([])

if __name__=='__main__':unittest.main()
