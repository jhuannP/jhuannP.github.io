"""Densidade conjunta sintética 2 em 0<x<y<1; cálculo racional, sem dados."""
from fractions import Fraction as F

def rational(value):
    if isinstance(value,bool) or not isinstance(value,(int,F)):
        raise ValueError('Use int ou Fraction, não float')
    return F(value)

def cdf(x,y):
    """Versão escolhida para Y=y interior: X uniforme em (0,y)."""
    x,y=map(rational,(x,y))
    if not 0<y<1: raise ValueError('y deve estar em (0,1)')
    return max(F(0),min(F(1),x/y))

def inspect(y=F(1,2),half_width=F(1,5),threshold=F(1,2)):
    y,h,a=map(rational,(y,half_width,threshold))
    if not 0<y<1 or not 0<h<=1 or not 0<=a<=1:
        raise ValueError('y em (0,1), meia largura em (0,1], limiar em [0,1]')
    lower=max(F(0),y-h);upper=min(F(1),y+h)
    mass=upper**2-lower**2
    if a<=lower: joint=2*a*(upper-lower)
    elif a>=upper: joint=mass
    else: joint=2*a*upper-a*a-lower*lower
    point=cdf(a,y);band=joint/mass
    return dict(lower=lower,upper=upper,band_mass=mass,joint=joint,
                point=point,band=band,difference=band-point,marginal=2*a-a*a)

if __name__=='__main__':
    r=inspect()
    assert r['band_mass']==F(2,5) and r['band']==F(9,10)
    assert r['point']==1 and r['marginal']==F(3,4)
    print(r)
