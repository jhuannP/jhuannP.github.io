"""Pulsos escalares lineares por partes, com extensão zero fora dos nós. Unidades SI."""
from fractions import Fraction as Q

def rational(v):
    if isinstance(v,bool) or not isinstance(v,(int,Q)):raise TypeError("Use int ou Fraction.")
    return Q(v)

def nodes(values):
    if not isinstance(values,(tuple,list)) or len(values)<2:raise ValueError("Dois ou mais nós necessários.")
    out=[]
    for row in values:
        if not isinstance(row,(tuple,list)) or len(row)!=2:raise ValueError("Nó=(tempo,força).")
        out.append(tuple(map(rational,row)))
    if any(out[i][0]>=out[i+1][0] for i in range(len(out)-1)):raise ValueError("Tempos estritamente crescentes.")
    return tuple(out)

def force(values,t):
    a=nodes(values);t=rational(t)
    if t<a[0][0] or t>a[-1][0]:return Q(0)
    for (u,f),(v,g) in zip(a,a[1:]):
        if u<=t<=v:return f+(g-f)*(t-u)/(v-u)
    raise AssertionError("Intervalo não encontrado.")

def moments(values,start,end):
    """Retorna integral Fdt e integral tFdt. Saltos nos extremos não mudam integrais."""
    a=nodes(values);start,end=rational(start),rational(end)
    if start>end:raise ValueError("Intervalo invertido.")
    J=M=Q(0)
    for (u,f),(v,g) in zip(a,a[1:]):
        lo,hi=max(start,u),min(end,v)
        if lo>=hi:continue
        slope=(g-f)/(v-u);height=f+slope*(lo-u);h=hi-lo
        J+=height*h+slope*h*h/2
        M+=lo*height*h+(height+lo*slope)*h*h/2+slope*h**3/3
    return J,M

def impulse(values,start,end):return moments(values,start,end)[0]

def mean_force(values,start,end):
    start,end=rational(start),rational(end)
    if start>=end:raise ValueError("Média exige duração positiva.")
    return impulse(values,start,end)/(end-start)

def propagate(values,mass,x0,v0,start,end):
    """Massa constante: resultado (posição,velocidade) no fim, condições dadas no início."""
    mass,x0,v0=map(rational,(mass,x0,v0));start,end=map(rational,(start,end))
    if mass<=0:raise ValueError("Massa positiva necessária.")
    J,M=moments(values,start,end)
    return x0+v0*(end-start)+(end*J-M)/mass,v0+J/mass

if __name__=='__main__':
    triangle=((0,0),(Q(1,4),12),(Q(1,2),0))
    print('J=',impulse(triangle,0,Q(1,2)),'N s')
    print('(x,v)=',propagate(triangle,2,0,-1,0,Q(1,2)))
