from itertools import product
import unittest
from .experiment import from_template,from_coding,transcribe_region

DNA={"A":"T","T":"A","C":"G","G":"C"}
RNA={"A":"U","T":"A","C":"G","G":"C"}

class TranscriptionOrientationTests(unittest.TestCase):
    def test_examples_and_roles(self):
        plus=transcribe_region("ACGTAACC","inferior")
        minus=transcribe_region("ACGTAACC","superior")
        self.assertEqual(plus["rna_5to3"],"ACGUAACC")
        self.assertEqual(minus["rna_5to3"],"GGUUACGU")
        self.assertEqual((plus["direction"],minus["direction"]),(1,-1))
        self.assertEqual(plus["template_5to3"],"GGTTACGT")
        self.assertEqual(minus["template_5to3"],"ACGTAACC")
    def test_exhaustive_short_strings(self):
        for n in range(1,6):
            for bases in product("ACGT",repeat=n):
                s="".join(bases)
                expected="".join(RNA[b] for b in reversed(s))
                self.assertEqual(from_template(s),expected)
                coding="".join("U" if b=="T" else b for b in s)
                self.assertEqual(from_coding(s),coding)
                opposite="".join(DNA[b] for b in reversed(s))
                self.assertEqual(from_template(opposite),coding)
                self.assertEqual(len(expected),n)
                self.assertNotIn("T",expected)
    def test_all_regions_by_explicit_template_reading(self):
        upper="ACGTAACC"
        for start in range(len(upper)):
            for stop in range(start+1,len(upper)+1):
                for side in ("superior","inferior"):
                    r=transcribe_region(upper,side,start,stop)
                    positions=range(start,stop) if side=="inferior" else range(stop-1,start-1,-1)
                    read=[DNA[upper[i]] if side=="inferior" else upper[i] for i in positions]
                    expected="".join(RNA[b] for b in read)
                    self.assertEqual(r["rna_5to3"],expected)
                    self.assertEqual(r["interval"],(start,stop))
                    self.assertEqual(from_coding(r["coding_5to3"]),expected)
    def test_reversing_the_display_reference(self):
        upper="ACGTAACC";N=len(upper)
        reversed_reference="".join(DNA[b] for b in reversed(upper))
        for start in range(N):
            for stop in range(start+1,N+1):
                for side,other in (("superior","inferior"),("inferior","superior")):
                    r=transcribe_region(upper,side,start,stop)
                    rr=transcribe_region(reversed_reference,other,N-stop,N-start)
                    self.assertEqual(r["rna_5to3"],rr["rna_5to3"])
                    self.assertEqual(r["coding_5to3"],rr["coding_5to3"])
                    self.assertEqual(r["direction"],-rr["direction"])
    def test_contracts(self):
        for bad in ("","ACN","ACU","acgt","A C",None,True):
            for fn in (from_template,from_coding):
                with self.assertRaises(ValueError):fn(bad)
        with self.assertRaises(ValueError):transcribe_region("ACGT","desconhecida")
        for start,stop in ((True,2),(0,False),(-1,2),(2,2),(3,1),(0,5),(0,2.0)):
            with self.assertRaises(ValueError):transcribe_region("ACGT","inferior",start,stop)
