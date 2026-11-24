"""Fonte de fem constante e resistência interna: modelo CC racional, sem transitório."""
from fractions import Fraction as F

def rational(value):
    if isinstance(value,bool) or not isinstance(value,(int,F)):
        raise ValueError('Use inteiro ou Fraction em unidades SI')
    return F(value)

def circuit(emf,internal,load):
    emf=rational(emf);internal=rational(internal)
    if emf<=0 or internal<0:raise ValueError('Fem positiva e resistência interna não negativa')
    if load is None:
        return dict(current=F(0),voltage=emf,source_power=F(0),load_power=F(0),internal_power=F(0),efficiency=None)
    load=rational(load)
    if load<0 or internal+load==0:raise ValueError('Carga não negativa e resistência total positiva')
    current=emf/(internal+load);voltage=current*load
    source_power=emf*current;load_power=current*current*load;internal_power=current*current*internal
    return dict(current=current,voltage=voltage,source_power=source_power,
                load_power=load_power,internal_power=internal_power,efficiency=load_power/source_power)

def max_power(emf,internal):
    emf=rational(emf);internal=rational(internal)
    if emf<=0 or internal<=0:raise ValueError('Máximo finito exige fem e r positivas')
    return emf*emf/(4*internal)

if __name__=='__main__':
    for load in (2,6,None):print('R=',load,circuit(12,2,load))
