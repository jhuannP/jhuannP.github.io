"""Geometria tetraédrica ideal e potencial ilustrativo, não ajuste experimental."""
from math import sin,cos,pi,sqrt,isfinite

def model(phi=60,barrier=12):
    if any(isinstance(x,bool) or not isinstance(x,(int,float)) or not isfinite(x) for x in (phi,barrier)) or not 0<=phi<=360 or not 0<=barrier<=18:
        raise ValueError('Ângulo 0–360 graus; barreira hipotética 0–18 kJ/mol')
    theta=phi*pi/180;rho=sqrt(8/9)
    front=[(rho*cos(pi/2+2*pi*k/3),rho*sin(pi/2+2*pi*k/3),-1/3) for k in range(3)]
    back=[(rho*cos(pi/2+2*pi*k/3+theta),rho*sin(pi/2+2*pi*k/3+theta),1/3) for k in range(3)]
    r=phi%120
    kind='eclipsada' if min(r,120-r)<1e-9 else 'alternada' if abs(r-60)<1e-9 else 'intermediária'
    return dict(phi=phi,barrier=barrier,front=front,back=back,kind=kind,energy=barrier*(1+cos(3*theta))/2,derivative=-1.5*barrier*sin(3*theta))

if __name__=='__main__':
    s=model();assert abs(s['energy'])<1e-12 and s['kind']=='alternada'
    print(s)
