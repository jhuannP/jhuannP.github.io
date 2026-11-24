import unittest
import math
from dataclasses import FrozenInstanceError
from .experiment import fit,transform,inverse

class ColumnScalingTests(unittest.TestCase):
    def test_lesson_columns(self):
        s=fit([(0,100),(2,300)])
        self.assertEqual(s.mean,(1,200));self.assertEqual(s.variance,(1,10000));self.assertEqual(s.scale,(1,100))
        self.assertEqual(transform([(0,100),(2,300)],s),[(-1,-1),(1,1)])
        self.assertEqual(transform([(4,500)],s),[(3,3)])

    def test_train_moments_and_inverse(self):
        for data in [[(0,1),(2,3),(4,9)],[(1,3),(1,7),(1,11)],[(2,10)],[(0,-5),(3,-2),(6,1),(9,4)]]:
            s=fit(data);z=transform(data,s);restored=inverse(z,s)
            for original,back in zip(data,restored):
                for a,b in zip(original,back):self.assertAlmostEqual(a,b,places=11)
            for j,var in enumerate(s.variance):
                self.assertAlmostEqual(math.fsum(row[j] for row in z)/len(z),0,places=12)
                self.assertAlmostEqual(math.fsum(row[j]**2 for row in z)/len(z),1 if var else 0,places=12)

    def test_no_refit_and_leaking_changes_state(self):
        train=[(0,100),(2,300)];s=fit(train);snapshot=(s.mean,s.variance,s.scale,s.n)
        transform([(4,500),(1000,-10)],s)
        self.assertEqual((s.mean,s.variance,s.scale,s.n),snapshot)
        with self.assertRaises(FrozenInstanceError):s.n=99
        wrong=fit(train+[(4,500)])
        self.assertEqual(wrong.mean,(2,300))
        self.assertNotEqual(transform([(4,500)],wrong),transform([(4,500)],s))
        self.assertAlmostEqual(transform([(4,500)],wrong)[0][0],math.sqrt(1.5),places=12)

    def test_positive_unit_conversion(self):
        data=[(0,100),(2,300),(5,50)];test=[(4,500)]
        a=transform(test,fit(data))
        changed=[(x,1000*y+7) for x,y in data];changed_test=[(x,1000*y+7) for x,y in test]
        b=transform(changed_test,fit(changed))
        for first,second in zip(a[0],b[0]):self.assertAlmostEqual(first,second,places=12)

    def test_constant_and_denominator(self):
        s=fit([(0,10),(2,10)])
        self.assertEqual(s.variance,(1,0));self.assertEqual(s.scale,(1,1))
        self.assertEqual(transform([(4,12)],s),[(3,2)])
        self.assertEqual(transform([],s),[])
        self.assertEqual(inverse([],s),[])

    def test_contract(self):
        for data in ([],[[]],[[1],[1,2]],[[True]],[[float('nan')]],[[float('inf')]]):
            with self.assertRaises(ValueError):fit(data)
        s=fit([[1,2]])
        for data in ([[1]],[[1,2,3]],[[1,float('nan')]]):
            with self.assertRaises(ValueError):transform(data,s)
        with self.assertRaises(ValueError):transform([[1]],None)
