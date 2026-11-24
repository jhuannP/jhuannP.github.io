"""Cadeia harmônica livre 1-M-1: somente deslocamentos longitudinais."""
import math


def modes(mass=1.,spring=1.):
    if not all(math.isfinite(v) and v>0 for v in (mass,spring)):
        raise ValueError('Massa e rigidez positivas finitas')
    raw=((1.,1.,1.),(-1.,0.,1.),(1.,-2/mass,1.))
    weights=(1.,mass,1.)
    eig=(0.,spring,spring*(1+2/mass))
    result=[]
    for lam,u in zip(eig,raw):
        norm=math.sqrt(sum(m*x*x for m,x in zip(weights,u)))
        shape=tuple(x/max(map(abs,u)) for x in u)
        result.append(dict(eigenvalue=lam,omega=math.sqrt(lam),
                           mass_vector=tuple(x/norm for x in u),shape=shape))
    return result


def model(mode=1,mass=1.,spring=1.,phase=45.):
    if mode not in (0,1,2) or not all(math.isfinite(v) for v in (mass,spring,phase)) or not .5<=mass<=4 or not .5<=spring<=2 or not 0<=phase<=360:
        raise ValueError('Modo 0..2, massa .5..4, rigidez .5..2, fase 0..360')
    s=modes(mass,spring)[mode];omega=s['omega'];shape=s['shape'];A=.15
    c,si={0:(1.,0.),90:(0.,1.),180:(-1.,0.),270:(0.,-1.),360:(1.,0.)}.get(phase,(math.cos(math.radians(phase)),math.sin(math.radians(phase))))
    if mode==0:c,si=1.,0. # Static member of the zero-mode family A+B*t.
    clean=lambda x:0. if x==0 else x
    q=tuple(clean(A*x*c) for x in shape)
    v=tuple(clean(-A*omega*x*si) for x in shape)
    bonds=(q[1]-q[0],q[2]-q[1])
    potential=.5*spring*sum(x*x for x in bonds)
    kinetic=.5*sum(m*x*x for m,x in zip((1.,mass,1.),v))
    return dict(mode=mode,mass=mass,spring=spring,phase=phase,omega=omega,
                cyclic=omega/(2*math.pi),shape=shape,q=q,v=v,bonds=bonds,
                potential=potential,kinetic=kinetic,energy=potential+kinetic,
                com=(q[0]+mass*q[1]+q[2])/(2+mass))


if __name__=='__main__':
    for mode in range(3):print(model(mode))
    assert modes(1,1)[1]['omega']==1
    assert abs(modes(1,1)[2]['omega']-math.sqrt(3))<1e-14
