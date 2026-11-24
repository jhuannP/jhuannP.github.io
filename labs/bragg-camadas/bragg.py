"""Original finite 1D stack; common length units, arbitrary amplitude units."""
import math
import cmath


def positive(x):
    if type(x) not in (int, float):
        raise ValueError('finite positive length required')
    try:
        x = float(x)
    except OverflowError as e:
        raise ValueError('length not representable') from e
    if not math.isfinite(x) or x <= 0:
        raise ValueError('finite positive length required')
    return x


def orders(d, wavelength):
    """Return (order, theta_deg, two_theta_deg); includes formal backscatter."""
    d, wavelength = positive(d), positive(wavelength)
    ratio = (d / wavelength) * 2
    if not math.isfinite(ratio) or ratio > 10000:
        raise ValueError('at most 10000 geometric orders')
    result = []
    for m in range(1, math.floor(ratio) + 1):
        theta = math.degrees(math.asin(m / ratio))
        result.append((m, theta, 2 * theta))
    return result


def intensity(n, cycles, b=1):
    """phi=2*pi*cycles, cells j=0..n-1, sites j and j+1/2, weights 1,b.

    Raw scalar |amplitude|^2; no instrument, atomic form factor or units fitted.
    """
    if type(n) is not int or not 1 <= n <= 10000:
        raise ValueError('1..10000 cells')
    if type(cycles) not in (int, float) or type(b) not in (int, float):
        raise ValueError('finite phase cycles and amplitude weight')
    if abs(cycles) > 1e6 or not math.isfinite(cycles):
        raise ValueError('phase cycles must have magnitude <= 1e6')
    if not 0 <= b <= 1 or not math.isfinite(b):
        raise ValueError('0 <= b <= 1')
    # Reduce each phase modulo a full turn before evaluating complex exponential.
    stack = sum(cmath.exp(2j * math.pi * ((j * cycles) % 1)) for j in range(n))
    motif = 1 + b * cmath.exp(2j * math.pi * ((cycles / 2) % 1))
    return abs(stack * motif) ** 2


if __name__ == '__main__':
    print('Geometric candidates, d=0.30 nm, lambda=0.15 nm:')
    for row in orders(.30, .15):
        print(row)
    print('Prescribed model, N=5; I/N² at orders 1..4:')
    for b in (1, .5, 0):
        print(b, [round(intensity(5, m, b) / 25, 8) for m in range(1, 5)])
    print('Not measured peak intensities; backscatter is a formal endpoint.')
