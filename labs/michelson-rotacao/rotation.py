"""Ideal equal/unequal arm interferometer. Prescribed inputs, no experimental fit."""
from math import sqrt, isfinite

def _real(x, positive=False):
    if isinstance(x, bool) or not isinstance(x, (float, int)):
        raise TypeError("expected a finite int or float")
    x = float(x)
    if not isfinite(x) or (positive and x <= 0):
        raise ValueError("outside finite domain")
    return x

def _inputs(l1, l2, c, beta):
    l1, l2, c = (_real(x, True) for x in (l1, l2, c))
    beta = _real(beta)
    if abs(beta) >= 1:
        raise ValueError("requires |beta| < 1")
    return l1, l2, c, beta

def gap(beta):
    """Stable 1/(1-beta**2) - 1/sqrt(1-beta**2)."""
    beta = _real(beta)
    if abs(beta) >= 1:
        raise ValueError("requires |beta| < 1")
    u = beta * beta
    r = sqrt(1-u)
    return u / ((1-u) * (1+r))

def ether_times(l1, l2, c, beta):
    """Arm-labelled round trips before/after 90 deg in the uncontracted model."""
    l1, l2, c, beta = _inputs(l1, l2, c, beta)
    r = sqrt(1-beta*beta)
    return ((2*l1/(c*r*r), 2*l2/(c*r)),
            (2*l1/(c*r), 2*l2/(c*r*r)))

def rotation_change(l1, l2, c, beta):
    """Signed (t1-t2)_after - (t1-t2)_before, stably evaluated."""
    l1, l2, c, beta = _inputs(l1, l2, c, beta)
    return -2*(l1+l2)/c*gap(beta)

def fringe_shift(l1, l2, wavelength, beta):
    """Magnitude of rotation signal, in fringes. All lengths in same unit."""
    l1, l2, wavelength, beta = _inputs(l1, l2, wavelength, beta)
    return 2*(l1+l2)/wavelength*gap(beta)

def relativistic_proper_times(l1, l2, c):
    """Inertial co-moving apparatus, fixed proper lengths, vacuum, no rotation transient."""
    l1, l2, c, _ = _inputs(l1, l2, c, 0)
    return (2*l1/c, 2*l2/c)

if __name__ == '__main__':
    print("Synthetic model, not data")
    print("before / after:", ether_times(3, 2, 1, .6))
    print("change:", rotation_change(3, 2, 1, .6))
    print("fringes:", fringe_shift(3, 2, .5, .6))
    for b in (1e-4, 1e-9):
        naive = 1/(1-b*b) - 1/sqrt(1-b*b)
        print("beta, naive gap, stable gap:", b, naive, gap(b))
