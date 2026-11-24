"""Fonte ideal, resistor série opcional e banco paralelo; regime DC estacionário."""
from fractions import Fraction as Q

def rational(value):
    if isinstance(value,bool) or not isinstance(value,(int,Q)):
        raise TypeError('Use int ou Fraction, sem bool ou float')
    return Q(value)

def solve(voltage,series,branches):
    voltage=rational(voltage);series=rational(series)
    if not isinstance(branches,(tuple,list)) or not branches:raise ValueError('Ao menos um ramo')
    resistances=tuple(rational(r) for r in branches)
    if voltage<0 or series<0 or any(r<=0 for r in resistances):raise ValueError('V,R0>=0; ramos>0')
    parallel=1/sum((1/r for r in resistances),Q(0))
    current=voltage/(series+parallel);load_voltage=current*parallel
    currents=tuple(load_voltage/r for r in resistances)
    powers=tuple(load_voltage*i for i in currents)
    return dict(parallel=parallel,total=series+parallel,current=current,
                load_voltage=load_voltage,currents=currents,powers=powers,
                series_power=current*current*series,source_power=voltage*current)
