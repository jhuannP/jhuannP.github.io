import unittest
from fractions import Fraction as F
from .power import dot,cart,nonlinear


class PowerTests(unittest.TestCase):
    def test_literal_cart(self):
        r=cart()
        for k,v in dict(acceleration=2,velocity=5,displacement=6,drive_power=30,
                        resistance_power=-10,net_power=20,drive_work=36,
                        resistance_work=-12,net_work=24,delta_k=24,kinetic=25).items():
            self.assertEqual(r[k],v)
        self.assertEqual(cart(t=0)['net_power'],4)
        self.assertEqual(cart(t=0)['kinetic'],1)
        self.assertEqual(cart()['net_work']/2,12)

    def test_work_energy_and_integrated_powers(self):
        # Independent trapezoid integration is exact for the affine powers of this model.
        for m,v0,drive,resistance in [(2,1,6,2),(3,2,9,3),(1,0,4,0),(4,3,2,2),(5,0,0,0),(7,2,5,1)]:
            for t in [F(1,4),F(1,2),1,2,3]:
                initial=cart(m,v0,drive,resistance,0);end=cart(m,v0,drive,resistance,t)
                integrated=[]
                for p,w in [('drive_power','drive_work'),('resistance_power','resistance_work'),('net_power','net_work')]:
                    q=t*(initial[p]+end[p])/2
                    self.assertEqual(q,end[w]);integrated.append(q)
                independent_delta_k=m*(end['velocity']**2-F(v0)**2)/2
                self.assertEqual(integrated[0]+integrated[1],independent_delta_k)
                self.assertEqual(integrated[2],independent_delta_k)

    def test_galilean_identity(self):
        for u in [-3,0,2,5]:
            for t in [0,F(1,2),1,2]:
                r=cart(t=t);s=cart(t=t,boost=u)
                self.assertEqual(s['net_power'],r['net_power']-4*u)
                self.assertEqual(s['drive_power'],r['drive_power']-6*u)
                delta_p=2*(r['velocity']-1)
                self.assertEqual(s['delta_k'],r['delta_k']-u*delta_p)
                self.assertEqual(s['net_work'],s['delta_k'])
        self.assertEqual(cart(boost=2)['net_work'],8)
        self.assertEqual(cart(t=F(1,2),boost=2)['drive_power'],0)
        self.assertEqual(cart(t=0,boost=2)['drive_power'],-6)

    def test_nonlinear_reference(self):
        for t in [F(1,4),F(1,2),1,2]:
            # Simpson integrates this cubic power exactly; not used by implementation.
            q=t*(nonlinear(0)['power']+4*nonlinear(F(t)/2)['power']+nonlinear(t)['power'])/6
            self.assertEqual(q,nonlinear(t)['delta_k'])
            self.assertEqual(q,nonlinear(t)['work'])
        self.assertEqual(nonlinear(F(1,2))['power'],F(5,2))
        self.assertEqual(nonlinear(1)['work'],3)

    def test_vector_geometry(self):
        self.assertEqual(dot((3,4),(4,-3)),0)
        self.assertEqual(dot((3,4),(6,8)),50)
        self.assertEqual(dot((3,4),(-6,-8)),-50)
        for force,velocity,boost in [((3,4),(4,-3),(1,2)),((1,2,3),(3,2,1),(-1,0,2))]:
            shifted=tuple(v-u for v,u in zip(velocity,boost))
            self.assertEqual(dot(force,shifted),dot(force,velocity)-dot(force,boost))

    def test_contracts(self):
        for kwargs in [dict(mass=0),dict(v0=-1),dict(resistance=-1),dict(drive=1),dict(t=-1),dict(boost=True),dict(t=.5)]:
            with self.assertRaises(ValueError):cart(**kwargs)
        for a,b in [([],[]),([1],[1,2]),([1.0],[2]),([True],[1]),([1]*4,[1]*4)]:
            with self.assertRaises(ValueError):dot(a,b)
        with self.assertRaises(ValueError):nonlinear(-1)

if __name__=='__main__':unittest.main()
