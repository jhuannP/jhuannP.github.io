from fractions import Fraction as Q
from itertools import product
import unittest
from .network import solve

class NetworkTests(unittest.TestCase):
    def test_examples(self):
        direct=solve(12,0,(6,3));mixed=solve(12,2,(6,3))
        self.assertEqual((direct['parallel'],direct['current'],direct['currents'],direct['source_power']),(Q(2),Q(6),(Q(2),Q(4)),Q(72)))
        self.assertEqual((mixed['total'],mixed['load_voltage'],mixed['currents'],mixed['series_power'],mixed['source_power']),(Q(4),Q(6),(Q(1),Q(2)),Q(18),Q(36)))

    def test_against_independent_nodal_equation_and_balances(self):
        # Obtain node potential from (Vs-Vb)/R0=Vb/r1+Vb/r2, no equivalent R.
        for vs,r0,r1,r2 in product((0,3,12),(1,2,5),(1,3,6),(2,4,9)):
            vb=Q(vs,r0)/(Q(1,r0)+Q(1,r1)+Q(1,r2))
            expected=(Q(vs)-vb)/r0
            result=solve(vs,r0,(r1,r2))
            self.assertEqual(result['load_voltage'],vb)
            self.assertEqual(result['current'],expected)
            self.assertEqual(sum(result['currents']),result['current'])
            self.assertEqual(sum(result['powers'])+result['series_power'],result['source_power'])
            self.assertEqual(result['load_voltage']+result['current']*r0,vs)

    def test_branch_changes_and_zero_source(self):
        alone=solve(12,0,(6,));added=solve(12,0,(6,3))
        self.assertEqual(alone['currents'][0],added['currents'][0])
        self.assertGreater(added['current'],alone['current'])
        alone=solve(12,2,(6,));added=solve(12,2,(6,3))
        self.assertLess(added['currents'][0],alone['currents'][0])
        self.assertGreater(added['current'],alone['current'])
        zero=solve(0,2,(6,3));self.assertEqual(zero['parallel'],2)
        self.assertEqual(zero['current'],0);self.assertEqual(zero['source_power'],0)

    def test_contracts_and_unequal_currents(self):
        for bad in (True,1.5,'12'):
            with self.assertRaises(TypeError):solve(bad,0,(3,6))
        for params in ((-1,0,(3,)),(12,-1,(3,)),(12,0,()),(12,0,(0,)),(12,0,(-1,))):
            with self.assertRaises(ValueError):solve(*params)
        values=[Q(3,2),Q(9,2)];r=solve(3,0,values)
        self.assertEqual(values,[Q(3,2),Q(9,2)])
        self.assertEqual(r['currents'][0]/r['currents'][1],3)

if __name__=='__main__':unittest.main()
