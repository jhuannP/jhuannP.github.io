"""Partículas livres em 1+1 dimensões, c=m0=1 em unidades normalizadas."""
import math


def gamma(beta):
    if not math.isfinite(beta) or abs(beta)>=1: raise ValueError('|beta|<1')
    return 1/math.sqrt((1-beta)*(1+beta))


def boost(energy,momentum,observer):
    if not all(math.isfinite(v) for v in (energy,momentum,observer)) or energy<abs(momentum):
        raise ValueError('Quadrimomento futuro causal e valores finitos')
    g=gamma(observer)
    return g*(energy-observer*momentum),g*(momentum-observer*energy)


def kinetic(energy,momentum,mass=1):
    if mass<=0 or energy<0: raise ValueError('Massa positiva e energia não negativa')
    return momentum*momentum/(energy+mass)


def model(system=1,beta=.6,observer=0.):
    if system not in (0,1) or not all(math.isfinite(v) for v in (beta,observer)) or not 0<=beta<=.95 or abs(observer)>.8:
        raise ValueError('Sistema 0/1, beta 0...95 e observador ±.8')
    g=gamma(beta);signs=[1] if system==0 else [1,-1]
    particles=[]
    for sign in signs:
        e,p=boost(g,sign*g*beta,observer)
        particles.append(dict(energy=e,momentum=p,kinetic=kinetic(e,p),velocity=p/e))
    energy=sum(x['energy'] for x in particles);momentum=sum(x['momentum'] for x in particles)
    mass=1 if system==0 else 2*g
    mass_squared=(energy-momentum)*(energy+momentum)
    bulk_kinetic=kinetic(energy,momentum,mass)
    sum_kinetic=sum(x['kinetic'] for x in particles)
    internal=0 if system==0 else 2*kinetic(g,g*beta)
    classical=.5*particles[0]['velocity']**2
    rel_error=(particles[0]['kinetic']-classical)/particles[0]['kinetic'] if particles[0]['kinetic'] else None
    return dict(system=system,beta=beta,observer=observer,particles=particles,energy=energy,
                momentum=momentum,mass=mass,mass_squared=mass_squared,rest_sum=len(signs),
                bulk_kinetic=bulk_kinetic,sum_kinetic=sum_kinetic,internal=internal,
                classical=classical,relative_error=rel_error,cm_velocity=momentum/energy)


if __name__=='__main__':
    for system in (0,1):
        for w in (0,.4):
            s=model(system,.6,w)
            print(system,w,'E=',s['energy'],'p=',s['momentum'],'M=',s['mass'])
            assert abs(s['mass_squared']-s['mass']**2)<1e-12
    assert abs(model(0,.6,0)['sum_kinetic']-.25)<1e-14
