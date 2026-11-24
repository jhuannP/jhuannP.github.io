"""Duas partículas em 1D, potencial k(x1-x2-ell)^2/2. Modelo original."""
from fractions import Fraction as Q
from itertools import product
from math import sin,cos,pi,isclose

def potential(x1,x2,k=Q(3),ell=Q(2)):
    return k*(x1-x2-ell)**2/2

def forces(x1,x2,k=Q(3),ell=Q(2)):
    f=-k*(x1-x2-ell)
    return f,-f

def coordinates(x1,x2,v1,v2,m1,m2,ell=Q(2)):
    if m1<=0 or m2<=0:raise ValueError("Massas positivas")
    M=m1+m2;mu=m1*m2/M
    return (m1*x1+m2*x2)/M,x1-x2-ell,(m1*v1+m2*v2)/M,v1-v2,mu

def analytic(t):
    # Unidades SI, massas1/3kg,k3N/m,ell2m,R0=0,V=1m/s,r0=1m,r_dot0=0.
    return (t+Q(3,4)*(2+cos(2*t)),t-Q(1,4)*(2+cos(2*t)),
            1-1.5*sin(2*t),1+.5*sin(2*t),-3*cos(2*t),cos(2*t))

def verify():
    # Invariância e forças por diferenças centrais exatas da quadrática.
    count=0
    for x1,x2,a in product(map(Q,(-2,0,3)),map(Q,(-1,1,2)),map(Q,(-5,0,4))):
        for k in (Q(1),Q(3),Q(7)):
            assert potential(x1+a,x2+a,k)==potential(x1,x2,k)
            f1,f2=forces(x1,x2,k);eps=Q(1,10)
            assert f1==-(potential(x1+eps,x2,k)-potential(x1-eps,x2,k))/(2*eps)
            assert f2==-(potential(x1,x2+eps,k)-potential(x1,x2-eps,k))/(2*eps)
            assert f1+f2==0
            count+=1
    energy_cases=0
    for m1,m2 in ((Q(1),Q(3)),(Q(2),Q(2)),(Q(3),Q(5))):
        for v1,v2 in product(map(Q,(-2,0,3)),repeat=2):
            R,r,V,vr,mu=coordinates(Q(2),Q(-1),v1,v2,m1,m2)
            assert m1*v1*v1/2+m2*v2*v2/2==(m1+m2)*V*V/2+mu*vr*vr/2
            assert m1*v1+m2*v2==(m1+m2)*V
            energy_cases+=1
    states=0;h=1e-4
    for i in range(41):
        t=i/10;x1,x2,v1,v2,a1,a2=analytic(t)
        f1,f2=forces(x1,x2)
        assert isclose(a1,f1,rel_tol=1e-11,abs_tol=1e-11)
        assert isclose(3*a2,f2,rel_tol=1e-11,abs_tol=1e-11)
        assert isclose(v1+3*v2,4,rel_tol=1e-12)
        assert isclose(v1*v1/2+3*v2*v2/2+potential(x1,x2),3.5,rel_tol=1e-12)
        assert isclose((x1+3*x2)/4,t,abs_tol=1e-12)
        lo=analytic(t-h);hi=analytic(t+h)
        assert abs((hi[0]-lo[0])/(2*h)-v1)<2e-8
        assert abs((hi[1]-lo[1])/(2*h)-v2)<2e-8
        assert abs((hi[0]-2*x1+lo[0])/(h*h)-a1)<1e-6
        assert x1-x2>=1-1e-12
        states+=1
    x1,x2,v1,v2,*_=analytic(pi/4)
    assert isclose(v1,-.5,abs_tol=1e-12) and isclose(v2,1.5,abs_tol=1e-12)
    assert isclose(x1-x2,2,abs_tol=1e-12)
    try:coordinates(0,1,0,0,0,1)
    except ValueError:pass
    else:raise AssertionError("massa nula")
    print(f"{count} translações/forças, {energy_cases} decomposições cinéticas e {states} estados analíticos conferidos")
    print("t=pi/4: v1,v2=",v1,v2,"; P=",v1+3*v2)

if __name__=='__main__':verify()
