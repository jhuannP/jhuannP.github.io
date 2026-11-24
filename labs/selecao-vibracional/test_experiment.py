import itertools
import runpy
from pathlib import Path
import unittest
from fractions import Fraction as F
from .experiment import OPS,NAMES,CHARACTERS,CHANNELS,model

class VibrationalSelectionTests(unittest.TestCase):
    def test_operator_characters_by_coordinate_evaluation(self):
        # Avalia as funções em pontos, independentemente da potência dos sinais.
        functions=(lambda x,y,z:x,lambda x,y,z:y,lambda x,y,z:z,
                   lambda x,y,z:x*x,lambda x,y,z:y*y,lambda x,y,z:z*z,
                   lambda x,y,z:x*y,lambda x,y,z:x*z,lambda x,y,z:y*z)
        for p in ((2,3,5),(-3,2,7),(5,-7,-2)):
            for ch,f in enumerate(functions):
                chars=[]
                for signs in OPS:
                    moved=[a*b for a,b in zip(p,signs)]
                    chars.append(F(f(*moved),f(*p)))
                self.assertEqual(tuple(chars),model(0,ch)['operator_character'])
    def test_group_products_projection_and_cancellation(self):
        for irrep,ch in itertools.product(range(4),range(9)):
            r=model(irrep,ch)
            self.assertEqual(r['allowed'],r['mode_character']==r['operator_character'])
            self.assertEqual(r['a1_multiplicity'],int(r['product_irrep']=='A1'))
            self.assertEqual(sum(r['product_character']),4 if r['allowed'] else 0)
            if not r['allowed']:
                self.assertEqual(r['product_character'].count(1),2)
                self.assertEqual(r['product_character'].count(-1),2)
        for a,b,c in itertools.product(CHARACTERS,repeat=3):
            product=tuple(x*y*z for x,y,z in zip(a,b,c))
            self.assertIn(product,CHARACTERS)
    def test_channels_and_existing_ab2_decomposition(self):
        expected=(('z',),(),('x',),('y',))
        raman=(('xx','yy','zz'),('xy',),('xz',),('yz',))
        build=runpy.run_path(str(Path(__file__).parents[1]/'deslocamentos-simetria'/'experiment.py'))['build']
        decomposition=build('bent')['multiplicities']
        self.assertEqual(decomposition,{'A1':2,'A2':0,'B1':1,'B2':0})
        for i,name in enumerate(NAMES):
            r=model(i,0)
            self.assertEqual(r['ir_components'],expected[i]);self.assertEqual(r['raman_components'],raman[i])
            self.assertEqual(r['ab2_multiplicity'],decomposition[name])
        self.assertEqual(sum(decomposition[name] for i,name in enumerate(NAMES) if model(i,0)['ir_components']),3)
        self.assertEqual(sum(decomposition[name] for i,name in enumerate(NAMES) if model(i,0)['raman_components']),3)
    def test_contract(self):
        for bad in (-1,4,True,.5,None,'A1'):
            with self.assertRaises(ValueError):model(bad,0)
        for bad in (-1,9,True,.5,None,'x'):
            with self.assertRaises(ValueError):model(0,bad)
