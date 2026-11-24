import unittest
from itertools import product
from fractions import Fraction as Q
from copy import deepcopy
from .experiment import dijkstra,path_to,example

def bellman_ford(graph,source):
    # Referência independente: até V−1 varreduras completas, sem fila/heap.
    dist={v:None for v in graph};dist[source]=Q(0)
    for _ in range(len(graph)-1):
        old=dist.copy()
        for u,edges in graph.items():
            if old[u] is None:continue
            for v,w in edges:
                value=old[u]+w
                if dist[v] is None or value<dist[v]:dist[v]=value
    return dist

class DijkstraTests(unittest.TestCase):
    def test_example_and_bfs_counterexample(self):
        r=dijkstra(example(),"A")
        self.assertEqual(r["dist"],dict(A=0,B=3,C=1,D=4,E=None))
        self.assertEqual(path_to(r,"D"),["A","C","B","D"])
        self.assertEqual(path_to(r,"A"),["A"])
        self.assertIsNone(path_to(r,"E"))
        self.assertEqual(r["settled"],[("A",0),("C",1),("B",3),("D",4)])
        self.assertEqual(dict(example()["A"])["D"],10) # direct one-edge path costs more
    def test_all_three_vertex_graphs(self):
        vertices=("a","b","c");edges=[(a,b) for a in vertices for b in vertices if a!=b]
        for weights in product((None,0,1,3),repeat=6):
            graph={v:[] for v in vertices}
            for (u,v),w in zip(edges,weights):
                if w is not None:graph[u].append((v,w))
            for source in vertices:
                r=dijkstra(graph,source)
                self.assertEqual(r["dist"],bellman_ford(graph,source))
                self.assertEqual(len(r["settled"]),len({v for v,_ in r["settled"]}))
                for target,distance in r["dist"].items():
                    path=path_to(r,target)
                    if distance is None:self.assertIsNone(path);continue
                    self.assertEqual(path[0],source);self.assertEqual(path[-1],target)
                    cost=sum(min(w for v,w in graph[u] if v==nextv) for u,nextv in zip(path,path[1:]))
                    self.assertEqual(cost,distance)
    def test_zero_cycles_parallel_edges_and_fractional_weights(self):
        graph=dict(s=[("s",0),("a",3),("a",Q(1,2)),("b",Q(1,2))],
                   a=[("b",0)],b=[("a",0),("t",Q(1,3))],t=[])
        r=dijkstra(graph,"s")
        self.assertEqual(r["dist"]["t"],Q(5,6))
        self.assertEqual(len(r["settled"]),4)
        self.assertEqual(path_to(r,"t"),["s","b","t"])
    def test_scaling_isolated_node_and_preservation(self):
        graph=example();old=deepcopy(graph);a=dijkstra(graph,"A")
        scaled={u:[(v,3*w) for v,w in e] for u,e in graph.items()}
        b=dijkstra(scaled,"A")
        for v,d in a["dist"].items():self.assertEqual(b["dist"][v],None if d is None else 3*d)
        self.assertEqual(graph,old)
        graph["unreachable"]=[("D",0)]
        self.assertEqual(dijkstra(graph,"A")["dist"]["D"],4)
    def test_contracts_including_unreachable_negative_edge(self):
        for graph,source in [({},"s"),({"s":[]}, "z"),({"s":[("z",1)]},"s"),
          ({"s":[("s",-1)]},"s"),({"s":[("s",True)]},"s"),
          ({"s":[("s",.5)]},"s"),({"s":[],"z":[("s",-1)]},"s"),
          ({"s":[("s",)]},"s"),({"s":[([],1)]},"s"),({"s":[]},[])]:
            with self.assertRaises(ValueError):dijkstra(graph,source)
        with self.assertRaises(ValueError):path_to(dijkstra({"s":[]},"s"),"z")
