"""Fonte ideal CC, resistores positivos em uma única malha, SI."""
from fractions import Fraction as Q


def rational(x):
    if type(x) not in (int,Q): raise ValueError('Use int/Fraction, sem bool/float')
    return Q(x)


def series(voltage, resistances, seconds=0):
    voltage,seconds=map(rational,(voltage,seconds))
    if voltage<0 or seconds<0: raise ValueError('Tensão e duração não negativas')
    if not isinstance(resistances,(list,tuple)) or not resistances: raise ValueError('Lista/tupla não vazia de resistores')
    resistances=tuple(map(rational,resistances))
    if any(r<=0 for r in resistances): raise ValueError('Resistências positivas')
    equivalent=sum(resistances,Q(0));current=voltage/equivalent
    drops=tuple(current*r for r in resistances)
    powers=tuple(current*d for d in drops)
    potentials=[voltage]
    for drop in drops: potentials.append(potentials[-1]-drop)
    supplied=voltage*current
    return dict(equivalent=equivalent,current=current,drops=drops,potentials=tuple(potentials),powers=powers,
                supplied_power=supplied,source_absorbed_power=-supplied,
                energies=tuple(p*seconds for p in powers),supplied_energy=supplied*seconds,charge=current*seconds)


if __name__=='__main__':
    result=series(12,[2,4],60)
    assert result['current']==2 and result['potentials']==(12,8,0)
    assert result['supplied_energy']==1440 and result['charge']==120
    print(result)
