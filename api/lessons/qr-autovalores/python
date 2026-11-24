"""QR explícito real 2x2 sem deslocamento: quatro exemplos, não solver geral."""
import math
CASES=[[[2.,1.],[1.,2.]],[[0.,1.],[1.,0.]],[[0.,-1.],[1.,0.]],[[2.,6.],[0.,1.]]]


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def trans(a):return [list(row) for row in zip(*a)]
def norm(a):return math.hypot(*(x for row in a for x in row))
def diff(a,b):return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]
def det(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def qr2(a):
    if len(a)!=2 or any(len(row)!=2 for row in a) or any(not math.isfinite(x) for row in a for x in row):
        raise ValueError('Matriz real finita 2x2')
    radius=math.hypot(a[0][0],a[1][0])
    c,s=(a[0][0]/radius,a[1][0]/radius) if radius else (1.,0.)
    q=[[c,-s],[s,c]]
    r=mm(trans(q),a)
    r[1][0]=0.  # entrada anulada pela rotação; arredondamento conferido em QR−A
    return q,r


def experiment(case=0,steps=4):
    if case not in range(4) or steps not in range(21):raise ValueError('Caso 0–3, passos 0–20')
    original=[row[:] for row in CASES[case]];a=[row[:] for row in original];u=[[1.,0.],[0.,1.]]
    history=[];base=norm(original)
    for k in range(steps+1):
        history.append(dict(k=k,lower=abs(a[1][0])/base,off=math.hypot(a[0][1],a[1][0])/base))
        if k<steps:
            q,r=qr2(a);a=mm(r,q);u=mm(u,q)
    q,r=qr2(a)
    identity=[[1.,0.],[0.,1.]]
    diagonal=[[a[0][0],0.],[0.,a[1][1]]]
    return dict(case=case,steps=steps,original=original,a=a,u=u,q=q,r=r,history=history,
                trace=a[0][0]+a[1][1],determinant=det(a),lower=history[-1]['lower'],off=history[-1]['off'],
                orthogonality=norm(diff(mm(trans(u),u),identity)),
                similarity=norm(diff(mm(original,u),mm(u,a)))/base,
                qr_error=norm(diff(mm(q,r),a))/base,
                vector_residual=norm(diff(mm(original,u),mm(u,diagonal)))/base)


if __name__=='__main__':
    for case in range(4):
        result=experiment(case,20)
        print(case,result['a'],'subdiagonal relativa',result['lower'])
    assert experiment(0,20)['lower']<1e-8
