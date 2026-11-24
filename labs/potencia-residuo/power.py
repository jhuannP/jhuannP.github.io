"""História racional de potência2D, normalização infinita, sem certificado dominante."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise TypeError('use int ou Fraction')
    return Q(x)

def history(matrix, initial, steps):
    if isinstance(steps,bool) or not isinstance(steps,int): raise TypeError('steps inteiro')
    if not 0 <= steps <= 100: raise ValueError('0 <= steps <= 100')
    if len(matrix)!=2 or any(len(row)!=2 for row in matrix) or len(initial)!=2:
        raise ValueError('matriz2x2, vetor2')
    A=tuple(tuple(rational(v) for v in row) for row in matrix)
    x=tuple(rational(v) for v in initial)
    def unit(v):
        scale=max(map(abs,v))
        if not scale: raise ArithmeticError('direção nula')
        return tuple(a/scale for a in v)
    def apply(v): return tuple(sum(a*b for a,b in zip(row,v)) for row in A)
    anorm=max(sum(map(abs,row)) for row in A)
    x=unit(x); result=[]
    for k in range(steps+1):
        ax=apply(x)
        rho=sum(a*b for a,b in zip(x,ax))/sum(v*v for v in x)
        residual=max(abs(a-rho*b) for a,b in zip(ax,x))
        denom=(anorm+abs(rho))*max(map(abs,x))
        eta=residual/denom if denom else Q(0)
        result.append({'k':k,'vector':x,'rayleigh':rho,'residual':residual,'scaled':eta})
        if k<steps: x=unit(ax)
    return result

if __name__=='__main__':
    for row in history(((3,0),(0,1)),(1,1),3): print(row)
