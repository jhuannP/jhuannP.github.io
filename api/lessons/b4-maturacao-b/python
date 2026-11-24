"""Filtro didático finito, não previsão de destinos de células reais."""
HEAVY=(False,True,True,True,True,False)
# Índices: painel de autoantígenos, precursor, L0/L1/L2. 1=reatividade estipulada.
SELF=(
 ((0,0,0),(0,1,1),(1,0,1),(1,1,0),(1,1,1),(0,0,0)),
 ((0,0,0),(1,0,0),(1,1,0),(0,1,1),(0,1,1),(0,0,0)),
)

def choose(reactivity,edits):
    if len(reactivity)!=3 or any(type(x) is not int or x not in (0,1) for x in reactivity):
        raise ValueError('Três indicadores 0/1, não afinidades.')
    if type(edits) is not int or not 0<=edits<=2:
        raise ValueError('Até duas alternativas didáticas.')
    visited=[]
    for j in range(edits+1):
        visited.append(j)
        if not reactivity[j]:
            return dict(visited=visited,last=j,passed=True,edits_used=j)
    return dict(visited=visited,last=edits,passed=False,edits_used=edits)

def model(edits=1,panel=0,cell=3):
    if type(panel) is not int or panel not in (0,1) or type(cell) is not int or not 1<=cell<=6:
        raise ValueError('Painel 0/1 e precursor 1..6.')
    # Valida também quando nenhuma célula precisasse editar.
    choose((0,0,0),edits)
    rows=[]
    for i,heavy in enumerate(HEAVY):
        result=choose(SELF[panel][i],edits) if heavy else dict(visited=[],last=None,passed=False,edits_used=0)
        rows.append(dict(cell=i+1,heavy=heavy,reactivity=list(SELF[panel][i]),**result))
    eligible=sum(HEAVY);passed=sum(row['passed'] for row in rows)
    return dict(edits=edits,panel=panel,cell=cell,rows=rows,selected=rows[cell-1],eligible=eligible,
                passed=passed,unresolved=eligible-passed,excluded=6-eligible,
                edited_pass=sum(row['passed'] and row['edits_used']>0 for row in rows),
                fraction=passed/eligible,all_fraction=passed/6)

if __name__=='__main__':
    s=model()
    assert (s['passed'],s['unresolved'],s['excluded'])==(2,2,2)
    print('Filtro da coorte fictícia:',s['passed'],'de',s['eligible'])
    print('Traço do precursor 3:',s['selected'])
