"""Exemplos originais: circunferência, resíduos e erro de quadratura."""
from cmath import exp
from math import pi,isfinite,fsum

def _radius(R):
    if isinstance(R,bool):raise ValueError("R positivo finito")
    try:R=float(R)
    except (TypeError,ValueError,OverflowError):raise ValueError("R positivo finito") from None
    if not isfinite(R) or R<=0:raise ValueError("R positivo finito")
    return R

def midpoint(f,R=1,n=1024,orientation=1):
    R=_radius(R)
    if isinstance(n,bool) or not isinstance(n,int) or n<4:raise ValueError("n inteiro >=4")
    if isinstance(orientation,bool) or orientation not in (-1,1):raise ValueError("orientação +1 ou -1")
    terms=[]
    for k in range(n):
        theta=2*pi*(k+.5)/n;z=R*exp(orientation*1j*theta)
        value=complex(f(z))*orientation*1j*z*(2*pi/n)
        if not isfinite(value.real) or not isfinite(value.imag):raise ValueError("integranda não finita")
        terms.append(value)
    return complex(fsum(t.real for t in terms),fsum(t.imag for t in terms))

def simple_reference(a,R=1,orientation=1):
    R=_radius(R)
    if isinstance(a,bool):raise ValueError("polo complexo finito")
    a=complex(a)
    if not isfinite(a.real) or not isfinite(a.imag):raise ValueError("polo complexo finito")
    if isinstance(orientation,bool) or orientation not in (-1,1):raise ValueError("orientação +1 ou -1")
    if abs(a)==R:raise ValueError("polo declarado no contorno: integral comum não fornecida")
    return orientation*2j*pi if abs(a)<R else 0j

def finite_sum_reference(a,R,n):
    # Identidade da regra de pontos médios, não da integral. Pode existir
    # mesmo com polo na curva se nenhum nó amostral coincidir com ele.
    q=complex(a)/R
    if abs(q)<=1:return 2j*pi/(1+q**n)
    inverse=(1/q)**n
    return 2j*pi*inverse/(1+inverse)

def verify():
    # Parametrização direta confrontada com referências por resíduos.
    count=0
    for R in (1,2):
        for a in (0,.2,-.5,.2+.3j,3,3j):
            for s in (-1,1):
                value=midpoint(lambda z:1/(z-a),R,1024,s)
                assert abs(value-simple_reference(a,R,s))<1e-10
                count+=1
    finite=0
    for a in (.99,1.01,-.99,.3+.7j):
        for n in (16,64,256,1024):
            value=midpoint(lambda z:1/(z-a),1,n)
            assert abs(value-finite_sum_reference(a,1,n))<1e-10
            finite+=1
    # A regra pode parecer convergente num problema que viola as hipóteses.
    for n in (16,64,256,1024):
        assert abs(midpoint(lambda z:1/(z-1),1,n)-1j*pi)<1e-9
    try:simple_reference(1,1)
    except ValueError:pass
    else:raise AssertionError("polo sobre a curva aceito")
    rational=lambda z:(2*z+1)/(z*(z-2))
    assert abs(midpoint(rational,1)+1j*pi)<1e-10
    assert abs(midpoint(rational,3)-4j*pi)<1e-10
    assert abs(midpoint(lambda z:1/(z-.5)**2))<1e-10
    assert abs(midpoint(lambda z:z/(z-.5)**2)-2j*pi)<1e-10
    assert abs(midpoint(lambda z:z*z))<1e-10
    # Monômios de Laurent: somente z^-1 contribui no círculo central.
    for k in range(-5,6):
        target=2j*pi if k==-1 else 0j
        assert abs(midpoint(lambda z:z**k)-target)<1e-10
    for R,n in ((0,16),(True,16),(1,True),(1,3),(float('nan'),16)):
        try:midpoint(lambda z:z,R,n)
        except ValueError:pass
        else:raise AssertionError("contrato")
    print(f"{count} integrais simples/orientações, {finite} somas finitas e exemplos de polos duplos conferidos")
    print("Regra no polo da curva (não é integral comum):",midpoint(lambda z:1/(z-1)))
    for a in (.99,1.01):
        print("a=",a,[(n,midpoint(lambda z:1/(z-a),1,n).imag/(2*pi)) for n in (16,64,256,1024)])

if __name__=='__main__':verify()
