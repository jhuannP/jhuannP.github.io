import unittest
from fractions import Fraction as Q
from .decomposition import model,decompose

class CovarianceTests(unittest.TestCase):
    def test_weights_and_total_identity(self):
        for i in range(17):
            q=Q(i,16);out=decompose(model(q));m=out['global_moments']
            self.assertEqual(out['within'],-1)
            self.assertEqual(out['between'],16*q*(1-q))
            self.assertEqual(m['cov'],out['within']+out['between'])
            self.assertEqual(m['vx'],1+16*q*(1-q))
            self.assertEqual(m['vy'],m['vx'])
            self.assertEqual(len(out['groups']),1 if q in (0,1) else 2)
    def test_reference_and_rare_group(self):
        o=decompose(model());m=o['global_moments']
        self.assertEqual(m['cov'],3);self.assertEqual(m['vx'],5)
        self.assertEqual(m['cov']/m['vx'],Q(3,5))
        for g in o['groups']:self.assertEqual(g['cov'],-1)
        m=decompose(model(Q(1,16)))['global_moments']
        self.assertEqual(m['cov'],Q(-1,16));self.assertEqual(m['cov']/m['vx'],Q(-1,31))
    def test_affine_transform_and_split_rows(self):
        base=model();old=decompose(base)
        for a,b in [(2,3),(-2,3),(1,-4),(0,2)]:
            transformed=[(g,a*x+100,b*y-23,w) for g,x,y,w in base]
            new=decompose(transformed)
            for k in ['within','between']:self.assertEqual(new[k],a*b*old[k])
            self.assertEqual(new['global_moments']['cov'],a*b*old['global_moments']['cov'])
        split=[row for g,x,y,w in base for row in [(g,x,y,w/3),(g,x,y,2*w/3)]]
        self.assertEqual(decompose(split),old)
    def test_contracts(self):
        for q in [-1,Q(17,16),True,.5]:
            with self.assertRaises(ValueError):model(q)
        for rows in [[],[('g',1,2,Q(1,2))],[('g',1,2,-1)],[('',1,2,1)],[('g',True,2,1)],[('g',1.,2,1)], [('g',1,2,True)]]:
            with self.assertRaises(ValueError):decompose(rows)
if __name__=='__main__':unittest.main()
