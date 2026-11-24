"""Dois ajustes NIST de Antoine, P em bar, T em kelvin. Consulta 27/10/2026.
Não estima parâmetros a partir de estruturas nem resolve misturas/solubilidade.
"""
from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Curve:
    A: float
    B: float
    C: float
    low: float
    high: float
    source: str

CURVES={
    "ethanol":Curve(5.37229,1670.409,-40.191,273.,351.70,
        "https://webbook.nist.gov/cgi/cbook.cgi?ID=C64175&Mask=4"),
    "dimethyl_ether":Curve(4.11475,894.669,-30.604,194.93,248.24,
        "https://webbook.nist.gov/cgi/cbook.cgi?ID=C115106&Mask=4")}


def curve(species):
    if not isinstance(species,str) or species not in CURVES:
        raise ValueError("Escolha ethanol ou dimethyl_ether.")
    return CURVES[species]


def number(value):
    if isinstance(value,bool) or not isinstance(value,(int,float)):
        raise TypeError("Use número int/float, sem bool.")
    try:value=float(value)
    except OverflowError as exc:raise ValueError("Valor fora da faixa finita.") from exc
    if not math.isfinite(value):raise ValueError("Valor deve ser finito.")
    return value


def vapor_pressure(species,kelvin):
    c=curve(species);t=number(kelvin)
    if not c.low<=t<=c.high:raise ValueError("Temperatura fora da faixa do ajuste.")
    return 10**(c.A-c.B/(t+c.C))


def boiling_temperature(species,pressure_bar):
    c=curve(species);pressure=number(pressure_bar)
    if pressure<=0:raise ValueError("Pressão deve ser positiva, em bar.")
    denominator=c.A-math.log10(pressure)
    if denominator<=0:raise ValueError("Pressão incompatível com a faixa do ajuste.")
    t=c.B/denominator-c.C
    # Apenas tolerância de arredondamento da inversão, cortada aos limites.
    if not c.low-1e-10<=t<=c.high+1e-10:
        raise ValueError("Resultado fora da faixa do ajuste; não extrapolar.")
    return min(c.high,max(c.low,t))


if __name__=="__main__":
    for species in CURVES:
        t=boiling_temperature(species,.9)
        print(species,"P/bar",.9,"T/K",t,"T/°C",t-273.15)
