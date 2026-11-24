import unittest
from collections import Counter
from itertools import product
from .experiment import CODE,decode_frame

class TranslationFrameTests(unittest.TestCase):
    def test_standard_code_facts_and_degeneracy(self):
        self.assertEqual(set(CODE),{"".join(c) for c in product("ACGU",repeat=3)})
        self.assertEqual(len(CODE),64)
        self.assertEqual({k for k,v in CODE.items() if v=="*"},{"UAA","UAG","UGA"})
        self.assertEqual(Counter(CODE.values()),Counter(dict(F=2,L=6,S=6,Y=2,C=2,W=1,P=4,H=2,Q=2,R=6,I=3,M=1,T=4,N=2,K=2,V=4,A=4,D=2,E=2,G=4,**{"*":3})))
        for codon,amino in {"AUG":"M","GCU":"A","GCC":"A","GCA":"A","GCG":"A","UUU":"F","CUU":"L","AAG":"K","GGC":"G","UUA":"L","AGG":"R","UGG":"W"}.items():self.assertEqual(CODE[codon],amino)

    def test_three_frames_of_lesson(self):
        rna="AUGGCUUUUUAAGG"
        zero=decode_frame(rna,0)
        self.assertEqual(zero,dict(peptide="MAF",stop_offset=9,suffix="GG",codons=("AUG","GCU","UUU","UAA")))
        self.assertEqual(decode_frame(rna,1)['peptide'],"WLFK")
        self.assertEqual(decode_frame(rna,1)['suffix'],"G")
        self.assertIsNone(decode_frame(rna,1)['stop_offset'])
        self.assertEqual(decode_frame(rna,2)['peptide'],"GFLR")
        self.assertEqual(decode_frame(rna,2)['suffix'],"")

    def test_stop_is_not_a_residue_and_suffix_not_decoded(self):
        for stop in ("UAA","UAG","UGA"):
            result=decode_frame("AUG"+stop+"GCU")
            self.assertEqual(result['peptide'],"M")
            self.assertEqual(result['codons'],("AUG",stop))
            self.assertEqual(result['suffix'],"GCU")
        self.assertEqual(decode_frame("GCU")['peptide'],"A") # Não procura início.

    def test_short_and_incomplete_windows(self):
        for rna in ("","A","AC"):
            self.assertEqual(decode_frame(rna)['peptide'],"")
            self.assertEqual(decode_frame(rna)['suffix'],rna)
        for tail in ("","A","AC"):
            result=decode_frame("GCU"+tail)
            self.assertEqual(result['peptide'],"A")
            self.assertEqual(result['suffix'],tail)
            self.assertIsNone(result['stop_offset'])

    def test_contract(self):
        for rna in ("ATG","aug","AUG N",None,b"AUG"):
            with self.assertRaises(ValueError):decode_frame(rna)
        for frame in (-1,3,True,.0):
            with self.assertRaises(ValueError):decode_frame("AUG",frame)
