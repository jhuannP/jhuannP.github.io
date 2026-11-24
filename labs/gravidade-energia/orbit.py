"""Gravitação central: energias específicas racionais, sem integrador orbital."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):
        raise TypeError('use int ou Fraction')
    return Q(x)

def positive(x):
    x=rational(x)
    if x<=0:raise ValueError('valor positivo necessário')
    return x

def circular(mu,radius):
    mu,r=map(positive,(mu,radius));v2=mu/r
    return {'v2':v2,'k':v2/2,'u':-v2,'energy':-v2/2,
            'angular2':mu*r,'period2_over_4pi2':r**3/mu,'escape2':2*v2}

def specific_energy(mu,radius,radial_speed,tangential_speed):
    mu,r=map(positive,(mu,radius));vr,vt=map(rational,(radial_speed,tangential_speed))
    return (vr*vr+vt*vt)/2-mu/r

def surface_change(mu,radius,height):
    mu,R=map(positive,(mu,radius));z=rational(height)
    if z<0:raise ValueError('altura não negativa; região externa')
    exact=mu/R-mu/(R+z)
    linear=mu*z/R**2
    relative=(linear-exact)/exact if exact else None
    return {'exact':exact,'linear':linear,'relative':relative}

if __name__=='__main__':
    for radius in (2,8):print('r=',radius,circular(8,radius))
    print('superfície:',surface_change(8,2,Q(1,5)))
