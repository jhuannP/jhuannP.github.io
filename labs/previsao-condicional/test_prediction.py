import math
import unittest
from fractions import Fraction as Q
from .prediction import bin_stats,partition,partition_risk,affine_risk,joint_moment

# Quadratura de Gauss de 3 pontos em x e u, y=xu.
# A densidade transformada é 3x² em [0,1]²; não usa as primitivas do módulo.
def numerical_risk(predict,a=0,b=1):
    t=math.sqrt(3/5)
    nodes=[-t,0,t]; weights=[5/9,8/9,5/9]
    total=0.0
    for nx,wx in zip(nodes,weights):
        x=(a+b)/2+(b-a)*nx/2
        for nu,wu in zip(nodes,weights):
            u=(1+nu)/2
            total+=wx*wu*(b-a)/4*3*x*x*(x*u-predict(x))**2
    return total

class PredictionTests(unittest.TestCase):
    def test_moments_and_total_variance(self):
        self.assertEqual(joint_moment(0),1)
        self.assertEqual(joint_moment(1),Q(3,8))
        self.assertEqual(joint_moment(2),Q(1,5))
        self.assertEqual(partition_risk([0,1]),Q(19,320))
        noise=Q(1,20); signal=Q(3,320)
        self.assertEqual(noise+signal,Q(19,320))
        self.assertEqual(affine_risk(0,Q(1,2)),noise)

    def test_affine_predictions_against_quadrature(self):
        for ia in range(-4,5):
            for ib in range(-4,5):
                a,b=Q(ia,4),Q(ib,4)
                expected=Q(1,20)+a*a+2*a*(b-Q(1,2))*Q(3,4)+(b-Q(1,2))**2*Q(3,5)
                self.assertEqual(affine_risk(a,b),expected)
                self.assertAlmostEqual(float(expected),numerical_risk(lambda x:float(a)+float(b)*x),places=12)

    def test_coarse_observation(self):
        low,high=partition([0,Q(1,2),1])
        self.assertEqual(low,(Q(1,8),Q(3,16),Q(19,1280)))
        self.assertEqual(high,(Q(7,8),Q(45,112),Q(3763,62720)))
        risk=partition_risk([0,Q(1,2),1])
        self.assertEqual(risk,Q(487,8960))
        self.assertEqual(risk-Q(1,20),Q(39,8960))
        self.assertEqual(Q(19,320)-risk,Q(9,1792))
        self.assertGreater(high[2],Q(19,320)) # Não melhora a variância em toda faixa.
        direct=numerical_risk(lambda x:float(low[1]),0,.5)+numerical_risk(lambda x:float(high[1]),.5,1)
        self.assertAlmostEqual(direct,float(risk),places=12)

    def test_refinement_and_tower(self):
        old=partition_risk([0,1])
        for n in [2,4,8,16]:
            edges=[Q(i,n) for i in range(n+1)]
            stats=partition(edges)
            risk=partition_risk(edges)
            self.assertEqual(sum((m for m,_,_ in stats),Q(0)),1)
            self.assertEqual(sum((m*mu for m,mu,_ in stats),Q(0)),Q(3,8))
            self.assertLess(risk,old)
            self.assertGreater(risk,Q(1,20))
            self.assertLess(risk-Q(1,20),Q(1,16*n*n))
            old=risk

    def test_contracts(self):
        for edges in [[0,0,1],[0,1,Q(1,2)],[Q(1,2),1],[0,2],[]]:
            with self.assertRaises(ValueError):partition(edges)
        for v in [True,.5,'0.5']:
            with self.assertRaises(TypeError):affine_risk(v,0)
        for a,b in [(0,0),(-1,1),(1,0)]:
            with self.assertRaises(ValueError):bin_stats(a,b)
        for k in [-1,True,21,Q(1,2)]:
            with self.assertRaises(ValueError):joint_moment(k)

if __name__=='__main__':unittest.main()
