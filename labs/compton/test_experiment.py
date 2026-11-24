import json,math,unittest
from pathlib import Path
from .experiment import model


class ComptonTests(unittest.TestCase):
    def test_independent_mass_shell_root(self):
        rows=json.loads(Path(__file__).with_name('decimal_reference.json').read_text())
        self.assertEqual(len(rows),20)
        for row in rows:
            s=model(row['alpha'],row['angle'])
            self.assertAlmostEqual(s['scattered'],float(row['scattered']),delta=5e-16)
            self.assertAlmostEqual(s['kinetic'],float(row['kinetic']),delta=5e-16)

    def test_energy_vector_momentum_and_mass(self):
        for alpha in (.1,.5,1,2):
            for angle in range(0,181,15):
                s=model(alpha,angle)
                self.assertAlmostEqual(s['scattered']+s['electron_energy'],alpha+1,delta=2e-15)
                self.assertAlmostEqual(s['photon_x']+s['electron_x'],alpha,delta=2e-15)
                self.assertEqual(s['photon_y']+s['electron_y'],0)
                self.assertAlmostEqual(s['mass_squared'],1,delta=6e-15)
                self.assertLess(s['beta'],1)
                p2=s['electron_x']**2+s['electron_y']**2
                self.assertAlmostEqual(p2/(s['electron_energy']+1),s['kinetic'],delta=1e-15)

    def test_shift_monotonicity_and_limits(self):
        for alpha in (.1,.5,1,2):
            states=[model(alpha,t) for t in range(181)]
            self.assertTrue(all(a['scattered']>=b['scattered'] for a,b in zip(states,states[1:])))
            self.assertTrue(all(a['kinetic']<=b['kinetic'] for a,b in zip(states,states[1:])))
            for s in states:
                self.assertAlmostEqual(s['wavelength_out']-s['wavelength_in'],s['d'],delta=2e-15)
                self.assertAlmostEqual(s['photon_fraction']+s['electron_fraction'],1,delta=3e-16)
                self.assertGreaterEqual(s['d'],0);self.assertLessEqual(s['d'],2)
            self.assertAlmostEqual(states[-1]['kinetic'],2*alpha**2/(1+2*alpha),delta=1e-15)
        for t in (0,30,90,180):self.assertEqual(model(.1,t)['d'],model(2,t)['d'])

    def test_small_angles_recoil_and_domain(self):
        s=model(1,0)
        self.assertEqual(s['scattered'],1);self.assertEqual(s['kinetic'],0)
        self.assertIsNone(s['recoil_angle'])
        self.assertEqual(model(1,180)['recoil_angle'],0)
        s=model(1,90)
        self.assertAlmostEqual(s['scattered'],.5,delta=2e-16)
        self.assertAlmostEqual(s['electron_x'],1,delta=3e-16)
        self.assertAlmostEqual(s['electron_y'],-.5,delta=2e-16)
        tiny=model(1,1e-9);expected=math.radians(1e-9)**2/2
        self.assertGreater(tiny['kinetic'],0)
        self.assertLess(abs(tiny['kinetic']/expected-1),1e-14)
        self.assertEqual(1-tiny['scattered'],0) # Subtraction loses the transfer; stable formula does not.
        for args in ((0,90),(3,90),(1,-1),(1,181),(float('nan'),90)):
            with self.assertRaises(ValueError):model(*args)
