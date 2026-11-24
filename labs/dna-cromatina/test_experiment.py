import itertools,unittest
from fractions import Fraction as F
from .experiment import model,reverse_complement


class ChromatinTests(unittest.TestCase):
    def test_independent_sequence_assembly(self):
        for n in range(1,9):
            for ell in range(81):
                tokens='C'*147+('L'*ell+'C'*147)*(n-1)
                s=model(n,ell)
                self.assertEqual(len(tokens),s['total_bp'])
                self.assertEqual(tokens.count('C'),s['wrapped'])
                self.assertEqual(tokens.count('L'),s['link_bp'])
                rebuilt=''.join(('C' if x['kind']=='core' else 'L')*(x['stop']-x['start']) for x in s['segments'])
                self.assertEqual(tokens,rebuilt)
                self.assertEqual(s['segments'][0]['start'],0)
                self.assertEqual(s['segments'][-1]['stop'],len(tokens))
                for left,right in zip(s['segments'],s['segments'][1:]):self.assertEqual(left['stop'],right['start'])

    def test_finite_end_correction_and_sensitivity(self):
        for n in range(1,8):
            for ell in (0,20,40,80):
                a=model(n,ell);b=model(n+1,ell)
                self.assertEqual(b['total_bp']-a['total_bp'],147+ell)
                self.assertEqual(a['histones'],sum(2*n for name in ('H2A','H2B','H3','H4')))
                if n>1:self.assertGreaterEqual(F(a['wrapped'],a['total_bp']),F(147,147+ell))
                if ell:self.assertEqual(a['total_bp'],n*(147+ell)-ell)
            self.assertGreaterEqual(model(n,0)['wrapped_fraction'],model(n,80)['wrapped_fraction'])
        self.assertEqual(model(1,80)['total_bp'],147)
        self.assertIsNone(model(1,40)['internal_repeat'])

    def test_sequence_orientation_exhaustive(self):
        pair=dict(A='T',T='A',C='G',G='C')
        for length in range(1,7):
            for letters in itertools.product('ACGT',repeat=length):
                s=''.join(letters);r=reverse_complement(s)
                self.assertEqual(reverse_complement(r),s)
                self.assertTrue(all(pair[a]==b for a,b in zip(s,r[::-1])))
                self.assertEqual(s.count('C')+s.count('G'),r.count('C')+r.count('G'))
        self.assertEqual(reverse_complement('AATG'),'CATT')
        self.assertNotEqual(reverse_complement('AATG'),'TTAC')

    def test_units_selection_and_contract(self):
        a=model(4,40,8)
        self.assertEqual(a['selected'],4)
        self.assertEqual(a['nucleotides'],1416)
        self.assertAlmostEqual(a['contour_nm'],float(F(17,50)*708))
        self.assertEqual(a['each_histone'],8)
        for args in ((0,40,1),(9,40,1),(1,-1,1),(1,81,1),(1,40,0),(True,40,1),(2,2.5,1)):
            with self.assertRaises(ValueError):model(*args)
        for s in ('','acgt','ACGU','AN',12):
            with self.assertRaises(ValueError):reverse_complement(s)
