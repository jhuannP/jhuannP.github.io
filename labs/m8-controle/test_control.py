import unittest
from itertools import product
from m8 import M8, encode, SOMA
from .control import controls


class ControlTests(unittest.TestCase):
    def test_add_reference(self):
        m=M8([0x4E]);m.acc=250;m.data[14]=10
        signals=controls(0x4E,m.acc)
        self.assertEqual((signals['acc_source'],signals['alu'],signals['acc_we'],signals['mem_we']),('alu','add',1,0))
        snapshot=m.data.copy();e=m.step()
        self.assertEqual((e['acc_after'],e['pc_after']), (4,1))
        self.assertEqual(m.data,snapshot)

    def test_signal_paths_against_engine(self):
        # 9 ops x 16 operands x 7 ACC values x 3 PC positions = 3024 transitions.
        for op, operand, acc, pc in product(('HALT','LDI','LDA','STA','ADD','SUB','JMP','JZ','OUT'),range(16),(0,1,7,15,127,250,255),(0,7,15)):
            instr=encode(op,operand)
            data=[(17*i+10)%256 for i in range(16)]
            program=[0]*16;program[pc]=instr
            m=M8(program,data);m.pc=pc;m.acc=acc;m.output=[19]
            sig=controls(instr,acc)
            # Interpret selections independently of the engine's opcode dispatch.
            candidates={'hold':acc,'immediate':operand,'memory':data[operand]}
            if sig['acc_source']=='alu':
                candidates['alu']=(acc+data[operand] if sig['alu']=='add' else acc-data[operand])%256
            expected_acc=candidates[sig['acc_source']] if sig['acc_we'] else acc
            expected_data=data.copy()
            if sig['mem_we']:expected_data[operand]=acc
            expected_pc=operand if sig['pc_source']=='target' else (pc+1)%16
            m.step()
            self.assertEqual((m.acc,m.pc,m.data,m.output,m.halted),
                (expected_acc,expected_pc,expected_data,[19]+([acc] if sig['out_we'] else []),bool(sig['stop'])))

    def test_conditional_old_state_and_wrap(self):
        for acc in range(256):
            s=controls(encode('JZ',9),acc)
            self.assertEqual(s['pc_source'],'target' if acc==0 else 'sequential')
            self.assertEqual(s['acc_we'],0)
        m=M8([0]*16);m.pc=15;m.step()
        self.assertTrue(m.halted);self.assertEqual(m.pc,0)

    def test_pure_description_and_ignored_low_bits(self):
        for low in range(16):
            s=controls(encode('OUT',low),77)
            self.assertEqual((s['out_we'],s['acc_we'],s['mem_we']),(1,0,0))
            self.assertEqual(controls(encode('HALT',low),77)['stop'],1)
        a=controls(0x4E,250);a['acc_we']=0
        self.assertEqual(controls(0x4E,250)['acc_we'],1)

    def test_previous_example_challenge_and_contracts(self):
        m=M8(SOMA)
        m.step();m.step()
        self.assertEqual((m.acc,m.data[14]),(3,3))
        m.step();e=m.step()
        self.assertEqual((e['acc_before'],m.acc,m.data[14],m.pc),(5,8,3,4))
        for instruction,acc in [(256,0),(-1,0),(True,0),(0,True),(0,256),(0x90,0)]:
            with self.assertRaises(ValueError):controls(instruction,acc)
