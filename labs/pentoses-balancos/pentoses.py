"""Contabilidade reduzida da PPP; quantidades em mmol, sem cinética.
Carbono do substrato e inventário NADP/NADPH, não equações moleculares completas.
"""
from fractions import Fraction as Q
SUGAR_C={'G6P':6,'6PGL':6,'6PG':6,'Ru5P':5,'R5P':5,'X5P':5,'GAP':3,'S7P':7,'E4P':4,'F6P':6,'CO2':1}
LABELS=set(SUGAR_C)|{'NADP','NADPH'}
REACTIONS={
 'oxidacao1':{'G6P':-1,'NADP':-1,'6PGL':1,'NADPH':1},
 'hidrolise':{'6PGL':-1,'6PG':1},
 'oxidacao2':{'6PG':-1,'NADP':-1,'Ru5P':1,'CO2':1,'NADPH':1},
 'isomerase':{'Ru5P':-1,'R5P':1},
 'epimerase':{'Ru5P':-1,'X5P':1},
 'transcetolase1':{'X5P':-1,'R5P':-1,'GAP':1,'S7P':1},
 'transaldolase':{'S7P':-1,'GAP':-1,'F6P':1,'E4P':1},
 'transcetolase2':{'X5P':-1,'E4P':-1,'F6P':1,'GAP':1}}

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(v)

def inventory(values):
    if set(values)-LABELS:raise ValueError("Espécie não implementada.")
    result={label:rational(values.get(label,0)) for label in LABELS}
    if any(v<0 for v in result.values()):raise ValueError("Inventários não negativos.")
    return result

def apply(values,reaction,extent):
    state=inventory(values);extent=rational(extent)
    if reaction not in REACTIONS or extent<0:raise ValueError("Reação e extensão válidas necessárias.")
    for species,coefficient in REACTIONS[reaction].items():state[species]+=extent*coefficient
    if any(v<0 for v in state.values()):raise ValueError("Estoque insuficiente.")
    return state

def oxidative(values,extent):
    state=inventory(values)
    for reaction in ['oxidacao1','hidrolise','oxidacao2']:state=apply(state,reaction,extent)
    return state

def carbon_backbone(values):
    state=inventory(values)
    return sum((state[s]*count for s,count in SUGAR_C.items()),Q(0))

def nadp_pool(values):
    state=inventory(values)
    return state['NADP']+state['NADPH']

if __name__=='__main__':
    s=oxidative({'G6P':3,'NADP':6},3)
    for reaction,extent in [('isomerase',1),('epimerase',2),('transcetolase1',1),('transaldolase',1),('transcetolase2',1)]:
        s=apply(s,reaction,extent)
    print({k:v for k,v in sorted(s.items()) if v})
