from math import exp,log
from decimal import Decimal as D,localcontext
from itertools import product
import unittest
from .experiment import inspect

class RCEnergy(unittest.TestCase):
    def test_decimal_independent_exponential_reference(self):
        with localcontext() as ctx:
            ctx.prec=70
            for R,C,V,V0,u in product([D('.5'),D('2')],[D('1'),D('3')],[D('0'),D('2'),D('4')],[D('0'),D('2'),D('4')],[D('0'),D('.5'),D('2'),D('5')]):
                e=(-u).exp();vc=V+(V0-V)*e;i=(V-vc)/R
                z=inspect(*map(float,(R,C,V,u,V0)))
                references={'VC':vc,'I':i,'source':C*V*(vc-V0),'stored':C*vc*vc/2,'change':C*(vc*vc-V0*V0)/2,'dissipated':C*(V-V0)**2*(1-e*e)/2}
                for k,value in references.items():self.assertAlmostEqual(z[k],float(value),places=11)

    def test_ode_and_integrated_powers(self):
        for R,C,V,V0,u in [(2,3,4,0,1),(.5,1,0,4,2),(2,3,2,4,1),(1,2,2,2,3)]:
            z=inspect(R,C,V,u,V0);tau=R*C
            h=1e-5
            derivative=(inspect(R,C,V,u+h,V0)['VC']-inspect(R,C,V,u-h,V0)['VC'])/(2*h*tau)
            self.assertAlmostEqual(C*derivative,z['I'],places=8)
            self.assertAlmostEqual(V,z['VR']+z['VC'],places=12)
            self.assertAlmostEqual(z['power_source'],z['power_C']+z['power_R'],places=12)
            N=2048;du=u/N
            # Integra potências diretamente pelo tempo físico,sem usar energias calculadas.
            for key,power in [('source',lambda s:V*(V-V0)/R*exp(-s)),('dissipated',lambda s:(V-V0)**2/R*exp(-2*s))]:
                value=tau*du/3*sum((1 if j in (0,N) else 4 if j%2 else 2)*power(j*du) for j in range(N+1))
                self.assertAlmostEqual(value,z[key],places=10)

    def test_initial_discharge_return_scaling_and_small_time(self):
        z=inspect(V0=2,u=0);self.assertEqual(z['VC'],2);self.assertEqual(z['stored'],6)
        self.assertEqual(z['source'],0);self.assertEqual(z['dissipated'],0)
        z=inspect(V=0,V0=4,u=log(2));self.assertAlmostEqual(z['stored'],6);self.assertAlmostEqual(z['dissipated'],18)
        self.assertEqual(z['source'],0)
        z=inspect(V=2,V0=4,u=log(2));self.assertAlmostEqual(z['source'],-6);self.assertAlmostEqual(z['dissipated'],4.5)
        for R in (.5,1,2,3):
            z=inspect(R=R)
            self.assertAlmostEqual(z['stored'],inspect()['stored'])
            self.assertAlmostEqual(z['time'],3*R)
        tiny=inspect(u=1e-16)
        self.assertGreater(tiny['VC'],0);self.assertGreater(tiny['source'],0)
        self.assertAlmostEqual(tiny['source'],tiny['change']+tiny['dissipated'],delta=1e-28)

    def test_contracts(self):
        for field,value in [('R',0),('C',0),('V',-1),('V0',-1),('u',-1),('R',True),('u',float('nan')),('V',float('inf'))]:
            with self.assertRaises(ValueError):inspect(**{field:value})
