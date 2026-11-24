import unittest
from itertools import product
from .path import shortest_crossing
from ..percolacao.experiment import crosses

def relaxation_distance(grid):
    # Oráculo por relaxações síncronas até ponto fixo, sem fila ou predecessores.
    h,w=len(grid),len(grid[0]);infinity=h*w+1
    dist=[[0 if i==0 and grid[i][j] else infinity for j in range(w)] for i in range(h)]
    for _ in range(h*w):
        following=[row[:] for row in dist]
        for i in range(h):
            for j in range(w):
                if not grid[i][j]:continue
                for a,b in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                    if 0<=a<h and 0<=b<w and grid[a][b]:following[i][j]=min(following[i][j],dist[a][b]+1)
        if following==dist:break
        dist=following
    value=min(dist[-1]);return None if value==infinity else value

class PathTests(unittest.TestCase):
    def test_682_small_grids_against_relaxation(self):
        count=0
        for h in range(1,4):
            for w in range(1,4):
                for cells in product((0,1),repeat=h*w):
                    grid=[list(cells[i*w:(i+1)*w]) for i in range(h)];before=[row[:] for row in grid]
                    result=shortest_crossing(grid);path=result['path']
                    self.assertEqual(result['distance'],relaxation_distance(grid))
                    self.assertEqual(path is not None,crosses(grid));self.assertEqual(grid,before)
                    self.assertLessEqual(result['expanded'],result['discovered']);self.assertLessEqual(result['discovered'],h*w)
                    if path is not None:
                        self.assertEqual(path[0][0],0);self.assertEqual(path[-1][0],h-1)
                        self.assertEqual(len(path)-1,result['distance']);self.assertEqual(len(path),len(set(path)))
                        self.assertTrue(all(grid[i][j] for i,j in path))
                        self.assertTrue(all(abs(a-c)+abs(b-d)==1 for (a,b),(c,d) in zip(path,path[1:])))
                    count+=1
        self.assertEqual(count,682)
    def test_fixtures_and_ties(self):
        result=shortest_crossing([[1,0,0],[1,1,0],[0,1,1]])
        self.assertEqual(result['path'],((0,0),(1,0),(1,1),(2,1)))
        self.assertEqual(result['distance'],3)
        self.assertEqual(shortest_crossing([[0,1,0]])['path'],((0,1),))
        self.assertIsNone(shortest_crossing([[1,0],[0,1]])['path'])
        self.assertEqual(shortest_crossing([[1,1],[1,1]])['distance'],1)
    def test_opening_sites_cannot_destroy_or_lengthen(self):
        for cells in product((0,1),repeat=6):
            grid=[list(cells[:3]),list(cells[3:])];before=shortest_crossing(grid)['distance']
            for k in range(6):
                changed=[row[:] for row in grid];changed[k//3][k%3]=1
                after=shortest_crossing(changed)['distance']
                if before is not None:self.assertIsNotNone(after);self.assertLessEqual(after,before)
    def test_contracts(self):
        for grid in ([],[[]],[[1],[1,0]],['10'],[[.5]],[[2]],[[None]],[[1]*31],[[1]]*31):
            with self.assertRaises(ValueError):shortest_crossing(grid)
