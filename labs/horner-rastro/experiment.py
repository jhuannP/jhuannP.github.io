"""Horner com rastro, derivada e divisão linear; aritmética racional exata."""
from fractions import Fraction as Q

def evaluate(coefficients,x):
    if not isinstance(coefficients,(list,tuple)) or not 1<=len(coefficients)<=256:
        raise ValueError("Use lista/tupla com 1 a 256 coeficientes crescentes.")
    if any(type(v) not in (int,Q) for v in (*coefficients,x)):
        raise ValueError("Use int/Fraction, sem bool ou float.")
    c=list(map(Q,coefficients));x=Q(x)
    n=len(c)-1
    b=c[-1];d=Q(0);bs=[Q(0)]*len(c);bs[-1]=b
    trace=[dict(index=n,value=b,derivative=d)]
    for k in range(n-1,-1,-1):
        d=x*d+b
        b=x*b+c[k]
        bs[k]=b
        trace.append(dict(index=k,value=b,derivative=d))
    return dict(value=b,derivative=d,quotient=bs[1:],remainder=b,trace=trace,
                value_multiplications=n,value_additions=n)

if __name__=="__main__":
    print(evaluate([1,-3,2],2))
