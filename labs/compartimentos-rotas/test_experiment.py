import unittest
from .experiment import path,model,NODES,EDGES

class CompartmentRouteTests(unittest.TestCase):
    def test_all_pairs_against_independent_path_enumeration(self):
        def enumerate_paths(current,end,visited):
            if current==end:return [[]]
            return [[edge]+tail for edge in EDGES if edge[0]==current and edge[1] not in visited for tail in enumerate_paths(edge[1],end,visited|{edge[1]})]
        for start in NODES:
            for end in NODES:
                alternatives=enumerate_paths(start,end,{start});actual=path(start,end)
                if not alternatives:self.assertIsNone(actual)
                else:self.assertIn(actual,alternatives);self.assertEqual(len(actual),min(map(len,alternatives)))
    def test_topology_routes_and_invalid_cases(self):
        groups=dict(citosol='cyt',nucleo='cyt',re='luminal',golgi='luminal',exterior='luminal',matriz='matrix')
        for source,target,kind in EDGES:
            if kind=='translocacao':self.assertNotEqual(groups[source],groups[target])
            else:self.assertEqual(groups[source],groups[target])
        self.assertEqual([k for _,_,k in model(1)['steps']],['translocacao','vesicular','vesicular'])
        self.assertEqual(model(0)['crossings'],0);self.assertEqual(model(2)['crossings'],1)
        self.assertEqual(model(3)['steps'],[]);self.assertIsNone(path('nucleo','golgi'))
        for case in (-1,4,.5,True):
            with self.assertRaises(ValueError):model(case)
        with self.assertRaises(ValueError):path('lisossomo','re')
