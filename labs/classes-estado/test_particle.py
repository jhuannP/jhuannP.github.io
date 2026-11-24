"""Verificação didática: lei fechada, identidade e rejeição sem mutação."""
from fractions import Fraction as Q
from itertools import product
import unittest
from particle import ParticulaMRU


class Checks(unittest.TestCase):
    def test_against_closed_form(self):
        for x, v, dt in product([Q(k,2) for k in range(-4,5)],
                                [Q(k,2) for k in range(-4,5)],
                                [Q(k,4) for k in range(9)]):
            p=ParticulaMRU(float(x),float(v))
            self.assertIsNone(p.avancar(float(dt)))
            self.assertEqual(Q(p.x),x+v*dt)
            self.assertEqual(Q(p.v),v)

    def test_time_composition(self):
        for x,v,a,b in product((-1,0,1),(-2,0,2),(0,.25,.5,1,2),(0,.25,.5,1,2)):
            p,q=ParticulaMRU(x,v),ParticulaMRU(x,v)
            p.avancar(a);p.avancar(b);q.avancar(a+b)
            self.assertEqual(p.x,q.x)
            self.assertEqual(p.v,q.v)

    def test_alias_and_return(self):
        p,q=ParticulaMRU(1,2),ParticulaMRU(0,-1)
        r=p
        self.assertIs(p,r);self.assertIsNot(p,q)
        result=p.avancar(3)
        self.assertEqual((p.x,r.x,q.x),(7,7,0))
        self.assertIsNone(result)
        p=p.avancar(1)
        self.assertIsNone(p)
        self.assertEqual(r.x,9)

    def test_invalid_input_preserves_state(self):
        for bad in (-1,True,False,'2',complex(1),float('inf'),float('-inf'),float('nan'),10**400):
            p=ParticulaMRU(1,2)
            with self.assertRaises(ValueError):p.avancar(bad)
            self.assertEqual((p.x,p.v),(1,2))
        for bad in (True,'2',complex(1),float('inf'),float('nan'),10**400):
            with self.assertRaises(ValueError):ParticulaMRU(bad,2)
            with self.assertRaises(ValueError):ParticulaMRU(1,bad)

    def test_overflow_preserves_state(self):
        # Multiplication overflow and addition overflow, separately.
        for x,v,dt in [(1,1e308,2),(1e308,1e308,1)]:
            p=ParticulaMRU(x,v)
            with self.assertRaises(ValueError):p.avancar(dt)
            self.assertEqual((p.x,p.v),(x,v))

    def test_list_ownership_example(self):
        class Shared:
            history=[]
            def append(self,x):self.history.append(x)
        class Own:
            def __init__(self):self.history=[]
            def append(self,x):self.history.append(x)
        a,b=Shared(),Shared();a.append(7)
        self.assertIs(a.history,b.history)
        self.assertEqual(b.history,[7])
        a,b=Own(),Own();a.append(7)
        self.assertIsNot(a.history,b.history)
        self.assertEqual(a.history,[7]);self.assertEqual(b.history,[])


if __name__=='__main__':unittest.main()
