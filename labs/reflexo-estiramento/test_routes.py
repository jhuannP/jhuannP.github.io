import itertools
import unittest
from .routes import routes,EDGES

class RouteTests(unittest.TestCase):
    def test_fixed_routes(self):
        self.assertEqual(routes(EDGES,"Ia","alfa_hom"),[{"path":("Ia","alfa_hom"),"synapses":1,"sign":1}])
        self.assertEqual(routes(EDGES,"Ia","alfa_ant"),[{"path":("Ia","inter","alfa_ant"),"synapses":2,"sign":-1}])
        cut=tuple(e for e in EDGES if e[0]!="inter")
        self.assertEqual(routes(cut,"Ia","alfa_hom")[0]["synapses"],1)
        # Destination remains present via a disconnected node; no surviving path.
        self.assertEqual(routes(cut+(("other","alfa_ant",1),),"Ia","alfa_ant"),[])

    def test_independent_permutation_oracle(self):
        nodes=("A","B","C","D")
        pairs=(("A","B"),("A","C"),("B","C"),("B","D"),("C","D"))
        for signals in itertools.product((-1,1),repeat=5):
            edges=tuple((a,b,s) for (a,b),s in zip(pairs,signals))
            lookup={(a,b):s for a,b,s in edges};expected=set()
            for length in range(3):
                for middle in itertools.permutations(("B","C"),length):
                    p=("A",)+middle+("D",);steps=list(zip(p,p[1:]))
                    if all(e in lookup for e in steps):
                        neg=sum(lookup[e]<0 for e in steps)
                        expected.add((p,len(steps),-1 if neg%2 else 1))
            actual={(a['path'],a['synapses'],a['sign']) for a in routes(edges,"A","D")}
            self.assertEqual(actual,expected)

    def test_opposing_paths_not_collapsed(self):
        edges=(("A","D",1),("A","B",1),("B","D",-1))
        result=routes(edges,"A","D")
        self.assertEqual({a['sign'] for a in result},{-1,1})
        self.assertEqual(len(result),2)

    def test_contracts(self):
        for bad in ((("A","B",0),),(("A","B",True),),(("A","B",1),("A","B",-1))):
            with self.assertRaises(ValueError): routes(bad,"A","B")
        with self.assertRaises(ValueError): routes(EDGES,"Ia","unknown")
        with self.assertRaises(ValueError): routes(EDGES,"Ia","Ia")
