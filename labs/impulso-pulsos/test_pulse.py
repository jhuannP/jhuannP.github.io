import unittest
from fractions import Fraction as Q
from .pulse import force,impulse,moments,mean_force,propagate

TRI=((0,0),(Q(1,4),12),(Q(1,2),0))
RECT=((0,6),(Q(1,2),6))

class PulseTests(unittest.TestCase):
    def test_examples_and_signs(self):
        self.assertEqual(impulse(TRI,0,Q(1,2)),3)
        self.assertEqual(impulse(RECT,0,Q(1,2)),3)
        self.assertEqual(impulse(TRI,0,Q(1,4)),Q(3,2))
        self.assertEqual(mean_force(TRI,0,Q(1,2)),6)
        self.assertEqual(propagate(TRI,2,0,-1,0,Q(1,2)),(Q(-1,8),Q(1,2)))
        self.assertEqual(propagate(TRI,2,0,-1,0,Q(1,4))[1],Q(-1,4))
        neg=tuple((t,-f) for t,f in TRI)
        self.assertEqual(impulse(neg,0,Q(1,2)),-3)
        self.assertEqual(force(TRI,1),0)

    def test_moments_by_piecewise_simpson(self):
        # Integral independente de F e tF por Simpson; exato até grau3.
        def simpson(fun,a,b):return (b-a)*(fun(a)+4*fun((a+b)/2)+fun(b))/6
        pulses=[TRI,((0,3),(Q(1,3),-2),(1,4))]
        grid=[Q(i,8) for i in range(-2,11)]
        for pulse in pulses:
            for a in grid:
                for b in grid:
                    if a>b:continue
                    j=m=Q(0)
                    for (u,f),(v,g) in zip(pulse,pulse[1:]):
                        lo,hi=max(a,u),min(b,v)
                        if lo>=hi:continue
                        fun=lambda t:f+(g-f)*(t-u)/(v-u)
                        j+=simpson(fun,lo,hi);m+=simpson(lambda t:t*fun(t),lo,hi)
                    self.assertEqual(moments(pulse,a,b),(j,m))

    def test_timing_changes_displacement(self):
        short=((0,6),(Q(1,2),6));long=((0,3),(1,3))
        xs,vs=propagate(short,2,0,0,0,1);xl,vl=propagate(long,2,0,0,0,1)
        self.assertEqual(vs,vl);self.assertEqual(vs,Q(3,2))
        self.assertEqual(xs,Q(9,8));self.assertEqual(xl,Q(3,4))
        self.assertEqual(xs-xl,Q(3,8))
        # Composição dos estados em dois subintervalos deve dar o mesmo resultado.
        x,v=propagate(TRI,2,0,-1,0,Q(1,4))
        self.assertEqual(propagate(TRI,2,x,v,Q(1,4),Q(1,2)),propagate(TRI,2,0,-1,0,Q(1,2)))

    def test_independent_time_integrator(self):
        # Velocity Verlet para F(t)=8t,m=2. Erro espacial O(h²); referência integral 2/3.
        errors=[]
        for n in [32,64,128]:
            h=1/n;x=v=0.0
            for k in range(n):
                acc=4*k*h;acc_next=4*(k+1)*h
                x+=v*h+acc*h*h/2;v+=(acc+acc_next)*h/2
            self.assertAlmostEqual(v,2,places=13)
            errors.append(abs(x-2/3))
        self.assertAlmostEqual(errors[0]/errors[1],4,places=8)
        self.assertAlmostEqual(errors[1]/errors[2],4,places=7)
        self.assertEqual(propagate(((0,0),(1,8)),2,0,0,0,1),(Q(2,3),Q(2)))

    def test_contracts(self):
        for bad in [True,.5,'0',None]:
            with self.assertRaises(TypeError):impulse(TRI,bad,1)
        for bad in [[],[(0,1)],[(0,1),(0,2)],[(1,1),(0,2)],[(0,1,2),(1,3)]]:
            with self.assertRaises(ValueError):impulse(bad,0,1)
        with self.assertRaises(ValueError):mean_force(TRI,1,1)
        with self.assertRaises(ValueError):impulse(TRI,1,0)
        with self.assertRaises(ValueError):propagate(TRI,0,0,0,0,1)
        self.assertEqual(impulse(TRI,1,1),0)

if __name__=='__main__':unittest.main()
