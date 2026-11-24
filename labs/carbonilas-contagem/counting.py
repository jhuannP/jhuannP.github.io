"""Contagem formal: um metal, apenas CO terminais; não prediz estabilidade."""
def count(group,n_co,charge=0):
    if any(type(x) is not int for x in (group,n_co,charge)):
        raise ValueError('inteiros sem bool')
    if not 3<=group<=10 or not 0<=n_co<=8 or not 0<=group-charge<=10:
        raise ValueError('grupo3..10, CO0..8 e d formal0..10')
    d=group-charge
    return dict(d_formal=d,ligand_electrons=2*n_co,total=d+2*n_co,coordination=n_co)

if __name__=='__main__':
    for label,g,n,q in [('Cr(CO)6',6,6,0),('Fe(CO)5',8,5,0),('Ni(CO)4',10,4,0),('candidato grupo9,5CO,carga+1',9,5,1)]:
        r=count(g,n,q);assert r['total']==18
        print(label,r)
    assert count(10,3)['total']==16
    # Agreement of ionic and neutral bookkeeping; neither tests molecular existence.
    cases=0
    for g in range(3,11):
        for d in range(11):
            q=g-d
            for n in range(9):
                r=count(g,n,q)
                assert r['total']==g+sum([2]*n)-q
                if n:assert r['total']-count(g,n-1,q)['total']==2
                cases+=1
    for bad in [(True,4,0),(10,4.0,0),(10,4,False),(2,4,0),(10,9,0),(10,4,-1)]:
        try:count(*bad)
        except ValueError:pass
        else:raise AssertionError('aceitou entrada fora do contrato')
    print('Inventários formais conferidos:',cases,'; não são espécies observadas.')
