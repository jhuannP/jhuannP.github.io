"""RL linear concentrado em SI, sem parasitas ou montagem real."""
from math import exp,isfinite,isclose

def state(L,R,V,I0,t):
    vals=[]
    for value in (L,R,V,I0,t):
        if isinstance(value,bool):raise ValueError('reais finitos necessários')
        try:value=float(value)
        except (TypeError,ValueError,OverflowError):raise ValueError('reais finitos necessários') from None
        if not isfinite(value):raise ValueError('reais finitos necessários')
        vals.append(value)
    L,R,V,I0,t=vals
    if L<=0 or R<=0 or t<0:raise ValueError('L,R positivos e t não negativo necessários')
    tau=L/R;q=exp(-t/tau);equilibrium=V/R
    I=equilibrium+(I0-equilibrium)*q
    derivative=-(I0-equilibrium)*q/tau
    result=dict(I=I,dI=derivative,vL=L*derivative,U=L*I*I/2,PR=R*I*I,PS=V*I,PL=L*I*derivative)
    if not all(isfinite(v) for v in result.values()):raise ValueError('escala fora da avaliação float finita')
    return result

def simpson(f,T,n=1000):
    h=T/n
    return h/3*(f(0)+f(T)+sum((4 if j%2 else 2)*f(j*h) for j in range(1,n)))

if __name__=='__main__':
    cases=[(2,4,12,0),(2,4,0,3),(1,2,3,4),(3,1,-2,1)]
    for L,R,V,I0 in cases:
        tau=L/R
        assert state(L,R,V,I0,0)['I']==I0
        for scaled in (0,.1,.5,1,2,5,10):
            s=state(L,R,V,I0,scaled*tau)
            assert isclose(V,R*s['I']+s['vL'],abs_tol=1e-12)
            assert isclose(s['PS'],s['PR']+s['PL'],abs_tol=1e-12)
            assert s['U']>=0 and s['PR']>=0
        T=3*tau
        supplied=simpson(lambda t:V*state(L,R,V,I0,t)['I'],T)
        dissipated=simpson(lambda t:R*state(L,R,V,I0,t)['I']**2,T)
        difference=state(L,R,V,I0,T)['U']-L*I0*I0/2
        assert isclose(supplied-dissipated,difference,rel_tol=1e-9,abs_tol=1e-9)
    from math import log
    half=state(2,4,0,3,.5*log(2))
    assert isclose(half['I'],1.5) and isclose(half['U'],2.25)
    assert isclose(9-half['U'],6.75)
    assert state(2,4,0,3,0)['vL']==-12
    for bad in [(0,4,0,3,0),(2,0,0,3,0),(2,4,0,3,-1),(True,4,0,3,0),(2,4,float('nan'),3,0)]:
        try:state(*bad)
        except ValueError:pass
        else:raise AssertionError('contrato inválido aceito')
    print('28 estados, quatro balanços integrados, condição inicial, descarga e contratos aprovados.')
