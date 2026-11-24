"""Três caminhos quase estáticos: p1=100 kPa, V1=3 L, nR=1 J/K, T1=T2=300 K."""
from fractions import Fraction as F
from math import log


def inspect(ratio=2):
    if type(ratio) not in (int,float,F):
        raise ValueError('Razão numérica, sem bool')
    try:r=F(ratio)
    except (ValueError,OverflowError):raise ValueError('Razão finita') from None
    if not F(1,2)<=r<=3 or (2*r).denominator!=1:
        raise ValueError('Razão de 1/2 a 3 em passos de 1/2')
    return dict(v2=3*r,p2=100/r,t1=300,t2=300,delta_u=0,
                isothermal=300*log(float(r)),
                pressure_first=300*(1-1/r),volume_first=300*(r-1),
                intermediate_pressure_first=300/r,intermediate_volume_first=300*r)


if __name__=='__main__':
    s=inspect(2)
    assert s['pressure_first']==150 and s['volume_first']==300
    assert s['delta_u']==0
    print(s)
