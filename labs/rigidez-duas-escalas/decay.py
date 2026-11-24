"""Decaimento diagonal, fatores exatos; não é solver implícito geral."""
from fractions import Fraction as Q

def positive(v):
    if type(v) not in (int,Q) or v<=0:raise ValueError('racional positivo sem bool/float')
    return Q(v)

def factors(rate,h):
    rate,h=map(positive,(rate,h));z=rate*h
    return dict(explicit=1-z,implicit=1/(1+z))

def sequence(rate,h,n,method):
    if type(n) is not int or not 0<=n<=1000 or method not in ('explicit','implicit'):raise ValueError('n inteiro0..1000 e método válido')
    r=factors(rate,h)[method];out=[Q(1)]
    for _ in range(n):out.append(out[-1]*r)
    return out

if __name__=='__main__':
    from math import exp
    r=factors(100,Q(1,10));assert r==dict(explicit=Q(-9),implicit=Q(1,11))
    assert sequence(100,Q(1,10),2,'explicit')[-1]==81
    assert sequence(100,Q(1,50),4,'explicit')==[1,-1,1,-1,1]
    assert sequence(100,Q(1,100),3,'explicit')==[1,0,0,0]
    for rate in (Q(1),Q(10),Q(100)):
        for h in (Q(1,100),Q(1,50),Q(1,10),Q(1)):
            r=factors(rate,h)
            implicit=sequence(rate,h,20,'implicit')
            assert all(0<b<a for a,b in zip(implicit,implicit[1:]))
            explicit=sequence(rate,h,20,'explicit')
            assert all(explicit[k]==r['explicit']**k for k in range(21))
            assert (abs(r['explicit'])<1)==(0<h*rate<2)
    for method in ('explicit','implicit'):
        errors=[abs(float(sequence(1,Q(1,n),n,method)[-1])-exp(-1)) for n in (20,40,80)]
        assert errors[0]>errors[1]>errors[2]>0
        assert all(1.9<a/b<2.1 for a,b in zip(errors,errors[1:]))
        print(method,'erros no tempo1:',errors)
    for call in (lambda:factors(True,1),lambda:factors(1,0),lambda:sequence(1,Q(1,10),True,'explicit'),lambda:sequence(1,Q(1,10),2,'outro')):
        try:call()
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('Passo0,1: rápido exato=',exp(-10),'explícito=',-9,'implícito=',Q(1,11))
