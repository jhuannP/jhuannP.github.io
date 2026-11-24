"""R/S no recorte em que quatro prioridades se resolvem nos átomos diretamente ligados."""
REFERENCE=((0,2,1),(2,-1,1),(-2,-1,1),(0,0,-3)) # prioridades 1,2,3,4
LIGANDS=((35,79),(17,35),(9,19),(1,1)) # Z,A explícitos: Br,Cl,F,H

def priority(ligands):
    ligands=tuple(ligands)
    if len(ligands)!=4:raise ValueError('Quatro átomos diretamente ligados')
    clean=[]
    for atom in ligands:
        if not isinstance(atom,(tuple,list)) or len(atom)!=2:raise ValueError('Use (Z,A)')
        z,a=atom
        if any(isinstance(v,bool) or type(v) is not int for v in (z,a)) or not 1<=z<=118 or not z<=a<=400:
            raise ValueError('Z e A inteiros no recorte didático')
        clean.append((z,a))
    if len(set(clean))!=4:
        raise ValueError('Empate: grupos iguais ou comparação exige esferas adicionais; não decidido')
    return tuple(sorted(range(4),key=lambda i:clean[i],reverse=True))

def determinant(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])

def configuration(ligands,positions):
    order=priority(ligands);positions=tuple(positions)
    if len(positions)!=4:raise ValueError('Quatro posições correspondentes')
    for v in positions:
        if not isinstance(v,(tuple,list)) or len(v)!=3 or any(isinstance(x,bool)or type(x)is not int or abs(x)>20 for x in v):
            raise ValueError('Coordenadas inteiras 3D, módulo até20')
    r=[positions[i]for i in order]
    v=[tuple(r[i][k]-r[3][k]for k in range(3))for i in range(3)]
    D=determinant(*v)
    if D==0:raise ValueError('Representação degenerada; não atribuir configuração')
    # Calibração em eixos destros: grupo4 para -z;1->2->3 horário visto de +z.
    return {'order':order,'determinant':D,'configuration':'R'if D<0 else'S'}

if __name__=='__main__':
    print(configuration(LIGANDS,REFERENCE))
    mirror=tuple((-x,y,z)for x,y,z in REFERENCE)
    print(configuration(LIGANDS,mirror))
