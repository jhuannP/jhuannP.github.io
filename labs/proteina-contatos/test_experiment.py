import unittest,json,hashlib
from pathlib import Path
from decimal import Decimal as D
from .experiment import ROWS,model,squared_distance

class ProteinContacts(unittest.TestCase):
    def test_original_public_snapshot(self):
        lab=Path(__file__).parent;raw=(lab/'1CRN.pdb').read_bytes();meta=json.loads((lab/'ca.json').read_text())
        self.assertEqual(hashlib.sha256(raw).hexdigest(),meta['sha256'])
        lines=[l for l in raw.decode().splitlines() if l.startswith('ATOM  ') and l[12:16].strip()=='CA']
        self.assertEqual(len(lines),46)
        for row,line in zip(ROWS,lines):
            self.assertEqual(line[16],' ');self.assertEqual(line[21],'A');self.assertEqual(line[26],' ')
            self.assertEqual(row[0],int(line[22:26]));self.assertEqual(row[1],line[17:20])
            self.assertEqual(row[2:],tuple(int(D(line[k:k+8])*1000) for k in (30,38,46)))
        self.assertEqual([list(x) for x in ROWS],meta['rows'])

    def test_all_cutoffs_and_separations_decimal_reference(self):
        # Independent unit system: decimal angstrom coordinates and unordered pairs.
        xyz=[tuple(D(v)/1000 for v in row[2:]) for row in ROWS]
        for cutoff in range(8,25):
            for separation in range(1,11):
                expected=set()
                for i,a in enumerate(xyz):
                    for j,b in enumerate(xyz):
                        if j>i and j-i>=separation and sum((x-y)**2 for x,y in zip(a,b))<=(D(cutoff)/2)**2:expected.add((i+1,j+1))
                r=model(cutoff,separation)
                self.assertEqual({(i,j) for i,j,_ in r['pairs']},expected)
                self.assertEqual(sum(r['degree']),2*len(expected))
                self.assertEqual(r['eligible'],sum(j-i>=separation for i in range(46) for j in range(i+1,46)))
                for k in [1,4,46]:self.assertEqual(r['degree'][k-1],len(model(cutoff,separation,k)['neighbors']))

    def test_invariance_monotonicity_and_known_pairs(self):
        moved=[(-r[3]+1000,r[2]-2000,r[4]+3000) for r in ROWS]
        for i,a in enumerate(ROWS):
            for j,b in enumerate(ROWS):self.assertEqual(squared_distance(a[2:],b[2:]),squared_distance(moved[i],moved[j]))
        previous=set()
        for cut in range(8,25):
            current={(i,j) for i,j,_ in model(cut,3)['pairs']};self.assertTrue(previous<=current);previous=current
        self.assertEqual([j for j,_ in model(10,10,4)['neighbors']],[32,44,46])
        self.assertNotIn(32,[j for j,_ in model(8,10,4)['neighbors']])
        self.assertEqual(32-4,28)

    def test_diagonal_and_contracts(self):
        self.assertEqual(model(16,1)['eligible'],1035)
        for args in [(7,3,4),(25,3,4),(16,0,4),(16,11,4),(16,3,0),(16,3,47),(True,3,4),(16.0,3,4)]:
            with self.assertRaises(ValueError):model(*args)
        for i,j,_ in model(24,1)['pairs']:self.assertLess(i,j)
