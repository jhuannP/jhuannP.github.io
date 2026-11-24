import unittest
from fractions import Fraction as F
from .source import circuit,max_power

class SourceTests(unittest.TestCase):
    def test_fixtures_and_boundaries(self):
        r=circuit(12,2,6)
        self.assertEqual((r['current'],r['voltage'],r['load_power'],r['internal_power'],r['source_power'],r['efficiency']),
                         (F(3,2),9,F(27,2),F(9,2),18,F(3,4)))
        r=circuit(12,2,2);self.assertEqual((r['load_power'],r['efficiency']),(18,F(1,2)))
        opened=circuit(12,2,None);self.assertEqual(opened['voltage'],12);self.assertIsNone(opened['efficiency'])
        self.assertEqual(circuit(12,2,0)['load_power'],0)
        self.assertEqual(circuit(12,0,6)['efficiency'],1)

    def test_energy_and_maximum_identity(self):
        for emf in (1,4,12):
            for internal in (F(1,2),2,5):
                for load in range(13):
                    r=circuit(emf,internal,load)
                    self.assertEqual(r['source_power'],r['load_power']+r['internal_power'])
                    self.assertEqual(r['voltage'],emf-r['current']*internal)
                    gap=F(emf)*emf*(load-internal)**2/(4*internal*(load+internal)**2)
                    self.assertEqual(max_power(emf,internal)-r['load_power'],gap)
                    self.assertGreaterEqual(gap,0)
                    self.assertEqual(gap==0,load==internal)

    def test_scaling_and_tradeoff(self):
        base=circuit(12,2,6)
        for k in (F(1,3),2,5):
            a=circuit(12*k,2,6);b=circuit(12,2*k,6*k)
            self.assertEqual(a['current'],k*base['current']);self.assertEqual(a['load_power'],k*k*base['load_power'])
            self.assertEqual(b['voltage'],base['voltage']);self.assertEqual(b['load_power'],base['load_power']/k)
            self.assertEqual(b['efficiency'],base['efficiency'])
        self.assertGreater(circuit(12,2,6)['efficiency'],circuit(12,2,2)['efficiency'])
        self.assertLess(circuit(12,2,6)['load_power'],circuit(12,2,2)['load_power'])
        # Fonte ideal com r=0: reduzir R aumenta potência, sem máximo finito.
        self.assertGreater(circuit(12,0,1)['load_power'],circuit(12,0,2)['load_power'])

    def test_contracts(self):
        for args in ((True,2,6),(0,2,6),(12,-1,6),(12,0,0),(12,2,-1),(12,2,0.5)):
            with self.assertRaises(ValueError):circuit(*args)
        with self.assertRaises(ValueError):max_power(12,0)
