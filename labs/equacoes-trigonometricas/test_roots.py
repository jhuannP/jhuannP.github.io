import unittest
from fractions import Fraction as Q
from .roots import solve


class RootsTests(unittest.TestCase):
    def test_example_and_all_families(self):
        bases=(Q(1,6),Q(5,6))
        r=solve(2,Q(-1,6),bases,2,0,2)
        self.assertEqual(r,{'kind':'finite','values':[Q(1,6),Q(1,2),Q(7,6),Q(3,2)]})
        self.assertEqual(solve(1,0,bases,2,0,2)['values'],list(bases))
        self.assertEqual(solve(1,0,(Q(1,4),),1,0,2)['values'],[Q(1,4),Q(5,4)])

    def test_transformed_ranges_and_direct_check(self):
        bases=(Q(1,6),Q(5,6))
        for a in (-2,-1,Q(-1,2),Q(1,2),1,2):
            for b in (Q(-1,6),0,Q(1,6)):
                r=solve(a,b,bases,2,0,2)['values']
                expected=sorted({(base+2*k-b)/a for base in bases for k in range(-20,21)
                                 if 0<=(base+2*k-b)/a<2})
                self.assertEqual(r,expected)
                for u in r:self.assertTrue(any(((a*u+b-base)/2).denominator==1 for base in bases))

    def test_endpoints_duplicates_and_constants(self):
        self.assertEqual(solve(1,0,(0,),2,0,2)['values'],[0])
        self.assertEqual(solve(1,0,(0,),2,0,2,True)['values'],[0,2])
        self.assertEqual(solve(-1,0,(0,0),2,0,2,True)['values'],[0,2])
        self.assertEqual(solve(0,Q(1,6),(Q(1,6),Q(5,6)),2,0,2)['kind'],'interval')
        self.assertEqual(solve(0,0,(Q(1,6),Q(5,6)),2,0,2),{'kind':'finite','values':[]})

    def test_contracts(self):
        for args in ((True,0,(0,),2,0,2),(1.,0,(0,),2,0,2),
                     (1,0,(),2,0,2),(1,0,(2,),2,0,2),
                     (1,0,(0,),0,0,2),(1,0,(0,),2,2,0),
                     (1,0,(0,),Q(1,10001),0,2)):
            with self.assertRaises(ValueError):solve(*args)
        with self.assertRaises(ValueError):solve(1,0,(0,),2,0,2,1)


if __name__=='__main__':unittest.main()
