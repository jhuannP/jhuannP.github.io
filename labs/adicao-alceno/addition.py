"""Contabilidade de dois caminhos formais; não ranqueia mecanismos."""
from collections import Counter
from copy import deepcopy
VALENCE={'C':4,'H':1,'Cl':7}
ATOMS={'C1':'C','C2':'C','C3':'C',**{f'H{i}':'H' for i in range(1,7)},'Ha':'H','Cl':'Cl'}

def key(a,b):return tuple(sorted((a,b)))

def paths(proton_carbon='C1'):
    if proton_carbon not in ('C1','C2'):raise ValueError('Protonar C1 ou C2 neste caso fixo.')
    bonds={key('C1','C2'):2,key('C2','C3'):1,key('Ha','Cl'):1}
    for carbon,hydrogens in [('C1',[1,2]),('C2',[3]),('C3',[4,5,6])]:
        for h in hydrogens:bonds[key(carbon,f'H{h}')]=1
    a={'atoms':dict(ATOMS),'bonds':bonds,'pairs':{'Cl':3}}
    b=deepcopy(a);b['bonds'][key('C1','C2')]=1
    del b['bonds'][key('Ha','Cl')]
    b['bonds'][key(proton_carbon,'Ha')]=1;b['pairs']['Cl']=4
    cation='C2' if proton_carbon=='C1' else 'C1'
    c=deepcopy(b);c['bonds'][key(cation,'Cl')]=1;c['pairs']['Cl']=3
    return (a,b,c),cation

def audit(state):
    atoms,bonds,pairs=state['atoms'],state['bonds'],state['pairs']
    if atoms!=ATOMS:raise ValueError('O contrato cobre apenas os átomos marcados deste caso.')
    order=dict.fromkeys(atoms,0)
    for edge,value in bonds.items():
        if not isinstance(edge,tuple) or len(edge)!=2 or edge[0]==edge[1] or any(x not in atoms for x in edge) or edge!=key(*edge):raise ValueError('Ligação inválida.')
        if isinstance(value,bool) or not isinstance(value,int) or value not in (1,2,3):raise ValueError('Ordem inválida.')
        for atom in edge:order[atom]+=value
    for atom,value in pairs.items():
        if atom not in atoms or isinstance(value,bool) or not isinstance(value,int) or value<0:raise ValueError('Pares inválidos.')
    charges={x:VALENCE[atoms[x]]-2*pairs.get(x,0)-order[x] for x in atoms}
    shell={x:2*(order[x]+pairs.get(x,0)) for x in atoms}
    for x,element in atoms.items():
        if shell[x]>(2 if element=='H' else 8):raise ValueError('Camada excede limite do recorte.')
    return {'composition':dict(Counter(atoms.values())),'charge':sum(charges.values()),'charges':charges,'shell':shell,'electrons':2*(sum(bonds.values())+sum(pairs.values()))}

if __name__=='__main__':
    for site in ('C1','C2'):
        states,cation=paths(site)
        print('H novo em',site,'carbono catiônico:',cation)
        for state in states:
            r=audit(state);print('elétrons',r['electrons'],'carga',r['charge'],'cargas locais',r['charges'])
    print('Consistência não é probabilidade ou evidência experimental.')
