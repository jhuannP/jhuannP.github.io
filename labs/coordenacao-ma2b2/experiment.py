"""MA2B2 pontual: rotações próprias, posições e órbitas. Sem energia química."""
from itertools import permutations, product, combinations
from math import acos, degrees

POINTS = (
    ((1,0,0),(0,1,0),(-1,0,0),(0,-1,0)),
    ((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)),
)
PAIRS = tuple(combinations(range(4),2))

def determinant(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
           -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
           +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))

def apply(a,v):
    return tuple(sum(x*y for x,y in zip(row,v)) for row in a)

def rotations(geometry):
    if isinstance(geometry,bool) or geometry not in (0,1): raise ValueError('Geometria 0 ou 1')
    points=POINTS[geometry]; found={}
    for axes in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            matrix=tuple(tuple(signs[i] if j==axes[i] else 0 for j in range(3)) for i in range(3))
            if determinant(matrix)!=1: continue
            moved=tuple(apply(matrix,p) for p in points)
            if all(p in points for p in moved):
                perm=tuple(points.index(p) for p in moved)
                found[perm]=matrix
    return tuple((p,found[p]) for p in sorted(found))

def orbit(geometry,pair):
    return tuple(sorted({tuple(sorted(p[i] for i in pair)) for p,_ in rotations(geometry)}))

def model(geometry=0,pair=0,rotation=0):
    if any(isinstance(v,bool) or not isinstance(v,int) for v in (geometry,pair,rotation)):
        raise ValueError('Controles inteiros')
    if geometry not in (0,1) or not 0<=pair<6 or not 0<=rotation<12: raise ValueError('Controle fora da faixa')
    points=POINTS[geometry]; group=rotations(geometry); rotation=min(rotation,len(group)-1)
    p,m=group[rotation]; a,b=PAIRS[pair]
    dot=sum(x*y for x,y in zip(points[a],points[b])); norm=sum(x*x for x in points[a])
    images=orbit(geometry,PAIRS[pair]); label=('cis' if dot==0 else 'trans') if geometry==0 else 'uma classe tetraédrica'
    return dict(geometry=geometry,pair=pair,rotation=rotation,permutation=p,
                moved_pair=tuple(sorted((p[a],p[b]))),orbit=images,
                group_size=len(group),orbit_size=len(images),stabilizer=len(group)//len(images),
                dot=dot,norm_squared=norm,cosine=dot/norm,angle=degrees(acos(dot/norm)),label=label,
                positions=tuple(apply(m,v) for v in points))

if __name__=='__main__':
    for g in (0,1):
        classes={orbit(g,p) for p in PAIRS}
        print('quadrado-planar' if g==0 else 'tetraédrica',len(rotations(g)),'rotações;',len(classes),'classes')
        for c in sorted(classes):print('  sítios de A (índices zero):',c)
