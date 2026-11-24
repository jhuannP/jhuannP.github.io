"""Contabilidade de Lewis para duas estruturas escolhidas; não prediz reação."""
from collections import Counter
ATOMS={'C':'C','S':'S','Cl':'Cl','H1':'H','H2':'H','H3':'H','H4':'H'}
VALENCE={'H':1,'C':4,'S':6,'Cl':7}
BEFORE=(('C','H1'),('C','H2'),('C','H3'),('C','Cl'),('S','H4'))
AFTER=(('C','H1'),('C','H2'),('C','H3'),('C','S'),('S','H4'))
LP_BEFORE={x:(3 if x in ('S','Cl') else 0) for x in ATOMS}
LP_AFTER={x:(2 if x=='S' else 4 if x=='Cl' else 0) for x in ATOMS}

def audit(bonds,lone_pairs):
    if not isinstance(lone_pairs,dict) or set(lone_pairs)!=set(ATOMS) or any(type(x) is not int or x<0 for x in lone_pairs.values()):
        raise ValueError("Declare pares livres inteiros não negativos para todos os átomos")
    degree=Counter({x:0 for x in ATOMS});seen=set()
    for edge in bonds:
        if not isinstance(edge,(list,tuple)) or len(edge)!=2:raise ValueError("Aresta com dois átomos")
        a,b=edge
        if a not in ATOMS or b not in ATOMS or a==b or frozenset(edge) in seen:
            raise ValueError("Aresta desconhecida, repetida ou reflexiva")
        seen.add(frozenset(edge));degree[a]+=1;degree[b]+=1
    charge={x:VALENCE[s]-2*lone_pairs[x]-degree[x] for x,s in ATOMS.items()}
    shells={x:2*lone_pairs[x]+2*degree[x] for x in ATOMS}
    return dict(charge=charge,total_charge=sum(charge.values()),
                electrons=2*(len(seen)+sum(lone_pairs.values())),shells=shells,
                closed_shell=all(shells[x]==(2 if s=='H' else 8) for x,s in ATOMS.items()),
                formula=dict(Counter(ATOMS.values())))

if __name__=='__main__':
    a,b=audit(BEFORE,LP_BEFORE),audit(AFTER,LP_AFTER)
    assert a['electrons']==b['electrons']==22
    assert a['total_charge']==b['total_charge']==-1
    assert a['closed_shell'] and b['closed_shell']
    print('Antes:',a);print('Depois:',b)
