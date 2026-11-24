"""Camada afim racional, W em H×D. Não é framework tensorial/autodiff."""
from fractions import Fraction as Q
from itertools import zip_longest

def matrix(a):
    if not isinstance(a,(list,tuple)) or not a or any(not isinstance(r,(list,tuple)) for r in a):raise ValueError('matriz necessária')
    d=len(a[0])
    if not d or any(len(r)!=d for r in a):raise ValueError('matriz retangular não vazia')
    if any(type(v) not in (int,Q) for r in a for v in r):raise ValueError('racionais sem bool/float')
    return [[Q(v) for v in r] for r in a]

def dense(x,w,b):
    x,w=matrix(x),matrix(w)
    if len(x[0])!=len(w[0]):raise ValueError('D inconsistente')
    if not isinstance(b,(list,tuple)) or len(b)!=len(w) or any(type(v) not in (int,Q) for v in b):raise ValueError('bias H racional necessário')
    return [[sum((row[j]*unit[j] for j in range(len(row))),Q(0))+b[h] for h,unit in enumerate(w)] for row in x]

def broadcast_shape(a,b):
    if any(not isinstance(s,(list,tuple)) or any(type(n) is not int or n<=0 for n in s) for s in (a,b)):
        raise ValueError('formas positivas ou escalar()')
    out=[]
    for x,y in zip_longest(reversed(a),reversed(b),fillvalue=1):
        if x!=y and x!=1 and y!=1:raise ValueError('formas incompatíveis')
        out.append(max(x,y))
    return tuple(reversed(out))

if __name__=='__main__':
    x=[[1,0,2],[0,1,-1]];w=[[1,2,0],[-1,1,3]];b=[1,-2]
    assert dense(x,w,b)==[[2,3],[3,-4]]
    # Batch independence and concatenation: adding samples does not couple rows.
    assert dense(x+x,w,b)==dense(x,w,b)*2
    for k in range(-4,5):
        shifted=[[v+k for v in row] for row in x]
        z=dense(shifted,w,b);base=dense(x,w,b)
        for i in range(2):
            for h in range(2):assert z[i][h]-base[i][h]==k*sum(w[h])
    pred=[2,4,8];target=[1,3,5]
    paired=sum((Q(p)-t)**2 for p,t in zip(pred,target))/3
    crossed=sum((Q(p)-t)**2 for p in pred for t in target)/9
    assert paired==Q(11,3) and crossed==Q(35,3)
    assert broadcast_shape((3,1),(3,))==(3,3)
    assert broadcast_shape((3,4),(4,))==(3,4)
    assert broadcast_shape((),(2,3))==(2,3)
    for a,bad in [((3,4),(3,)),((2,0),(2,)),((True,),(1,))]:
        try:broadcast_shape(a,bad)
        except ValueError:pass
        else:raise AssertionError('forma inválida aceita')
    for bad_x,bad_w,bad_b in [([[1,2],[3]],w,b),(x,[[1,2]],b),(x,w,[0]),([[True,0,0]],w,b)]:
        try:dense(bad_x,bad_w,bad_b)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    source=[[1,2,3],[4,5,6]];flat=[v for row in source for v in row]
    reshaped=[flat[k:k+2] for k in range(0,6,2)]
    transposed=[list(col) for col in zip(*source)]
    assert reshaped!=transposed
    print('Z=',dense(x,w,b),'perda pareada=',paired,'perda cruzada=',crossed)
    print('reshape=',reshaped,'transposta=',transposed)
