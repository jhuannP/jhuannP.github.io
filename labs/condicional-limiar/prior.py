"""Sensor ideal com lei inicial f_X(x)=2x. Exemplo original, adimensional."""
from fractions import Fraction as Q
from math import isclose

def posterior_zero(a):
    if isinstance(a,bool) or not isinstance(a,(int,Q)) or not 0<a<1:
        raise ValueError("Limiar racional estritamente entre zero e um necessário")
    a=Q(a)
    return {"evidence":a*a,"mean":2*a/3,"variance":a*a/18,"risk":a**4/18}

def simpson(f,lo,hi,n=100):
    # Usado somente na verificação numérica; polinômios de grau até três.
    step=(hi-lo)/n
    return step/3*(f(lo)+f(hi)+sum((4 if i%2 else 2)*f(lo+i*step) for i in range(1,n)))

if __name__=="__main__":
    for k in range(1,20):
        a=Q(k,20); r=posterior_zero(a); af=float(a)
        evidence=simpson(lambda x:2*x,0.,af)
        mean=simpson(lambda x:2*x*x,0.,af)/evidence
        variance=simpson(lambda x:(x-mean)**2*2*x,0.,af)/evidence
        risk=evidence*variance
        positive_mean=simpson(lambda y:2*(af+y)**2,0.,1-af)
        predicted_second=evidence*mean**2+simpson(lambda y:2*(af+y)**3,0.,1-af)
        for found,key in [(evidence,'evidence'),(mean,'mean'),(variance,'variance'),(risk,'risk')]:
            assert isclose(found,float(r[key]),abs_tol=1e-12)
        assert isclose(evidence+simpson(lambda y:2*(af+y),0.,1-af),1.,abs_tol=1e-12)
        assert isclose(evidence*mean+positive_mean,2/3,abs_tol=1e-12)
        assert isclose(risk+predicted_second-(2/3)**2,1/18,abs_tol=1e-12)
    assert posterior_zero(Q(1,2))==dict(evidence=Q(1,4),mean=Q(1,3),variance=Q(1,72),risk=Q(1,288))
    for bad in [True,False,0,1,-1,Q(3,2),.5,'1/2',None]:
        try:posterior_zero(bad)
        except ValueError:pass
        else:raise AssertionError(bad)
    print('19 limiares: normalização, momentos, esperança iterada e variância total conferidos; contratos e exemplo exato aprovados.')
