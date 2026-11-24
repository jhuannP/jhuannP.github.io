"""Representações geométricas exatas de AB2; sem frequências ou espectros."""
from fractions import Fraction as Q
OPS={'E':(1,1,1),'C2z':(-1,-1,1),'sxz':(1,-1,1),'syz':(-1,1,1)}
IRREPS={'A1':(1,1,1,1),'A2':(1,1,-1,-1),'B1':(1,-1,1,-1),'B2':(1,-1,-1,1)}
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def mul(A,B):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*B)] for row in A]
def sub(A,B):return [[x-y for x,y in zip(a,b)] for a,b in zip(A,B)]
def trace(A):return sum(A[i][i] for i in range(len(A)))
def orthogonal(columns):
    basis=[]
    for v in columns:
        w=list(map(Q,v))
        for b in basis:
            factor=dot(w,b)/dot(b,b);w=[x-factor*y for x,y in zip(w,b)]
        if any(w):basis.append(w)
    return basis

def projector(columns):
    basis=orthogonal(columns)
    return [[sum((b[i]*b[j]/dot(b,b) for b in basis),Q(0)) for j in range(9)] for i in range(9)]
def reduce_characters(chars):
    result={name:sum(Q(c)*r for c,r in zip(chars,row))/4 for name,row in IRREPS.items()}
    if any(x.denominator!=1 or x<0 for x in result.values()):raise ValueError('Caracteres incompatíveis com esta redução')
    return {name:int(x) for name,x in result.items()}
def build(geometry='bent'):
    if geometry not in ('bent','linear'):raise ValueError('Use bent ou linear')
    c=1 if geometry=='bent' else 0
    positions=[(0,0,0),(1,0,c),(-1,0,c)]
    identity=[[int(i==j) for j in range(9)] for i in range(9)]
    translations=[[int(k%3==axis) for k in range(9)] for axis in range(3)]
    rotations=[]
    for axis in range(3):
        col=[]
        for x,y,z in positions:col+=((0,-z,y),(z,0,-x),(-y,x,0))[axis]
        rotations.append(col)
    PT=projector(translations);PR=projector(translations+rotations);PV=sub(identity,PR)
    matrices={}
    for name,signs in OPS.items():
        D=[[0]*9 for _ in range(9)]
        for i,r in enumerate(positions):
            moved=tuple(s*x for s,x in zip(signs,r));j=positions.index(moved)
            for axis,sign in enumerate(signs):D[3*j+axis][3*i+axis]=sign
        matrices[name]=D
    full=[trace(D) for D in matrices.values()]
    trans=[trace(mul(D,PT)) for D in matrices.values()]
    rot=[trace(mul(D,sub(PR,PT))) for D in matrices.values()]
    vib=[trace(mul(D,PV)) for D in matrices.values()]
    return {'geometry':geometry,'positions':positions,'matrices':matrices,'translations':translations,
            'rotations':rotations,'PT':PT,'PR':PR,'PV':PV,'rigid_rank':int(trace(PR)),
            'vibration_dimension':int(trace(PV)),'characters':{'total':full,'translation':trans,'rotation':rot,'vibration':vib},
            'multiplicities':reduce_characters(vib)}
if __name__=='__main__':
    for geometry in ('bent','linear'):
        m=build(geometry)
        print(geometry,'rigid rank=',m['rigid_rank'],'vibration dimension=',m['vibration_dimension'])
        print(m['characters']);print(m['multiplicities'])
