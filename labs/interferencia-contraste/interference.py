"""Duas amplitudes escaladas: suas intensidades são a²,b². Não são E em V/m."""
from math import cos,sin,pi,sqrt,isfinite,isclose

def intensity(a,b,delta,w=1):
    values=[]
    for v in (a,b,delta,w):
        if isinstance(v,bool):raise ValueError('reais finitos necessários')
        try:v=float(v)
        except (TypeError,ValueError,OverflowError):raise ValueError('reais finitos necessários') from None
        if not isfinite(v):raise ValueError('reais finitos necessários')
        values.append(v)
    a,b,delta,w=values
    if a<0 or b<0 or not 0<=w<=1:raise ValueError('amplitudes não negativas e peso0..1 necessários')
    c=cos(delta)
    # Formas equivalentes sem subtrair intensidades grandes em oposição de fase.
    result=w*((a-b)**2+2*a*b*(1+c))+(1-w)*((a-b)**2+2*a*b*(1-c))
    if not isfinite(result):raise ValueError('escala fora da avaliação float finita')
    return result

def temporal_mean(a,b,delta,n=128):
    return sum(2*(a*cos(2*pi*j/n)+b*cos(2*pi*j/n+delta))**2 for j in range(n))/n

if __name__=='__main__':
    cases=0
    for a,b in [(1,1),(2,1),(.5,3),(0,2),(0,0)]:
        for delta in [0,pi/4,pi/2,pi,3*pi/2,2*pi,-pi/3,pi/6]:
            for w in [0,.25,.5,.75,1]:
                found=intensity(a,b,delta,w)
                sampled=w*temporal_mean(a,b,delta)+(1-w)*temporal_mean(a,b,delta+pi)
                assert isclose(found,sampled,rel_tol=1e-12,abs_tol=1e-12)
                assert (a-b)**2-1e-12<=found<=(a+b)**2+1e-12
                if w==.5:assert isclose(found,a*a+b*b,abs_tol=1e-12)
                cases+=1
    assert intensity(2,1,0)==9 and intensity(2,1,pi)==1
    assert intensity(2,1,0,.75)==7 and intensity(2,1,pi,.75)==3
    assert isclose(intensity(2,1,pi/2),5,abs_tol=1e-12)
    for args in [(True,1,0),(-1,1,0),(1,1,0,1.5),(1,1,float('nan'))]:
        try:intensity(*args)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print(cases,'estados versus média temporal; extremos, fase equilibrada e contratos aprovados.')
