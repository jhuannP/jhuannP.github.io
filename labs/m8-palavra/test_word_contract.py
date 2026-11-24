import unittest
from .word_contract import inspect
from m8 import M8,encode,decode

class WordContract(unittest.TestCase):
    def test_every_byte_against_positional_arithmetic(self):
        names=('HALT','LDI','LDA','STA','ADD','SUB','JMP','JZ','OUT')
        valid=[];invalid=[]
        for byte in range(256):
            op,arg=divmod(byte,16)
            if op>=9:
                with self.assertRaises(ValueError):inspect(byte)
                invalid.append(byte);continue
            item=inspect(byte);valid.append(byte)
            self.assertEqual((item['operation'],item['operand']),(names[op],arg))
            self.assertEqual(item['opcode_bits']+item['operand_bits'],item['binary'])
            self.assertEqual(sum(int(bit)*2**(7-i) for i,bit in enumerate(item['binary'])),byte)
            self.assertEqual(encode(*decode(byte)),byte)
        self.assertEqual((len(valid),len(invalid)),(144,112))
        self.assertEqual(len({inspect(w)['canonical_word'] for w in valid}),114)

    def test_ignored_operands_preserve_effect_but_not_ir(self):
        for name in ['HALT','OUT']:
            for acc in [0,1,15,128,255]:
                reference=M8([encode(name,0)]);reference.acc=acc;reference.step()
                for arg in range(16):
                    machine=M8([encode(name,arg)]);machine.acc=acc;machine.step()
                    self.assertEqual((machine.pc,machine.acc,machine.data,machine.output,machine.halted),
                                     (reference.pc,reference.acc,reference.data,reference.output,reference.halted))
                    self.assertEqual(machine.ir,encode(name,arg))
                    self.assertEqual(inspect(machine.ir)['canonical_word'],encode(name,0))

    def test_immediate_address_and_data_range(self):
        data=[(17*i+6)%256 for i in range(16)];data[3]=203
        for arg in range(16):
            a=M8([encode('LDI',arg)],data);a.step()
            b=M8([encode('LDA',arg)],data);b.step()
            self.assertEqual(a.acc,arg);self.assertEqual(b.acc,data[arg])
            self.assertEqual(inspect(a.ir)['operand_kind'],'immediate')
            self.assertEqual(inspect(b.ir)['operand_kind'],'data_address')
        self.assertEqual(M8([0x13],data).program,[0x13])
        with self.assertRaises(ValueError):encode('LDI',203)
        # Um operando fora do campo derrama sobre o opcode se não for validado.
        self.assertEqual(decode((4<<4)|16),('SUB',0))
        with self.assertRaises(ValueError):encode('ADD',16)

    def test_store_preserves_program_and_other_addresses(self):
        for arg in range(16):
            for acc in [0,203,255]:
                data=[i+20 for i in range(16)];machine=M8([encode('STA',arg)],data);machine.acc=acc
                program=machine.program.copy();event=machine.step()
                self.assertEqual(machine.program,program);self.assertEqual(machine.acc,acc)
                self.assertEqual(machine.data[arg],acc);self.assertEqual(event['write'],[arg,acc])
                self.assertEqual([v for i,v in enumerate(machine.data) if i!=arg],[v for i,v in enumerate(data) if i!=arg])
                self.assertEqual(data,list(range(20,36)))

    def test_pc_branch_wrap_and_missing_word(self):
        machine=M8([encode('OUT')]*16);machine.pc=15;machine.acc=203
        machine.step();self.assertEqual((machine.pc,machine.output),(0,[203]))
        for acc,target in [(0,15),(203,1)]:
            machine=M8([encode('JZ',15)]);machine.acc=acc;machine.step()
            self.assertEqual(machine.pc,target)
            with self.assertRaises(ValueError):machine.step() # alvo/caminho não carregados
        machine=M8([encode('HALT',15)]);machine.step()
        self.assertEqual((machine.pc,machine.halted),(1,True))
        with self.assertRaises(RuntimeError):machine.step()

    def test_bad_bytes_and_input_contract(self):
        for value in [-1,256,True,None,3.5,'0x3E']:
            with self.assertRaises(ValueError):inspect(value)
        for value in [0x90,0xFF]:
            with self.assertRaises(ValueError):inspect(value)
        self.assertEqual(inspect(0x3E)['hex'],'0x3E')
        self.assertEqual(inspect(0x3E)['binary'],'00111110')
