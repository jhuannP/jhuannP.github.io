import unittest
from itertools import product
from .affine import normalize,execute,compile_affine,compose,encode,decode


class AffineTests(unittest.TestCase):
    def test_original_and_extension(self):
        p=[('ADD',3),('MUL',2)]
        self.assertEqual(execute(p),dict(result=6,steps=2,trace=(0,3,6)))
        self.assertEqual(compile_affine(p),(2,6))
        self.assertEqual(execute([('ADD',4),('MUL',3)],1)['result'],15)
        self.assertEqual(execute([('ADD',5),('SUB',2),('MUL',3)])['result'],9)
        self.assertEqual(p,[('ADD',3),('MUL',2)])

    def test_every_short_program_against_compiled_semantics_and_encoding(self):
        instructions=list(product(('ADD','SUB','MUL'),range(-2,3)))
        count=0
        for length in range(4):
            for p in product(instructions,repeat=length):
                a,b=compile_affine(p)
                self.assertEqual(decode(encode(p)),p)
                for x in range(-3,4):
                    result=execute(p,x)
                    self.assertEqual(result['result'],a*x+b)
                    self.assertEqual(result['steps'],length)
                    self.assertEqual(len(result['trace']),length+1)
                count+=1
        self.assertEqual(count,3616)

    def test_prefix_invariant_and_composition(self):
        programs=[(),(('ADD',3),),(('MUL',-2),),(('ADD',3),('MUL',2)),(('MUL',0),('SUB',5))]
        for p in programs:
            for x in range(-3,4):
                trace=execute(p,x)['trace']
                for k in range(len(p)+1):
                    a,b=compile_affine(p[:k]);self.assertEqual(trace[k],a*x+b)
            for q in programs:
                self.assertEqual(compose(p,q),compile_affine(p+q))
                for x in range(-3,4):
                    a,b=compose(p,q)
                    self.assertEqual(a*x+b,execute(q,execute(p,x)['result'])['result'])
        self.assertNotEqual(compose((('ADD',3),),(('MUL',2),)),compose((('MUL',2),),(('ADD',3),)))

    def test_affine_class_and_square_obstruction(self):
        for a,b in product(range(-3,4),repeat=2):
            p=(('MUL',a),('ADD',b))
            self.assertEqual(compile_affine(p),(a,b))
            outputs=[execute(p,x)['result'] for x in range(3)]
            self.assertEqual(outputs[2]-2*outputs[1]+outputs[0],0)
        self.assertEqual(2**2-2*1**2+0**2,2)
        # Matching square at 0 and 1 uniquely forces the identity affine map.
        self.assertEqual(execute((('MUL',1),('ADD',0)),2)['result'],2)

    def test_large_integers_and_empty_program(self):
        n=10**100
        self.assertEqual(execute((('ADD',n),('MUL',n)),n)['result'],2*n*n)
        self.assertEqual(execute((),-17),dict(result=-17,steps=0,trace=(-17,)))

    def test_contracts_and_invalid_descriptions(self):
        for p in [None,'ADD 2',[('ADD',True)],[('ADD',1.0)],[('RUN','x')],[('ADD',)],[(1,2)]]:
            with self.subTest(p=p),self.assertRaises(ValueError):normalize(p)
        for text in ['null','{}','[["ADD",true]]','[["ADD",1.0]]','[["ADD",NaN]]','[["ADD",Infinity]]','[["X",1]]','[']:
            with self.subTest(text=text),self.assertRaises(ValueError):decode(text)
        with self.assertRaises(ValueError):execute([],True)
        with self.assertRaises(ValueError):decode(1)

if __name__=='__main__':unittest.main()
