"""Fenótipos CD4/CD8 pré-classificados; dados sintéticos, sem inferência de destino."""
from collections import Counter

def phenotype(cd4, cd8):
    if type(cd4) is not bool or type(cd8) is not bool:
        raise ValueError('Use classificações booleanas, não intensidades de fluorescência')
    return {(False,False):'DN', (True,True):'DP',
            (True,False):'CD4 único', (False,True):'CD8 único'}[(cd4,cd8)]

def summarize(records):
    counts = Counter({'DN':0, 'DP':0, 'CD4 único':0, 'CD8 único':0})
    for cd4, cd8 in records:
        counts[phenotype(cd4,cd8)] += 1
    return dict(counts)

if __name__ == '__main__':
    synthetic = [(False,False)] + [(True,True)]*4 + [(True,False)]*2 + [(False,True)]
    counts = summarize(synthetic)
    assert counts == {'DN':1, 'DP':4, 'CD4 único':2, 'CD8 único':1}
    print(counts)
    print('DP:', counts['DP']/sum(counts.values()))
    print('Fenótipo não determina maturidade, localização, seleção ou taxa de transição.')
