import math,unittest
from fractions import Fraction as F
from .experiment import oscillator_step,oscillator_trace,experiment

class RK4OscillatorTests(unittest.TestCase):
    def test_stages_and_matrix_polynomial_oracle(self):
        y,stages=oscillator_step((1,0),1)
        self.assertEqual(stages,((0,-1),(-.5,-1),(-.5,-.75),(-.75,-.5)))
        self.assertAlmostEqual(y[0],13/24);self.assertAlmostEqual(y[1],-5/6)
        # Matriz explícita independente dos estágios, com coeficientes racionais.
        for h in (F(1,8),F(1,2),F(1),F(2),F(3),F(4)):
            a=1-h*h/2+h**4/24;b=h-h**3/6
            for initial in ((F(1),F(0)),(F(2),F(-3)),(F(-1),F(4))):
                exact=(a*initial[0]+b*initial[1],-b*initial[0]+a*initial[1])
                got,_=oscillator_step(tuple(map(float,initial)),float(h))
                for u,v in zip(got,exact):self.assertAlmostEqual(u,float(v),places=12)
                self.assertEqual(a*a+b*b,1-h**6/72+h**8/576)

    def test_full_traces_against_complex_power_and_energy(self):
        for level in range(1,8):
            for T in (4.,8.,12.):
                s=experiment(level,T);h=T/s['n'];a=1-h*h/2+h**4/24;b=h-h**3/6
                for j,(_,q,v) in enumerate(s['coarse']):
                    expected=complex(a,-b)**j
                    scale=max(1,abs(expected))
                    self.assertLess(abs(complex(q,v)-expected)/scale,3e-13)
                self.assertAlmostEqual(s['energy_ratio']/((a*a+b*b)**s['n']),1,places=11)
                self.assertEqual(s['evaluations'],12*s['n'])
                self.assertAlmostEqual(s['coarse'][-1][0],T)

    def test_order_and_step_doubling_is_asymptotic(self):
        for T in (4.,8.,12.):
            for level in (5,6,7):
                s=experiment(level,T)
                self.assertTrue(3.95<s['order']<4.05)
                self.assertLess(abs(s['estimate_fine']/s['error_fine']-1),.03)
        rough=experiment(1,8)
        self.assertFalse(rough['stable']);self.assertGreater(rough['energy_ratio'],1)
        self.assertGreater(abs(rough['estimate_fine']/rough['error_fine']-1),1)

    def test_stability_is_not_energy_or_accuracy_and_contracts(self):
        for level,T in ((2,8),(3,8),(4,8),(4,4)):
            s=experiment(level,T);self.assertTrue(s['stable']);self.assertLess(s['energy_ratio'],1)
            self.assertGreater(s['error_coarse'],0)
        h=math.sqrt(8);a=1-h*h/2+h**4/24;b=h-h**3/6
        self.assertAlmostEqual(a*a+b*b,1,places=13)
        # A rotação de um passo não é a rotação exata mesmo na borda de módulo um.
        self.assertGreater(abs(complex(a,-b)-complex(math.cos(h),-math.sin(h))),.1)
        for args in ((0,8),(8,8),(4,3),(4,13)):
            with self.assertRaises(ValueError):experiment(*args)
