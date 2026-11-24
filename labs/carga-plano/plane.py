"""Plano condutor aterrado: domínio físico z>=0, carga em(0,0,a)."""
from fractions import Fraction as Q
from math import hypot,isfinite


def finite(x):
    if isinstance(x,bool) or not isinstance(x,(int,float,Q)):
        raise ValueError('Número real finito exigido')
    try:x=float(x)
    except (ValueError,OverflowError):raise ValueError('Fora da representação float') from None
    if not isfinite(x):raise ValueError('Número finito exigido')
    return x


def parameters(q,a,k):
    q,a,k=map(finite,(q,a,k))
    if q==0 or a<=0 or k<=0:raise ValueError('q não nulo,a e k positivos')
    return q,a,k


def potential_field(x,y,z,q=3,a=2,k=2):
    x,y,z=map(finite,(x,y,z));q,a,k=parameters(q,a,k)
    if z<0:raise ValueError('Domínio físico externo z>=0')
    r1=hypot(x,y,z-a);r2=hypot(x,y,z+a)
    if r1==0:raise ValueError('Auto-campo singular excluído')
    try:
        phi=k*q*(1/r1-1/r2)
        field=tuple(k*q*(u/r1**3-v/r2**3)
                    for u,v in zip((x,y,z-a),(x,y,z+a)))
    except (OverflowError,ZeroDivisionError):raise ValueError('Faixa numérica não resolvida') from None
    if not all(map(isfinite,(phi,*field))):raise ValueError('Resultado não finito')
    return phi,field


def surface(rho,q=3,a=2,k=2):
    rho=finite(rho);q,a,k=parameters(q,a,k)
    if rho<0:raise ValueError('Raio não negativo')
    distance=hypot(rho,a)
    try:sigma_times_2pi=-q*a/distance**3
    except (OverflowError,ZeroDivisionError):raise ValueError('Faixa numérica não resolvida') from None
    # A primeira saída NÃO é sigma: multiplique/divida conscientemente por2pi.
    charge=-q*(1-a/distance)
    if not all(map(isfinite,(sigma_times_2pi,charge))):raise ValueError('Resultado não finito')
    return dict(sigma_times_2pi=sigma_times_2pi,charge_in_disk=charge)


def force_energy(q=3,a=2,k=2):
    args=(q,a,k)
    if any(isinstance(x,bool) or not isinstance(x,(int,Q)) for x in args):
        raise ValueError('Use int/Fraction para a referência exata')
    q,a,k=map(Q,args)
    if q==0 or a<=0 or k<=0:raise ValueError('q não nulo,a e k positivos')
    induced_potential=-k*q/(2*a)
    return dict(fz=-k*q*q/(4*a*a),energy=q*induced_potential/2,
                induced_potential=induced_potential,pair_energy=q*induced_potential)


if __name__=='__main__':
    r=force_energy();assert r['fz']==Q(-9,8) and r['energy']==Q(-9,4)
    print('Força/energia exatas:',r)
    print('Potencial/campo em(0,0,4):',potential_field(0,0,4))
    print('Superfície emrho1,5:',surface(1.5))
