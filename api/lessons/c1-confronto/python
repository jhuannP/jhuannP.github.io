"""Intervalos racionais e sequências analíticas; modelos didáticos."""
from fractions import Fraction as Q
from math import pi, sin, isfinite


def value(mode,x):
    if isinstance(mode,bool) or mode not in (0,1,2):raise ValueError('Modelo 0, 1 ou 2')
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('x racional')
    x=Q(x)
    return x**3-2 if mode==0 else x**3-x if mode==1 else Q(-1 if x<0 else 1)


def interval_trace(mode=0,steps=5):
    if isinstance(steps,bool) or not isinstance(steps,int) or not 0<=steps<=16:
        raise ValueError('Entre 0 e 16 etapas')
    value(mode,0)
    a,b=(Q(1),Q(2)) if mode==0 else (Q(-2),Q(2)) if mode==1 else (Q(-1),Q(1))
    actual=0
    for _ in range(steps):
        mid=(a+b)/2; fm=value(mode,mid);actual+=1
        if fm==0:a=b=mid;break
        if (value(mode,a)<0)==(fm<0):a=mid
        else:b=mid
    mid=(a+b)/2
    return dict(a=a,b=b,mid=mid,residual=value(mode,mid),width=b-a,steps=actual)


def extrema(n=2,power=2):
    if isinstance(n,bool) or not isinstance(n,int) or not 1<=n<=100:
        raise ValueError('n entre 1 e 100')
    if isinstance(power,bool) or power not in (0,1,2):raise ValueError('Potência 0,1,2')
    plus=1/(pi/2+2*pi*n);minus=1/(3*pi/2+2*pi*n)
    return dict(plus=plus,minus=minus,positive=plus**power,negative=-(minus**power))


def oscillation(x,power=2):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) or x==0:
        raise ValueError('x real finito não nulo')
    if isinstance(power,bool) or power not in (0,1,2):raise ValueError('Potência 0,1,2')
    phase=1/x
    if not isfinite(phase):raise ValueError('Recíproco fora da resolução numérica')
    return abs(x)**power*sin(phase)


if __name__=='__main__':
    for mode in (0,1,2):print('Modelo',mode,interval_trace(mode,5))
    assert interval_trace(2,12)['residual']==-1  # Estreitar intervalo não cria raiz no salto.
    assert interval_trace(1,5)['mid']==0
    for n in (1,2,10,20):
        r=extrema(n,2)
        assert abs(oscillation(r['plus'])-r['positive'])<1e-12
        assert abs(oscillation(r['minus'])-r['negative'])<1e-12
        print('Extremos analíticos aproximados:',r)
