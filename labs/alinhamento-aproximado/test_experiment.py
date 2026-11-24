import itertools
import unittest
from fractions import Fraction as F
from .experiment import search,model,revcomp

class ApproximateMappingTests(unittest.TestCase):
    def test_exhaustive_words_both_strands(self):
        for letters in itertools.product('ACGT',repeat=4):
            reference=''.join(letters)
            for pair in itertools.product('ACGT',repeat=2):
                query=''.join(pair)
                reverse=''.join({'A':'T','C':'G','G':'C','T':'A'}[x] for x in query[::-1])
                expected=[]
                for start in range(3):
                    for strand,seq in (('+',query),('-',reverse)):
                        cost=sum(reference[start+j]!=seq[j] for j in range(2))
                        expected.append((start,strand,cost))
                for limit in range(3):
                    r=search(reference,query,limit)
                    self.assertEqual([(x['start'],x['strand'],x['cost']) for x in r['rows']],expected)
                    accepted=[v for v in expected if v[2]<=limit]
                    minimum=min(v[2] for v in expected)
                    best=[v for v in accepted if v[2]==minimum]
                    self.assertEqual([(x['start'],x['strand'],x['cost']) for x in r['best']],best)
                    self.assertEqual(r['interval_count'],len({v[0] for v in best}))
    def test_likelihood_is_distribution_of_reads_not_origins(self):
        template='CGTT'
        for q in (10,20,40):
            p=F(1,10**(q//10));total=F(0)
            for letters in itertools.product('ACGT',repeat=4):
                query=''.join(letters)
                result=search(template,query,4,q)
                row=result['rows'][0]
                product=F(1)
                for ref,base in zip(template,query):product*=1-p if ref==base else p/3
                self.assertEqual(row['likelihood'],product)
                total+=product
            self.assertEqual(total,1)
        self.assertEqual(model()['best'][0]['likelihood'],F(323433,100000000))
    def test_ties_threshold_and_quality(self):
        self.assertEqual(model(2)['interval_count'],2)
        palindrome=model(4,0);self.assertEqual(palindrome['interval_count'],1);self.assertEqual(palindrome['oriented_count'],2)
        self.assertFalse(model(3,2)['best']);self.assertEqual(model(3,2)['minimum'],3)
        for kind in range(5):
            for limit in range(3):
                baseline=model(kind,limit,10)
                for q in (20,30,40):
                    r=model(kind,limit,q)
                    self.assertEqual([(x['start'],x['strand']) for x in r['best']],[(x['start'],x['strand']) for x in baseline['best']])
                    for a,b in itertools.product(r['rows'],repeat=2):
                        if a['cost']<b['cost']:self.assertGreater(a['likelihood'],b['likelihood'])
                if limit<2:
                    self.assertLessEqual({(x['start'],x['strand']) for x in baseline['accepted']},{(x['start'],x['strand']) for x in model(kind,limit+1,10)['accepted']})
    def test_contract_and_long_read(self):
        self.assertFalse(search('AC','ACGT')['rows'])
        self.assertEqual(revcomp(revcomp('ACGTT')),'ACGTT')
        for bad in ('','N','acgt',None,'A'*257):
            with self.assertRaises(ValueError):search('ACGT',bad)
        for args in [('AC','AC',-1,20),('AC','AC',3,20),('AC','AC',True,20),('AC','AC',1,0),('AC','AC',1,25)]:
            with self.assertRaises(ValueError):search(*args)
