import unittest
from math import cos,sin,pi
from .experiment import evaluate,beat_metrics,standing_energy,A,F,K,OMEGA

class WaveSuperpositionTests(unittest.TestCase):
    def test_sum_product_and_wave_equation(self):
        for x in (0,.17,.25,.5,1):
            for t in (0,.03125,.13,.5):
                for phase in (0,.5,1,2):
                    r=evaluate(0,x,t,phase)
                    reference=2*A*cos(pi*phase/2)*cos(K*x-OMEGA*t+pi*phase/2)
                    self.assertAlmostEqual(r['total'],reference,places=14)
                r=evaluate(1,x,t)
                self.assertAlmostEqual(r['total'],2*A*cos(K*x)*cos(OMEGA*t),places=14)
        # Verificação por diferenças centrais, independente da identidade trigonométrica.
        x,t,h=.19,.047,1e-5
        fn=lambda x,t:evaluate(1,x,t)['total']
        dtt=(fn(x,t+h)-2*fn(x,t)+fn(x,t-h))/h**2
        dxx=(fn(x+h,t)-2*fn(x,t)+fn(x-h,t))/h**2
        self.assertAlmostEqual(dtt,F*F*dxx,delta=2e-5)

    def test_nodes_are_zero_for_all_times_and_boundaries(self):
        for x in (.25,.75):
            for t in (0,.013,.03125,.19,.5):
                self.assertAlmostEqual(evaluate(1,x,t)['total'],0,places=14)
                self.assertAlmostEqual(evaluate(1,x,t)['envelope'],0,places=14)
        self.assertAlmostEqual(evaluate(1,0,1/(4*F))['total'],0,places=14)
        self.assertEqual(evaluate(1,0,0)['envelope'],2*A) # Zero instantâneo não é nó.
        self.assertAlmostEqual(evaluate(0,.1,.1,1)['envelope'],0,places=14)
        # Família senoidal independente para corda fixa, não o cosseno da janela.
        for n in (1,2,3):
            for x in (0,2):self.assertAlmostEqual(sin(n*pi*x/2),0,places=14)

    def test_beats_envelope_and_equal_frequency_limit(self):
        for df in (.25,.5,1,2):
            T=beat_metrics(df)['beat_period']
            self.assertEqual(T,1/df)
            for t in (0,.13,.5,1,2):
                r=evaluate(2,0,t,df=df)
                ref=2*A*cos(pi*df*t)*cos(2*pi*(F+df/2)*t)
                self.assertAlmostEqual(r['total'],ref,places=14)
                self.assertLessEqual(abs(r['total']),r['envelope']+1e-14)
                self.assertAlmostEqual(r['envelope'],evaluate(2,0,t+T,df=df)['envelope'],places=14)
            self.assertAlmostEqual(evaluate(2,0,T/2,df=df)['envelope'],0,places=14)
        self.assertIsNone(beat_metrics(0)['beat_period'])
        self.assertEqual(evaluate(2,0,.13,df=0)['envelope'],2*A)

    def test_energy_flux_and_invalid_domain(self):
        N=1024
        for x in (0,.17,.25,.5):
            rows=[standing_energy(x,j/(F*N)) for j in range(N)]
            self.assertAlmostEqual(sum(r['power'] for r in rows)/N,0,places=12)
            self.assertAlmostEqual(sum(r['density'] for r in rows)/N,A*A*OMEGA*OMEGA,places=12)
        self.assertGreater(standing_energy(.25,0)['density'],0) # Energia elástica num nó.
        for mode,df in [(3,1),(1,-1)]:
            with self.assertRaises(ValueError):evaluate(mode,0,0,df=df)
        with self.assertRaises(ValueError):evaluate(0,float('nan'),0)

if __name__=='__main__':unittest.main()
