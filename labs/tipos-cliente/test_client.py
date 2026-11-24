import unittest,math,json
from pathlib import Path
from .client import label_key,interference

class ClientTests(unittest.TestCase):
    def test_label_examples_and_no_accent_erasure(self):
        for a,b in ((' FÍSICA ','FI\u0301SICA'),(' Biologia ','BIOLOGIA'),(' Química','QUI\u0301MICA ')):
            saved=a;self.assertEqual(label_key(a),label_key(b));self.assertEqual(a,saved)
            self.assertEqual(label_key(label_key(a)),label_key(a))
        self.assertNotEqual(label_key('física'),label_key('fisica'))
        self.assertEqual(len('FÍSICA'),6);self.assertEqual(len('FI\u0301SICA'),7)
        self.assertEqual(len('FÍSICA'.encode('utf-8')),7)

    def test_mutation_return_alias_and_shallow_copy(self):
        a=[1];b=a;result=b.append(2)
        self.assertIsNone(result);self.assertIs(a,b);self.assertEqual(a,[1,2])
        c=a.copy();c.append(3);self.assertEqual(a,[1,2]);self.assertEqual(c,[1,2,3])
        nested=[[1]];outer=nested.copy();outer[0].append(2)
        self.assertEqual(nested,[[1,2]]);self.assertIsNot(nested,outer)
        # Annotation alone is not a runtime check; explicit guard is separate.
        def length(text:str)->int:return len(text)
        self.assertEqual(length([10,20]),2)

    def test_complex_reference_and_zero(self):
        r=interference(3+4j,-3+4j)
        self.assertEqual((r['z_abs'],r['w_abs'],r['sum_abs']),(5,5,8))
        self.assertEqual((r['sum_square'],r['component_squares'],r['cross']),(64,50,14))
        self.assertEqual(interference(3+4j,-3-4j)['sum_abs'],0)
        self.assertEqual(interference(0,0)['sum_square'],0)

    def test_grid_independent_cartesian_identity(self):
        for a in range(-2,3):
            for b in range(-2,3):
                for c in range(-2,3):
                    for d in range(-2,3):
                        r=interference(complex(a,b),complex(c,d))
                        self.assertEqual(r['sum_square'],(a+c)**2+(b+d)**2)
                        self.assertEqual(r['cross'],2*(a*c+b*d))
                        self.assertEqual(r['sum_square'],r['component_squares']+r['cross'])
        root=Path(__file__).resolve().parents[2]
        lesson=next(l for l in json.loads((root/'content/lessons.json').read_text()) if l['id']=='usar-tipos')
        exec(lesson['python'],{});exec(lesson['codingPractice']['solution'],{})

    def test_contracts(self):
        for x in ('','  ',None,2,True):
            with self.assertRaises(ValueError):label_key(x)
        for x in (True,'3+4j',float('nan'),complex(0,float('inf')),10**1000,1e308):
            with self.assertRaises(ValueError):interference(x,x)
