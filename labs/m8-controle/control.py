"""Control description for the existing behavioral M8, not a second CPU engine."""
from m8 import decode, word

# acc source, ALU operation, ACC write, memory write, output append, halt request.
TABLE = {
    'HALT': ('hold', None, 0, 0, 0, 1),
    'LDI':  ('immediate', None, 1, 0, 0, 0),
    'LDA':  ('memory', None, 1, 0, 0, 0),
    'STA':  ('hold', None, 0, 1, 0, 0),
    'ADD':  ('alu', 'add', 1, 0, 0, 0),
    'SUB':  ('alu', 'sub', 1, 0, 0, 0),
    'JMP':  ('hold', None, 0, 0, 0, 0),
    'JZ':   ('hold', None, 0, 0, 0, 0),
    'OUT':  ('hold', None, 0, 0, 1, 0),
}


def controls(instruction, acc):
    """Pure description, using the old ACC to choose the conditional PC path."""
    word(acc)
    op, operand = decode(instruction)
    source, alu, acc_we, mem_we, out_we, stop = TABLE[op]
    return dict(operation=op, operand=operand, acc_source=source, alu=alu,
                acc_we=acc_we, mem_we=mem_we, out_we=out_we, stop=stop,
                pc_source='target' if op == 'JMP' or (op == 'JZ' and acc == 0) else 'sequential',
                pc_we=1)


if __name__ == '__main__':
    from m8 import M8
    m=M8([0x4E]);m.acc=250;m.data[14]=10
    print('before',m.pc,m.acc,m.data[14])
    print('controls',controls(m.program[m.pc],m.acc))
    print('existing engine',m.step())
