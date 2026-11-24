"""Modelo fechado A -> I -> P de primeira ordem: RK4 didático com passo limitado."""
from math import isfinite,ceil
from dataclasses import dataclass

def real(v):
    if isinstance(v,bool) or not isinstance(v,(int,float)):raise TypeError("Use int/float finito.")
    try:v=float(v)
    except OverflowError:raise ValueError("Valor fora da escala float.") from None
    if not isfinite(v):raise ValueError("Valor finito necessário.")
    return v

def rhs(state,k1,k2):
    a,i,p=state;v1=k1*a;v2=k2*i
    return -v1,v1-v2,v2

@dataclass(frozen=True)
class Result:
    a:float
    intermediate:float
    product:float
    steps:int
    mass_error:float

def integrate(k1,k2,initial,time,max_step=.05):
    """Constantes em min^-1, tempo min, concentrações numa mesma unidade.
    max_step limita h*max(k1,k2), não fornece certificado de erro.
    """
    k1,k2,a0,t,s=map(real,(k1,k2,initial,time,max_step))
    if k1<=0 or k2<=0 or a0<=0 or t<0:raise ValueError("k1,k2,A0 positivos e tempo não negativo.")
    if not 0<s<=.25:raise ValueError("0<max_step<=0.25.")
    x=t*max(k1,k2)
    if not isfinite(x) or x/s>100000:raise ValueError("Mais de100000 passos ou escala inválida; não executar.")
    if t==0:return Result(a0,0.,0.,0,0.)
    n=max(1,ceil(x/s));h=t/n;z=(a0,0.,0.)
    def add(z,w,c):return tuple(z[j]+c*w[j] for j in range(3))
    for _ in range(n):
        q1=rhs(z,k1,k2);q2=rhs(add(z,q1,h/2),k1,k2)
        q3=rhs(add(z,q2,h/2),k1,k2);q4=rhs(add(z,q3,h),k1,k2)
        z=tuple(z[j]+h*(q1[j]+2*q2[j]+2*q3[j]+q4[j])/6 for j in range(3))
        if any(not isfinite(v) or v<0 for v in z):raise ArithmeticError("Estado numérico inválido; rever escala/passo.")
    return Result(*z,n,sum(z)-a0)

if __name__=='__main__':
    for t in (0,.5,1,2,4):print(t,integrate(1,1,1,t))
