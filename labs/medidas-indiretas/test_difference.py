from fractions import Fraction as Q
from itertools import product
import unittest
from .difference import difference

def moments(atoms):
    mass=sum(w for _,_,w in atoms)
    a=sum(x*w for x,_,w in atoms)/mass
    b=sum(y*w for _,y,w in atoms)/mass
    v1=sum((x-a)**2*w for x,_,w in atoms)/mass
    v2=sum((y-b)**2*w for _,y,w in atoms)/mass
    cov=sum((x-a)*(y-b)*w for x,y,w in atoms)/mass
    direct=sum(((y-x)-(b-a))**2*w for x,y,w in atoms)/mass
    return a,b,v1,v2,cov,direct

class DifferenceTests(unittest.TestCase):
    def test_shared_offset_against_discrete_distribution(self):
        common=((Q(-3,10),1),(Q(0),4),(Q(3,10),1))
        atoms=[(20+b+e1,70+b+e2,Q(w)) for (b,w),e1,e2 in
               product(common,(Q(-1,10),Q(1,10)),(Q(-1,10),Q(1,10)))]
        a,b,v1,v2,cov,direct=moments(atoms)
        self.assertEqual((a,b,v1,v2,cov),(20,70,Q(1,25),Q(1,25),Q(3,100)))
        self.assertEqual(difference(a,b,v1,v2,cov)['variance'],direct)
        self.assertEqual(direct,Q(1,50))

    def test_independent_offsets_have_other_covariance(self):
        common=((Q(-3,10),1),(Q(0),4),(Q(3,10),1))
        atoms=[(20+b1+e1,70+b2+e2,Q(w1*w2)) for (b1,w1),(b2,w2),e1,e2 in
               product(common,common,(Q(-1,10),Q(1,10)),(Q(-1,10),Q(1,10)))]
        a,b,v1,v2,cov,direct=moments(atoms)
        self.assertEqual(cov,0)
        self.assertEqual(difference(a,b,v1,v2,cov)['variance'],direct)
        self.assertEqual(direct,Q(2,25))

    def test_unit_conversion_and_common_shift(self):
        base=difference(20,70,Q(1,25),Q(1,25),Q(3,100))
        for shift in (Q(-30),Q(3,10),Q(100)):
            self.assertEqual(difference(20-shift,70-shift,Q(1,25),Q(1,25),Q(3,100)),base)
        mm=difference(200,700,4,4,3)
        self.assertEqual(mm['value'],base['value']*10)
        self.assertEqual(mm['variance'],base['variance']*100)
        self.assertEqual(difference(70,20,Q(1,25),Q(1,25),Q(3,100))['value'],-50)

    def test_covariance_boundaries(self):
        for cov in (Q(-1,25),Q(0),Q(1,25)):
            self.assertEqual(difference(0,1,Q(1,25),Q(1,25),cov)['variance'],Q(2,25)-2*cov)
        self.assertEqual(difference(0,1,0,1,0)['variance'],1)
        for cov in (Q(41,1000),Q(-41,1000)):
            with self.assertRaises(ValueError):difference(0,1,Q(1,25),Q(1,25),cov)
        with self.assertRaises(ValueError):difference(0,1,0,1,Q(1,100))

    def test_contracts(self):
        for i in range(5):
            for bad in (True,0.,'0',None):
                args=[0,1,1,1,0];args[i]=bad
                with self.assertRaises(ValueError):difference(*args)
        with self.assertRaises(ValueError):difference(0,1,-1,1,0)

if __name__=='__main__':unittest.main()
