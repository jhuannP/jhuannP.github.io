import unittest
from math import exp
from .experiment import model

def rk4(b,t):
    # Integra o sistema x'=v, v'=-b*v-4*x, sem usar raízes ou fórmulas fechadas.
    n=8000;h=t/n;x,v=1.,0.
    for _ in range(n):
        a1=-b*v-4*x;k1=v
        k2=v+h*a1/2;a2=-b*k2-4*(x+h*k1/2)
        k3=v+h*a2/2;a3=-b*k3-4*(x+h*k2/2)
        k4=v+h*a3;a4=-b*k4-4*(x+h*k3)
        x+=h*(k1+2*k2+2*k3+k4)/6;v+=h*(a1+2*a2+2*a3+a4)/6
    return x,v

class DampingTests(unittest.TestCase):
    def test_against_independent_ode_integration(self):
        for b in (0,.5,2,3.999999,4,4.000001,6,8):
            for t in (.5,2,5):
                r=model(b,t);x,v=rk4(b,t)
                self.assertAlmostEqual(r['x'],x,places=9)
                self.assertAlmostEqual(r['v'],v,places=9)

    def test_initial_conditions_and_critical_limit(self):
        for b in (0,1,2,3.999999,4,4.000001,8):
            r=model(b,0);self.assertEqual(r['x'],1);self.assertEqual(r['v'],0);self.assertEqual(r['energy'],2)
        for t in (.5,2,5):
            c=model(4,t)
            self.assertAlmostEqual(c['x'],exp(-2*t)*(1+2*t))
            for b in (4-1e-8,4+1e-8):self.assertAlmostEqual(model(b,t)['x'],c['x'],places=7)

    def test_energy_balance_by_quadrature(self):
        for b in (0,1,2,4,6,8):
            n=4000;end=3;h=end/n
            dissipated=h/3*sum((1 if j in (0,n) else 4 if j%2 else 2)*(-model(b,j*h)['power']) for j in range(n+1))
            self.assertAlmostEqual(model(b,end)['energy']+dissipated,2,places=8)
            energies=[model(b,j/20)['energy'] for j in range(201)]
            self.assertTrue(all(y<=x+1e-12 for x,y in zip(energies,energies[1:])))
        self.assertGreater(model(8,2)['x'],model(4,2)['x'])

    def test_contracts(self):
        for z in (True,None,'2',-1,float('nan'),float('inf')):
            with self.assertRaises(ValueError):model(z,1)
            with self.assertRaises(ValueError):model(2,z)
        with self.assertRaises(ValueError):model(9,1)
        with self.assertRaises(ValueError):model(2,11)
