import unittest,itertools
from fractions import Fraction as Q
from .experiment import build,OPS,IRREPS,mul,trace,reduce_characters

def rank(columns):
    rows=[list(map(Q,r)) for r in zip(*columns)];pivot=0
    for j in range(len(rows[0])):
        k=next((k for k in range(pivot,len(rows)) if rows[k][j]),None)
        if k is None:continue
        rows[pivot],rows[k]=rows[k],rows[pivot];v=rows[pivot][j]
        rows[pivot]=[x/v for x in rows[pivot]]
        for i in range(len(rows)):
            if i!=pivot:
                t=rows[i][j];rows[i]=[x-t*y for x,y in zip(rows[i],rows[pivot])]
        pivot+=1
    return pivot

class DisplacementRepresentationTests(unittest.TestCase):
    def test_group_and_independent_fixed_atom_trace(self):
        for geometry in ('bent','linear'):
            m=build(geometry)
            for i,(name,s) in enumerate(OPS.items()):
                fixed=sum(tuple(a*x for a,x in zip(s,r))==r for r in m['positions'])
                self.assertEqual(m['characters']['total'][i],fixed*sum(s))
                for other,t in OPS.items():
                    signs=tuple(a*b for a,b in zip(s,t));product=next(n for n,v in OPS.items() if v==signs)
                    self.assertEqual(mul(m['matrices'][name],m['matrices'][other]),m['matrices'][product])
    def test_projectors_invariance_and_independent_rank(self):
        for geometry,expected in [('bent',6),('linear',5)]:
            m=build(geometry)
            self.assertEqual(rank(m['translations']+m['rotations']),expected)
            self.assertEqual(m['rigid_rank'],expected)
            self.assertEqual(m['vibration_dimension'],9-expected)
            for P in [m['PT'],m['PR'],m['PV']]:
                self.assertEqual(mul(P,P),P)
                self.assertEqual(P,list(map(list,zip(*P))))
                for D in m['matrices'].values():self.assertEqual(mul(D,P),mul(P,D))
    def test_characters_orthogonality_and_reconstruction(self):
        for x,y in itertools.product(IRREPS,repeat=2):self.assertEqual(sum(a*b for a,b in zip(IRREPS[x],IRREPS[y])),4*int(x==y))
        for geometry in ('bent','linear'):
            m=build(geometry)
            for chars in m['characters'].values():
                multiplicities=reduce_characters(chars)
                reconstructed=[sum(multiplicities[n]*IRREPS[n][i] for n in IRREPS) for i in range(4)]
                self.assertEqual(reconstructed,chars)
            self.assertEqual(m['characters']['total'],[9,-1,3,1])
        self.assertEqual(build()['multiplicities'],{'A1':2,'A2':0,'B1':1,'B2':0})
        self.assertEqual(build('linear')['multiplicities'],{'A1':2,'A2':0,'B1':1,'B2':1})
    def test_axis_rotation_and_contract(self):
        self.assertTrue(any(build()['rotations'][0]))
        self.assertFalse(any(build('linear')['rotations'][0]))
        with self.assertRaises(ValueError):build('coincident')
        with self.assertRaises(ValueError):reduce_characters([1,0,0,0])
