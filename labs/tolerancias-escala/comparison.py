"""Comparação finita didática, com tolerâncias explícitas e sem I/O no núcleo."""
from math import isclose,isfinite

def finite(value):
    if type(value) not in (int,float):raise ValueError("Use int ou float, sem bool")
    try:result=float(value)
    except OverflowError:raise ValueError("Valor fora da representação finita") from None
    if not isfinite(result):raise ValueError("Valor finito necessário")
    return result

def within(a,b,*,rtol,atol):
    a,b,rtol,atol=map(finite,(a,b,rtol,atol))
    if not 0<=rtol<1 or atol<0:
        raise ValueError("Exija 0<=rtol<1 e atol>=0")
    return isclose(a,b,rel_tol=rtol,abs_tol=atol)

if __name__=="__main__":
    print("Zero, só relativa:",within(0,1e-8,rtol=1e-6,atol=0))
    print("Zero, com absoluta:",within(0,1e-8,rtol=1e-6,atol=1e-7))
    print("Escala grande, relativa:",within(1e9,1e9+500,rtol=1e-6,atol=5))
    print("Escala grande, só absoluta:",within(1e9,1e9+500,rtol=0,atol=5))
