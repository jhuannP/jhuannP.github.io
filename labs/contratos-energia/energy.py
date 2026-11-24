"""Contrato didático: energia cinética clássica, kg e m/s, sem efeitos externos."""
from math import isfinite
from fractions import Fraction

def finite_real(value, name):
    if type(value) not in (int,float):
        raise ValueError(name+": use int ou float, sem bool")
    try:
        result=float(value)
    except OverflowError:
        raise ValueError(name+": entrada não representável como float finito") from None
    if not isfinite(result):
        raise ValueError(name+": entrada deve ser finita")
    return result

def energy_si(mass_kg, velocity_m_s):
    """Retorna float em joules; massa zero permitida; velocidade assinada.

    ValueError: entrada fora do contrato.
    OverflowError: energia não representável como float finito.
    ArithmeticError: energia positiva arredondaria para zero.
    Não verifica unidades nem validade do regime clássico.
    """
    m=finite_real(mass_kg,"massa");v=finite_real(velocity_m_s,"velocidade")
    if m<0:raise ValueError("massa: valor não negativo necessário")
    # Fraction representa exatamente os floats já convertidos, não os decimais ideais.
    exact=Fraction(m)*Fraction(v)**2/2
    try:
        energy=float(exact)
    except OverflowError:
        raise OverflowError("energia: resultado fora da representação finita") from None
    if not isfinite(energy):raise OverflowError("energia: resultado fora da representação finita")
    if exact>0 and energy==0:raise ArithmeticError("energia: resultado positivo arredondaria para zero")
    return energy

if __name__=="__main__":
    print("3 kg a −4 m/s:",energy_si(3,-4),"J")
    print("2 kg a 72 km/h, convertidos para m/s:",energy_si(2,72/3.6),"J")
