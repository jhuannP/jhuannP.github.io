import importlib.util
import itertools
import unittest
from fractions import Fraction as F
from pathlib import Path
spec=importlib.util.spec_from_file_location('conditional',Path(__file__).with_name('experiment.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class ConditionalTests(unittest.TestCase):
    def test_exact_rational_projection_and_risk(self):
        # Referência racional, construindo cada evento separadamente.
        for info, noise, shift in itertools.product(range(3), [0,.5,1,2], [-1,0,.25,1]):
            r=m.model(info,noise,shift)
            p=list(map(F,r['weights'])); x=list(map(F,r['values'])); g=r['groups']
            ref=[sum(p[j]*x[j] for j in range(6) if g[j]==g[i])/sum(p[j] for j in range(6) if g[j]==g[i]) for i in range(6)]
            self.assertEqual(r['means'],list(map(float,ref)))
            err=sum(p[i]*(x[i]-ref[i]-F(shift))**2 for i in range(6))
            self.assertAlmostEqual(r['risk'],float(err))
            expected=[F(1,4)+F(noise)**2,F(noise)**2,F(0)][info]
            self.assertAlmostEqual(r['optimal'],float(expected))
            self.assertAlmostEqual(r['risk'],r['optimal']+shift**2)
            self.assertAlmostEqual(r['var_x'],r['optimal']+r['explained'])

    def test_orthogonality_tower_and_nested_information(self):
        for noise in [0,.25,1,2]:
            states=[m.model(i,noise) for i in range(3)]
            for fine in range(3):
                r=states[fine]
                for coarse in range(fine+1):
                    c=states[coarse]
                    self.assertEqual(m.project(r['means'],r['weights'],c['groups']),c['means'])
                    gain=sum(p*(a-b)**2 for p,a,b in zip(r['weights'],r['means'],c['means']))
                    self.assertAlmostEqual(c['optimal']-r['optimal'],gain)
                # Todos os indicadores da partição: base de funções observáveis.
                for label in set(r['groups']):
                    self.assertAlmostEqual(sum(p*e for p,e,g in zip(r['weights'],r['residuals'],r['groups']) if g==label),0)

    def test_zero_covariance_not_independence_and_realization_error(self):
        r=m.model(1,0)
        self.assertEqual(sum(p*x*y for p,x,y in zip(r['weights'],r['values'],r['ys'])),0)
        # P(X=1|Y=0)=0, mas P(X=1)=1/2.
        self.assertEqual(r['means'],[1,1,0,0,1,1])
        self.assertEqual(m.model(0,0)['optimal'],.25)
        self.assertEqual(r['optimal'],0)
        r=m.model(1,1); c=m.model(0,1)
        self.assertGreater((r['values'][3]-r['means'][3])**2,(c['values'][3]-c['means'][3])**2)

    def test_null_events_and_invalid_inputs(self):
        self.assertEqual(m.project([2,100],[1,0],['a','b']),[2,0])
        for args in [([],[],[]),([1],[.5],[0]),([1],[-1],[0]),([float('nan')],[1],[0])]:
            with self.assertRaises(ValueError): m.project(*args)
        for args in [(3,1,0),(1,-1,0),(1,float('inf'),0)]:
            with self.assertRaises(ValueError): m.model(*args)

if __name__=='__main__':unittest.main()
