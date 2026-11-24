import unittest
from fractions import Fraction as Q
from dataclasses import FrozenInstanceError
from itertools import product
from statistics import mean
from .readings import Leituras


class ValueReadings(unittest.TestCase):
    def test_snapshot_and_new_value_example(self):
        origem=[1,2,3];a=Leituras('m',origem);origem[0]=100;origem.append(7)
        b=a.com_acrescimo(6)
        self.assertEqual(a.valores,(1,2,3));self.assertEqual(a.media,2)
        self.assertEqual(b.valores,(1,2,3,6));self.assertEqual(b.media,3)
        self.assertEqual(b.desvios,(-2,-1,0,3))
        self.assertIsNot(a,b)
        self.assertIsInstance(a.valores,tuple)
        self.assertTrue(all(type(x) is Q for x in a.valores))

    def test_exhaustive_small_samples_against_statistics(self):
        count=0
        for n in range(1,5):
            for values in product([-1,0,2],repeat=n):
                a=Leituras('m',values);count+=1
                self.assertEqual(a.media,mean(list(map(Q,values))))
                self.assertEqual(sum(a.desvios),0)
                self.assertEqual(tuple(a.desvios[i]+a.media for i in range(n)),values)
                reversed_a=Leituras('m',tuple(reversed(values)))
                self.assertEqual(a.media,reversed_a.media)
                shifted=Leituras('m',tuple(v+5 for v in values))
                self.assertEqual(shifted.media,a.media+5)
                self.assertEqual(shifted.desvios,a.desvios)
        self.assertEqual(count,120)

    def test_composition_preserves_order_units_and_weighted_mean(self):
        for n,m in product(range(1,5),repeat=2):
            a=Leituras('s',tuple(range(n)));b=Leituras('s',tuple(-v for v in range(m)))
            c=a.juntar(b)
            self.assertEqual(c.valores,tuple(range(n))+tuple(-v for v in range(m)))
            self.assertEqual(c.media,(n*a.media+m*b.media)/(n+m))
            self.assertEqual(c.unidade,'s')
            self.assertEqual(a.valores,tuple(range(n)))
            self.assertEqual(b.valores,tuple(-v for v in range(m)))
        x=Leituras('m',[0,2]);y=Leituras('m',[10])
        self.assertEqual(x.juntar(y).media,4)
        self.assertNotEqual(x.juntar(y).media,(x.media+y.media)/2)

    def test_value_equality_hash_and_order_semantics(self):
        a=Leituras('m',[1,2,3]);b=Leituras('m',[Q(1),Q(2),Q(3)])
        self.assertEqual(a,b);self.assertIsNot(a,b)
        table={a:'original'};self.assertEqual(table[b],'original')
        h=hash(a);a.com_acrescimo(6);self.assertEqual(hash(a),h)
        self.assertNotEqual(a,Leituras('s',[1,2,3]))
        self.assertNotEqual(a,Leituras('m',[3,2,1]))
        self.assertEqual(a.media,Leituras('m',[3,2,1]).media)

    def test_ordinary_mutation_blocked_and_failure_leaves_original(self):
        a=Leituras('m',[1,2,3]);before=a.valores
        with self.assertRaises(FrozenInstanceError):a.unidade='s'
        with self.assertRaises(FrozenInstanceError):a.valores=(9,)
        with self.assertRaises(TypeError):a.valores[0]=9
        with self.assertRaises(ValueError):a.com_acrescimo(True)
        with self.assertRaises(ValueError):a.juntar(Leituras('s',[1]))
        with self.assertRaises(TypeError):a.juntar([1])
        self.assertEqual(a.valores,before);self.assertEqual(a.unidade,'m')

    def test_contracts_and_type_hints_not_runtime_validation(self):
        for unit in ['cm','M','',None,True,['m']]:
            with self.assertRaises(ValueError):Leituras(unit,[1])
        for values in [[],(),None,'123',(True,),(.5,),('1',),([1],),iter([1])]:
            with self.assertRaises(ValueError):Leituras('m',values)
        self.assertEqual(Leituras('m',[Q(1,3),Q(2,3)]).media,Q(1,2))
        self.assertEqual(Leituras('m',[-2,0,2]).media,0)
