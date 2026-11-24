import importlib.util
import itertools
import unittest
from decimal import Decimal as D,localcontext
from pathlib import Path
spec=importlib.util.spec_from_file_location('photo',Path(__file__).with_name('experiment.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class PhotoTests(unittest.TestCase):
    def test_energy_units_and_threshold(self):
        for ratio,work in itertools.product([.5,1,1.5,2],[1,2,5]):
            r=m.model(ratio,work)
            self.assertAlmostEqual(m.H*r['frequency_hz']/m.E,r['photon_ev'])
            self.assertAlmostEqual(r['frequency_hz']*r['wavelength_nm']*1e-9,m.C,delta=1e-7)
            if ratio<1:self.assertIsNone(r['kinetic_ev']);self.assertEqual(r['emitted_rate'],0)
            else:self.assertAlmostEqual(r['photon_ev'],work+r['kinetic_ev'])
            if ratio==1:self.assertEqual(r['kinetic_ev'],0);self.assertIsNone(r['current_a'])

    def test_intensity_and_frequency_are_distinct(self):
        low=m.model(1.5,2,2);high=m.model(1.5,2,4)
        self.assertEqual(low['kinetic_ev'],high['kinetic_ev'])
        self.assertEqual(high['photon_rate'],2*low['photon_rate'])
        self.assertEqual(high['current_a'],2*low['current_a'])
        faster=m.model(2,2,2)
        self.assertGreater(faster['kinetic_ev'],low['kinetic_ev'])
        self.assertLess(faster['photon_rate'],low['photon_rate'])
        for i in [0,1,10]:self.assertEqual(m.model(.5,2,i)['emitted_rate'],0)

    def test_independent_decimal_references(self):
        with localcontext() as ctx:
            ctx.prec=60;h=D('6.62607015e-34');e=D('1.602176634e-19')
            for ratio,work,irr in itertools.product(['0.5','1','1.5','2'],['1','2','5'],['0','2','10']):
                r=m.model(float(ratio),float(work),float(irr))
                energy=D(ratio)*D(work)*e
                f=energy/h;rate=D(irr)*D('1e-6')/energy
                for actual,ref in [(r['frequency_hz'],f),(r['photon_rate'],rate)]:
                    self.assertAlmostEqual(actual,float(ref),delta=max(1,abs(float(ref)))*2e-15)
                if D(ratio)>1:
                    current=e*D('0.2')*rate
                    self.assertAlmostEqual(r['current_a'],float(current),delta=1e-21)

    def test_light_off_and_domain(self):
        for ratio in [.5,1,1.5]:
            r=m.model(ratio,2,0)
            self.assertEqual(r['photon_rate'],0);self.assertEqual(r['emitted_rate'],0);self.assertEqual(r['current_a'],0)
        # Energia por evento possível é distinta de evento observado.
        self.assertEqual(m.model(1.5,2,0)['kinetic_ev'],1)
        for args in [(0,2,2),(1,0,2),(1,2,-1),(float('nan'),2,2)]:
            with self.assertRaises(ValueError):m.model(*args)

if __name__=='__main__':unittest.main()
