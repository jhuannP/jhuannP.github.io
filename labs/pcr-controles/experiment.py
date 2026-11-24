"""Tabela lógica didática de quatro sinais, sem simular química ou dados de PCR."""
from itertools import product
KEYS=('target','inhibited','contamination','working','nonspecific')

def signals(target=1,inhibited=0,contamination=0,working=1,nonspecific=0):
    args=(target,inhibited,contamination,working,nonspecific)
    if any(type(v) is not int or v not in (0,1) for v in args):
        raise ValueError('Use cinco indicadores inteiros 0 ou 1')
    sample=int(bool(working and not inhibited and (target or contamination or nonspecific)))
    ntc=int(bool(working and contamination))
    positive=working
    matrix=int(bool(working and not inhibited))
    return (sample,ntc,positive,matrix)

def model(target=1,inhibited=0,contamination=0,working=1,nonspecific=0):
    observed=signals(target,inhibited,contamination,working,nonspecific)
    compatible=[dict(zip(KEYS,state)) for state in product((0,1),repeat=5) if signals(*state)==observed]
    return dict(observed=observed,compatible=compatible,compatible_count=len(compatible),
                target_values=sorted({s['target'] for s in compatible}))

if __name__=='__main__':
    a=model();b=model(0,0,0,1,1)
    assert a['observed']==b['observed']==(1,0,1,1)
    assert a['target_values']==[0,1]
    print('Sinais (amostra, NTC, positivo, matriz):',a['observed'])
    print('Estados compatíveis no modelo:',a['compatible_count'])
