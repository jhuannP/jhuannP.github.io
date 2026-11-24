import unittest
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import log10
from .experiment import encode,decode,parse_record,summarize,model

class QualityTests(unittest.TestCase):
    def test_ascii_and_restricted_records(self):
        fixture=(Path(__file__).parent/'synthetic.fastq').read_text().splitlines()
        records=[parse_record('\n'.join(fixture[i:i+4])) for i in range(0,len(fixture),4)]
        self.assertEqual([r['qualities'] for r in records],[[20]*6,[40,40,40,40,10,10],[30]*6])
        for q in range(41):
            self.assertEqual(ord(encode([q])),q+33)
            self.assertEqual(decode(chr(q+33)),[q])
        for ending in ('','\n','\r\n'):
            text='@inventada\nACGTAC\n+\n555555'+ending
            self.assertEqual(parse_record(text)['qualities'],[20]*6)
        for text in ('','@x\nA\n+\n','@x\nAA\n+\n5','x\nA\n+\n5','@\nA\n+\n5','@x\nA\n+x\n5','@x\na\n+\n5','@x\nX\n+\n5','@x\nA\n+\nJ','@x\nA\n+\n '):
            with self.assertRaises(ValueError):parse_record(text)
        self.assertEqual(parse_record('@x\nN\n+\n!')['sequence'],'N')

    def test_joint_enumeration(self):
        # Distribuição conjunta independente enumerada, não estimada por Monte Carlo.
        for qs in ([0,10,20],[20]*6,[40,40,40,40,10,10],[30]*6):
            ps=[F(1,10**(q//10)) for q in qs];en=F(0);any_error=F(0);mass=F(0)
            for bits in product((0,1),repeat=len(qs)):
                weight=F(1)
                for bit,p in zip(bits,ps):weight*=p if bit else 1-p
                mass+=weight;en+=sum(bits)*weight
                if any(bits):any_error+=weight
            s=summarize(list(qs));self.assertEqual(mass,1)
            self.assertAlmostEqual(s['expected'],float(en),places=14)
            self.assertAlmostEqual(s['any_independent'],float(any_error),places=14)
            self.assertLessEqual(s['lower'],s['any_independent']+1e-14)
            self.assertLessEqual(s['any_independent'],s['upper']+1e-14)
        # Mesmas marginais, mas erros perfeitamente correlacionados: produto não se aplica.
        self.assertAlmostEqual(summarize([10,10])['expected'],.2)
        self.assertAlmostEqual(summarize([10,10])['any_independent'],.19)
        self.assertNotEqual(.19,.1)

    def test_profiles_thresholds_and_invariants(self):
        self.assertAlmostEqual(model()['rows'][0]['expected'],.06)
        self.assertAlmostEqual(model()['rows'][1]['expected'],.2004)
        self.assertGreater(model()['rows'][1]['mean_q'],model()['rows'][0]['mean_q'])
        self.assertEqual(model()['retained_count'],2)
        for shift in range(-10,1):
            prev=-1
            for j in range(61):
                m=model(1,shift,j/20)
                self.assertGreaterEqual(m['retained_count'],prev);prev=m['retained_count']
                for row in m['rows']:
                    self.assertEqual(row['retained'],row['expected']<=j/20)
                    self.assertAlmostEqual(row['expected'],model(row['case'],0,0)['selected']['expected']*10**(-shift/10),places=13)
            self.assertEqual(model(0,shift,1)['rows'],model(2,shift,1)['rows'])
        for q in range(41):
            s=summarize([q]);self.assertAlmostEqual(-10*log10(s['ps'][0]),q,places=12)
            self.assertAlmostEqual(s['effective_q'],q,places=12)
        s=model()['selected'];self.assertEqual(model(1,0,s['expected'])['selected']['retained'],True)
        self.assertFalse(model(1,0,s['expected']-1e-8)['selected']['retained'])

    def test_invalid_inputs(self):
        for qs in ([],[-1],[41],[1.5],[True],'555',None):
            with self.assertRaises(ValueError):summarize(qs)
        for args in ((3,0,.1),(0,-11,.1),(0,1,.1),(0,.5,.1),(True,0,.1),(0,0,-1),(0,0,float('nan')),(0,0,True)):
            with self.assertRaises(ValueError):model(*args)
