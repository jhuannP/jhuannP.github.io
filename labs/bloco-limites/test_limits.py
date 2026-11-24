import unittest
from fractions import Fraction as Q
from .limits import static_state

class LimitTests(unittest.TestCase):
    def test_reference_and_first_mode(self):
        r=static_state(300,Q(4,5),Q(6,5),Q(2,5),90)
        self.assertEqual((r['x'],r['edge_margin'],r['friction_margin']),(Q(9,25),Q(1,25),30))
        self.assertEqual((r['left'],r['right']),(15,285))
        self.assertEqual((r['slide_threshold'],r['tip_threshold'],r['first']),(120,100,'tombamento'))
        for mu,mode,load in ((Q(1,5),'deslizamento',60),(Q(1,3),'simultâneos',100)):
            s=static_state(300,Q(4,5),Q(6,5),mu,0)
            self.assertEqual((s['first'],s['threshold']),(mode,load))

    def test_force_and_torque_about_independent_origins(self):
        for W in (100,300):
            for B in (Q(1,2),Q(4,5),2):
                for H in (0,Q(3,5),Q(6,5)):
                    for P in (0,50,110):
                        W,B,H,P=map(Q,(W,B,H,P))
                        r=static_state(W,B,H,Q(2,5),P)
                        # Actual forces at bottom0, top(H), base points(-B/2,+B/2), weight at x0.
                        forces=[(0,H,P,0),(0,0,r['friction'],0),
                                (-B/2,0,0,r['left']),(B/2,0,0,r['right']),(0,1,0,-W)]
                        self.assertEqual(sum(f[2] for f in forces),0)
                        self.assertEqual(sum(f[3] for f in forces),0)
                        for ox,oy in ((0,0),(Q(1,3),Q(-2)),(-B/2,0)):
                            self.assertEqual(sum((x-ox)*fy-(y-oy)*fx for x,y,fx,fy in forces),0)
                        self.assertEqual(r['admissible'],r['left']>=0 and P<=Q(2,5)*W)

    def test_boundary_and_two_distinct_failures(self):
        for P,want in ((99,True),(100,True),(101,False),(110,False)):
            r=static_state(300,Q(4,5),Q(6,5),Q(2,5),P)
            self.assertEqual(r['admissible'],want)
        r=static_state(300,Q(4,5),Q(6,5),Q(2,5),110)
        self.assertGreater(r['friction_margin'],0)
        self.assertLess(r['edge_margin'],0)
        s=static_state(300,Q(4,5),Q(6,5),Q(1,5),70)
        self.assertLess(s['friction_margin'],0)
        self.assertGreater(s['edge_margin'],0)

    def test_scalings_and_zero_height(self):
        r=static_state(300,Q(4,5),Q(6,5),Q(2,5),90)
        for k in (Q(1,3),Q(2),Q(5)):
            s=static_state(300*k,Q(4,5),Q(6,5),Q(2,5),90*k)
            self.assertEqual(s['x'],r['x'])
            self.assertEqual(s['threshold'],k*r['threshold'])
            t=static_state(300,k*Q(4,5),k*Q(6,5),Q(2,5),90)
            self.assertEqual(t['x'],k*r['x'])
            self.assertEqual(t['threshold'],r['threshold'])
        z=static_state(300,1,0,Q(1,5),50)
        self.assertIsNone(z['tip_threshold']);self.assertEqual(z['x'],0)
        self.assertEqual(z['first'],'deslizamento')
        self.assertEqual(static_state(300,1,1,0,0)['threshold'],0)

    def test_contracts(self):
        for args in ((0,1,1,1,1),(1,0,1,1,1),(1,1,-1,1,1),
                     (1,1,1,-1,1),(1,1,1,1,-1),(True,1,1,1,1),(1.,1,1,1,1)):
            with self.assertRaises(ValueError):static_state(*args)
