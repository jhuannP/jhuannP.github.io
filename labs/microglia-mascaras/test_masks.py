import unittest
from fractions import Fraction as Q
from itertools import product
from .masks import measure,threshold,projection_xy_overlap,cell_aggregates,CELL,FIELD,LYSOSOME

class MaskTests(unittest.TestCase):
    def test_fixture_and_physical_scale(self):
        signal=threshold(FIELD,10)
        result=measure(CELL,signal,LYSOSOME,(Q(1,2),Q(1,2),2))
        self.assertEqual((result['cell_count'],result['signal_count'],result['inside_count'],result['lysosome_inside_count']),(12,5,2,1))
        self.assertEqual((result['cell_volume'],result['inside_volume']),(6,1))
        self.assertEqual((result['occupancy'],result['signal_inside_fraction'],result['lysosome_fraction']),(Q(1,6),Q(2,5),Q(1,2)))
        larger=measure(CELL,signal,LYSOSOME,(1,1,4))
        self.assertEqual(larger['cell_volume'],8*result['cell_volume'])
        self.assertEqual(larger['inside_volume'],8*result['inside_volume'])
        self.assertEqual(larger['occupancy'],result['occupancy'])

    def test_dense_boolean_oracle_256_patterns(self):
        grid=((0,0,0),(1,0,0),(0,0,1),(1,0,1));m_bits=(True,True,False,True)
        m={p for p,b in zip(grid,m_bits) if b}
        for sb,lb in product(product((False,True),repeat=4),repeat=2):
            s={p for p,b in zip(grid,sb) if b};l={p for p,b in zip(grid,lb) if b}
            r=measure(m,s,l)
            # Independent dense per-site logic, no set-intersection oracle.
            inside=sum(a and b for a,b in zip(m_bits,sb))
            triple=sum(a and b and c for a,b,c in zip(m_bits,sb,lb))
            self.assertEqual((r['inside_count'],r['lysosome_inside_count']),(inside,triple))
            self.assertEqual(r['occupancy'],Q(inside,3))

    def test_projection_loses_axial_information(self):
        signal=threshold(FIELD,10)
        self.assertEqual(projection_xy_overlap(CELL,signal),(4,5))
        self.assertEqual(measure(CELL,signal,LYSOSOME)['inside_count'],2)
        # Same xy footprint, different z, completely outside the cell.
        shifted={(x,y,z+10) for x,y,z in signal}
        self.assertEqual(projection_xy_overlap(CELL,shifted),(4,5))
        self.assertEqual(measure(CELL,shifted,LYSOSOME)['inside_count'],0)

    def test_threshold_sensitivity_with_unchanged_cell(self):
        self.assertEqual([measure(CELL,threshold(FIELD,t),LYSOSOME)['occupancy'] for t in (10,15,25)],[Q(1,6),Q(1,12),Q(0)])
        self.assertEqual(len(threshold(FIELD,20)),2) # >= includes equality, point20 and point30.
        self.assertEqual(measure(CELL,threshold(FIELD,31),LYSOSOME)['signal_inside_fraction'],None)

    def test_aggregation_targets_differ(self):
        self.assertEqual(cell_aggregates([(10,2),(90,9)]),(Q(3,20),Q(11,100)))
        self.assertEqual(cell_aggregates([(10,2),(10,1)]),(Q(3,20),Q(3,20)))
        self.assertEqual(cell_aggregates([(20,4),(180,18)]),(Q(3,20),Q(11,100)))

    def test_contracts_and_empty_denominators(self):
        r=measure({(0,0,0)},set(),set())
        self.assertEqual(r['occupancy'],0);self.assertIsNone(r['signal_inside_fraction']);self.assertIsNone(r['lysosome_fraction'])
        for args in [(set(),set(),set()),({(True,0,0)},set(),set()),({(1.,0,0)},set(),set())]:
            with self.assertRaises(ValueError):measure(*args)
        for spacing in [(0,1,1),(1.,1,1),(1,1)]:
            with self.assertRaises(ValueError):measure(CELL,set(),set(),spacing)
        with self.assertRaises(ValueError):threshold(FIELD,10.)
        for counts in [[],[(0,0)],[(2,3)],[(True,0)]]:
            with self.assertRaises(ValueError):cell_aggregates(counts)

if __name__=='__main__':unittest.main()
