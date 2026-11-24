import unittest
from itertools import product
from .machine import run,UNARY,PARITY,unary_tape,binary_tape


class MachineTests(unittest.TestCase):
    def test_unary_result_steps_and_invariant(self):
        for n in range(31):
            original=unary_tape(n)
            r=run(UNARY,original,max_steps=n+1)
            self.assertEqual((r['status'],r['steps'],r['head']),('aceita',n+1,n+1))
            self.assertEqual(r['tape'],{i:'1' for i in range(n+1)})
            self.assertEqual(original,unary_tape(n))
            self.assertEqual(len(r['history']),n+2)
            for k,s in enumerate(r['history'][:-1]):
                self.assertEqual((s['state'],s['head'],s['steps']),('buscar',k,k))
                self.assertEqual(s['tape'],original)

    def test_parity_all_binary_words_up_to_eight(self):
        for length in range(9):
            for letters in product('01',repeat=length):
                word=''.join(letters);tape=binary_tape(word)
                r=run(PARITY,tape,state='par',max_steps=length+1)
                expected='aceita' if word.count('1')%2==0 else 'rejeita'
                self.assertEqual((r['status'],r['steps'],r['head']),(expected,length+1,length+1))
                self.assertEqual(r['tape'],tape)

    def test_budget_boundary_and_already_final(self):
        before=run(UNARY,unary_tape(3),max_steps=3)
        self.assertEqual((before['status'],before['state'],before['head']),('limite','buscar',3))
        self.assertEqual(run(UNARY,unary_tape(3),max_steps=4)['status'],'aceita')
        self.assertEqual(run({}, {},state='aceita',max_steps=0)['status'],'aceita')
        self.assertEqual(run({}, {},state='rejeita',max_steps=0)['status'],'rejeita')

    def test_undefined_is_not_rejection_and_limit_is_not_nontermination(self):
        self.assertEqual(run({}, {})['status'],'sem_regra')
        loop={('buscar','_'):('buscar','_',1)}
        for limit in [0,1,7]:
            r=run(loop,{},max_steps=limit)
            self.assertEqual((r['status'],r['head'],r['steps'],r['tape']),('limite',limit,limit,{}))
        # Same budget status also occurs in a machine with a known finite termination.
        self.assertEqual(run(UNARY,unary_tape(7),max_steps=7)['status'],'limite')

    def test_left_write_and_blank_erasure(self):
        program={('buscar','1'):('voltar','0',-1),('voltar','_'):('aceita','_',0)}
        r=run(program,{0:'1'},max_steps=2)
        self.assertEqual((r['status'],r['head'],r['tape']),('aceita',-1,{0:'0'}))
        erase={('buscar','1'):('aceita','_',0)}
        r=run(erase,{0:'1',3:'_'})
        self.assertEqual(r['tape'],{})
        self.assertEqual(r['history'][0]['tape'],{0:'1'})

    def test_input_contracts(self):
        for n in [-1,True,1.0,'3']:
            with self.assertRaises(ValueError):unary_tape(n)
        for word in ['102','_1',True]:
            with self.assertRaises(ValueError):binary_tape(word)
        cases=[({}, {},dict(head=True)),({}, {},dict(max_steps=-1)),({}, {},dict(max_steps=True)),
               ({}, {True:'1'},{}),({}, {0:'ab'},{}),({}, {},dict(accept='x',reject='x')),
               ({('buscar','_'):('aceita','_',True)}, {},{}),
               ({('buscar','_'):('aceita','_',2)}, {},{}),
               ({('buscar','_'):('aceita','_')}, {},{})]
        for program,tape,options in cases:
            with self.subTest(options=options),self.assertRaises(ValueError):run(program,tape,**options)

if __name__=='__main__':unittest.main()
