import unittest
from fractions import Fraction as F
from .experiment import inspect,cdf

class ContinuousConditioningTests(unittest.TestCase):
    def test_strip_by_polygon_clipping(self):
        # Interseção do triângulo (0,0),(1,1),(0,1) com três semiplanos.
        # A área shoelace não usa a antiderivada da implementação.
        def clip(poly,axis,value,sign):
            out=[]
            for p,q in zip(poly,poly[1:]+poly[:1]):
                pin=sign*(p[axis]-value)>=0; qin=sign*(q[axis]-value)>=0
                if pin: out.append(p)
                if pin!=qin:
                    t=(value-p[axis])/(q[axis]-p[axis])
                    out.append(tuple(p[j]+t*(q[j]-p[j]) for j in range(2)))
            return out
        def area(poly):
            return abs(sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(poly,poly[1:]+poly[:1])))/2 if poly else F(0)
        triangle=[(F(0),F(0)),(F(1),F(1)),(F(0),F(1))]
        for iy in range(1,10):
            for ih in (1,5,10,20):
                y=F(iy,10);h=F(ih,100)
                for ia in range(11):
                    a=F(ia,10);r=inspect(y,h,a)
                    strip=clip(clip(triangle,1,r['lower'],1),1,r['upper'],-1)
                    selected=clip(strip,0,a,-1)
                    self.assertEqual(2*area(strip),r['band_mass'])
                    self.assertEqual(2*area(selected),r['joint'])
                    self.assertEqual(area(selected)/area(strip),r['band'])
    def test_shrinking_bands_and_support(self):
        y=F(1,2)
        for h in (F(1,5),F(1,10),F(1,20),F(1,100)):
            r=inspect(y,h,y)
            self.assertEqual(r['point'],1)
            self.assertEqual(1-r['band'],h/(4*y))
        for a in (F(1,10),F(1,4),F(3,4),F(9,10)):
            self.assertLessEqual(abs(inspect(y,F(1,10000),a)['difference']),F(1,1000))
        self.assertEqual(cdf(-1,y),0);self.assertEqual(cdf(2,y),1)
    def test_total_probability_and_cdf_monotonicity(self):
        # Integra em y o produto F(X<=a|y)*fY(y), usando trapézios.
        # O integrando 2 min(a,y) é linear em cada lado do ponto a.
        for ia in range(11):
            a=F(ia,10)
            points=[F(i,100) for i in range(101)]
            values=[2*min(a,y) for y in points]
            integral=sum((values[i]+values[i+1])*(points[i+1]-points[i])/2 for i in range(100))
            self.assertEqual(integral,inspect(F(1,2),F(1,10),a)['marginal'])
        for iy in range(1,10):
            vals=[inspect(F(iy,10),F(1,5),F(i,100))['band'] for i in range(101)]
            self.assertEqual(vals[0],0);self.assertEqual(vals[-1],1)
            self.assertEqual(vals,sorted(vals))
    def test_contract_and_clipped_bands(self):
        r=inspect(F(1,10),F(1,5),F(1,10))
        self.assertEqual((r['lower'],r['upper']),(0,F(3,10)))
        self.assertEqual(r['band'],F(5,9))
        self.assertEqual(inspect(F(1,2),1,F(1,4))['band'],F(7,16))
        for args in [(0,F(1,10),0),(1,F(1,10),0),(F(1,2),0,0),(F(1,2),2,0),(F(1,2),F(1,10),2),(.5,F(1,10),0),(True,F(1,10),0)]:
            with self.assertRaises(ValueError):inspect(*args)
