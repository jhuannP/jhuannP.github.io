"""Trecho e fita-molde fornecidos; orientação ideal, sem predição de expressão."""
from importlib import import_module
_dna = import_module("labs.replicacao-orientacao.experiment")

def from_template(template_5to3):
    return _dna.reverse_complement(template_5to3).replace("T","U")

def from_coding(coding_5to3):
    _dna.complement(coding_5to3)  # Reutiliza o contrato de sequência DNA.
    return coding_5to3.replace("T","U")

def transcribe_region(upper_5to3,template_side,start=0,stop=None):
    _dna.complement(upper_5to3)
    if template_side not in ("superior","inferior"):
        raise ValueError("Escolha fita-molde superior ou inferior")
    if stop is None:stop=len(upper_5to3)
    if type(start) is not int or type(stop) is not int or not 0<=start<stop<=len(upper_5to3):
        raise ValueError("Intervalo não vazio [start,stop) na referência superior")
    segment=upper_5to3[start:stop]
    coding=segment if template_side=="inferior" else _dna.reverse_complement(segment)
    template=_dna.reverse_complement(coding)
    return dict(interval=(start,stop),template_side=template_side,
                direction=1 if template_side=="inferior" else -1,
                template_5to3=template,coding_5to3=coding,rna_5to3=from_template(template))

if __name__=="__main__":
    upper="ACGTAACC"
    plus=transcribe_region(upper,"inferior")
    minus=transcribe_region(upper,"superior")
    assert plus["rna_5to3"]=="ACGUAACC"
    assert minus["rna_5to3"]=="GGUUACGU"
    print("Molde inferior:",plus)
    print("Molde superior:",minus)
