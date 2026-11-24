import json
import subprocess
import unittest
from m8 import M8, CONTAGEM, encode
from test_m8 import NODE_SCRIPT
from .countdown import make, PROGRAM


class CountdownTests(unittest.TestCase):
    def test_three_and_translation(self):
        self.assertEqual(PROGRAM,(0x2E,0x76,0x80,0x5F,0x3E,0x60,0x00))
        m=make(3);self.assertEqual(m.run(21),[3,2,1])
        self.assertEqual(len(m.trace),21);self.assertEqual(m.data[14],0)
        self.assertEqual(m.trace[-1]['pc_before'],6)
        self.assertEqual(m.pc,7)
        self.assertEqual([e['pc_before'] for e in m.trace[:6]],list(range(6)))

    def test_full_input_domain_and_invariant(self):
        for n in range(256):
            m=make(n);original=list(m.data)
            self.assertEqual(m.run(6*n+3),list(range(n,0,-1)))
            self.assertEqual(len(m.trace),6*n+3)
            self.assertEqual(m.data[:14],original[:14]);self.assertEqual(m.data[15],1)
            self.assertEqual(m.program,list(PROGRAM))
            entries=[e for e in m.trace if e['pc_before']==0]
            self.assertEqual(len(entries),n+1)
            for k,e in enumerate(entries):
                self.assertEqual(e['acc_after'],n-k)
                self.assertEqual(e['output'],list(range(n,n-k,-1)))
            self.assertTrue(all(e['write'] is None or e['write'][0]==14 for e in m.trace))

    def test_budget_and_resume(self):
        m=make(0);self.assertEqual(m.run(3),[])
        m=make(3)
        with self.assertRaises(TimeoutError):m.run(20)
        self.assertFalse(m.halted);self.assertEqual(m.pc,6)
        self.assertEqual(m.output,[3,2,1]);self.assertEqual(m.run(1),[3,2,1])
        self.assertTrue(m.halted)

    def test_postcondition_zero_wrap(self):
        # O exemplo antigo tem precondição de contador positivo; não o alteramos.
        program=list(CONTAGEM);program[0]=encode('LDI',0)
        m=M8(program);self.assertEqual(m.run(1540),[0]+list(range(255,0,-1)))
        self.assertEqual(len(m.trace),1540);self.assertEqual(m.data[14],0)

    def test_decrement_changes_contract(self):
        m=make(4,2);self.assertEqual(m.run(15),[4,2])
        for d in (0,2):
            m=make(3,d)
            with self.assertRaises(TimeoutError):m.run(6*129)
            entries=[e['acc_after'] for e in m.trace if e['pc_before']==0]
            self.assertTrue(all(x!=0 for x in entries))
            self.assertEqual(entries,[(3-d*k)%256 for k in range(129)])
        # Não inferimos ausência de término só do timeout; a prova modular está na aula.

    def test_existing_javascript_agrees(self):
        cases=[];expected=[]
        for n,budget in [(0,3),(1,9),(3,20),(3,21),(15,93)]:
            m=make(n);cases.append(dict(program=list(PROGRAM),data=list(m.data),budget=budget))
            for _ in range(budget):
                if m.halted:break
                m.step()
            expected.append(m.trace)
        r=subprocess.run(['node','-e',NODE_SCRIPT],input=json.dumps(cases),text=True,capture_output=True,check=True)
        self.assertEqual(json.loads(r.stdout),expected)

    def test_contracts(self):
        for n in (-1,256,True,3.0,None):
            with self.assertRaises(ValueError):make(n)
        for d in (-1,256,True,1.0):
            with self.assertRaises(ValueError):make(3,d)
