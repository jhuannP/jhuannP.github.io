import unittest,json
from pathlib import Path
from fractions import Fraction as Q
from .spline import natural,evaluate,local

class SplineTests(unittest.TestCase):
    def test_nonuniform_reference_and_overshoot(self):
        s=natural([0,1,3],[0,1,1])
        self.assertEqual(s[1],(0,-1,0))
        self.assertEqual(s[2],((0,Q(7,6),0,Q(-1,6)),(1,Q(2,3),Q(-1,2),Q(1,12))))
        self.assertEqual(evaluate(s,2),Q(5,4))
        self.assertEqual(evaluate(s,3,1),Q(-1,3))
        self.assertNotEqual(local(s[2][0],1,3),local(s[2][1],0,3))

    def test_nodes_continuity_and_natural_ends(self):
        for xs in ((0,1),(0,1,3),(Q(-1),0,Q(1,3),2),(0,Q(1,10),1,4,9)):
            for ys in ([x*x for x in xs],[(-1)**i for i in range(len(xs))],[x**3-x for x in xs]):
                s=natural(xs,ys)
                for x,y in zip(xs,ys): self.assertEqual(evaluate(s,x),y)
                self.assertEqual(evaluate(s,xs[0],2),0)
                self.assertEqual(evaluate(s,xs[-1],2),0)
                for i in range(1,len(xs)-1):
                    for order in range(3):
                        self.assertEqual(local(s[2][i-1],xs[i]-xs[i-1],order),local(s[2][i],0,order))

    def test_all_affine_data(self):
        xs=[Q(-2),Q(-1,3),Q(1,4),Q(5)]
        for a in range(-3,4):
            for b in range(-3,4):
                s=natural(xs,[a*x+b for x in xs])
                self.assertEqual(s[1],(0,0,0,0))
                for x in (Q(-2),Q(-1),Q(0),Q(3),Q(5)):
                    self.assertEqual(evaluate(s,x),a*x+b)
                    self.assertEqual(evaluate(s,x,1),a)

    def test_quadratic_boundary_counterexample(self):
        s=natural([0,1,2],[0,1,4])
        self.assertEqual(s[1],(0,3,0))
        self.assertEqual(evaluate(s,Q(1,2)),Q(5,16))
        self.assertEqual(evaluate(s,Q(1,2))-Q(1,4),Q(1,16))

    def test_independent_dense_previous_implementation(self):
        root=Path(__file__).resolve().parents[2]
        lesson=next(l for l in json.loads((root/'content/lessons.json').read_text()) if l['id']=='splines-cubicas')
        ns={};exec(lesson['python'],ns)
        for xs in ((0,1,3),(0,1,2,5),(Q(-1),Q(1,3),2,4)):
            for ys in ([x*x-2*x for x in xs],[(-1)**i for i in range(len(xs))]):
                s=natural(xs,ys);f,M=ns['spline_natural'](xs,ys)
                for i in range(17):
                    x=xs[0]+(xs[-1]-xs[0])*Q(i,16)
                    self.assertAlmostEqual(float(evaluate(s,x)),f(x),places=10)
                for a,b in zip(s[1],M): self.assertAlmostEqual(float(a),b,places=10)
        exec(lesson['codingPractice']['solution'],{})

    def test_contracts(self):
        for xs,ys in (([],[]),([0],[1]),([0,0],[1,2]),([1,0],[1,2]),([0,1],[1]),([0,True],[1,2]),([0.,1],[1,2])):
            with self.assertRaises(ValueError):natural(xs,ys)
        s=natural([0,1],[0,1])
        for x in (-1,2,True,0.5):
            with self.assertRaises(ValueError):evaluate(s,x)
        for order in (-1,4,True,1.5):
            with self.assertRaises(ValueError):evaluate(s,0,order)
