"""Leitura didática de um quadro fornecido, código padrão NCBI tabela 1 em RNA."""
from itertools import product
# Ordem das bases UCAG; tabela factual padrão, com T convertido em U.
AMINO_ACIDS = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODE = dict(zip(("".join(c) for c in product("UCAG",repeat=3)),AMINO_ACIDS))

def decode_frame(rna,frame=0):
    if not isinstance(rna,str) or any(base not in "ACGU" for base in rna):
        raise ValueError("RNA deve usar somente A,C,G,U maiúsculos")
    if type(frame) is not int or frame not in (0,1,2):
        raise ValueError("Quadro deve ser 0,1 ou 2")
    window=rna[frame:];residues=[];codons=[]
    for j in range(len(window)//3):
        codon=window[3*j:3*j+3];codons.append(codon)
        amino=CODE[codon]
        if amino=="*":
            return dict(peptide="".join(residues),stop_offset=frame+3*j,
                        suffix=window[3*j+3:],codons=tuple(codons))
        residues.append(amino)
    return dict(peptide="".join(residues),stop_offset=None,
                suffix=window[3*(len(window)//3):],codons=tuple(codons))

if __name__=="__main__":
    rna="AUGGCUUUUUAAGG"
    for frame in range(3):print(frame,decode_frame(rna,frame))
