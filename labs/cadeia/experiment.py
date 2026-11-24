"""Composição y=(1+bx)^3; referência exata e comparação de passo."""
from math import isfinite

def finite(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x):
        raise ValueError('Número finito, sem booleanos')
    return float(x)

def factors(x,b):
    x,b=finite(x),finite(b);u=1+b*x;external=3*u*u
    return dict(internal_value=u,external_rate=external,internal_rate=b,
                derivative=external*b,value=u**3)

def central(x,b,h):
    x,b,h=finite(x),finite(b),finite(h)
    if h<=0:raise ValueError('Passo positivo')
    return (factors(x+h,b)['value']-factors(x-h,b)['value'])/(2*h)

if __name__=='__main__':
    for x,b in [(1,2),(-.5,2),(1,0),(1,-2)]:
        reference=factors(x,b)
        for h in [.1,.01,.001]:
            approx=central(x,b,h)
            print('x,b,h:',x,b,h,'derivada:',reference['derivative'],
                  'diferença central:',approx,'erro:',abs(approx-reference['derivative']))
