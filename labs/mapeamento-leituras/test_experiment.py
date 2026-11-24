import itertools,unittest
from .experiment import revcomp,locate,coverage,model

class ReadMappingTests(unittest.TestCase):
    def test_exhaustive_matches_against_strand_alignment_oracle(self):
        # Compara letra por letra com referência direta e complementar, sem substring.
        comp={'A':'T','C':'G','G':'C','T':'A'}
        for word in itertools.product('ACGT',repeat=4):
            ref=''.join(word)
            for k in (1,2):
                for query in map(''.join,itertools.product('ACGT',repeat=k)):
                    expected=[]
                    for i in range(5-k):
                        strands=[]
                        if all(ref[i+j]==query[j] for j in range(k)):strands.append('+')
                        if all(ref[i+j]==comp[query[k-1-j]] for j in range(k)):strands.append('-')
                        if strands:expected.append(dict(start=i,end=i+k,strands=strands))
                    self.assertEqual(locate(ref,query),expected)
        self.assertEqual(locate('ATAT','ATAT'),[dict(start=0,end=4,strands=['+','-'])])
        self.assertEqual(locate('AAAA','C'),[])
        self.assertEqual(locate('AC','ACG'),[])

    def test_cohort_coverage_by_difference_array_and_mass(self):
        for g in (0,1):
            for L in range(4,9):
                s=model(g,L);delta=[0]*25
                for row in s['rows']:
                    delta[row['origin']]+=1;delta[row['origin']+L]-=1
                    self.assertTrue(any(h['start']==row['origin'] and row['origin_strand'] in h['strands'] for h in row['hits']))
                    if row['unique']:self.assertEqual(row['hits'][0]['start'],row['origin'])
                cur=0;expected=[]
                for d in delta[:-1]:cur+=d;expected.append(cur)
                self.assertEqual(s['truth'],expected);self.assertEqual(sum(s['truth']),5*L)
                self.assertEqual(sum(s['retained']),s['unique_count']*L)
                self.assertTrue(all(0<=a<=b for a,b in zip(s['retained'],s['truth'])))
                self.assertAlmostEqual(s['mean_truth'],5*L/24)
                self.assertEqual(s['unique_count']+s['ambiguous_count'],5)

    def test_orientation_reversal_covariance_and_display_selection(self):
        for g in (0,1):
            for L in range(4,9):
                s=model(g,L)
                for row in s['rows']:
                    q=row['query'];hits=locate(s['reference'],q)
                    self.assertEqual([h['start'] for h in hits],[h['start'] for h in locate(s['reference'],revcomp(q))])
                    reversed_hits=locate(revcomp(s['reference']),q)
                    self.assertEqual(sorted((h['start'],h['end']) for h in reversed_hits),sorted((24-h['end'],24-h['start']) for h in hits))
                    self.assertEqual(revcomp(revcomp(q)),q)
                for r in range(1,6):
                    t=model(g,L,r);self.assertEqual(t['rows'],s['rows']);self.assertEqual(t['truth'],s['truth']);self.assertEqual(t['selected'],t['rows'][r-1])

    def test_intervals_palindromes_and_contracts(self):
        self.assertEqual(coverage([(0,1),(1,3),(2,4)],4),[1,1,2,1])
        for q in ('','acgt','AN','A-G'):
            with self.assertRaises(ValueError):revcomp(q)
        for args in ((2,6,3),(0,3,1),(0,9,1),(0,6,0),(0,6,6),(0,6.5,1)):
            with self.assertRaises(ValueError):model(*args)
        for intervals in ([(-1,2)],[(0,5)],[(2,2)]):
            with self.assertRaises(ValueError):coverage(intervals,4)
