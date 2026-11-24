"""Três exemplos reais com domínio explícito; None não é zero."""
from math import sqrt,isfinite

def model(case=0,a=1,x=5):
    if isinstance(case,bool) or case not in (0,1,2) or any(isinstance(v,bool) or not isinstance(v,(int,float)) or not isfinite(v) for v in (a,x)) or not -2<=a<=2 or not -4<=x<=6:
        raise ValueError('Caso 0/1/2, a em [-2,2], x em [-4,6]')
    if case==0:
        valid=x>=a and x!=a+1
        value=sqrt(x-a)/(x-(a+1)) if valid else None
        reason='radicando negativo' if x<a else 'denominador zero' if x==a+1 else 'válido'
        candidate=None
    elif case==1:
        valid=x!=a;value=x+a if valid else None;candidate=x+a
        reason='denominador zero' if not valid else 'válido'
    else:
        valid=True;value=abs(x-a);candidate=x-a;reason='válido'
    if value==0:value=0.0
    return dict(case=case,a=a,x=x,defined=valid,value=value,candidate=candidate,reason=reason)

if __name__=='__main__':
    assert abs(model()['value']-2/3)<1e-12
    assert model(1,1,1)['value'] is None and model(1,1,1)['candidate']==2
    print(model())
