import unittest
from fractions import Fraction as Q
from itertools import product
from copy import deepcopy
from balance import total, balanced, residuals, ACID_LEFT, ACID_RIGHT


class BalanceTests(unittest.TestCase):
    def test_half_reactions_and_sum(self):
        self.assertTrue(balanced({'MnO4-':1,'H+':8,'e-':5},{'Mn2+':1,'H2O':4}))
        self.assertTrue(balanced({'Fe2+':1},{'Fe3+':1,'e-':1}))
        self.assertTrue(balanced(ACID_LEFT,ACID_RIGHT))
        self.assertEqual(total(ACID_LEFT),dict(Mn=1,Fe=5,O=4,H=8,charge=17))
        # A reaction can conserve every atom and still violate charge.
        wrong=residuals({'MnO4-':1,'Fe2+':4,'H+':8},{'Mn2+':1,'Fe3+':4,'H2O':4})
        self.assertEqual(wrong,dict(Mn=0,Fe=0,O=0,H=0,charge=-1))

    def test_unique_normalized_integer_candidate(self):
        # Independent enumeration of positive integer coefficients with Mn fixed at 1.
        found=[]
        for iron,hydrogen,water in product(range(1,13),range(1,17),range(1,9)):
            if balanced({'MnO4-':1,'Fe2+':iron,'H+':hydrogen},
                        {'Mn2+':1,'Fe3+':iron,'H2O':water}):
                found.append((iron,hydrogen,water))
        self.assertEqual(found,[(5,8,4)])

    def test_scale_and_same_species_on_both_sides(self):
        for scale in (Q(1,3),Q(1,2),Q(1),Q(2),Q(7)):
            left={k:scale*v for k,v in ACID_LEFT.items()}
            right={k:scale*v for k,v in ACID_RIGHT.items()}
            self.assertTrue(balanced(left,right))
            for extra in (Q(1,2),Q(1),Q(4)):
                a,b=deepcopy(left),deepcopy(right)
                a['H2O']=extra;b['H2O']+=extra
                self.assertTrue(balanced(a,b))
                self.assertEqual(left,{k:scale*v for k,v in ACID_LEFT.items()})

    def test_acid_to_basic_oxygen(self):
        self.assertTrue(balanced({'O2':1,'H+':4,'e-':4},{'H2O':2}))
        self.assertTrue(balanced({'O2':1,'H2O':2,'e-':4},{'OH-':4}))
        # Charge is -4 on both sides of the basic half reaction.
        self.assertEqual(total({'O2':1,'H2O':2,'e-':4})['charge'],-4)

    def test_contracts(self):
        for side in ({}, {'H2O':0},{'H2O':True},{'H2O':-1},{'H2O':1.0},
                     {'H2O':float('nan')},{'XYZ':1},[],None):
            with self.assertRaises(ValueError): total(side)


if __name__=='__main__': unittest.main()
