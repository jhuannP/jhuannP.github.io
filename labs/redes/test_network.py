import unittest,itertools
from math import inf,ceil
try:
    from .network import ring,network,metrics,bfs
except ImportError:
    from network import ring,network,metrics,bfs

class NetworkTests(unittest.TestCase):
    def test_bfs_against_floyd_all_four_node_graphs(self):
        pairs=list(itertools.combinations(range(4),2))
        for bits in itertools.product([False,True],repeat=6):
            g=[set() for _ in range(4)];d=[[0 if i==j else inf for j in range(4)] for i in range(4)]
            for (u,v),present in zip(pairs,bits):
                if present:g[u].add(v);g[v].add(u);d[u][v]=d[v][u]=1
            for k in range(4):
                for i in range(4):
                    for j in range(4):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
            for source in range(4):self.assertEqual(bfs(g,source),{j:x for j,x in enumerate(d[source]) if x!=inf})
            m=metrics(g);connected=all(x!=inf for row in d for x in row)
            self.assertEqual(m['connected'],connected)
            if connected:self.assertAlmostEqual(m['mean_distance'],sum(map(sum,d))/12)
            else:self.assertIsNone(m['mean_distance'])

    def test_known_ring_complete_and_path(self):
        for n in [8,12,20]:
            m=metrics(ring(n));self.assertEqual(m['edges'],2*n)
            self.assertAlmostEqual(m['mean_clustering'],.5)
            expected=sum(ceil(min(k,n-k)/2) for k in range(1,n))/(n-1)
            self.assertAlmostEqual(m['mean_distance'],expected)
        complete=[set(range(4))-{u} for u in range(4)]
        self.assertEqual(metrics(complete)['mean_distance'],1)
        self.assertEqual(metrics(complete)['mean_clustering'],1)
        self.assertEqual(metrics([{1},{0,2},{1}])['mean_clustering'],0)

    def test_reproduction_and_monotonic_distance(self):
        for n in [8,12,20]:
            for seed in [0,42,100]:
                before=metrics(ring(n))['mean_distance']
                for extra in range(13):
                    g,added=network(n,extra,seed);g2,a2=network(n,extra,seed)
                    self.assertEqual(g,g2);self.assertEqual(added,a2)
                    self.assertEqual(metrics(g)['edges'],2*n+extra)
                    value=metrics(g)['mean_distance'];self.assertLessEqual(value,before);before=value
                    self.assertEqual(len(set(added)),extra)
        self.assertEqual(metrics(network(8,12,42)[0])['mean_distance'],1)
        self.assertEqual(metrics(network(8,12,42)[0])['mean_clustering'],1)

    def test_contracts(self):
        for args in [(7,0,42),(8,13,42),(8,0,True),(8,-1,1)]:
            with self.assertRaises(ValueError):network(*args)
        for graph in [[{0},set()],[{1},set()],[{2},set()],[{True},{0}]]:
            with self.assertRaises(ValueError):metrics(graph)
        with self.assertRaises(ValueError):bfs(ring(8),8)

if __name__=='__main__':unittest.main()
