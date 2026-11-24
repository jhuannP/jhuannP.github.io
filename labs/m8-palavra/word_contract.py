"""Inspeção do contrato M8 já existente; não altera ISA ou interpretador."""
from m8 import decode,encode
KINDS={'HALT':'ignored','LDI':'immediate','LDA':'data_address','STA':'data_address',
       'ADD':'data_address','SUB':'data_address','JMP':'program_address','JZ':'program_address','OUT':'ignored'}

def inspect(instruction):
    name,arg=decode(instruction)
    kind=KINDS[name]
    return {'word':instruction,'hex':f'0x{instruction:02X}','binary':f'{instruction:08b}',
            'opcode_bits':f'{instruction>>4:04b}','operand_bits':f'{arg:04b}',
            'operation':name,'operand':arg,'operand_kind':kind,
            'canonical_word':encode(name,0 if kind=='ignored' else arg)}

if __name__=='__main__':
    for w in [0x3E,0x4E,0x13,0x23,0x0F,0x8F]:print(inspect(w))
