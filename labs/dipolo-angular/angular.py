"""Frações da potência média de um dipolo elétrico linear ideal, zona distante."""
from fractions import Fraction as F

def rational(value):
    if type(value) not in (int, F):
        raise TypeError("Use int ou Fraction; bool e float são rejeitados")
    return F(value)

def fraction(mu_lo, mu_hi):
    """Anel completo em azimute, mu=cos(theta); resultado adimensional."""
    lo, hi = rational(mu_lo), rational(mu_hi)
    if not -1 <= lo <= hi <= 1:
        raise ValueError("Exija -1 <= mu_lo <= mu_hi <= 1")
    return F(3, 4) * (hi - lo) - (hi**3 - lo**3) / 4

def isotropic_fraction(mu_lo, mu_hi):
    # Valida o mesmo domínio sem transformar a hipótese física.
    fraction(mu_lo, mu_hi)
    return (rational(mu_hi) - rational(mu_lo)) / 2

def relative_power(amplitude_ratio, frequency_ratio):
    """P'/P para p0'=a*p0 e omega'=w*omega, no mesmo vácuo ideal."""
    a, w = rational(amplitude_ratio), rational(frequency_ratio)
    if a < 0 or w <= 0:
        raise ValueError("Razão de amplitude >=0 e de frequência >0")
    return a*a*w**4

if __name__ == '__main__':
    print('Cone norte theta<=60 graus:', fraction(F(1,2), 1))
    print('Faixa equatorial |mu|<=1/2:', fraction(F(-1,2), F(1,2)))
    print('Frequência dobrada, p0 fixo:', relative_power(1, 2))
