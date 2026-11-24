"""Contabilidade de Lewis para dois exemplos curados; não calcula a função de onda."""
VALENCE={'C':4,'N':5,'O':6}


def audit(atoms, hydrogens, bonds, pairs, charge):
    n=len(atoms)
    if not n or len(hydrogens)!=n or len(pairs)!=n or any(a not in VALENCE for a in atoms):
        raise ValueError('Átomos C/N/O e vetores de igual tamanho')
    if not isinstance(charge,int) or any(not isinstance(x,int) or x<0 for x in [*hydrogens,*pairs]):
        raise ValueError('Contagens inteiras não negativas')
    orders=list(hydrogens); seen=set()
    for i,j,b in bonds:
        if any(not isinstance(x,int) for x in (i,j,b)) or not 0<=i<n or not 0<=j<n or i==j or b not in (1,2,3):
            raise ValueError('Ligação inválida')
        edge=tuple(sorted((i,j)))
        if edge in seen: raise ValueError('Ligação duplicada')
        seen.add(edge); orders[i]+=b; orders[j]+=b
    formal=[VALENCE[a]-2*p-b for a,p,b in zip(atoms,pairs,orders)]
    local=[2*(p+b) for p,b in zip(pairs,orders)]
    actual=2*(sum(b for _,_,b in bonds)+sum(hydrogens)+sum(pairs))
    target=sum(VALENCE[a] for a in atoms)+sum(hydrogens)-charge
    return dict(orders=orders,formal=formal,local=local,electrons=actual,target=target,
                total_charge=sum(formal),electron_ok=actual==target,charge_ok=sum(formal)==charge,
                octet_ok=all(x==8 for x in local))


def model(family=0, form=0):
    if family not in (0,1) or form not in (0,1,2):
        raise ValueError('Família 0/1, forma 0/1/2')
    atoms=['C','C','O','O' if family==0 else 'N']
    hydrogens=[3,0,0,0 if family==0 else 2]
    orders=[2,1] if form==0 else ([1,2] if form==1 else [2,2])
    pairs=[0,0,2 if form in (0,2) else 3,
           (3 if form==0 else 2) if family==0 else (1 if form==0 else 0)]
    bonds=[[0,1,1],[1,2,orders[0]],[1,3,orders[1]]]
    charge=-1 if family==0 else 0
    result=audit(atoms,hydrogens,bonds,pairs,charge)
    return dict(family=family,form=form,atoms=atoms,hydrogens=hydrogens,bonds=bonds,pairs=pairs,
                charge=charge,formula='C2H3O2−' if family==0 else 'C2H5NO',**result)


def enumerate_octets(family=0):
    """Enumeração restrita: mesmos núcleos/H, ordens terminais 1/2 e pares 0..3."""
    from itertools import product
    if family not in (0,1): raise ValueError('Família 0/1')
    base=model(family,0); candidates=[]
    for b1,b2,l1,l2 in product((1,2),(1,2),range(4),range(4)):
        state=audit(base['atoms'],base['hydrogens'],[[0,1,1],[1,2,b1],[1,3,b2]],
                    [0,0,l1,l2],base['charge'])
        if state['electron_ok'] and state['charge_ok'] and state['octet_ok']:
            candidates.append((b1,b2,l1,l2))
    return candidates


if __name__=='__main__':
    for family in (0,1):
        for form in (0,1,2):
            s=model(family,form)
            print(s['formula'],form,s['formal'],s['electrons'],s['local'])
            assert s['electron_ok'] and s['charge_ok']
            assert s['octet_ok']==(form!=2)
