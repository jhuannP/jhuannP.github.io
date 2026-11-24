import unittest
from fractions import Fraction as Q
from .transport import apical_readout,recovery

class TransportTests(unittest.TestCase):
    def test_reference_and_volume_counterexample(self):
        a=apical_readout(12,2,Q(1,2),1,2)
        b=apical_readout(7,2,Q(1,2),1,2)
        self.assertEqual(a,{'mass_ug':Q(5),'apparent_rate_ug_cm2_h':Q(5,2)})
        self.assertEqual(b['apparent_rate_ug_cm2_h']/a['apparent_rate_ug_cm2_h'],Q(1,2))
        self.assertEqual(apical_readout(7,2,1,1,2),a)
    def test_units_and_additive_blank(self):
        for volume in [Q(1,4),Q(1,2),Q(1),Q(2)]:
            for area in [Q(1,2),Q(1),Q(3)]:
                for hours in [Q(1,2),Q(2),Q(5)]:
                    v=apical_readout(12,2,volume,area,hours)
                    self.assertEqual(v['mass_ug'],10*volume)
                    self.assertEqual(v['apparent_rate_ug_cm2_h']*area*hours,v['mass_ug'])
                    self.assertEqual(apical_readout(17,7,volume,area,hours),v)
    def test_recovery_flags_without_clipping(self):
        self.assertEqual(recovery(20,12,5,1),{'fraction':Q(9,10),'unaccounted_ug':Q(2),'over_recovery':False})
        self.assertEqual(recovery(20,16,5,1),{'fraction':Q(11,10),'unaccounted_ug':Q(-2),'over_recovery':True})
        self.assertEqual(recovery(20,0,0,0)['fraction'],0)
    def test_contracts(self):
        self.assertEqual(apical_readout(2,2,1,1,1)['mass_ug'],0)
        for args in [(1,2,1,1,1),(2,0,0,1,1),(2,0,1,0,1),(2,0,1,1,0),(2,-1,1,1,1),(True,0,1,1,1),(float('nan'),0,1,1,1),(2,0,1.0,1,1)]:
            with self.assertRaises(ValueError):apical_readout(*args)
        for args in [(0,0,0,0),(1,-1,0,0),(1,0,False,0)]:
            with self.assertRaises(ValueError):recovery(*args)
if __name__=='__main__':unittest.main()
