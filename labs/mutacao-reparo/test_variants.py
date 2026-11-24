import unittest
from .variants import substitute,delete,read_coding_dna


class VariantTests(unittest.TestCase):
    def test_examples_and_stops(self):
        ref="ATGGAATTTTAA"
        cases=[(ref,"MEF",9,""),
               (substitute(ref,6,"G"),"MEF",9,""),
               (substitute(ref,5,"T"),"MVF",9,""),
               (substitute(ref,4,"T"),"M",3,"UUUUAA"),
               (delete(ref,4),"MNF",None,"AA"),
               (delete(ref,4,3),"MF",6,"")]
        for sequence,peptide,stop,suffix in cases:
            out=read_coding_dna(sequence)
            self.assertEqual((out["peptide"],out["stop_offset"],out["suffix"]),
                             (peptide,stop,suffix))

    def test_single_substitutions_preserve_length_and_other_positions(self):
        ref="ATGGAATTTTAA"
        for pos,old in enumerate(ref,1):
            for base in "ACGT":
                if base==old:continue
                new=substitute(ref,pos,base)
                self.assertEqual(len(new),len(ref))
                self.assertEqual([i+1 for i,(a,b) in enumerate(zip(ref,new)) if a!=b],[pos])
                self.assertEqual(new[pos-1],base)
                # Antes do códon alterado, a leitura permanece igual, salvo parada anterior.
                before=(pos-1)//3
                a=read_coding_dna(ref);b=read_coding_dna(new)
                self.assertEqual(a["codons"][:before],b["codons"][:before])

    def test_deletions_against_identified_positions_and_modulo(self):
        ref="ATGGAATTTTAA"
        for first in range(1,len(ref)+1):
            for count in range(1,len(ref)-first+2):
                new=delete(ref,first,count)
                expected="".join(base for i,base in enumerate(ref,1)
                                 if i not in range(first,first+count))
                self.assertEqual(new,expected)
                self.assertEqual(len(new)%3,(-count)%3)
                out=read_coding_dna(new)
                if out["stop_offset"] is None:
                    self.assertEqual(len(out["suffix"]),len(new)%3)
                else:
                    self.assertEqual(new[out["stop_offset"]:out["stop_offset"]+3],
                                     out["codons"][-1].replace("U","T"))

    def test_factual_code_and_contracts(self):
        expected={"ATG":"M","GAA":"E","GAG":"E","GTA":"V","TTT":"F","AAT":"N"}
        for codon,aa in expected.items():self.assertEqual(read_coding_dna(codon)["peptide"],aa)
        for stop in ("TAA","TAG","TGA"):
            out=read_coding_dna(stop+"ATG")
            self.assertEqual((out["peptide"],out["stop_offset"],out["suffix"]),("",0,"AUG"))
        for seq in ("AUG","atg","ANG",None,12):
            with self.assertRaises(ValueError):read_coding_dna(seq)
        for pos in (0,13,True,1.0):
            with self.assertRaises(ValueError):substitute("ATGGAATTTTAA",pos,"C")
        for base in ("", "AA", "U",True):
            with self.assertRaises(ValueError):substitute("ATG",1,base)
        with self.assertRaises(ValueError):substitute("ATG",1,"A")
        for count in (0,-1,True,1.5,4):
            with self.assertRaises(ValueError):delete("ATG",1,count)
        self.assertEqual(read_coding_dna("")["peptide"],"")

if __name__=="__main__":unittest.main()
