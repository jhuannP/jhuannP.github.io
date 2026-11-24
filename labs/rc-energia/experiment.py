"""RC ideal com tensão inicial; fonte pode fornecer ou absorver energia."""
from math import exp,expm1,isfinite

def inspect(R=2,C=3,V=4,u=1,V0=0):
    if any(isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) for x in (R,C,V,u,V0)) or R<=0 or C<=0 or V<0 or V0<0 or u<0:
        raise ValueError('R,C positivos;V,V0,u não negativos e finitos')
    e=exp(-u);fraction=-expm1(-u);delta=V-V0
    VC=V0+delta*fraction;I=delta/R*e
    initial=C*V0*V0/2;stored=C*VC*VC/2
    change=C*delta*fraction*(VC+V0)/2
    source=C*V*delta*fraction
    dissipated=C*delta*delta*(-expm1(-2*u))/2
    result=dict(tau=R*C,time=u*R*C,VC=VC,I=I,q=C*VC,VR=R*I,
                initial=initial,stored=stored,change=change,source=source,dissipated=dissipated,
                power_source=V*I,power_R=R*I*I,power_C=VC*I)
    return {key:0.0 if value==0 else value for key,value in result.items()}

if __name__=='__main__':
    from math import log
    z=inspect(V=2,V0=4,u=log(2))
    assert abs(z['VC']-3)<1e-12 and abs(z['source']+6)<1e-12
    assert abs(z['change']+10.5)<1e-12 and abs(z['dissipated']-4.5)<1e-12
    print(z)
