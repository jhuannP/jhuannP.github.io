import unittest
from fractions import Fraction as Q
from .optics import snell,critical_sine,angle_degrees,thin_lens


class OpticsTests(unittest.TestCase):
    def test_normal_and_known_angles(self):
        r=snell(1,Q(3,2),Q(1,2))
        self.assertEqual((r['regime'],r['sine_transmitted']),('propagante',Q(1,3)))
        self.assertAlmostEqual(angle_degrees(Q(1,3)),19.47122063449069,delta=1e-12)
        self.assertAlmostEqual(angle_degrees(Q(1,2)),30,delta=1e-12)
        self.assertEqual(snell(1,2,0)['sine_transmitted'],0)
        self.assertEqual(angle_degrees(1),90)

    def test_critical_and_exact_neighbor_classification(self):
        critical=critical_sine(2,1)
        self.assertEqual(critical,Q(1,2))
        self.assertEqual(snell(2,1,critical)['regime'],'rasante')
        tiny=Q(1,2**200)
        self.assertEqual(snell(2,1,critical-tiny)['regime'],'propagante')
        self.assertEqual(snell(2,1,critical+tiny)['regime'],'total')
        self.assertIsNone(snell(2,1,Q(3,4))['sine_transmitted'])
        self.assertIsNone(critical_sine(1,2))
        self.assertIsNone(critical_sine(1,1))

    def test_snell_reciprocity_when_transmitted(self):
        for n1 in [Q(1),Q(3,2),Q(2)]:
            for n2 in [Q(1),Q(3,2),Q(2)]:
                for i in range(10):
                    incident=Q(i,10);r=snell(n1,n2,incident)
                    self.assertEqual(r['sine_reflected'],incident)
                    if r['regime']=='propagante':
                        transmitted=r['sine_transmitted']
                        self.assertEqual(n1*incident,n2*transmitted)
                        self.assertEqual(snell(n2,n1,transmitted)['sine_transmitted'],incident)
                        if n2>n1 and incident:self.assertLess(transmitted,incident)

    def test_lens_real_virtual_and_focal(self):
        self.assertEqual(thin_lens(2,4),dict(kind='real',q=Q(4),magnification=Q(-1)))
        self.assertEqual(thin_lens(2,1),dict(kind='virtual',q=Q(-2),magnification=Q(2)))
        self.assertEqual(thin_lens(-2,4),dict(kind='virtual',q=Q(-4,3),magnification=Q(1,3)))
        self.assertEqual(thin_lens(2,2),dict(kind='sem_imagem_finita',q=None,magnification=None))

    def test_lens_identity_and_unit_conversion(self):
        for f in [-3,-2,-1,1,2,3]:
            for p in [Q(i,2) for i in range(1,21)]:
                r=thin_lens(f,p)
                if r['q'] is not None:
                    self.assertEqual(Q(1,f),1/p+1/r['q'])
                    self.assertEqual(r['magnification'],-r['q']/p)
                    scaled=thin_lens(Q(f,100),p/100)
                    self.assertEqual(scaled['q'],r['q']/100)
                    self.assertEqual(scaled['magnification'],r['magnification'])

    def test_contracts(self):
        for args in [(0,1,0),(1,-1,0),(1,1,True),(1,1,1),(1,1,-1),(1,1,0.5)]:
            with self.assertRaises(ValueError):snell(*args)
        for value in [-1,Q(3,2),True]:
            with self.assertRaises(ValueError):angle_degrees(value)
        for args in [(0,1),(1,0),(1,-1),(True,1),(1,1.0)]:
            with self.assertRaises(ValueError):thin_lens(*args)

if __name__=='__main__':unittest.main()
