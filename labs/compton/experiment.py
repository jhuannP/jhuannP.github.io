"""Compton em elétron livre inicialmente em repouso; m_e=c=1, lambda_C=h/(m_e*c)."""
import math


def model(alpha=1.,angle=90.):
    if not all(math.isfinite(v) for v in (alpha,angle)) or not .1<=alpha<=2 or not 0<=angle<=180:
        raise ValueError('alpha 0.1..2 e ângulo 0..180 graus')
    theta=math.radians(angle)
    d=1. if angle==90 else 2*math.sin(theta/2)**2
    cosine=1-d;sine=0. if angle in (0,180) else math.sin(theta)
    denominator=1+alpha*d;scattered=alpha/denominator
    kinetic=alpha*alpha*d/denominator  # avoids alpha-scattered at small angles
    px=alpha*(1+alpha)*d/denominator;py=-scattered*sine
    electron_energy=1+kinetic;momentum=math.hypot(px,py)
    recoil_angle=math.degrees(math.atan2(abs(py),px)) if momentum else None
    return dict(alpha=alpha,angle=angle,d=d,scattered=scattered,kinetic=kinetic,
                photon_x=scattered*cosine,photon_y=scattered*sine,
                electron_x=px,electron_y=py,electron_energy=electron_energy,
                beta=momentum/electron_energy,recoil_angle=recoil_angle,
                wavelength_in=1/alpha,wavelength_out=1/alpha+d,
                photon_fraction=1/denominator,electron_fraction=alpha*d/denominator,
                mass_squared=electron_energy**2-px*px-py*py)


if __name__=='__main__':
    for angle in (0,90,180):print(model(1,angle))
    s=model(1,90)
    assert abs(s['scattered']-.5)<1e-14
    assert abs(s['electron_x']-1)<1e-14
    assert abs(s['electron_y']+.5)<1e-14
