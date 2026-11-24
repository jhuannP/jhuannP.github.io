"""AB2 + uma correção trapezoidal (PECE); início por Heun, passo fixo."""
from math import exp, isfinite
from cmath import sqrt


def finite(x):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x):
        raise ValueError('Escalar real finito, sem booleanos.')
    return float(x)


def count(n):
    if isinstance(n, bool) or not isinstance(n, int) or not 2 <= n <= 4096:
        raise ValueError('Entre 2 e 4096 passos inteiros.')
    return n


def pece(f, final=1, steps=20, y0=1):
    T, y=map(finite, (final, y0));n=count(steps)
    if T <= 0:raise ValueError('Tempo final positivo; início t=0.')
    h=T/n
    if h == 0:raise ValueError('Passo abaixo da precisão numérica.')
    evaluations=0
    def evaluate(t, value):
        nonlocal evaluations
        evaluations+=1
        return finite(f(t,value))
    trace=[dict(t=0.0,y=y,predictor=None)]
    previous=evaluate(0,y)
    prediction=finite(y+h*previous)
    current_y=finite(y+h*(previous+evaluate(h,prediction))/2)
    current=evaluate(h,current_y)
    trace.append(dict(t=h,y=current_y,predictor=prediction))
    for i in range(1,n):
        t=(i+1)*h
        prediction=finite(current_y+h*(3*current-previous)/2)
        next_y=finite(current_y+h*(current+evaluate(t,prediction))/2)
        next_f=evaluate(t,next_y)
        previous,current,current_y=current,next_f,next_y
        trace.append(dict(t=t,y=current_y,predictor=prediction))
    return dict(trace=trace,evaluations=evaluations)


def stability(z,method='pece'):
    z=finite(z)
    if method=='trap':
        if 1-z/2 == 0:raise ValueError('Fator trapezoidal singular.')
        return abs((1+z/2)/(1-z/2))
    if method!='pece':raise ValueError('Método pece ou trap.')
    a=1+z+3*z*z/4;b=z*z/4
    root=sqrt(a*a-4*b)
    return max(abs((a+root)/2),abs((a-root)/2))


def decay(rate=2,steps=16,method='pece',final=4):
    lam,T=map(finite,(rate,final));n=count(steps)
    if min(lam,T)<=0:raise ValueError('Taxa e tempo final positivos.')
    h=T/n;z=-lam*h
    if method=='pece':result=pece(lambda t,y:-lam*y,T,n)
    elif method=='trap':
        factor=(1+z/2)/(1-z/2);y=1.;trace=[dict(t=0.,y=y,predictor=None)]
        for i in range(1,n+1):
            y=finite(y*factor);trace.append(dict(t=i*h,y=y,predictor=None))
        result=dict(trace=trace,evaluations=None)
    else:raise ValueError('Método pece ou trap.')
    errors=[abs(p['y']-exp(-lam*p['t'])) for p in result['trace']]
    return dict(**result,z=z,radius=stability(z,method),
                final_error=errors[-1],max_error=max(errors),reference=exp(-lam*T))


if __name__=='__main__':
    for n in (20,40,80):
        q=decay(1,n,final=1)
        print('n=',n,'erro final=',q['final_error'],'avaliações=',q['evaluations'])
    for method in ('pece','trap'):
        print(method,'passo grosseiro:',decay(4,4,method))
    print('Uma correção não resolve o problema implícito; sem adaptação de passo.')
