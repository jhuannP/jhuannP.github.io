"""Experimento decimal prescrito: nenhuma precisão é uma tolerância universal."""
from decimal import Decimal as D, localcontext, ROUND_HALF_EVEN

def parameter(eps):
    if not isinstance(eps,str):raise TypeError('epsilon como texto decimal exato')
    try:e=D(eps)
    except Exception:raise ValueError('decimal inválido') from None
    if not e.is_finite() or not D('1e-8')<=e<=D(1):raise ValueError('epsilon em [1e-8,1]')
    return e

def columns(eps):
    e=parameter(eps);z=D(0);one=D(1)
    return ((one,e,z,z),(one,z,e,z),(one,z,z,e))

def dot(x,y):return sum((a*b for a,b in zip(x,y)),D(0))

def factor(eps='0.0001',precision=8,method='CGS'):
    A=columns(eps)
    if type(precision) is not int or not 8<=precision<=80:raise ValueError('precisão inteira8..80')
    if method not in ('CGS','MGS','MGS2'):raise ValueError('CGS, MGS ou MGS2')
    with localcontext() as ctx:
        ctx.prec=precision;ctx.rounding=ROUND_HALF_EVEN
        Q=[];R=[[D(0)]*3 for _ in range(3)]
        for j,v in enumerate(A):
            w=list(v)
            if method=='CGS':
                # Todos os coeficientes são calculados com a coluna original.
                coeff=[dot(q,v) for q in Q]
                for i,q in enumerate(Q):
                    R[i][j]=coeff[i]
                    w=[x-coeff[i]*y for x,y in zip(w,q)]
            else:
                for _ in range(2 if method=='MGS2' else 1):
                    for i,q in enumerate(Q):
                        c=dot(q,w);R[i][j]+=c
                        w=[x-c*y for x,y in zip(w,q)]
            r=dot(w,w).sqrt()
            if r==0:raise ArithmeticError('resíduo decimal nulo; sem decisão geral de posto')
            R[j][j]=r;Q.append(tuple(x/r for x in w))
        return tuple(Q),tuple(tuple(row) for row in R)

def diagnostics(eps,Q,R):
    """Avalia saídas a90 dígitos, separando cálculo do diagnóstico."""
    A=columns(eps)
    if len(Q)!=3 or any(len(q)!=4 for q in Q) or len(R)!=3 or any(len(r)!=3 for r in R):
        raise ValueError('Q por3 colunas4D, R3x3')
    with localcontext() as ctx:
        ctx.prec=90;ctx.rounding=ROUND_HALF_EVEN
        orth=max(abs(dot(Q[i],Q[j])-D(i==j)) for i in range(3) for j in range(3))
        resid=max(abs(A[j][k]-sum((Q[i][k]*R[i][j] for i in range(3)),D(0))) for j in range(3) for k in range(4))
        return {'orthogonality_max':orth,'reconstruction_max':resid}

def analytic_columns(eps):
    """Referência por fórmulas fechadas normalizadas a90 dígitos, não chama factor."""
    e=parameter(eps)
    with localcontext() as ctx:
        ctx.prec=90;ctx.rounding=ROUND_HALF_EVEN
        raw=[(D(1),e,D(0),D(0)),(e,D(-1),1+e*e,D(0)),(e,D(-1),D(-1),2+e*e)]
        return tuple(tuple(x/dot(v,v).sqrt() for x in v) for v in raw)

if __name__=='__main__':
    for name in ['CGS','MGS','MGS2']:
        q,r=factor(method=name)
        print(name,{k:str(v) for k,v in diagnostics('0.0001',q,r).items()})
