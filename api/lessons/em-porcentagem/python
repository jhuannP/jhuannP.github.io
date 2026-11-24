"""Porcentagens hipotéticas com frações exatas; sem arredondar etapas."""
from fractions import Fraction as Q

def rational(value):
    return value if isinstance(value,Q) else Q(str(value))

def sequence(initial,rates):
    value=rational(initial)
    if value<=0:raise ValueError('Base inicial positiva neste recorte.')
    trace=[value]
    for rate in rates:
        r=rational(rate)
        if r<-100:raise ValueError('Taxa abaixo de -100% fora do recorte.')
        value*=1+r/100;trace.append(value)
    return trace

def rate_back(rate):
    r=rational(rate)
    if r<-100:raise ValueError('Taxa abaixo de -100%.')
    return None if r==-100 else -100*r/(100+r)

def summary(initial,a,b):
    trace=sequence(initial,[a,b]);factor=trace[-1]/trace[0]
    return dict(values=[float(v) for v in trace],net=float(100*(factor-1)),
                naive=float(rational(a)+rational(b)),
                recovery=None if factor==0 else float(100*(1/factor-1)))

if __name__=='__main__':
    print('Traço exato:',sequence(100,[20,-20]))
    print('Resumo:',summary(100,20,-20))
    print('Taxa que desfaz queda de 20%:',rate_back(-20))
    print('Taxa que desfaz queda de 100%:',rate_back(-100))
