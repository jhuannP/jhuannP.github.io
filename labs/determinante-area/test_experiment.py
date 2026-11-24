import importlib.util
import itertools
import unittest
from decimal import Decimal,localcontext
from fractions import Fraction as F
from pathlib import Path
spec=importlib.util.spec_from_file_location('detarea',Path(__file__).with_name('experiment.py'))
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class DeterminantTests(unittest.TestCase):
    def test_polygon_and_exact_family(self):
        for s,k,t,w in itertools.product([.25,1,2],[-2,0,.5,2],[-2,-.5,0,.5,2],[0,1]):
            r=m.model(s,k,t,w); exact=F(s)**2*F(t)*(-1 if w else 1)
            self.assertEqual(r['determinant'],float(exact))
            self.assertEqual(r['polygon_area'],float(exact))
            self.assertEqual(r['area'],abs(float(exact)))
            # Base/altura também independem do cisalhamento.
            self.assertEqual(r['area'],s*abs(s*t))

    def test_composition_and_column_operations(self):
        mats=[[[a,b],[c,d]] for a,b,c,d in itertools.product([-1,0,1],repeat=4)]
        for a in mats:
            swapped=[[row[1],row[0]] for row in a]
            self.assertEqual(m.det2(swapped),-m.det2(a))
            self.assertEqual(m.det2([[a[0][0],a[0][1]+3*a[0][0]],[a[1][0],a[1][1]+3*a[1][0]]]),m.det2(a))
            self.assertEqual(m.det2([[2*x for x in row] for row in a]),4*m.det2(a))
            for b in mats:self.assertEqual(m.det2(m.multiply(a,b)),m.det2(a)*m.det2(b))

    def test_scale_is_not_conditioning_and_rounding(self):
        # Diagonais: kappa_2 = maior |entrada| / menor |entrada|.
        small=[1e-8,1e-8];anisotropic=[1e8,1e-8]
        self.assertEqual(max(small)/min(small),1)
        self.assertAlmostEqual(small[0]*small[1],1e-16,delta=1e-30)
        self.assertEqual(anisotropic[0]*anisotropic[1],1)
        self.assertEqual(max(anisotropic)/min(anisotropic),1e16)
        with localcontext() as ctx:
            ctx.prec=50
            z=Decimal('1.000000000000000001')
            self.assertEqual(z-Decimal(1),Decimal('1e-18'))
            self.assertEqual(m.det2([[1,1],[1,float(z)]]),0)

    def test_degenerate_orientation_and_domain(self):
        self.assertEqual(m.model(height=0)['orientation'],0)
        self.assertEqual(m.model(height=-1)['orientation'],-1)
        self.assertEqual(m.model(height=-1,swap=1)['orientation'],1)
        for args in [(0,0,1,0),(1,3,1,0),(1,0,3,0),(1,0,1,2),(float('nan'),0,1,0)]:
            with self.assertRaises(ValueError):m.model(*args)

if __name__=='__main__':unittest.main()
