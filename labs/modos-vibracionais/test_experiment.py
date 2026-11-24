import math,unittest
from fractions import Fraction as F
from .experiment import modes,model


class VibrationalTests(unittest.TestCase):
    def test_generalized_eigenproblem_and_orthogonality(self):
        for M in map(F,(.5,1,2,4)):
            for k in map(F,(.5,1,2)):
                weights=(F(1),M,F(1))
                K=((k,-k,F(0)),(-k,2*k,-k),(F(0),-k,k))
                # Derive forces from two independent bond extensions.
                for u,lam in (((F(1),F(1),F(1)),F(0)),((F(-1),F(0),F(1)),k),((F(1),-2/M,F(1)),k*(1+2/M))):
                    self.assertEqual(tuple(sum(a*b for a,b in zip(row,u)) for row in K),tuple(lam*m*x for m,x in zip(weights,u)))
                v=modes(float(M),float(k))
                for i in range(3):
                    for j in range(3):
                        dot=sum(float(m)*x*y for m,x,y in zip(weights,v[i]['mass_vector'],v[j]['mass_vector']))
                        self.assertAlmostEqual(dot,float(i==j),places=13)

    def test_energy_and_zero_mode(self):
        for M in (.5,1,4):
            for k in (.5,2):
                for mode in range(3):
                    start=model(mode,M,k,0)
                    for phase in range(0,361,15):
                        s=model(mode,M,k,phase)
                        self.assertAlmostEqual(s['energy'],start['energy'],places=14)
                        if mode:self.assertAlmostEqual(s['com'],0,places=14)
                        else:
                            self.assertEqual(s['q'],(.15,.15,.15));self.assertEqual(s['v'],(0.,0.,0.))
                            self.assertEqual(s['energy'],0)

    def test_independent_verlet_superposition(self):
        M,k=1.5,1.2
        q0=[.07*(-1)+(-.04),(-.04)*(-2/M),.07+(-.04)]
        exact=[.07*u*math.cos(math.sqrt(k)*4)-.04*v*math.cos(math.sqrt(k*(1+2/M))*4) for u,v in zip((-1,0,1),(1,-2/M,1))]
        def integrate(dt):
            q=q0[:];v=[0.,0.,0.]
            def accel(q):
                b1=q[1]-q[0];b2=q[2]-q[1]
                return [k*b1,k*(-b1+b2)/M,-k*b2]
            a=accel(q)
            for _ in range(round(4/dt)):
                q=[x+dt*y+.5*dt*dt*z for x,y,z in zip(q,v,a)]
                b=accel(q);v=[x+.5*dt*(y+z) for x,y,z in zip(v,a,b)];a=b
            return math.sqrt(sum((x-y)**2 for x,y in zip(q,exact)))
        coarse,fine=integrate(.04),integrate(.02)
        self.assertLess(fine,1e-4);self.assertGreater(coarse/fine,3.8)

    def test_scaling_mass_and_contract(self):
        for M in (.5,1,2,4):
            a=modes(M,.5);b=modes(M,2)
            for i in (1,2):self.assertAlmostEqual(b[i]['omega'],2*a[i]['omega'])
            self.assertEqual(modes(M,1)[1]['omega'],1)
        self.assertGreater(modes(.5,1)[2]['omega'],modes(4,1)[2]['omega'])
        self.assertAlmostEqual(modes(1e8,1)[2]['omega'],1,places=7)
        for args in ((3,1,1,0),(1,0,1,0),(1,1,0,0),(1,1,1,361),(1,1,1,float('nan'))):
            with self.assertRaises(ValueError):model(*args)
