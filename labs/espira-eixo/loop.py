"""Campo axial normalizado: B/B0, sem fixar valor numérico de mu0."""
from math import cos,sin,pi,fsum,isfinite

def coordinate(u):
    if isinstance(u,bool) or not isinstance(u,(int,float)) or not isfinite(u) or abs(u)>1000:
        raise ValueError("u=z/a real finito com |u|<=1000")
    return float(u)

def profile(u):
    u=coordinate(u)
    return (1+u*u)**(-1.5)

def integrate_axis(u,n=64):
    u=coordinate(u)
    if type(n) is not int or not 4<=n<=4096:
        raise ValueError("4 a4096 pontos de quadratura")
    scale=1/(n*(1+u*u)**1.5)
    # Componentes de dl x R: (a*z*cos(phi),a*z*sin(phi),a*a)dphi.
    # Coordenadas e resultado normalizados por a e B0=mu0*I/(2*a).
    angles=[2*pi*(j+.5)/n for j in range(n)]
    return (scale*fsum(u*cos(t) for t in angles),
            scale*fsum(u*sin(t) for t in angles),
            scale*fsum(1. for t in angles))

def dipole_profile(u):
    u=coordinate(u)
    if not u:raise ValueError("dipolo distante não definido no centro")
    return abs(u)**(-3)

if __name__=='__main__':
    for u in (0.,.75,-.75,1.,3.,10.):
        print("u=",u,"perfil=",profile(u),"integral=",integrate_axis(u))
    u=10.
    print("erro relativo da aproximação dipolar:",dipole_profile(u)/profile(u)-1)
