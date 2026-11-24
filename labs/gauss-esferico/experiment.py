"""Esfera uniforme e casca fina prescritas; R=epsilon0=1 normalizados."""
import math


def sphere(profile=0, charge=1, radius=.5):
    if profile not in (0, 1) or not math.isfinite(charge) or not math.isfinite(radius) or radius < 0:
        raise ValueError('Perfil 0/1, carga finita e raio não negativo')
    boundary = profile == 1 and radius == 1 and charge != 0
    if boundary:
        inside = field = flux = None
    else:
        inside = charge*min(radius**3, 1) if profile == 0 else (0 if radius < 1 else charge)
        field = 0 if radius == 0 else inside/(4*math.pi*radius**2)
        flux = inside
    return dict(profile=profile, charge=charge, radius=radius, boundary=boundary,
                inside=inside, field=field, flux=flux,
                inner_limit=charge/(4*math.pi) if profile == 0 else 0,
                outer_limit=charge/(4*math.pi))


def shell_coulomb(radius, charge=1, panels=4000):
    """Integração angular de Coulomb para casca de raio um, fora da superfície."""
    if radius == 1 or radius < 0 or panels < 2 or panels % 2:
        raise ValueError('Raio fora da superfície e painéis pares')
    def f(u):
        return (radius-u)/(radius*radius+1-2*radius*u)**1.5
    h=2/panels
    integral=h/3*(f(-1)+f(1)+sum((4 if j%2 else 2)*f(-1+j*h) for j in range(1,panels)))
    return charge*integral/(8*math.pi)


if __name__ == '__main__':
    for profile in (0, 1):
        for radius in (0, .5, 1, 2):
            print(sphere(profile, 1, radius))
    assert abs(shell_coulomb(.5)) < 1e-10
