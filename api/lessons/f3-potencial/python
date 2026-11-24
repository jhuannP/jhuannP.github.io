"""Fontes esféricas prescritas, R=epsilon0=1; C é o deslocamento 4*pi*C_fisico."""
import math


def potential(profile=0, charge=1, radius=.5, test_charge=-1, shift=0):
    if profile not in (0, 1) or not all(math.isfinite(x) for x in (charge, radius, test_charge, shift)) or radius < 0:
        raise ValueError('Perfil 0/1, parâmetros finitos e raio não negativo')
    scaled = charge*((3-radius*radius)/2 if profile == 0 else 1) if radius <= 1 else charge/radius
    base = scaled/(4*math.pi)
    value = (scaled+shift)/(4*math.pi)
    # Compute differences before adding the arbitrary constant.
    delta = (scaled-charge/2)/(4*math.pi)
    boundary = profile == 1 and radius == 1 and charge != 0
    field = None if boundary else (charge*radius/(4*math.pi) if profile == 0 and radius <= 1 else (0 if radius < 1 else charge/(4*math.pi*radius*radius)))
    energy = test_charge*delta
    return dict(profile=profile, charge=charge, radius=radius, test_charge=test_charge, shift=shift,
                base=base, value=value, start=(charge/2+shift)/(4*math.pi), delta=delta,
                field=field, energy=energy, work=-energy, boundary=boundary,
                inner_field=charge/(4*math.pi) if profile == 0 else 0,
                outer_field=charge/(4*math.pi))


def simpson(fn, a, b, panels=2000):
    if panels < 2 or panels % 2:
        raise ValueError('Número par de painéis')
    h=(b-a)/panels
    return h/3*(fn(a)+fn(b)+sum((4 if j%2 else 2)*fn(a+j*h) for j in range(1,panels)))


def coulomb_shell(radius, charge=1):
    """Integral angular de Coulomb; u=1-t² remove singularidade integrável em r=1."""
    if radius < 0:
        raise ValueError('Raio não negativo')
    def integrand(t):
        if radius == 1:
            return math.sqrt(2)
        return 2*t/math.sqrt((radius-1)**2+2*radius*t*t)
    return charge*simpson(integrand,0,math.sqrt(2))/(8*math.pi)


if __name__ == '__main__':
    for profile in (0,1):
        s=potential(profile)
        print(s)
        assert abs(s['energy']+s['work']) < 1e-14
    assert abs(coulomb_shell(1)-1/(4*math.pi)) < 1e-12
