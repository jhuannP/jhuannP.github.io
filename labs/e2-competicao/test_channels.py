import unittest,math,itertools
from .channels import state

class E2ChannelTests(unittest.TestCase):
    def test_reference_and_atom_charge_balance(self):
        r=state(.2,.8,.5,.1,math.log(2)/.5)
        for key,value in [('substrate',.05),('elimination',.01),('substitution',.04),('fraction_e',.2)]:self.assertAlmostEqual(r[key],value)
        # Independent molecular inventories: C,H,O,Br,charge; spectators omitted.
        substrate=(2,5,0,1,0);ethoxide=(2,5,1,0,-1)
        ethene=(2,4,0,0,0);ethanol=(2,6,1,0,0);bromide=(0,0,0,1,-1);ether=(4,10,1,0,0)
        left=tuple(a+b for a,b in zip(substrate,ethoxide))
        e2=tuple(a+b+c for a,b,c in zip(ethene,ethanol,bromide))
        sn2=tuple(a+b for a,b in zip(ether,bromide))
        self.assertEqual(left,e2);self.assertEqual(left,sn2)
    def test_inventory_positivity_and_differential_equations(self):
        h=1e-5
        for ke,ks,base in itertools.product([0,.2,1],[0,.8],[.1,1]):
            for t in [.2,1,2]:
                r=state(ke,ks,base,.1,t)
                self.assertAlmostEqual(sum(r[k] for k in ['substrate','elimination','substitution']),.1,places=14)
                self.assertTrue(all(r[k]>=0 for k in ['substrate','elimination','substitution']))
                left=state(ke,ks,base,.1,t-h);right=state(ke,ks,base,.1,t+h)
                for key,derivative in [('substrate',-r['rate_e']-r['rate_s']),('elimination',r['rate_e']),('substitution',r['rate_s'])]:
                    self.assertAlmostEqual((right[key]-left[key])/(2*h),derivative,delta=1e-11)
    def test_independent_rk4_refinement(self):
        def integrate(n):
            h=2/n;y=[.1,0,0]
            def rhs(y):return [-.5*y[0],.1*y[0],.4*y[0]]
            for _ in range(n):
                a=rhs(y);b=rhs([v+h*u/2 for v,u in zip(y,a)])
                c=rhs([v+h*u/2 for v,u in zip(y,b)]);d=rhs([v+h*u for v,u in zip(y,c)])
                y=[v+h*(a[i]+2*b[i]+2*c[i]+d[i])/6 for i,v in enumerate(y)]
            return y
        ref=state(.2,.8,.5,.1,2);errors=[]
        for n in [4,8,16]:
            y=integrate(n)
            errors.append(max(abs(v-ref[k]) for v,k in zip(y,['substrate','elimination','substitution'])))
        self.assertGreater(errors[0]/errors[1],15);self.assertGreater(errors[1]/errors[2],15)
        self.assertLess(errors[-1],5e-8)
    def test_base_and_time_scaling(self):
        for base in [.1,.5,1,2]:
            r=state(.2,.8,base,.1,1/base)
            ref=state(.2,.8,1,.1,1)
            for key in ['substrate','elimination','substitution','fraction_e']:self.assertAlmostEqual(r[key],ref[key])
            self.assertAlmostEqual(r['elimination']/(r['elimination']+r['substitution']),.2)
    def test_zero_channels_and_contracts(self):
        self.assertIsNone(state(0,0,1,.1,2)['fraction_e'])
        self.assertIsNone(state(1,1,0,.1,2)['fraction_e'])
        self.assertEqual(state(0,1,1,.1,1)['elimination'],0)
        self.assertEqual(state(1,0,1,.1,1)['substitution'],0)
        self.assertEqual(state(1,1,1,.1,0)['substrate'],.1)
        for args in [(-1,1,1,1,1),(1,1,-1,1,1),(1,1,1,1,-1),(True,1,1,1,1),(1,1,1,1,float('nan'))]:
            with self.assertRaises(ValueError):state(*args)
