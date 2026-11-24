import unittest,math,itertools
from .modes import state,transform,acceleration,energy

class CoupledModeTests(unittest.TestCase):
    def test_reference_and_pure_modes(self):
        r=state(1,4,4,(.1,0),(0,0),0)
        self.assertAlmostEqual(r['omega'][0],2)
        self.assertAlmostEqual(r['omega'][1],2*math.sqrt(3))
        self.assertAlmostEqual(r['energy'],.04)
        self.assertAlmostEqual(r['modal_energy'][0],.01)
        self.assertAlmostEqual(r['modal_energy'][1],.03)
        self.assertAlmostEqual(r['acceleration'][0],-.8)
        self.assertAlmostEqual(r['acceleration'][1],.4)
        for t in [0,.2,.7,1,2]:
            a=state(1,4,4,(.1,.1),(0,0),t)
            b=state(1,4,4,(.1,-.1),(0,0),t)
            self.assertAlmostEqual(a['position'][0],.1*math.cos(2*t),places=13)
            self.assertAlmostEqual(a['position'][1],a['position'][0],places=13)
            self.assertAlmostEqual(b['position'][1],-b['position'][0],places=13)
            self.assertAlmostEqual(b['position'][0],.1*math.cos(2*math.sqrt(3)*t),places=13)

    def test_initial_conditions_and_differential_equations(self):
        h=1e-4;count=0
        for x1,x2 in itertools.product([-.1,0,.2],repeat=2):
            pos=(x1,x2);vel=(.3,-.1)
            initial=state(2,3,1,pos,vel,0)
            for a,b in zip(initial['position'],pos):self.assertAlmostEqual(a,b,places=14)
            for a,b in zip(initial['velocity'],vel):self.assertAlmostEqual(a,b,places=14)
            for t in [0,.3,1]:
                r=state(2,3,1,pos,vel,t)
                left=state(2,3,1,pos,vel,t-h);right=state(2,3,1,pos,vel,t+h)
                for j in range(2):
                    fd=(right['position'][j]-2*r['position'][j]+left['position'][j])/(h*h)
                    self.assertAlmostEqual(fd,r['acceleration'][j],delta=3e-8)
                count+=1
        self.assertEqual(count,27)

    def test_energy_and_coordinate_normalization(self):
        pos=(.1,-.2);vel=(.3,.1);e0=energy(2,3,1,pos,vel)
        initial=state(2,3,1,pos,vel,0)
        q=transform(pos)
        self.assertAlmostEqual(sum(v*v for v in q),sum(v*v for v in pos),places=14)
        for t in [0,.1,.5,1,3,10]:
            r=state(2,3,1,pos,vel,t)
            self.assertAlmostEqual(r['energy'],e0,places=13)
            self.assertAlmostEqual(sum(r['modal_energy']),e0,places=13)
            for current,start in zip(r['modal_energy'],initial['modal_energy']):
                self.assertAlmostEqual(current,start,places=13)
        # Forças externas das molas das paredes não conservam momento em geral.
        a=acceleration(2,3,1,pos)
        self.assertAlmostEqual(2*sum(a),-3*sum(pos),places=14)

    def test_independent_verlet_refinement(self):
        pos=(.1,0);vel=(0,0);target=state(1,4,4,pos,vel,1)['position']
        errors=[]
        for n in [50,100,200]:
            x=list(pos);v=list(vel);dt=1/n
            for _ in range(n):
                a=acceleration(1,4,4,x)
                new=[u+w*dt+.5*b*dt*dt for u,w,b in zip(x,v,a)]
                b=acceleration(1,4,4,new)
                v=[u+.5*(old+fresh)*dt for u,old,fresh in zip(v,a,b)]
                x=new
            errors.append(math.dist(x,target))
        self.assertGreater(errors[0]/errors[1],3.9)
        self.assertGreater(errors[1]/errors[2],3.9)
        self.assertLess(errors[2],1e-5)

    def test_decoupled_and_contracts(self):
        r=state(1,4,0,(.1,0),(0,0),.7)
        self.assertAlmostEqual(r['position'][0],.1*math.cos(1.4),places=14)
        self.assertAlmostEqual(r['position'][1],0,places=14)
        self.assertEqual(r['omega'][0],r['omega'][1])
        for args in [(0,1,1),(-1,1,1),(1,0,1),(1,1,-1),(True,1,1)]:
            with self.assertRaises(ValueError):state(*args,(0,0),(0,0),0)
        with self.assertRaises(ValueError):state(1,1,1,(0,),(0,0),0)
        with self.assertRaises(ValueError):state(1,1,1,(0,0),(0,0),math.inf)

if __name__=='__main__':unittest.main()
