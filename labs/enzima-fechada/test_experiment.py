import importlib.util
import itertools
import json
import unittest
from pathlib import Path
spec=importlib.util.spec_from_file_location('batch',Path(__file__).with_name('experiment.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class BatchTests(unittest.TestCase):
    def test_inventory_and_physical_bounds(self):
        for case,window in itertools.product(range(3),range(2)):
            r=m.experiment(case,window)
            self.assertLess(r['max_mass_error'],2e-13)
            last_p=-1
            for y in r['history']:
                self.assertGreaterEqual(min(y['s'],y['c'],y['p'],r['enzyme']-y['c']),-1e-13)
                self.assertLessEqual(y['c'],min(r['enzyme'],r['s0'])+1e-13)
                self.assertGreaterEqual(y['p'],last_p-1e-13)
                last_p=y['p']
                self.assertLessEqual(y['p'],r['s0']+1e-13)

    def test_independent_binding_limit(self):
        for s0,e,t in itertools.product([.2,2],[.02,2],[.1,1,4]):
            y=m.solve(s0,e,t,kcat=0)['history'][-1]
            exact=m.exact_binding_complex(s0,e,t)
            self.assertAlmostEqual(y['c'],exact,delta=3e-9)
            self.assertAlmostEqual(y['s'],s0-exact,delta=3e-9)
            self.assertEqual(y['p'],0)

    def test_refinement_and_reduction_gap(self):
        for case,window in itertools.product(range(3),range(2)):
            a=m.experiment(case,window);b=m.experiment(case,window,refinement=2)
            error=max(abs(u[k]-v[k]) for u,v in zip(a['history'],b['history']) for k in ['s','c','p'])
            self.assertLess(error,2e-8)
        refs=json.loads(Path(__file__).with_name('taylor_reference.json').read_text())
        for ref in refs:
            y=m.solve(ref['s0'],ref['enzyme'],ref['time'])['history'][-1]
            for key,target in zip(['s','c','p'],ref['state']):
                self.assertAlmostEqual(y[key],float(target),delta=3e-9)
        # Redução é outro modelo: seu erro não desaparece refinando RK4.
        rich=m.experiment(1,0,fraction=.5)
        self.assertGreater(abs(rich['selected']['p']-rich['selected']['qssa_p']),.05)
        self.assertGreater(m.experiment(1,1,1)['selected']['clamp_p'],2)
        self.assertEqual(m.reduced_product(2,0,4),0)

    def test_derivative_conservation_and_domain(self):
        for y,e in [((2,0,0),.02),((.5,.7,.8),2)]:self.assertAlmostEqual(sum(m.rhs(y,e)),0)
        for args in [(-1,1,1),(1,-1,1),(1,1,-1),(float('nan'),1,1)]:
            with self.assertRaises(ValueError):m.solve(*args)
        self.assertTrue(all(r['p']==0 for r in m.solve(0,2,2)['history']))
        self.assertTrue(all(r['p']==0 for r in m.solve(2,0,2)['history']))
        with self.assertRaises(ValueError):m.experiment(3)

if __name__=='__main__':unittest.main()
