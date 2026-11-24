"""Tetraedro regular ideal com grupos abstratos; não atribui R/S."""
import itertools,math
BASE=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1))


def determinant(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def oriented(points):
    return determinant([[points[i][j]-points[3][j] for j in range(3)] for i in range(3)])


def matching_rotations(points,labels):
    matches=[]
    for p in itertools.permutations(range(4)):
        if any(labels[i]!=labels[p[i]] for i in range(4)):continue
        # Sum of r_i r_i^T is 4I for this regular tetrahedron.
        Q=[[sum(points[p[t]][i]*BASE[t][j] for t in range(4))/4 for j in range(3)] for i in range(3)]
        orth=max(abs(sum(Q[i][k]*Q[j][k] for k in range(3))-(i==j)) for i in range(3) for j in range(3))
        error=max(abs(sum(Q[i][j]*BASE[t][j] for j in range(3))-points[p[t]][i]) for t in range(4) for i in range(3))
        if determinant(Q)>0 and orth<1e-10 and error<1e-10:matches.append(dict(matrix=Q,assignment=p,error=error))
    return matches


def model(kind=0,mirror=1,swap=0,angle=0):
    if kind not in (0,1) or mirror not in (0,1) or swap not in (0,1) or not math.isfinite(angle) or not 0<=angle<=360:
        raise ValueError('Casos/reflexão/troca 0/1, ângulo 0..360')
    labels=('A','B','C','D') if kind==0 else ('A','A','C','D')
    points=[(-x if mirror else x,y,z) for x,y,z in BASE]
    if swap:points[0],points[1]=points[1],points[0]
    c,s=math.cos(math.radians(angle)),math.sin(math.radians(angle))
    points=[(c*x-s*y,s*x+c*y,z) for x,y,z in points]
    matches=matching_rotations(points,labels)
    return dict(kind=kind,mirror=mirror,swap=swap,angle=angle,labels=labels,points=points,
                orientation=oriented(points),reference=oriented(BASE),
                proper_count=len(matches),superposable=bool(matches),
                match=matches[0] if matches else None)


if __name__=='__main__':
    assert oriented(BASE)==16
    assert not model()['superposable']
    assert model(swap=1)['superposable']
    assert model(kind=1)['superposable']
    print(model())
