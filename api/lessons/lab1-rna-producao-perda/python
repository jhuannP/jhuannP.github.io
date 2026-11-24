"""Abundância contínua hipotética: produção constante e perda de primeira ordem."""
import math

def finite(v):
    if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v):
        raise ValueError('Use número real finito')
    return float(v)

def solution(production,loss,initial,time):
    a,d,m0,t=map(finite,(production,loss,initial,time))
    if a<0 or d<=0 or m0<0 or t<0:raise ValueError('Produção, início e tempo não negativos; perda positiva')
    stationary=a/d
    if not math.isfinite(stationary):raise ValueError('Escala fora do intervalo numérico')
    value=m0+(stationary-m0)*(-math.expm1(-d*t))
    if not math.isfinite(value):raise ValueError('Resultado fora do intervalo numérico')
    return value

def model(fold=2,initial=10,time=10):
    if type(fold) is not int or fold not in range(1,5):raise ValueError('Fator inteiro 1..4')
    if type(initial) is not int or initial not in range(0,51,5):raise ValueError('Início 0..50 em passos de 5')
    if type(time) is not int or not 0<=time<=30:raise ValueError('Tempo inteiro 0..30')
    def row(a,d):
        level=solution(a,d,initial,time)
        return dict(production=a,loss=d,stationary=a/d,level=level,
                    derivative=a-d*level,half_life=math.log(2)/d)
    return dict(a=row(2*fold,.2),b=row(2,.2/fold))

if __name__=='__main__':
    r=model();assert r['a']['stationary']==r['b']['stationary']==20
    assert abs(r['a']['level']-18.646647167633873)<1e-12
    print('Hipóteses A/B:',r)
