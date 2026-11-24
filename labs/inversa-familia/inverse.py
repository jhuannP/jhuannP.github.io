"""Matrizes racionais 2×2: exemplo didático, sem solver numérico geral."""
from fractions import Fraction as Q

def matrix(a):
    if not isinstance(a,(tuple,list)) or len(a)!=2 or any(not isinstance(r,(tuple,list)) or len(r)!=2 for r in a):
        raise ValueError('matriz 2×2 necessária')
    if any(type(x) not in (int,Q) for r in a for x in r):raise ValueError('use int/Fraction sem bool')
    return tuple(tuple(Q(x) for x in r) for r in a)

def multiply(a,b):
    a,b=matrix(a),matrix(b)
    return tuple(tuple(sum((a[i][k]*b[k][j] for k in range(2)),Q(0)) for j in range(2)) for i in range(2))

def inverse(a):
    a=matrix(a);(u,v),(w,z)=a;det=u*z-v*w
    if not det:raise ValueError('matriz singular')
    return ((z/det,-v/det),(-w/det,u/det))

if __name__=='__main__':
    from itertools import product
    identity=matrix([[1,0],[0,1]]);count=0;singular=0
    for values in product(range(-2,3),repeat=4):
        a=matrix([values[:2],values[2:]])
        # Independent decision: columns dependent iff their 2D cross product is zero.
        if values[0]*values[3]==values[1]*values[2]:
            try:inverse(a)
            except ValueError:singular+=1
            else:raise AssertionError('aceitou singular')
            continue
        b=inverse(a)
        assert multiply(a,b)==identity and multiply(b,a)==identity
        count+=1
    a=matrix([[2,1],[0,1]]);b=matrix([[1,0],[1,1]])
    assert inverse(multiply(a,b))==multiply(inverse(b),inverse(a))
    assert inverse(multiply(a,b))!=multiply(inverse(a),inverse(b))
    assert inverse([[Q(1,100),1],[0,1]])==matrix([[100,-100],[0,1]])
    for bad in ([[True,0],[0,1]],[[1.0,0],[0,1]],[[1,2,3],[0,1,2]]):
        try:inverse(bad)
        except ValueError:pass
        else:raise AssertionError('aceitou entrada inválida')
    print('Matrizes invertíveis conferidas:',count,'singulares rejeitadas:',singular)
    print('Inversa original:',inverse(a),'inversa de AB:',inverse(multiply(a,b)))
