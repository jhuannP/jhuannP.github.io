"""Cobertura de peptídeos anotados em banco sintético; sem escores ou inferência estatística."""
from itertools import combinations

AA=set('ACDEFGHIKLMNPQRSTVWY')
DATABASE={'A':{'ACDF','GHIK'},'B':{'GHIK','LMNP'},'C':{'QRST'}}


def peptides(values):
    if not isinstance(values,(list,tuple,set,frozenset)):raise ValueError('Use coleção de peptídeos.')
    if any(not isinstance(v,str) or not v or len(v)>100 or set(v)-AA for v in values):
        raise ValueError('Sequências de1..100resíduos canônicos em maiúsculas.')
    return set(values)


def infer(database,observed):
    if not isinstance(database,dict) or not 1<=len(database)<=12:
        raise ValueError('Banco com1..12entradas necessário.')
    if any(not isinstance(k,str) or not k for k in database):raise ValueError('IDs não vazios.')
    db={k:peptides(v) for k,v in database.items()}
    if any(not v for v in db.values()):raise ValueError('Anotação não vazia por entrada.')
    obs=peptides(observed);names=sorted(db)
    matches={p:[k for k in names if p in db[k]] for p in sorted(obs)}
    unmatched=[p for p in matches if not matches[p]]
    covers=[]
    if not unmatched:
        for size in range(len(names)+1):
            for group in combinations(names,size):
                union=set().union(*(db[k] for k in group))
                if obs<=union:covers.append(group)
    minimum=[g for g in covers if len(g)==len(covers[0])] if covers else []
    return dict(matches=matches,unmatched=unmatched,covers=covers,minimum=minimum,
                unique_within_database={p:v[0] for p,v in matches.items() if len(v)==1})


if __name__=='__main__':
    for obs in [{'GHIK'},{'ACDF','GHIK'},{'GHIK','QRST'},{'VWYA'},set()]:
        print('Observações:',sorted(obs),'resultado:',infer(DATABASE,obs))
    print('Ausência de peptídeo não foi usada como evidência de ausência de proteína.')
