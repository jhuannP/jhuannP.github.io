import unittest
from fractions import Fraction as Q
from .wave import parameters,phase_cycles,phase_marker,interface,pressure_intensity_ratio


class WaveTests(unittest.TestCase):
    def test_original_scales_and_crest_motion(self):
        p=parameters(5,2)
        self.assertEqual((p['speed'],p['period']),(10,Q(1,5)))
        self.assertEqual(phase_marker(0,0),Q(1,2))
        self.assertEqual(phase_marker(0,Q(1,20)),1)
        self.assertEqual((phase_marker(0,Q(1,20))-phase_marker(0,0))/Q(1,20),10)
        self.assertEqual(phase_cycles(Q(1,2),0),Q(1,4))
        self.assertEqual(phase_cycles(Q(1,2),Q(1,20)),0)

    def test_periodicity_and_phase_markers(self):
        for f in [Q(1,2),Q(1),Q(5),Q(10)]:
            for wavelength in [Q(1,3),Q(2),Q(5)]:
                p=parameters(f,wavelength)
                for x in [Q(i,4) for i in range(-4,9)]:
                    for t in [Q(i,20) for i in range(7)]:
                        phase=phase_cycles(x,t,f,wavelength)
                        self.assertTrue(0<=phase<1)
                        self.assertEqual(phase_cycles(x,t+p['period'],f,wavelength),phase)
                        self.assertEqual(phase_cycles(x+wavelength,t,f,wavelength),phase)
                for index in range(-2,3):
                    for t in [Q(0),Q(1,20),Q(1,3)]:
                        marker=phase_marker(index,t,f,wavelength)
                        self.assertEqual(phase_cycles(marker,t,f,wavelength),Q(1,4))
                        self.assertEqual(phase_marker(index+1,t,f,wavelength)-marker,wavelength)

    def test_interface_frequency_is_input_hypothesis(self):
        for f in [1,5,10]:
            for v1 in [5,10,20]:
                for v2 in [5,10,20]:
                    r=interface(f,v1,v2)
                    self.assertEqual(r['frequency'],f)
                    self.assertEqual(r['wavelength_after']/r['wavelength_before'],Q(v2,v1))
                    self.assertEqual(r['period'],Q(1,f))
        self.assertEqual(interface(5,10,20)['wavelength_after'],4)

    def test_unit_changes_preserve_phase(self):
        for x,t in [(Q(1,2),Q(1,20)),(Q(-3,2),Q(7,10))]:
            self.assertEqual(phase_cycles(x,t,5,2),phase_cycles(100*x,t,5,200))
        self.assertEqual(parameters(5,200)['speed']/100,parameters(5,2)['speed'])
        self.assertEqual(pressure_intensity_ratio(Q(1,1000),Q(2,1000)),pressure_intensity_ratio(1,2))

    def test_pressure_amplitude_is_not_frequency(self):
        self.assertEqual(pressure_intensity_ratio(1,2),4)
        self.assertEqual(pressure_intensity_ratio(2,1),Q(1,4))
        self.assertEqual(pressure_intensity_ratio(1,0),0)

    def test_contracts(self):
        for args in [(0,2),(5,-1),(True,2),(5,2.0)]:
            with self.assertRaises(ValueError):parameters(*args)
        with self.assertRaises(ValueError):phase_cycles(0,-1)
        with self.assertRaises(ValueError):phase_marker(True,0)
        with self.assertRaises(ValueError):interface(5,0,10)
        for args in [(0,1),(1,-1),(1,True)]:
            with self.assertRaises(ValueError):pressure_intensity_ratio(*args)

if __name__=='__main__':unittest.main()
