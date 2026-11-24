"""Edições de strings de DNA codificante; não prevê efeitos biológicos.
Execute a partir da raiz do protótipo; reutiliza a tabela da aula de tradução.
"""
from importlib import import_module
_decode = import_module("labs.traducao-quadro.experiment").decode_frame


def dna(sequence):
    if not isinstance(sequence,str) or any(b not in "ACGT" for b in sequence):
        raise ValueError("DNA deve conter apenas A,C,G,T maiúsculos.")
    return sequence


def position(sequence,pos):
    if type(pos) is not int or not 1<=pos<=len(sequence):
        raise ValueError("Posição inteira, começando em 1, dentro da sequência.")
    return pos-1


def substitute(sequence,pos,base):
    sequence=dna(sequence);i=position(sequence,pos)
    if not isinstance(base,str) or len(base)!=1 or base not in "ACGT":
        raise ValueError("A nova base deve ser A,C,G ou T.")
    if sequence[i]==base:
        raise ValueError("A substituição deve mudar a base.")
    return sequence[:i]+base+sequence[i+1:]


def delete(sequence,pos,count=1):
    sequence=dna(sequence);i=position(sequence,pos)
    if type(count) is not int or count<1 or i+count>len(sequence):
        raise ValueError("A deleção deve ter tamanho positivo dentro do trecho.")
    return sequence[:i]+sequence[i+count:]


def read_coding_dna(sequence):
    """Quadro 0 fornecido, DNA codificante 5'->3', código padrão.

    Não procura início, não interpreta íntrons, lesões ou alelos de organismos.
    Campos codons e suffix usam RNA (U), como o decodificador reutilizado.
    Sufixo após parada não equivale a bases incompletas; veja stop_offset.
    """
    sequence=dna(sequence)
    return _decode(sequence.replace("T","U"),0)


if __name__=="__main__":
    ref="ATGGAATTTTAA"
    examples={"referência":ref,"sinônima":substitute(ref,6,"G"),
              "troca de resíduo":substitute(ref,5,"T"),
              "parada antecipada":substitute(ref,4,"T"),
              "deleção de uma base":delete(ref,4),
              "deleção de um códon":delete(ref,4,3)}
    for name,sequence in examples.items():
        print(name,sequence,read_coding_dna(sequence))
