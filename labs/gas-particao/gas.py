"""Monoatomic 3D Maxwell–Boltzmann model; exact arithmetic at a prescribed state."""
from fractions import Fraction as Q
from math import factorial


def positive(value):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise TypeError("Use int or Fraction, without bool or float")
    value = Q(value)
    if value <= 0:
        raise ValueError("Positive quantity required")
    return value


def state(n, theta, volume, thermal_volume):
    """thermal_volume is lambda**3 at THIS theta, not an independent control."""
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError("n must be an integer")
    if not 1 <= n <= 100:
        raise ValueError("Didactic domain: 1 <= n <= 100")
    theta, volume, thermal_volume = map(positive, (theta, volume, thermal_volume))
    return dict(Z=(volume / thermal_volume)**n / factorial(n),
                pressure=n * theta / volume,
                energy=Q(3, 2) * n * theta,
                cv_over_kB=Q(3, 2) * n,
                degeneracy=n * thermal_volume / volume)


if __name__ == '__main__':
    ref = state(3, 2, 300, 1)
    expanded = state(3, 2, 600, 1)
    hot = state(3, 8, 300, Q(1, 8))
    for name, s in [('base', ref), ('volume x2', expanded), ('theta x4', hot)]:
        print(name, {k: str(v) for k, v in s.items()})
