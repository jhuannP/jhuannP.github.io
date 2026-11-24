"""Dois problemas de valor inicial, t/y adimensionais; sem integração numérica."""
from math import exp,isfinite

def model(case=1,y0=1,t=.5):
    if type(case) is not int or case not in (0,1):raise ValueError('Caso0/1.')
    for v in (y0,t):
        if isinstance(v,bool) or not isinstance(v,(int,float)) or not isfinite(v) or not -2<=v<=2:raise ValueError('Controle finito em [-2,2].')
    pole=None if case==0 or y0==0 else 1/y0
    lower=pole if pole is not None and y0<0 else None
    upper=pole if pole is not None and y0>0 else None
    denominator=1-y0*t
    reason='polo' if case==1 and y0!=0 and denominator==0 else 'outro-intervalo' if case==1 and denominator<0 else 'valida'
    defined=reason=='valida'
    value=(y0*exp(2*t) if case==0 else y0/denominator) if defined else None
    derivative=(2*value if case==0 else value*value) if defined else None
    return dict(case=case,y0=y0,t=t,pole=pole,lower=lower,upper=upper,defined=defined,reason=reason,value=value,derivative=derivative)

if __name__=='__main__':
    assert model()['value']==2
    assert model(t=1)['value'] is None
    assert model(t=1.5)['reason']=='outro-intervalo'
    print(model())
