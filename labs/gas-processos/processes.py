"""Expansões de gás ideal: saídas normalizadas por p1, T1 e p1V1=nRT1."""
from math import exp,expm1,isfinite,log

def finite(x):
    if type(x) not in (int,float):raise ValueError("Use int/float sem bool")
    try:y=float(x)
    except OverflowError:raise ValueError("Valor não representável como float finito") from None
    if not isfinite(y):raise ValueError("Número finito necessário")
    return y

def expansion(ratio,*,gamma,kind):
    r,gamma=map(finite,(ratio,gamma))
    if r<1 or gamma<=1:raise ValueError("Expansão exige r>=1 e gamma>1")
    if kind not in ("isothermal_reversible","adiabatic_reversible","free_adiabatic"):
        raise ValueError("Processo não reconhecido")
    if kind=="adiabatic_reversible":
        x=(1-gamma)*log(r)
        temperature=exp(x);pressure=temperature/r
        work=-expm1(x)/(gamma-1)
        heat=0.;du=-work
    elif kind=="isothermal_reversible":
        temperature=1.;pressure=1/r;work=log(r);heat=work;du=0.
    else:
        temperature=1.;pressure=1/r;work=0.;heat=0.;du=0.
    if min(temperature,pressure)<=0 or not all(isfinite(v) for v in (temperature,pressure,work,heat,du)):
        raise ArithmeticError("Saída fora da representação finita positiva de estado")
    return dict(volume_ratio=r,temperature_ratio=temperature,pressure_ratio=pressure,
                work_over_nRT1=work,heat_over_nRT1=heat,du_over_nRT1=du)

if __name__=="__main__":
    for kind in ("isothermal_reversible","adiabatic_reversible","free_adiabatic"):
        print(kind,expansion(2,gamma=5/3,kind=kind))
