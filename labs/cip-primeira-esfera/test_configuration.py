import unittest
from itertools import permutations,product
from .configuration import priority,configuration,REFERENCE,LIGANDS

class Tests(unittest.TestCase):
    def test_priority_and_calibration(self):
        self.assertEqual(priority(((1,1),(9,19),(1,2),(17,35))),(3,1,2,0))
        r=configuration(LIGANDS,REFERENCE)
        self.assertEqual(r['determinant'],-48)
        self.assertEqual(r['configuration'],'R')
        # Orientação projetada independente, com4 atrás: área assinada negativa.
        xy=[v[:2]for v in REFERENCE[:3]]
        area=sum(xy[i][0]*xy[(i+1)%3][1]-xy[(i+1)%3][0]*xy[i][1]for i in range(3))
        self.assertLess(area,0)
    def test_rotations_and_reflections(self):
        proper=improper=0
        for perm in permutations(range(3)):
            parity=(-1)**sum(perm[i]>perm[j]for i in range(3)for j in range(i+1,3))
            for signs in product((-1,1),repeat=3):
                det=parity*signs[0]*signs[1]*signs[2]
                transformed=tuple(tuple(signs[i]*v[perm[i]]for i in range(3))for v in REFERENCE)
                r=configuration(LIGANDS,transformed)
                self.assertEqual(r['configuration'],'R'if det==1 else'S')
                proper+=det==1;improper+=det==-1
        self.assertEqual((proper,improper),(24,24))
    def test_relabel_swap_and_translation(self):
        # Reordenar registros em conjunto não troca ligantes fisicamente.
        for perm in permutations(range(4)):
            self.assertEqual(configuration(tuple(LIGANDS[i]for i in perm),tuple(REFERENCE[i]for i in perm))['configuration'],'R')
        swapped=list(REFERENCE);swapped[0],swapped[1]=swapped[1],swapped[0]
        self.assertEqual(configuration(LIGANDS,swapped)['configuration'],'S')
        translated=tuple(tuple(v[i]+(2,-3,1)[i]for i in range(3))for v in REFERENCE)
        self.assertEqual(configuration(LIGANDS,translated)['determinant'],-48)
    def test_contracts(self):
        for bad in ((((6,12),(6,12),(9,19),(1,1))),((True,1),(17,35),(9,19),(1,1)),((35,79),)):
            with self.assertRaises(ValueError):priority(bad)
        with self.assertRaises(ValueError):configuration(LIGANDS,((0,0,0),)*4)
        with self.assertRaises(ValueError):configuration(LIGANDS,((0.,2,1),)+REFERENCE[1:])
        with self.assertRaises(ValueError):configuration(LIGANDS,((21,2,1),)+REFERENCE[1:])
