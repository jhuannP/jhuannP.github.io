"""Programa novo para a M8 existente, sem mudar ISA ou interpretador."""
from m8 import M8, encode, word

ASSEMBLY=(('LDA',14),('JZ',6),('OUT',0),('SUB',15),('STA',14),('JMP',0),('HALT',0))
PROGRAM=tuple(encode(op,arg) for op,arg in ASSEMBLY)


def make(n, decrement=1):
    n=word(n); decrement=word(decrement)
    # Outras posições têm valores conhecidos para conferir preservação.
    data=list(range(16));data[14]=n;data[15]=decrement
    return M8(PROGRAM,data)


if __name__=='__main__':
    for n in (0,3,20):
        machine=make(n)
        result=machine.run(6*n+3)
        assert result==list(range(n,0,-1))
        print('n=',n,'saída=',result,'instruções=',len(machine.trace))
