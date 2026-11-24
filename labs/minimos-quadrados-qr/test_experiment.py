import unittest
from math import sqrt
from .experiment import qr_fit,normal_fit,dataset

class LeastSquaresQRTests(unittest.TestCase):
    def test_qr_factorization_and_orthogonality(self):
        for A,y in [([[1,0],[1,1],[1,2]],[1,2,4]),([[1,-2,4],[1,-1,1],[1,0,0],[1,1,1],[1,2,4]],[2,1,1,2,4])]:
            r=qr_fit(A,y);qt=r['qt'];m=len(A);n=len(A[0])
            for i in range(m):
                for j in range(m):self.assertAlmostEqual(sum(qt[k][i]*qt[k][j] for k in range(m)),float(i==j),places=12)
                for j in range(n):self.assertAlmostEqual(sum(qt[i][k]*A[k][j] for k in range(m)),r['R'][i][j],places=12)
            self.assertLess(max(map(abs,r['gradient'])),1e-11)

    def test_closed_form_references_and_minimum(self):
        r=qr_fit([[1,0],[1,1],[1,2]],[1,2,4]);self.assertAlmostEqual(r['beta'][0],5/6);self.assertAlmostEqual(r['beta'][1],1.5);self.assertAlmostEqual(r['sse'],1/6)
        for delta in (-1,0,1):
            for mode in (0,1):
                d=dataset(mode,delta);r=qr_fit(d['A'],d['y'])
                expected=[2+delta/5,.5] if mode==0 else [1+17*delta/35,.5,.5-delta/7]
                for a,b in zip(r['beta'],expected):self.assertAlmostEqual(a,b,places=12)
                expected_sse=3.5-2*delta+4*delta*delta/5 if mode==0 else 18*delta*delta/35
                self.assertAlmostEqual(r['sse'],expected_sse,places=12)
                perturbed=[b+.3 for b in r['beta']]
                sse=sum((yi-sum(a*b for a,b in zip(row,perturbed)))**2 for row,yi in zip(d['A'],d['y']))
                increase=sum(sum(a*.3 for a in row)**2 for row in d['A'])
                self.assertAlmostEqual(sse,r['sse']+increase,places=10)

    def test_basis_change_and_normal_equation_limit(self):
        for level in (0,1,2):
            for delta in (-1,0,1):
                d=dataset(2,delta,level);r=qr_fit(d['A'],d['y']);canonical=qr_fit(dataset(1,delta)['A'],d['y'])
                self.assertEqual(r['status'],'ok')
                for a,b in zip(r['pred'],canonical['pred']):self.assertAlmostEqual(a,b,delta=2e-7)
                self.assertAlmostEqual(r['sse'],canonical['sse'],delta=2e-7)
        d=dataset(2,0,2)
        self.assertEqual(normal_fit(d['A'],d['y'])['status'],'pivot')
        self.assertGreater(abs(qr_fit(d['A'],d['y'])['beta'][2]),1e7)

    def test_rank_weighted_rows_and_domain(self):
        d=dataset(2,0,3);self.assertEqual(qr_fit(d['A'],d['y'])['status'],'rank')
        self.assertEqual(qr_fit([[1,1],[1,1]],[2,3])['status'],'rank')
        # Pesos positivos aplicados como raiz do peso às duas partes.
        xs=[0,1,2];weights=[1,4,9];A=[[sqrt(w),sqrt(w)*x] for x,w in zip(xs,weights)];y=[sqrt(w)*(2*x+1) for x,w in zip(xs,weights)]
        r=qr_fit(A,y);self.assertAlmostEqual(r['beta'][0],1);self.assertAlmostEqual(r['beta'][1],2)
        for A,y in [([],[]),([[1,2]],[1]),([[1],[1,2]],[1,2]),([[float('nan')]],[1])]:
            with self.assertRaises(ValueError):qr_fit(A,y)

if __name__=='__main__':unittest.main()
