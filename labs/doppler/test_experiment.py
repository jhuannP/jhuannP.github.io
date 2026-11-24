import unittest
from fractions import Fraction as Q
from .experiment import doppler,arrival

class DopplerTests(unittest.TestCase):
    def test_time_of_flight_independent_events(self):
        # Cada frente sai da posição da fonte no instante de emissão.
        for vs in (-100,0,34,100):
            for vo in (-100,0,34,100):
                data=doppler(340,100,vs,vo)
                events=[arrival(n,340,340,100,vs,vo) for n in range(7)]
                for event in events:
                    self.assertGreater(event['arrival'],event['emission'])
                    self.assertEqual(event['source_x']+340*(event['arrival']-event['emission']),event['observer_x'])
                gaps=[b['arrival']-a['arrival'] for a,b in zip(events,events[1:])]
                self.assertEqual(len(set(gaps)),1)
                self.assertEqual(1/gaps[0],data['frequency'])

    def test_signs_and_common_motion(self):
        self.assertEqual(doppler(340,100,34,0)['frequency'],Q(1000,9))
        self.assertEqual(doppler(340,100,0,-34)['frequency'],110)
        self.assertEqual(doppler(340,100,0,34)['frequency'],90)
        for speed in (-100,0,34,100):self.assertEqual(doppler(340,100,speed,speed)['frequency'],100)
        # Mesma velocidade relativa, porém movimento diferente em relação ao meio.
        self.assertNotEqual(doppler(340,100,34,0)['frequency'],doppler(340,100,0,-34)['frequency'])

    def test_distance_changes_delay_not_frequency(self):
        for distance in (34,340,680):
            first=arrival(0,distance,340,100,34,-34)
            second=arrival(1,distance,340,100,34,-34)
            self.assertEqual(first['arrival'],Q(distance,374))
            self.assertEqual(second['arrival']-first['arrival'],Q(9,1100))
        self.assertEqual(doppler(340,100,34,-34)['wavelength'],Q(153,50))

    def test_contracts_and_wrong_branch(self):
        for args in ((0,100,0,0),(340,0,0,0),(340,100,340,0),(340,100,0,-340),(340,100,True,0)):
            with self.assertRaises(ValueError):doppler(*args)
        for n in (-1,101,True,Q(1,2)):
            with self.assertRaises(ValueError):arrival(n,340,340,100,0,0)
        with self.assertRaises(ValueError):arrival(100,1,340,100,100,0)
