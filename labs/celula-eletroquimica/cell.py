"""Reversible thermodynamic cell model; no current or kinetic model."""
import math
R = 8.314462618  # J mol^-1 K^-1; rounded input constant
F = 96485.33212  # C mol^-1; rounded input constant

def finite(value, name):
    if type(value) not in (int,float):
        raise TypeError(name + " must be int or float, excluding bool")
    try:
        value = float(value)
    except OverflowError as exc:
        raise ValueError(name + " is outside float range") from exc
    if not math.isfinite(value):
        raise ValueError(name + " must be finite")
    return value

def log_quotient(a_m, a_n):
    """ln Q for M(s)+N2+ -> M2+ +N(s), pure solids activity 1."""
    a_m, a_n = finite(a_m,"a_m"),finite(a_n,"a_n")
    if a_m <= 0 or a_n <= 0:
        raise ValueError("activities must be positive")
    return math.log(a_m)-math.log(a_n)

def state(e0, n, temperature, ln_q):
    """n is positive electron number for the balanced reaction as written."""
    if type(n) is not int:
        raise TypeError("n must be int, excluding bool")
    if n <= 0:
        raise ValueError("n must be positive")
    finite(n,"n")  # Reject integer inputs outside the supported float range.
    e0, t, lq = finite(e0,"e0"),finite(temperature,"temperature"),finite(ln_q,"ln_q")
    if t <= 0:
        raise ValueError("absolute temperature must be positive")
    e = e0 - R*t/(n*F)*lq
    delta_g = -n*F*e
    ln_k = n*F*e0/(R*t)
    if not all(math.isfinite(x) for x in (e,delta_g,ln_k)):
        raise ValueError("derived quantity is outside float range")
    return {"E_V":e,"delta_r_G_J_mol":delta_g,"ln_K":ln_k}

if __name__ == "__main__":
    for am,an in ((1.,1.),(100.,1.)):
        print(am,an,state(.60,2,300.,log_quotient(am,an)))
