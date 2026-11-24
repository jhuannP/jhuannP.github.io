"""Bloco em piso fixo horizontal, força horizontal; sem integração temporal."""
from fractions import Fraction as Q

def rational(x):
    if isinstance(x,bool) or not isinstance(x,(int,Q)):raise ValueError('Use int ou Fraction')
    return Q(x)

def contact(mass,g,force,mu_s,mu_k,velocity):
    mass,g,force,mu_s,mu_k,velocity=map(rational,(mass,g,force,mu_s,mu_k,velocity))
    if not mass>0 or not g>0 or not 0<=mu_k<=mu_s:
        raise ValueError('m,g positivos e 0<=mu_k<=mu_s')
    normal=mass*g;limit=mu_s*normal;kinetic=mu_k*normal
    if velocity==0 and abs(force)<=limit:
        friction=-force;status='repouso admissível'
    else:
        direction=1 if (velocity if velocity else force)>0 else -1
        friction=-direction*kinetic
        status='deslizamento' if velocity else 'início de deslizamento'
    return dict(normal=normal,static_limit=limit,kinetic_magnitude=kinetic,
                friction=friction,acceleration=(force+friction)/mass,
                status=status,friction_power=friction*velocity)

if __name__=='__main__':
    for force,velocity in ((10,0),(20,0),(24,0),(10,1),(0,1)):
        print(force,velocity,contact(4,10,force,Q(1,2),Q(3,10),velocity))
