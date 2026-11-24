import unittest
from fractions import Fraction as F
from itertools import product
from .model import table

class ModelTests(unittest.TestCase):
    def test_cases(self):
        free=table(2,0,3);forced=table(2,2,3)
        self.assertEqual([r['x_m'] for r in free],[0,3,6,9])
        self.assertEqual([r['v_m_s'] for r in free],[3,3,3,3])
        self.assertEqual([r['x_m'] for r in forced],[0,F(7,2),8,F(27,2)])
        self.assertEqual([r['v_m_s'] for r in forced],[3,4,5,6])

    def test_independent_recurrence_and_work_energy(self):
        for m,f,v0,dt in product((F(1),F(2),F(3,2)),(F(-2),F(0),F(2)),(F(-1),F(0),F(3)),(F(1),F(1,3))):
            rows=table(m,f,v0,dt,6)
            for previous,current in zip(rows,rows[1:]):
                self.assertEqual(current['v_m_s']-previous['v_m_s'],f*dt/m)
                self.assertEqual(current['x_m']-previous['x_m'],(current['v_m_s']+previous['v_m_s'])*dt/2)
                delta_k=m*(current['v_m_s']**2-previous['v_m_s']**2)/2
                self.assertEqual(f*(current['x_m']-previous['x_m']),delta_k)

    def test_fractional_times_and_model_difference(self):
        rows=table(2,0,3,F(1,3),9)
        self.assertEqual(rows[-1]['t_s'],3);self.assertEqual(rows[-1]['x_m'],9)
        self.assertEqual(table(2,2,3)[2]['x_m']-table(2,0,3)[2]['x_m'],2)
        self.assertEqual(len(table(2,0,3,1,0)),1)

    def test_contract(self):
        for bad in (True,2.0,'2',None):
            with self.assertRaises(TypeError):table(bad,0,3)
        for mass,dt in ((0,1),(-1,1),(2,0)):
            with self.assertRaises(ValueError):table(mass,0,3,dt)
        with self.assertRaises(TypeError):table(2,0,3,1,True)
        with self.assertRaises(ValueError):table(2,0,3,1,101)
