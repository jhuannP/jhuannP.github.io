import unittest,itertools
from .electrons import boxes,configuration,counts,unpaired

class ElectronTests(unittest.TestCase):
    def test_reference_light_atoms(self):
        references={1:(('1s',1),),2:(('1s',2),),6:(('1s',2),('2s',2),('2p',2)),8:(('1s',2),('2s',2),('2p',4)),10:(('1s',2),('2s',2),('2p',6)),11:(('1s',2),('2s',2),('2p',6),('3s',1)),12:(('1s',2),('2s',2),('2p',6),('3s',2)),18:(('1s',2),('2s',2),('2p',6),('3s',2),('3p',6))}
        for z,expected in references.items():self.assertEqual(counts(configuration(z)),expected)
        self.assertEqual(unpaired(configuration(6)),2)
        self.assertEqual(unpaired(configuration(7)),3)
        self.assertEqual(unpaired(configuration(8)),2)
        self.assertEqual(unpaired(configuration(10)),0)

    def test_all_formal_counts_and_pauli(self):
        for z in range(1,19):
            for n in range(19):
                config=configuration(z,z-n)
                self.assertEqual(sum(c for _,c in counts(config)),n)
                for _,occupied in config:
                    for up,down in occupied:
                        self.assertIn(up,(0,1));self.assertIn(down,(0,1))
                        self.assertLessEqual(up+down,2)
        # 342 formalidades contábeis não são uma lista de íons estáveis.
        self.assertEqual(configuration(1,1),())

    def test_hund_by_enumerating_spin_orbitals(self):
        states=list(itertools.product((0,1),repeat=6))
        for n in range(7):
            allowed=[bits for bits in states if sum(bits)==n]
            max_spin=max(abs(sum(bits[:3])-sum(bits[3:])) for bits in allowed)
            actual=boxes(n,3)
            self.assertEqual(abs(sum(u-d for u,d in actual)),max_spin)
            self.assertEqual(sum(u+d==1 for u,d in actual),min(n,6-n))
        self.assertEqual(boxes(4,3),((1,1),(1,0),(1,0)))
        # Mesmo número de elétrons e Pauli permitido não bastam para Hund.
        alternative=((1,1),(1,1),(0,0))
        self.assertEqual(sum(u+d for u,d in alternative),4)
        self.assertLess(abs(sum(u-d for u,d in alternative)),2)

    def test_isoelectronic_and_charge(self):
        neon=configuration(10)
        for z,q in [(11,1),(12,2),(9,-1),(8,-2)]:
            self.assertEqual(configuration(z,q),neon)
        self.assertEqual(sum(c for _,c in counts(configuration(11))),11)
        self.assertEqual(sum(c for _,c in counts(configuration(11,1))),10)
        self.assertEqual(sum(c for _,c in counts(configuration(9,-1))),10)

    def test_contracts(self):
        for z,q in [(0,0),(19,0),(1,2),(18,-1)]:
            with self.assertRaises(ValueError):configuration(z,q)
        for z,q in [(True,0),(8.,0),(8,.5),(8,False)]:
            with self.assertRaises(TypeError):configuration(z,q)
        for n,m in [(-1,3),(7,3),(2,2)]:
            with self.assertRaises(ValueError):boxes(n,m)

if __name__=='__main__':unittest.main()
